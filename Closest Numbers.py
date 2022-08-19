# closest numbers
# for a list of numbers, return all of the pairs of numbers that have the lowest difference between them.

# Given an array of distinct integers, determine the minimum absolute difference between any two elements.
# Print all element pairs with that difference in ascending order.ord

# Example
# numbers = [6,2,4,10]
# the minimum absolute difference is 2 and the pairs with that difference are (2,4) and (4,6). When printing element pairs (i,j), they should be ordered ascending first by i and then by j.bytearray
# 2 4
# 4 6


def closestNumber(nums):
    nums.sort()
    nums_dif_dict = {}
    for i in range(1,len(nums)):
        nums_dif = nums(i)-nums(i-1)
        if nums_dif in nums_dif_dict:
            nums_dif_dict[nums_dif] += [nums(i), nums(i-1)]
        else:
            nums_dif_dict[nums_dif] = [nums(i), nums(i-1)]
        
    return