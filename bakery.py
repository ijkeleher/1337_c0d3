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


def calculate_price(amount: int, item: str) -> None:
    iter_list = [k for k in ITEMS[item]]  # grab bundle types
    combos = subsets_with_sum(iter_list, amount)
    smallest_combo = reduce(lambda a, b: a if a >
                            b else b, combos)  # get smallest list
    print(str(amount) + ' ' + str(item) + ' $' +  # print price details
          str("{:.2f}".format(sum(ITEMS[item][s] for s in smallest_combo))))
    for c in set(smallest_combo):  # use set to get only unique integers
        print(4*' ' + str(smallest_combo.count(c)) +
              " x " + str(c) + " $" + str(ITEMS[item][c]))


def subsets_with_sum(iter_lst: list, target: int) -> list:

    def _a(lst: list, rtn: list, tgt: int, lookup: dict) -> list:
        lst.sort()  # this really makes it shine
        if tgt == sum(lst):
            rtn.append(lst)  # found a solution!
        elif tgt < sum(lst):
            return  # uh-oh we went too far!
        key = tuple(lst)
        if (key not in lookup):
            for u in range(0, len(iter_lst)):  # recursively keep going
                _a(lst + [iter_lst[u]], rtn, tgt, lookup)
            lookup[key] = lst
        elif key in lookup:
            return
        return rtn  # return combos
    return _a([], [], target, {})


if __name__ == "__main__":
    # input = input()
    # amount, item = input.split()
    # calculate_price(amount, item)
    calculate_price(150, "VS5")
    calculate_price(140, "MB11")
    calculate_price(130, "CF")
