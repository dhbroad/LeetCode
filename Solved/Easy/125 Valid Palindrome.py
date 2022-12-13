# https://leetcode.com/problems/valid-palindrome/
# 
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    new_s = ""
    for char in s:
        check = ord(char.lower())
        if check > 96 and check < 123 or check > 47 and check < 58:
            new_s += char.lower()
    if new_s[::-1] == new_s:
        return True
    else:
        return False
            