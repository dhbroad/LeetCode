# https://leetcode.com/problems/first-unique-character-in-a-string/
# 
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1
 

# Constraints:
# 1 <= s.length <= 105
# s consists of only lowercase English letters.



def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    lc_dict = {} # (letter count)
    for ltr in s:
        if ltr in lc_dict:
            lc_dict[ltr] += 1
        else:
            lc_dict[ltr] = 1
    for ltr in s:
        if lc_dict[ltr] == 1:
            return s.index(ltr)
    return -1
