def find_outlier(integers):
    even_list = []
    odd_list = []
    for integer in integers:
        if integer % 2 == 0:
            even_list.append(integer)
        else:
            odd_list.append(integer)
    if len(even_list) < len(odd_list):
        return even_list[0]
    elif len(odd_list) < len(even_list):
        return odd_list[0]

    return find_outlier(integers)
