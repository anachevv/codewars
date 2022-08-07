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
