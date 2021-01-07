#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools
"""
this is a program to calculate the prices of baked goods
"""

# price info
VS5 = {3: 6.99, 5: 8.99}
MB11 = {2: 9.95, 5: 16.95, 8: 24.95}
CF = {3: 5.95, 5: 9.95, 9: 16.99}

# a way to access using the item code
ITEMS = {"VS5": VS5, "MB11": MB11, "CF": CF}

def calculate_price(amount, item):

    iter_list = [k for k in ITEMS[item]] # grab bundle types
    combos = a(iter_list, amount) # work out the best combination
    # calculate the smallest (by length) list
    smallest_combo = functools.reduce(lambda a,b : a if a > b else b,combos)

    # sum the price and print details
    print(str(amount) + ' ' + str(item) + ' $' + str("{:.2f}".format(sum(ITEMS[item][s] for s in smallest_combo))))
    
    for c in set(smallest_combo): # using set here to get only unique integers
        print(4*' ' +  str(smallest_combo.count(c)) + " x " + str(c) + " $" + str(ITEMS[item][c]))

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
    # amount, item = input.split()
    # calculate_price(amount, item)
    # tests
    calculate_price(10, "VS5")
    calculate_price(14, "MB11")
    calculate_price(13, "CF")
