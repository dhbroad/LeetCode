# Valid Anagram

# Solution
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s_dict = {}
    t_dict = {}
    for a in s:
        if a in s_dict:
            s_dict[a] += 1
        else:
            s_dict[a] = 1
    for b in t:
        if b in t_dict:
            t_dict[b] += 1
        else:
            t_dict[b] = 1 
    if s_dict == t_dict:
        return True
    else:
        return False


s1 = 'anagram'
t1 = 'nagaram'

s2 = 'ab'
t2 = 'ba'

s3 = 'fail'
t3 = 'pass'

print(isAnagram(s1, t1))
print(isAnagram(s2, t2))
print(isAnagram(s3, t3))
