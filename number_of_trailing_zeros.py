'''
Link to the problem -> https://www.codewars.com/kata/52f787eb172a8b4ae1000a34

Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.
'''


def zeros(n):
    #     from math import factorial

    #     factorial_n = factorial(n)
    #     string_factorial_n = str(factorial_n)

    #     trailing_zeros = len(string_factorial_n) - len(string_factorial_n.rstrip('0'))

    #     return trailing_zeros

    #     from math import factorial

    #     factorial_n = factorial(n)
    #     return len(s := str(factorial_n)) - len(s.rstrip("0"))

    #     from re import findall
    #     from math import factorial

    #     num = factorial(n)
    #     return len(findall("0*$", str(num))[0])

    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count
