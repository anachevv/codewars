'''
Link to the problem -> https://www.codewars.com/kata/55983863da40caa2c900004e

Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1
nextBigger(num: 9)   // returns nil
nextBigger(num: 111) // returns nil
nextBigger(num: 531) // returns nil
'''


def next_bigger(n):
    #your code here
#     from itertools import permutations
#     num = str(n)
#     listOfNums = set([int(''.join(nums)) for nums in permutations(num, len(num))])
#     listOfNums = sorted(list(listOfNums))
#     try:
#         return listOfNums[listOfNums.index(n)+1]
#     except Exception:
#         return -1
    string_n = list(str(n))
    for current in range(len(string_n)-2,-1,-1):
        if string_n[current] < string_n[current+1]:
            t = string_n[current:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            string_n[current:] = [m] + t
            return int("".join(string_n))
    return -1
