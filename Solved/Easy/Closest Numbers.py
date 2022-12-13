# https://www.hackerrank.com/challenges/closest-numbers/problem# 
# 
# closest numbers
# for a list of numbers, return all of the pairs of numbers that have the lowest difference between them.

# Given an array of distinct integers, determine the minimum absolute difference between any two elements.
# Print all element pairs with that difference in ascending order.ord

# Example
# numbers = [6,2,4,10]
# the minimum absolute difference is 2 and the pairs with that difference are (2,4) and (4,6). When printing element pairs (i,j), they should be ordered ascending first by i and then by j.bytearray
# 2 4
# 4 6


def closestNumber(arr):
    arr.sort()
    nums_dif_dict = {}
    min_value = arr[1]-arr[0]
    for i in range(1,len(arr)):
        nums_dif = arr[i]-arr[i-1]
        if nums_dif < min_value:
            min_value = nums_dif
        if nums_dif in nums_dif_dict:
            nums_dif_dict[nums_dif] += [arr[i-1], arr[i]]
        else:
            nums_dif_dict[nums_dif] = [arr[i-1], arr[i]]

    return nums_dif_dict[min_value]