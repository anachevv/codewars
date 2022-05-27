import random

player = 0
computer = 0

print("Three points win the game!")

while player < 3 and computer < 3:
    computer_choice = random.choice(["rock","paper","scissors"])
    player_choice = input("Rock, Paper or Scissors: ")

    print(f"Computer: {computer_choice} VS Player: {player_choice}")

    if player_choice.lower() == computer_choice:
        print("Tie!No points!")
    elif player_choice.lower() == "rock":
        if computer_choice == "scissors":
            player += 1
            print(f"Player wins!One point!")
        elif computer_choice == "paper":
            computer += 1
            print("Computer wins!One point!")

    elif player_choice.lower() == "scissors":
        if computer_choice == "paper":
            player += 1
            print(f"Player wins!One point!")
        elif computer_choice == "rock":
            computer += 1
            print(f"Computer wins!One point!")

    elif player_choice.lower() == "paper":
        if computer_choice == "rock":
            player += 1
            print(f"Player wins!One point!")
        elif computer_choice == "scissors":
            computer += 1
            print(f"Computer wins!One point!")
    else:
        print("Invalid input!New round!")

print("PLayer wins!" if player > computer else "Computer wins!")
