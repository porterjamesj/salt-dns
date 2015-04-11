from dnslib import QTYPE, RR, A
from dnslib.server import BaseResolver, DNSServer

import time

from salt.client import Caller

import random


class SaltResolver(BaseResolver):
    """
    DNS Resolver class that uses network.ipaddrs via the salt mine to
    resolve requests. Must be run on a salt minion
    """

    def __init__(self):
        self.caller = Caller()

    def resolve(self, request, handler):
        reply = request.reply()
        qname = request.q.qname
        if not qname.label[-1] == "salt":
            # We don't know anything!
            return reply
        grain_path = qname.label[0:-1]
        grain_query = ":".join(reversed(grain_path))
        minions = self.caller.sminion.functions["mine.get"](
            grain_query,
            "network.ipaddrs",
            expr_form="grain"
        )
        random.shuffle(minions)  # load balancing!
        # only return the first three minions
        for hostname, addrs in minions.items()[0:2]:
            for addr in addrs:
                answer = RR(hostname, QTYPE.A, rdata=A(addr), ttl=5)
                reply.add_answer(answer)
        return reply


if __name__ == "__main__":
    resolver = SaltResolver()
    server = DNSServer(
        resolver,
        port=5435,
        address="127.0.0.1"
    )
    server.start_thread()
    while server.isAlive():
        time.sleep(1)
