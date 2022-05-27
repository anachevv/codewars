import random

number = random.randint(1, 20)
my_list = [1, 2, 5, 6, 9, 10, 13, 14, 17, 18]
if number in my_list:
    print(number)
    print("The number matches!")
else:
    print(number)
    print("The number doesn't match!")
print(my_list)
