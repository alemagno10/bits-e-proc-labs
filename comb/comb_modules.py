# -*- coding: utf-8 -*-
"""Exercice 1

Implemente a equacão:

q = a or !b
"""


from myhdl import *


@block
def exe1(q, a, b):
    """
    q = a or !b
    """

    @always_comb
    def comb():
        q.next = a or not b

    return instances()


@block
def exe2(q, a, b, c):
    """
    Implemente a tabela verdade a seguir:

    A B C | Q
    ------|--
    0 0 0 | 1
    0 0 1 | 0
    0 1 0 | 0
    0 1 1 | 1
    1 0 0 | 1
    1 0 1 | 0
    1 1 0 | 0
    1 1 1 | 1

    Não utilize IF!
    """

    @always_comb
    def comb():
        q.next = (b and c) or (not b and not c)

    return instances()


@block
def exe3(q, a, b, c, d, e):
    """
    Exercice 3

    Implemente o circuito lógico a seguir:

                __
    a---------\  \
                |  |-  __
    b---------/__/  -|  \
                    |   )-
    c----------------|__/  -  __
                            -|  \
                            |   )-
    d------------------------|__/  -  __
                                    -|  \
                                    |   )-----
    e--------------------------------|__/
    """

    @always_comb
    def comb():
        q.next = (a or b) and c and d and e

    return instances()


@block
def exe4(led, sw):
    @always_comb
    def comb():
        led[0].next = sw[0] and (not sw[1])

    return instances()


@block
def exe5(leds, sw):
    """
    led0 é uma copia da chave sw0
    led1 é sw0 & sw1
    led2 é o led1 invertido
    led3 é xor entre sw0 e sw1
    todos os outros leds acesos
    """

    @always_comb
    def comb():
        leds[0].next = sw[0]
        leds[1].next = sw[0] & sw[1]
        leds[2].next = not sw[0]
        leds[3].next = sw[0] ^ sw[1]
        for i in range(4, 10):
            leds[i].next = 1

    return instances()


@block
def sw2hex(hex0, sw):
    @always_comb
    def comb():
        for i in range(len(hex0)):
            hex0[i].next = sw[i]

    return instances()


@block
def bin2hex(hex0, sw):
    @always_comb
    def comb():
        if sw[4:0] == 0:
            hex0.next = "1000000"
        elif sw[4:0] == 1:
            hex0.next = "1111001"
        elif sw[4:0] == 2:
            hex0.next = "0100100"
        elif sw[4:0] == 3:
            hex0.next = "0110000"
        elif sw[4:0] == 4:
            hex0.next = "0011001"
        elif sw[4:0] == 5:
            hex0.next = "0010010"
        elif sw[4:0] == 6:
            hex0.next = "0000010"
        elif sw[4:0] == 7:
            hex0.next = "1111000"
        elif sw[4:0] == 8:
            hex0.next = "0000000"
        elif sw[4:0] == 9:
            hex0.next = "0011000"
        elif sw[4:0] == 10:
            hex0.next = "0001000"
        elif sw[4:0] == 11:
            hex0.next = "0000011"
        elif sw[4:0] == 12:
            hex0.next = "1000110"
        elif sw[4:0] == 13:
            hex0.next = "0100001"
        elif sw[4:0] == 14:
            hex0.next = "0000110"
        else:
            hex0.next = "0001110"

    return instances()


@block
def bin2bcd(dig2, dig1, dig0, sw):
    @always_comb
    def comb():
        h2 = Signal(modbv(0)[4:])
        h1 = Signal(modbv(0)[4:])
        h0 = Signal(modbv(0)[4:])

        for i in range(7):
            if h2 >= 5:
                h2.next = h2 + 3
            if h1 >= 5:
                h1.next = h1 + 3
            if h0 >= 5:
                h0.next = h0 + 3

            h2.next = h2 << 1
            h2[0].next = h1[3]

            h1.next = h1 << 1
            h1[0].next = h0[3]

            h0.next = h0 << 1
            h0[0].next = sw[i]

        dig2.next = h2
        dig1.next = h1
        dig0.next = h0

    return instances()