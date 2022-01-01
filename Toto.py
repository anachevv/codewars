import random

# attempts

attempts1 = 0
attempts2 = 0

# guessed_numbers

guessed_numbers1 = []
guessed_numbers2 = []

# number
number1 = random.randint(1, 35)
number11 = random.randint(1, 49)
number2 = random.randint(1, 35)
number22 = random.randint(1, 49)
number3 = random.randint(1, 35)
number33 = random.randint(1, 49)
number4 = random.randint(1, 35)
number44 = random.randint(1, 49)
number5 = random.randint(1, 35)
number55 = random.randint(1, 49)
number6 = random.randint(1, 35)
number66 = random.randint(1, 49)

# Game1

print("Hello! You have the opportunity to choose between these two games:\nGame1 - Toto 5 out of 35."
      "\nGame2 - Toto 6 out of 49.\nIf you play 'Toto 5 out of 35' and guess the five numbers,you will win $500,000. "
      "If you play 'Toto 6 out of 49' and guess the six numbers, you will win $750,000.\nWhich one are you choosing?")

user_input = input("I'm choosing:\n")

while attempts1 == 5:
    break
if user_input == "Game1":
    print("Guess the five numbers between 1 and 35:")
    while attempts1 < 5:
        guess1 = int(input())
        attempts1 += 1

        if attempts1 == 5:
            print("Game over!The five numbers were " + str(number1) + "," + str(number2) + "," + str(number3) + "," +
                  str(number4) + "," + str(number5) + ".")

            if len(guessed_numbers1) == 1:
                print("Guessed number: " + str(guessed_numbers1))
            else:
                print("Guessed numbers: " + str(guessed_numbers1))

            print("\nThere is one game left: Game2\nTry your luck one more time!\nI'm guessing:")
            break

        elif guess1 == number1:
            guessed_numbers1.append(number1)
            print("You guessed correctly!")
            continue
        elif guess1 == number2:
            guessed_numbers1.append(number2)
            print("You guessed correctly!")
            continue
        elif guess1 == number3:
            guessed_numbers1.append(number3)
            print("You guessed correctly!")
            continue
        elif guess1 == number4:
            guessed_numbers1.append(number4)
            print("You guessed correctly!")
            continue
        elif guess1 == number5:
            guessed_numbers1.append(number5)
            print("You guessed correctly!")
        elif guessed_numbers1 == [number1, number2, number3, number4, number5]:
            print("Congratulations!You guessed the five numbers!Your prize is: $500,000.")
            break

# Game2

while attempts2 == 6:
    break
if user_input == "Game2":
    print("Guess the six numbers between 1 and 49:")
while attempts2 < 6:
    guess2 = int(input())
    attempts2 += 1

    if attempts2 == 6:
        print("Game over!The six numbers were " + str(number11) + "," + str(number22) + "," + str(number33) + "," +
              str(number44) + "," + str(number55) + "," + str(number66) + ".")
        if len(guessed_numbers2) == 1:
            print("Guessed number: " + str(guessed_numbers2))
        else:
            print("Guessed numbers: " + str(guessed_numbers2))

        break

    elif guess2 == number11:
        guessed_numbers2.append(number11)
        print("You guessed correctly!")
        continue
    elif guess2 == number22:
        guessed_numbers2.append(number22)
        print("You guessed correctly!")
        continue
    elif guess2 == number33:
        guessed_numbers2.append(number33)
        print("You guessed correctly!")
        continue
    elif guess2 == number44:
        guessed_numbers2.append(number44)
        print("You guessed correctly!")
        continue
    elif guess2 == number55:
        guessed_numbers2.append(number55)
        print("You guessed correctly!")
        continue
    elif guess2 == number66:
        guessed_numbers2.append(number66)
        print("You guessed correctly!")
    elif guessed_numbers2 == [number11, number22, number33, number44, number55, number66]:
        print("Congratulations!You guessed the six numbers!Your prize is: $750,000.")
        break

# If 'Game2' has already been chosen first.

while attempts1 == 5:
    break
if attempts1 == 0 and attempts2 == 6:
    print("\nThere is one game left: Game1\nTry your luck one more time!\nI'm guessing:")
    while attempts1 < 5:
        guess1 = int(input())
        attempts1 += 1
        if attempts1 == 5:
            print("Game over!The five numbers were " + str(number1) + "," + str(number2) + "," + str(number3) + "," +
                  str(number4) + "," + str(number5) + ".")
            print("Guessed numbers: " + str(guessed_numbers1))
            print("\nGame is over! You tried your chance!")
            break
        elif guess1 == number1:
            guessed_numbers1.append(number1)
            print("You guessed correctly!")
            continue
        elif guess1 == number2:
            guessed_numbers1.append(number2)
            print("You guessed correctly!")
            continue
        elif guess1 == number3:
            guessed_numbers1.append(number3)
            print("You guessed correctly!")
            continue
        elif guess1 == number4:
            guessed_numbers1.append(number4)
            print("You guessed correctly!")
            continue
        elif guess1 == number5:
            guessed_numbers1.append(number5)
            print("You guessed correctly!")
        elif guessed_numbers1 == [number1, number2, number3, number4, number5]:
            print("Congratulations!You guessed the five numbers!Your prize is: $500,000.")
            break
