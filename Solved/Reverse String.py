# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is a printable ascii character.

def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    l = len(s)
    j = l-1
    i = 0
    k = ""
    while i < l/2:
        k = s[i]
        s[i] = s[j]
        s[j] = k
        i+=1
        j-=1
    return s


string1 = ["h", "e", "l", "l", "o"]

print(reverseString(string1))