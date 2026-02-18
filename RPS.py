# utline: Create a program to play rock, paper, and scissors. Use a random module to select from the given options Check whether the random guess matches the user’s answer

import random

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_action = ["rock", "paper", "scissors"] 
    computer_action = random.choice(possible_action)
    print(f"\nYou chose{user_action}, computer chose {computer_action}.\n")
    
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors. You win!")
        else: 
            print("paper cover rock, you lose!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper cover rock, you win!")
        else:
            print("scissor cuts paper, you lose!")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissor cuts paper, you win!")
        else:
            print("Rock smashes scissors. You lose!")
            
    play_again = input("Play Again? (y/n): ")
    if play_again != "y":
        break