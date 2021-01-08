#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
"""
This is a program to calculate the prices of baked goods
"""
VS5 = {3: 6.99, 5: 8.99}
MB11 = {2: 9.95, 5: 16.95, 8: 24.95}
CF = {3: 5.95, 5: 9.95, 9: 16.99}
ITEMS = {"VS5": VS5, "MB11": MB11, "CF": CF}  # access data using item code


def calculate_price(amount, item):
    iter_list = [k for k in ITEMS[item]]  # grab bundle types
    # combos = subsets_with_sum(iter_list, amount)  # find best combination
    combos = subsets_with_sum(iter_list, amount)
    # combos = subsetSum(iter_list, amount)
    # print("FINAL CHOICES: ", combos)
    smallest_combo = reduce(lambda a, b: a if a >
                            b else b, combos)  # get smallest list
    print(str(amount) + ' ' + str(item) + ' $' +  # print price details
          str("{:.2f}".format(sum(ITEMS[item][s] for s in smallest_combo))))
    for c in set(smallest_combo):  # use set to get only unique integers
        print(4*' ' + str(smallest_combo.count(c)) +
              " x " + str(c) + " $" + str(ITEMS[item][c]))


def subsets_with_sum(lst, target):
    lookup = {} # avoid duplicate combos
    # Time Complexity: ???
    def _a(l, r, t, lookup):
        l.sort() # this really makes it shine
        if t == sum(l):
            r.append(l)  # found a solution!
        elif t < sum(l):
            return  # uh-oh we went too far!
        key = tuple(l)
        # print("KEY:", key)
        if (key not in lookup):
            for u in range(0, len(lst)):  # recursively keep going
                _a(l + [lst[u]], r, t, lookup)
            lookup[key] = l
        elif key in lookup:
            return
        return r  # return combos
    return _a([], [], target, lookup)


if __name__ == "__main__":
    # input = input()
    # amount, item = input.split()
    # calculate_price(amount, item)
    calculate_price(150, "VS5")
    calculate_price(14, "MB11")
    calculate_price(13, "CF")
