import random
import sys

print("")
choices = {"1": "Rock", "2": "Paper", "3": "Scissors"}
player_scores = 0
computer_scores = 0
turns = 3


while turns > 0:
    player_choice = input(
        "\nEnter ... \n 1) for Rock \n 2) for Paper \n 3) for Scissors \n\n")
    player = int(player_choice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2 or 3")

    computer_choice = random.choice("123")
    computer = int(computer_choice)

    print("")
    print(f"You choose {choices[player_choice]} and Computer choose {
          choices[computer_choice]}")


    if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        player_scores += 1
        turns -= 1
        print(f"You score {player_scores} and computer scores {computer_scores}.")
        
    elif player == computer:
        turns -= 1
        print(f"You score {player_scores} and computer scores {computer_scores}.")
        
    else:
        computer_scores += 1
        turns -= 1
        print(f"You score {player_scores} and computer scores {computer_scores}.")


    if turns == 0:
        print("")
        print("****** You win ******") if player_scores > computer_scores else print("It is a Tie!") if player_scores == computer_scores else print("****** Computer wins ******")
        break