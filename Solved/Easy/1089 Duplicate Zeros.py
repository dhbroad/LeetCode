# https://leetcode.com/problems/duplicate-zeros/

# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

 

# Example 1:

# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
# Example 2:

# Input: arr = [1,2,3]
# Output: [1,2,3]
# Explanation: After calling your function, the input array is modified to: [1,2,3]
 

# Constraints:

# 1 <= arr.length <= 104
# 0 <= arr[i] <= 9


def duplicateZeros(arr):
    """
    :type arr: List[int]
    :rtype: None Do not return anything, modify arr in-place instead.
    """
    # using a nested for loop to move each value one at a time
    # for i in reversed(range(len(arr))):
    #     if arr[i] == 0 and i != len(arr)-1:
    #         for j in reversed(range(i+1,len(arr))):
    #             arr[j] = arr[j-1]
    
    # Using python's built in methods to pop and insert
    # for i in reversed(range(len(arr))):
    #     if arr[i] == 0 and i != len(arr)-1:
    #         arr.pop()
    #         arr.insert(i,0)
    # return arr
    
    # Python's built in methods but with a while loop
    # i = 0
    # while i < len(arr) - 1:
    #     if arr[i] == 0:
    #         arr.pop()
    #         arr.insert(i+1, 0)
    #         i = i + 2
    #     else:
    #         i = i + 1
    
    # Allocating values to a new array to avoid having to use any sorting algorithms
    new_arr=[]
    n=len(arr)
    for i in range(n):
        if(arr[i]==0):
            new_arr.append(0)    
        new_arr.append(arr[i])

    for i in range(n):
        arr[i]=new_arr[i]
    return arr[i]
        