# https://www.codewars.com/kata/53db96041f1a7d32dc0004d2/python

import sys
import numpy as np

sys.path.append('/Users/dianaavalos/Programming/python-test-framework')
import codewars_test as test

array = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
    , [4, 9, 8, 2, 6, 1, 3, 7, 5]
    , [7, 5, 6, 3, 8, 4, 2, 1, 9]
    , [6, 4, 3, 1, 5, 8, 7, 9, 2]
    , [5, 2, 1, 7, 9, 3, 8, 4, 6]
    , [9, 8, 7, 4, 2, 6, 5, 3, 1]
    , [2, 1, 4, 9, 3, 5, 6, 8, 7]
    , [3, 6, 5, 8, 1, 7, 9, 2, 4]
    , [8, 7, 9, 6, 4, 2, 1, 5, 3]]

array=[[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9, 1], [3, 4, 5, 6, 7, 8, 9, 1, 2], [4, 5, 6, 7, 8, 9, 1, 2, 3], [5, 6, 7, 8, 9, 1, 2, 3, 4], [6, 7, 8, 9, 1, 2, 3, 4, 5], [7, 8, 9, 1, 2, 3, 4, 5, 6], [8, 9, 1, 2, 3, 4, 5, 6, 7], [9, 1, 2, 3, 4, 5, 6, 7, 8]]

def done_or_not(array):
   if  not False in list(map(lambda i: set(range(1, 10)) == set(array[i]) , range(1,len(array)-1))): # if only trues
       array=np.rot90(array, 1)
       if not False in list(map(lambda i: set(range(1, 10)) == set(array[i]) , range(1,len(array)-1))):
           return ('Finished!')
       else:
           return ('Try again!')
   else:
       return ('Try again!')



test.assert_equals(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                                   , [4, 9, 8, 2, 6, 1, 3, 7, 5]
                                   , [7, 5, 6, 3, 8, 4, 2, 1, 9]
                                   , [6, 4, 3, 1, 5, 8, 7, 9, 2]
                                   , [5, 2, 1, 7, 9, 3, 8, 4, 6]
                                   , [9, 8, 7, 4, 2, 6, 5, 3, 1]
                                   , [2, 1, 4, 9, 3, 5, 6, 8, 7]
                                   , [3, 6, 5, 8, 1, 7, 9, 2, 4]
                                   , [8, 7, 9, 6, 4, 2, 1, 5, 3]]), 'Finished!');

test.assert_equals(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                                   , [4, 9, 8, 2, 6, 1, 3, 7, 5]
                                   , [7, 5, 6, 3, 8, 4, 2, 1, 9]
                                   , [6, 4, 3, 1, 5, 8, 7, 9, 2]
                                   , [5, 2, 1, 7, 9, 3, 8, 4, 6]
                                   , [9, 8, 7, 4, 2, 6, 5, 3, 1]
                                   , [2, 1, 4, 9, 3, 5, 6, 8, 7]
                                   , [3, 6, 5, 8, 1, 7, 9, 2, 4]
                                   , [8, 7, 9, 6, 4, 2, 1, 3, 5]]), 'Try again!');
