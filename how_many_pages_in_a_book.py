def amount_of_pages(summary):
    digit = 0
    count = 0
    while summary != digit:
        count += 1
        digit += len(str(count))
    return count
