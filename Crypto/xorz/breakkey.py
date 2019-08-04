#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script uses hamming distance to calculate possible length of the repeating key

See https://crypto.stackexchange.com/questions/8115/repeating-key-xor-and-hamming-distance
"""

from itertools import *
import string

# key XOR plain
from constants import key_plain


def split_by_key_length(keysize, ciphertext):

    # the original cipher is in 2-digit hex format
    HEXKEYSIZE = KEYSIZE * 2

    # Each list within this list contains ciphertext
    # XOR-ed with the same key character
    same_key_ciphertexts = [[] for _ in range(KEYSIZE)]

    index = 0

    for (c1, c2) in izip(islice(key_plain, 0, None, 2), islice(key_plain, 1, None, 2)):

        # Concatenates the two hex digits and convert them into dec
        c = '0x' + c1 + c2
        cint = int(c, 16)

        # the new two hex digits will be appended to the list
        same_key_ciphertexts[index % KEYSIZE].append(chr(cint))
        # chr() gets the ASCII char

        index += 1

    return same_key_ciphertexts


def breakkey(text):

    """
    This function takes in a list of all characters XOR-ed with the same key character

    it is based on the idea that
    ord("X") ^ ord(" ") == ord("x")
    """

    key = ""
    possible_space = ""
    max_possibility = 0

    # All ASCII alphabets
    letters = string.ascii_letters.encode('ascii')

    for char1 in range(0, len(text)):
        # counter for number of possible spaces
        possibility = 0

        for char2 in range(0, len(text)):
            if(char1 == char2):
                continue

            xor_result = chr(ord(text[char1]) ^ ord(text[char2]))

            if xor_result not in letters and xor_result != 0:
                # char1 and char2 must not contain spaces
                continue

            possibility += 1

        if possibility > max_possibility:
            # possible_space is the plaintext with highest possibility of being a space
            max_possibility = possibility
            possible_space = char1

    # key = cipher XOR plain
    key = ord(text[possible_space]) ^ ord(" ")
    return chr(key)


def decode_plaintext(key, ciphertext):

    keysize = len(key)
    cipher_size = len(ciphertext)

    # Repeats the key to the length of the ciphertext
    full_key = (key * (cipher_size / len(key) + 1))[:cipher_size]

    ki = cycle(full_key)

    plaintext = ""

    # iterates over 2 characters each time (since ciphertext comes in two digits of hex)
    for (c1, c2) in izip(islice(ciphertext, 0, None, 2), islice(ciphertext, 1, None, 2)):

        # Concatenates the two hex digits and convert them into dec
        c = '0x' + c1 + c2
        cint = int(c, 16)

        plaintext = (
            # the new two hex digits will be appended to the string
            plaintext +

            # ord() gets the decimal ASCII code of the alphabet
            chr( cint ^ ord(next(ki)) )
        )

    return plaintext

possible_KEYSIZE = [30]

for KEYSIZE in possible_KEYSIZE:

    same_key_ciphertexts = split_by_key_length(KEYSIZE, key_plain)

    keys = ''

    for ciphertext in same_key_ciphertexts:
        keys += breakkey(ciphertext)

    print "\nkeysize:", KEYSIZE
    print "key is:", keys

    plaintext = decode_plaintext(keys, key_plain)

    print(plaintext)

 # for bbytes in block_bytes:
 #        keys += break_single_key_xor(bbytes)
 #    key = bytearray(keys * len(b), "utf-8")
 #    plaintext = bxor(b, key)
 #    print("keysize:", KEYSIZE)
 #    print("key is:", keys, "n")
 #    s = bytes.decode(plaintext)
 #    print(s)
