#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b
        carry.next = a & b
    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b ^ c
        carry.next = (a & b)|(b & c)|(a & c)
    return instances()


@block
def adder2bits(x, y, soma, carry):
    return instances()


@block
def adder(x, y, soma, carry):
    @always_comb
    def comb():
        pass

    return instances()
