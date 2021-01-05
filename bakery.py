#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
this is a program to calculate the prices of baked goods
"""

# price info
VS5 = {3: 6.99, 5: 8.99}
MB11 = {2: 9.95, 5: 16.95, 8: 24.95}
CF = {3: 5.95, 5: 9.95, 9: 16.99}

# a way to access using the code
ITEMS = {"VS5": VS5, "MB11": MB11, "CF": CF}

def calculate_price(num, item):
    # fill the list of possible combos
    iter_list = [k for k in ITEMS[item]]
    # now we work out the best combination
    combos = a(iter_list, num)
    # grab the smallest number in combo list
    smallest_combo_len = min(map(lambda x: len(x), combos))
    # and calculated the smallest (by length) list
    smallest_combo = 0
    for c in combos:
        if len(c) <= smallest_combo_len:
            smallest_combo = c
    # then sum up for our prices
    total_price = 0
    for s in smallest_combo:
        total_price += ITEMS[item][s]
    # print our calculations
    print(str(num) + " " + str(item) + " " + str(total_price))
    print(smallest_combo)

# modified from:
# https://stackoverflow.com/questions/20193555/finding-combinations-to-the-provided-sum-value

def a(lst, target):
    # lst = list of combos, target is what we are summing to
    def _a(l, r, t):
        if t == sum(l): # if we reach our target append and escape
            r.append(l)
        elif t < sum(l): # uh-oh we went too far!
            return
        # otherwise recursively keep going
        for u in range(0, len(lst)): 
            _a(l + [lst[u]], r, t)
        return r # our return list
    return _a([], [], target)

if __name__ == "__main__":
    # input = input()
    # num, item = input.split()
    # calculate_price(num, item)
    # tests
    calculate_price(10, "VS5")
    calculate_price(14, "MB11")
    calculate_price(13, "CF")
