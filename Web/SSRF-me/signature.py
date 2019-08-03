#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script intends to test whether the signature generation step is vulnerable

If you run the script, you will get the following results:

$ python signature.py
The two strings are equal
"""

import os

secret_key = os.urandom(16)

# In python 3, you would need to convert the bytes to str
secret_key = secret_key.decode("utf-8", errors='ignore')

str1 = secret_key + "flag.txt" + "readscan"
str2 = secret_key + "flag.txtread" + "scan"

assert str1 == str2

print("The two strings are equal")
