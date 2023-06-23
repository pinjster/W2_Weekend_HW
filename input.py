import random
from list import *
# #
# """
# Import Random
# Rock, Paper, scissors:
# Integrate scoring system:
# Input Validation:
# Computer-player: Random
# Prompt User:
# Display Results: "Game Tied", "You Win!" "You Lose."
# """
player_score = 0 
computer_score = 0

def play_game():
    valid_choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Enter your choice: rock/paper/scissors:  ").lower()
        if user_choice in valid_choices:
            return user_choice
        else:
            print("Invalid Choices. Sorry, please try again.")
            continue

def random_choice():
    computer_choice = random.choice(list_choices)
    return computer_choice
    
def determine_winner(user_ch, comp_ch):
    global player_score , computer_score
    print(f"You chose {user_ch}")
    print(f"The computer chose {comp_ch['name']}")
    if user_ch == comp_ch['name'].lower():
        return 'Game Tied'
    
    elif (
        (user_ch == 'rock' and comp_ch['name'] == 'Scissors') or
        (user_ch == 'paper' and comp_ch['name'] =='Rock') or
        (user_ch =='scissors' and comp_ch['name'] =='Paper') 
    ):
        player_score += 1
        return 'You Win!'
    else:
        computer_score += 1
        return "You Lose!"
    
def still_playing():
    while True:
        user_input = input("Keep playing? Y or N ").lower()
        if user_input == 'y':
            break
        elif user_input == 'n':
            print(f"Your score was: {player_score}-{computer_score}")
            print("Thanks for playing!")
            quit()
        else:
            print("Invalid input. Please try again! ")
            continue


#main body        
print( "Welcome to our rock ,paper, scissors!")
while True:
    user_choice = play_game()
    comp_choice = random_choice()
    outcome = determine_winner(user_choice, comp_choice)
    print(outcome)
    print(f"Score: {player_score}-{computer_score}")
    still_playing()
   