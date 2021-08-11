# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

import sys
import numpy as np

sys.path.append('/Users/dianaavalos/Programming/python-test-framework')
import codewars_test as test



snail_map=[[1, 2, 3, 4, 5],
 [6, 7, 8, 9, 10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20],
 [21, 22, 23, 24, 25]]


def new_coordinates(i, j, dim, direction, visited):
    if direction is "left":
        if (j + 1) in range(dim) and visited[i][j + 1] == 0:
            j += 1
        else:
            direction = "down"
    if direction is "down":
        if (i + 1) in range(dim) and visited[i + 1][j] == 0:
            i += 1
        else:
            direction = "right"
    if direction is "right":
        if (j - 1) in range(dim) and visited[i][j - 1] == 0:
            j -= 1
        else:
            direction = "up"
    if direction is "up":
        if (i - 1) in range(dim) and visited[i - 1][j] == 0:
            i -= 1
        else:
            direction = "left"
    # print(i, j, direction)
    return (i, j, direction)


def snail(snail_map):
    print(snail_map)
    dim = len(snail_map[0])
    if dim == 0:  return []
    else:
        visited = np.full([dim, dim], 0)
        i, j, direction = 0, 0, "left"
        ls = [snail_map[i][j]]
        visited[i][j] = 1

        while (np.sum(visited) < dim * dim):
            i, j, direction2 = new_coordinates(i, j, dim, direction, visited)

            if  (direction == "up" and direction2 == "left"): direction=direction2
            else:
                visited[i][j] = 1
                direction = direction2
                ls.append(snail_map[i][j])
        return ls

### best solutions


def snail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:]) ## this is the line
    return m

# my implementation/explanation of the solution by foxxyz
def snail(array):
  if array:
    # force to list because zip returns a list of tuples
    top_row = list(array[0])
    # rotate the array by switching remaining rows & columns with zip
    # the * expands the remaining rows so they can be matched by column
    rotated_array = zip(*array[1:])
    # then reverse rows to make the formerly last column the next top row
    rotated_array = rotated_array[::-1]
    return top_row + snail(rotated_array)
  else:
    return []

def snail(array):
  out = []
  while len(array):
      out += array.pop(0)
      array = list(zip(*array))[::-1]  # Rotate
  return out


def trans(array):
    # Do an inverse transpose (i.e. rotate left by 90 degrees
    return [[row[-i - 1] for row in array] for i in range(len(array[0]))] if len(array) > 0 else array


def snail(array):
    output = []

    while len(array) > 0:
        # Add the 1st row of the array
        output += array[0]
        # Chop off the 1st row and transpose
        array = trans(array[1:])

    return output


def snail(array):
    res = []
    while len(array) > 1:
        res = res + array.pop(0)
        res = res + [row.pop(-1) for row in array]
        res = res + list(reversed(array.pop(-1)))
        res = res + [row.pop(0) for row in array[::-1]]
    return res if not array else res + array[0]


snail_map
a = snail(snail_map)
array= snail_map

array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
test.assert_equals(snail(array), expected)

array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test.assert_equals(snail(array), expected)

# clockwise
