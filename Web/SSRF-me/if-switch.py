#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script intends to test whether the if switches is vulnerable

If you run the script, you will get the following results:

$ python if-switch.py
scan is in action
read is in action
"""

action = "readscan"

if "scan" in action:
    print('scan is in action')

if "read" in action:
    print("read is in action")
