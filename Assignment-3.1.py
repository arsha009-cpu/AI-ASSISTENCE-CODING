#Write a Python function that checks whether a given number is a palindrome.
#The function should return True if it is a palindrome and False otherwise.

"""def is_palindrome(number):
    original = number
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    return original == reverse
print(is_palindrome(121))     # Expected: True
print(is_palindrome(123))     # Expected: False
print(is_palindrome(1221))    # Expected: True
print(is_palindrome(10))      # Expected: False
print(is_palindrome(7))       # Expected: True"""

"""Now write a python function that compute the factorial of given number. The function should return the result.
Example:
Input:5
Output:120"""
"""def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Example usage
print(factorial(5))   # Expected: 120
print(factorial(0))   # Expected: 1
print(factorial(1))   # Expected: 1
print(factorial(4))   # Expected: 24"""

"""Example 1:
Input: 153
Output: Armstrong Number

Example 2:
Input: 370
Output: Armstrong Number

Example 3:
Input: 123
Output: Not an Armstrong Number

Now write a Python function that checks whether a given number is an Armstrong number.
The function should return an appropriate result."""

"""def is_armstrong(number):
    total = 0
    temp = number
    digits = len(str(number))

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == number:
        return "Armstrong Number"
    else:
        return "Not an Armstrong Number"
print(is_armstrong(153))   # Expected: Armstrong Number
print(is_armstrong(370))   # Expected: Armstrong Number
print(is_armstrong(123))   # Expected: Not an Armstrong Number"""

"""You are writing a Python program for number classification.

Requirements:
- Accept only integer input
- Handle invalid and negative inputs properly
- Classify the number as Prime, Composite, or Neither
- Optimize the logic for efficiency (avoid unnecessary checks)
- Return clear and user-friendly messages
- Write clean and readable Python code

Generate the program accordingly.
"""
"""def classify_number(n):
    if not isinstance(n, int):
        return "Invalid input"

    if n <= 1:
        return "Neither Prime nor Composite"

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "Composite"

    return "Prime"
print(classify_number(2))
print(classify_number(7))
print(classify_number(10))
print(classify_number(1))
print(classify_number(0))"""

"""Write a Python function that checks whether a given number is a perfect number.
The function should return an appropriate result.
"""
"""def is_perfect(number):
    total = 0

    for i in range(1, number):
        if number % i == 0:
            total += i

    if total == number:
        return "Perfect Number"
    else:
        return "Not a Perfect Number"
    
print(is_perfect(6))     # 1 + 2 + 3 = 6
print(is_perfect(28))    # 1 + 2 + 4 + 7 + 14 = 28"""



"""Example 1:
Input: 8
Output: Even

Example 2:
Input: 15
Output: Odd

Example 3:
Input: 0
Output: Even

Now write a Python program that determines whether a given number is Even or Odd.
The program should include proper input validation and return clear messages.
"""
def check_even_odd(value):
    if not isinstance(value, int):
        return "Invalid input"

    if value % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(8))
print(check_even_odd(15))
print(check_even_odd(0))








