#!/usr/bin/env python
# -*- coding: utf-8 -*-

# After acquiring the first result, we can see that there are still some flaws in the plaintext, which indicates minor flaws in the key
# In this script, we can debug the key character by character
# by printing out the possible keys and the plaintext generated

def breakkey_returnall(text):

    """
    This function takes in a list of all characters XOR-ed with the same key character

    it is based on the idea that
    ord("X") ^ ord(" ") == ord("x")
    """

    possible_key = []

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

        # if possibility > max_possibility:
        #     # possible_space is the plaintext with highest possibility of being a space
        #     max_possibility = possibility
        #     possible_space = char1

        key = chr(ord(text[char1]) ^ ord(" "))

        possible_key.append([key, possibility])

    # key = cipher XOR plain
    # key = ord(text[possible_space]) ^ ord(" ")
    return possible_key

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

from constants import key_plain
from itertools import *
import string

KEYSIZE = 30
same_key_ciphertexts = split_by_key_length(KEYSIZE, key_plain)

ciphertext = same_key_ciphertexts[1]


keys = breakkey_returnall(ciphertext)

# print "keys sorted by possibility are:", keys

for key in keys:

    plaintext = []
    keyc = key[0]

    print "\nkey is ", keyc
    print "possibility", key[1]

    for cipher in same_key_ciphertexts[1]:
        plain = chr(ord(cipher) ^ ord(keyc))
        plaintext.append(plain)

    letters = string.printable.encode('ascii')
    plaintext_valid = 1

    for text in plaintext:
        # print(text)
        if text not in letters:
            plaintext_valid = 0
            break

    # print(plaintext_valid)
    if plaintext_valid == 1:
        print(plaintext)


# results
#
# key is  }
# possibility 10
# 1
# [' ', '&', 'n', 'n', 'n', '9', "'", '+', 'n', ':', '8', 'n', ' ', 'n', ')', 'n', '+', 'n', 'n', 'n']
#
# key is  {
# possibility 10
# 1
# ['&', ' ', 'h', 'h', 'h', '?', '!', '-', 'h', '<', '>', 'h', '&', 'h', '/', 'h', '-', 'h', 'h', 'h']
#
# key is  3
# possibility 10
# 1
# ['n', 'h', ' ', ' ', ' ', 'w', 'i', 'e', ' ', 't', 'v', ' ', 'n', ' ', 'g', ' ', 'e', ' ', ' ', ' ']
#
# key is  3
# possibility 10
# 1
# ['n', 'h', ' ', ' ', ' ', 'w', 'i', 'e', ' ', 't', 'v', ' ', 'n', ' ', 'g', ' ', 'e', ' ', ' ', ' ']
#
# key is  3
# possibility 10
# 1
# ['n', 'h', ' ', ' ', ' ', 'w', 'i', 'e', ' ', 't', 'v', ' ', 'n', ' ', 'g', ' ', 'e', ' ', ' ', ' ']
#
# key is  d
# possibility 10
# 1
# ['9', '?', 'w', 'w', 'w', ' ', '>', '2', 'w', '#', '!', 'w', '9', 'w', '0', 'w', '2', 'w', 'w', 'w']
#
# key is  z
# possibility 10
# 1
# ["'", '!', 'i', 'i', 'i', '>', ' ', ',', 'i', '=', '?', 'i', "'", 'i', '.', 'i', ',', 'i', 'i', 'i']
#
# key is  v
# possibility 10
# 1
# ['+', '-', 'e', 'e', 'e', '2', ',', ' ', 'e', '1', '3', 'e', '+', 'e', '"', 'e', ' ', 'e', 'e', 'e']
#
# key is  3
# possibility 10
# 1
# ['n', 'h', ' ', ' ', ' ', 'w', 'i', 'e', ' ', 't', 'v', ' ', 'n', ' ', 'g', ' ', 'e', ' ', ' ', ' ']
#
# key is  g
# possibility 10
# 1
# [':', '<', 't', 't', 't', '#', '=', '1', 't', ' ', '"', 't', ':', 't', '3', 't', '1', 't', 't', 't']
#
# key is  e
# possibility 10
# 1
# ['8', '>', 'v', 'v', 'v', '!', '?', '3', 'v', '"', ' ', 'v', '8', 'v', '1', 'v', '3', 'v', 'v', 'v']
#
# key is  3
# possibility 10
# 1
# ['n', 'h', ' ', ' ', ' ', 'w', 'i', 'e', ' ', 't', 'v', ' ', 'n', ' ', 'g', ' ', 'e', ' ', ' ', ' ']
#
# key is  }
# possibility 10
# 1
# [' ', '&', 'n', 'n', 'n', '9', "'", '+', 'n', ':', '8', 'n', ' ', 'n', ')', 'n', '+', 'n', 'n', 'n']
#
# key is  3
# possibility 10
# 1
# ['n', 'h', ' ', ' ', ' ', 'w', 'i', 'e', ' ', 't', 'v', ' ', 'n', ' ', 'g', ' ', 'e', ' ', ' ', ' ']
#
# key is  t
# possibility 10
# 1
# [')', '/', 'g', 'g', 'g', '0', '.', '"', 'g', '3', '1', 'g', ')', 'g', ' ', 'g', '"', 'g', 'g', 'g']
#
# key is  3
# possibility 10
# 1
# ['n', 'h', ' ', ' ', ' ', 'w', 'i', 'e', ' ', 't', 'v', ' ', 'n', ' ', 'g', ' ', 'e', ' ', ' ', ' ']
#
# key is  v
# possibility 10
# 1
# ['+', '-', 'e', 'e', 'e', '2', ',', ' ', 'e', '1', '3', 'e', '+', 'e', '"', 'e', ' ', 'e', 'e', 'e']
#
# key is  3
# possibility 10
# 1
# ['n', 'h', ' ', ' ', ' ', 'w', 'i', 'e', ' ', 't', 'v', ' ', 'n', ' ', 'g', ' ', 'e', ' ', ' ', ' ']
#
# key is  3
# possibility 10
# 1
# ['n', 'h', ' ', ' ', ' ', 'w', 'i', 'e', ' ', 't', 'v', ' ', 'n', ' ', 'g', ' ', 'e', ' ', ' ', ' ']
#
# key is  3
# possibility 10
# 1
# ['n', 'h', ' ', ' ', ' ', 'w', 'i', 'e', ' ', 't', 'v', ' ', 'n', ' ', 'g', ' ', 'e', ' ', ' ', ' ']
