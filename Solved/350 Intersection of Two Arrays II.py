# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 # https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

def intersect2P(nums1, nums2):
    nums1.sort()
    nums2.sort()
    intersect = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            intersect.append(nums1[i])
            i+=1
            j+=1
        elif nums1[i] > nums2[j]:
            j+=1
        elif nums1[i] < nums2[j]:
            i+=1
    return intersect


# Hashmap approach with shortest list being used first
# Faster than 97.83% of leetcode submissions for "intersections of Two Arrays ii"
def intersectHM(nums1, nums2):
    if len(nums1) > len(nums2):
        placeholder = nums1
        nums1 = nums2
        nums2 = placeholder
    nums_dict = {}
    intersect_array = []
    for num in nums1:
        if num in nums_dict:
            nums_dict[num] += 1
        else: 
            nums_dict[num] = 1
    for num in nums2:
        if num in nums_dict:
            if nums_dict[num] > 0:
                intersect_array.append(num)
                nums_dict[num] -= 1
    return intersect_array


ex1_nums1 = [1,2,2,1]
ex1_nums2 = [2,2]

ex2_nums1 = [4,9,5]
ex2_nums2 = [9,4,9,8,4]

print(intersect2P(ex1_nums1,ex1_nums2))
print(intersectHM(ex1_nums1,ex1_nums2))
print(intersect2P(ex2_nums1,ex2_nums2))
print(intersectHM(ex2_nums1,ex2_nums2))