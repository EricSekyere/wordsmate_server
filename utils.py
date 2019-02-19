import os
import re
import json
import itertools



def read_file(filename, mode='r'):
    data = []
    fpath = os.path.dirname(__file__)
    filename = os.path.join(fpath, filename)
    with open(filename, mode, encoding = "utf-8", newline="") as file_item:
        content = file_item.readlines()
        for line in content:
            data.append(line.replace("\r\n", "").replace("\n", ""))
    return data

def find_perms(target, num):
    perms = itertools.permutations(target.lower(), num)
    return set(map(lambda x: "".join(x), perms))


def find_combs(target, num):
    combs = itertools.combinations(target.lower(), num)
    return set(map(lambda x: "".join(x), combs))

def search_word(words, target):
    return binary_search(words, target)
      

def search_words(words, target_list):
    return [x for x  in target_list if search_word(words, x)]

def combine_sets(s1, s2):
    if type(s1) and type(s2) not in [set]:
        raise TypeError("Please provide arguments of type set only")
    return s1.union(s2)

def binary_search(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found
