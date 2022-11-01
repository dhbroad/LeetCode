# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
# 
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.



def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 1:
        return strs[0]
    min_common = ""
    for i in range(1,len(strs)): # Looping through list of strings
        test_common = ""
        sm_str = min(len(strs[i]),len(strs[i-1]))
        if sm_str == 0:
            return ""
        for j in range(sm_str): # Looping through each string
            if strs[i][j] == strs[i-1][j]: # if both letters at j match
                test_common += strs[i][j] # add the letter to test_common
                if j == sm_str-1: # if every letter has matched until the end of the smaller string, compare
                    if len(min_common) > len(test_common):
                        min_common = test_common
                        break
                    if min_common == "":
                        min_common = test_common
                        break
            else: # if they do not match, compare and break
                if j == 0: 
                    return ""
                if len(min_common) > len(test_common):
                    min_common = test_common
                    break
                if min_common == "":
                    min_common = test_common
                    break
            
    return min_common