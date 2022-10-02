# Fizz Buzz

# https://leetcode.com/problems/fizz-buzz/

# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
 

# Example 1:

# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:

# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:

# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

# Constraints:

# 1 <= n <= 104


def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    # fizz_buzz_output = ""

    # if n % 3 == 0:
    #     fizz_buzz_output += "Fizz"
    # if n % 5 == 0:
    #     fizz_buzz_output += "Buzz"
    # if fizz_buzz_output == "":
    #     fizz_buzz_output = "i"
    # return fizz_buzz_output

    fizz_buzz_array = []
    for num in range(1,n+1):
        fizz_buzz_output = ""
        if num % 3 == 0:
            fizz_buzz_output += "Fizz"
        if num % 5 == 0:
            fizz_buzz_output += "Buzz"
        if fizz_buzz_output == "":
            fizz_buzz_output = str(num)
        fizz_buzz_array.append(fizz_buzz_output)
    return fizz_buzz_array

print(fizzBuzz(15))



        