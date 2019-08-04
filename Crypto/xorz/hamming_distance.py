#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script uses hamming distance to calculate possible length of the repeating key

See https://crypto.stackexchange.com/questions/8115/repeating-key-xor-and-hamming-distance
"""

from itertools import *


def hamming_distance(hex1, hex2):
    differing_bits = 0

    # In case hex1 and hex2 have different lengths
    max_len = min(len(hex1), len(hex2))

    for (hex1c1, hex1c2, hex2c1, hex2c2) in izip(
        islice(hex1, 0, max_len, 2),
        islice(hex1, 1, max_len, 2),
        islice(hex2, 0, max_len, 2),
        islice(hex2, 1, max_len, 2)
    ):

        # Concatenates the two hex digits and convert them into dec
        hex1c = int('0x' + hex1c1 + hex1c2, 16)
        hex2c = int('0x' + hex2c1 + hex2c2, 16)

        # Each "1" indicates difference and "0" indicates identicalness
        bit_difference = bin(hex1c ^ hex2c)

        differing_bits += bit_difference.count("1")

    return differing_bits

# key XOR plain
key_plain = "1e5d4c055104471c6f234f5501555b5a014e5d001c2a54470555064c443e235b4c0e590356542a130a4242335a47551a590a136f1d5d4d440b0956773613180b5f184015210e4f541c075a47064e5f001e2a4f711844430c473e2413011a100556153d1e4f45061441151901470a196f035b0c4443185b322e130806431d5a072a46385901555c5b550a541c1a2600564d5f054c453e32444c0a434d43182a0b1c540a55415a550a5e1b0f613a5c1f10021e56773a5a0206100852063c4a18581a1d15411d17111b052113460850104c472239564c0755015a13271e0a55553b5a47551a54010e2a06130b5506005a393013180c100f52072a4a1b5e1b165d50064e411d0521111f235f114c47362447094f10035c066f19025402191915110b4206182a544702100109133e394505175509671b6f0b01484e06505b061b50034a2911521e44431b5a233f13180b5508131523050154403740415503484f0c2602564d470a18407b775d031110004a54290319544e06505b060b424f092e1a770443101952333213030d554d551b2006064206555d50141c454f0c3d1b5e4d43061e453e39544c17580856581802001102105443101d111a043c03521455074c473f3213000a5b085d113c194f5e08555415180f5f433e270d131d420c1957773f560d11440d40543c060e470b55545b114e470e193c155f4d47110947343f13180c100f565a000403484e184c15050250081f2a54470545104c5536251325435302461a3b4a02484e12545c1b4265070b3b5440055543185b36231301025b084054220f4f42071b1554020f430b196f19564d4002055d79"

normalized_distances = {}

for KEYSIZE in range(2, 39):

    # the original cipher is in 2-digit hex format
    HEXKEYSIZE = KEYSIZE * 2

    #我们取其中前6段计算平均汉明距离
    cipher1 = key_plain[: HEXKEYSIZE]
    cipher2 = key_plain[HEXKEYSIZE: HEXKEYSIZE * 2]
    cipher3 = key_plain[HEXKEYSIZE * 2: HEXKEYSIZE * 3]
    cipher4 = key_plain[HEXKEYSIZE * 3: HEXKEYSIZE * 4]
    cipher5 = key_plain[HEXKEYSIZE * 4: HEXKEYSIZE * 5]
    cipher6 = key_plain[HEXKEYSIZE * 5: HEXKEYSIZE * 6]

    normalized_distance = float(
        hamming_distance(cipher1, cipher2) +
        hamming_distance(cipher2, cipher3) +
        hamming_distance(cipher3, cipher4) +
        hamming_distance(cipher4, cipher5) +
        hamming_distance(cipher5, cipher6)
    ) / (KEYSIZE * 5)

    normalized_distances[KEYSIZE] = normalized_distance

print(normalized_distances)

# result
# {
#     2: 3.0,
#     3: 3.2666666666666666,
#     4: 3.35,
#     5: 3.24,
#     6: 3.4,
#     7: 3.0,
#     8: 3.55,
#     9: 2.888888888888889,
#     10: 3.54,
#     11: 3.4545454545454546,
#     12: 3.4,
#     13: 3.2153846153846155,
#     14: 3.1714285714285713,
#     15: 3.4,
#     16: 3.3375,
#     17: 3.2470588235294118,
#     18: 3.1444444444444444,
#     19: 3.1157894736842104,
#     20: 3.43,
#     21: 3.2285714285714286,
#     22: 3.1363636363636362,
#     23: 3.4434782608695653,
#     24: 3.425,
#     25: 3.24,
#     26: 3.4384615384615387,
#     27: 3.2444444444444445,
#     28: 3.357142857142857,
#     29: 3.462068965517241,
#     30: 2.62,
#     31: 3.432258064516129,
#     32: 3.29375,
#     33: 3.1636363636363636,
#     34: 3.4235294117647057,
#     35: 3.2857142857142856,
#     36: 3.3777777777777778,
#     37: 3.345945945945946,
#     38: 3.142105263157895
# }
