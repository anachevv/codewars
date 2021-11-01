import random

number = random.randint(1,10)
attempts = 0
print("Guess the secret number between 1 and 10:")
while attempts < 5:
    guess = int(input())
    attempts += 1
    if attempts == 5:
        break
    if guess < number:
        print("Your guess is smaller than the secret number!")
    elif guess > number:
        print("Your guess is greater than the secret number!")
    elif guess == number:
        break

if guess == number and attempts > 1:
    print("You guessed the secret number in " + str(attempts) + " tries!")
if guess == number and attempts == 1:
    print("You guessed the secret number from the first time!")
else:
    print("Game Over! The secret number was " + str(number) + ".")
