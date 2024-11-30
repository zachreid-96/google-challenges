"""
Description: see ../text_files/palindrome.txt for description
    Converts a number to another base than base 10
    will loop through bases up to n^2 to check for a base where the passed num is a palindrome
    uses is_palindrome() to reverse a string and returns True if strings are equal (palindrome)
    base case is 2 since 0 <= n <= 1000
Args:
    n: the passed number to be converted into a different base than base 10
Returns:
    returns the smallest base where n is a palindrome
Test Cases Used:
    n = 0 # Expected output 2
    n = 42 # Expected output 4
    n = 845 # Expected output 44
"""


def is_palindrome(s):
    temp_str = ""
    for t in range(len(s) - 1, -1, -1):
        temp_str += s[t]
    return s == temp_str


def solution(n):
    base = 2

    for b in range(2, n):
        palindrome_str = ""
        temp_num = n

        while temp_num > -1:
            if temp_num == 0:
                if is_palindrome(palindrome_str):
                    return b
                break
            palindrome_str += str(temp_num % b)
            temp_num = int(temp_num / b)

    return base
