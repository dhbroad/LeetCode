# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsDict = {}
        i = 0
        for num in nums:
            if target-num in numsDict:
                return [numsDict[target-num], i]
            else:
                numsDict[num] = i
                i += 1

n1 = [1,3,5,9]
t1 = 10

print(twoSum(n1, t1))