#!/usr/bin/env python3
from awscli import Root
from util import note
class DESCRIBE_KEY_PAIRS(Root):
    def keypairs(self):
        return [ KeyPair(x) for x in self.KeyPairs ]

class KeyPair(Root):
    def name(self):
        return self.KeyName
    def _repr(self):
        return self.name()

ROOT=DESCRIBE_KEY_PAIRS
