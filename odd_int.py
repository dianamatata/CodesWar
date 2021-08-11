# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
import sys

sys.path.append('/Users/dianaavalos/Programming/python-test-framework')
import codewars_test as test
from collections import Counter


# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    counts = dict(Counter(seq))

    dict((v, k) for k, v in counts.iteritems())

    inv_map = dict(zip(counts.values(), counts.keys()))

    inv_map = {str(v): str(k) for k, v in counts.items()} # no
    odds = list(filter(lambda x: x % 2 != 0, counts.values()))  # we filter the odd values

    keys = [counts[x] for x in odds]
    for key, value in counts.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if value == int(odds[1]):
            print(value)
    return keys  # get the keys


test.describe("Example")
test.assert_equals(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)

seq = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]
