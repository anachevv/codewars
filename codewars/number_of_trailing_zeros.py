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
