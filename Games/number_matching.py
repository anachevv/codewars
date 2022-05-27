import random

number = random.randint(1, 51 + 1)
my_list = [num * 3 for num in range(1, 17 + 1)]

if number in my_list:
    print(number)
    print("The number matches!")
else:
    print(number)
    print("The number doesn't match!")
print(my_list)
