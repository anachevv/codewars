def longest_consec(strarr, k):
    # your code
    k -= 1
    if k < 0:
        exit()
    if strarr == []:
        return ""
    else:
        if k == 0:
            max_length_number = max(strarr, key=len)
            return max_length_number
        else:
            list_length = len(strarr)
            paired_list = [strarr[i] + strarr[i + 1] for i in range(0, list_length - k)]

            if list_length % 2 == 1:
                paired_list.append(strarr[list_length - 1])

            max_length_number = max(paired_list, key=len)

            return max_length_number
