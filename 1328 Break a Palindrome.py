# Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

# Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

# A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. 
# For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.

 

# Example 1:

# Input: palindrome = "abccba"
# Output: "aaccba"
# Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
# Of all the ways, "aaccba" is the lexicographically smallest.
# Example 2:

# Input: palindrome = "a"
# Output: ""
# Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.


def palindromeBreak(astring):
    if len(astring) == 1:
        return ""
    pos_of_letter_to_change = 0
    for i in range(1,len(astring)):
        if ord(astring[i]) > ord(astring[i-1]) and i != (len(astring)-1)/2:
            pos_of_letter_to_change = i
    if astring[pos_of_letter_to_change] == "a":
        return ""
    else:
        string_list = list(astring)
        string_list[pos_of_letter_to_change] = 'a'
        return ''.join(string_list)

