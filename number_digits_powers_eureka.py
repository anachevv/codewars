def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    # your code here
    special_numbers = []

    for number in range(a, b + 1):
        n_power = 0
        result = 0

        for digit in str(number):
            n_power += 1
            result += int(digit) ** n_power

            if result == number:
                special_numbers.append(number)

    return special_numbers
