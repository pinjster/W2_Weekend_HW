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
    valid_choices = ["rock", "paper", "scissors", "lizard", "spock"]
    while True:
        user_choice = input("Enter your choice: rock/paper/scissors/spock/lizard:  ").lower()
        for item in list_choices: 
            if user_choice == item['name'].lower():
                return item
        print("Invalid Choices. Sorry, please try again.")
        continue

def random_choice():
    computer_choice = random.choice(list_choices)
    return computer_choice
    
def determine_winner(user_ch, comp_ch):
    global player_score , computer_score
    print(f"You chose {user_ch['name']} {user_ch['emoji']}")
    print(f"The computer chose {comp_ch['name']} {comp_ch['emoji']}")
    if user_ch['name'] == comp_ch['name']:
        return 'Game Tied'
    
    elif (user_ch['name'] == 'Rock' and comp_ch['name'] == 'Scissors'):
        print_outcome(rock, 'scissors')
        player_score += 1
        return 'You Win!'
    elif (user_ch['name'] == 'Rock' and comp_ch['name'] == 'Lizard'):
        print_outcome(rock, 'lizard')
        player_score += 1
        return 'You Win!'
    elif (user_ch['name'] == 'Paper' and comp_ch['name'] == 'Rock'):
        print_outcome(paper, 'rock')
        player_score += 1
        return 'You Win!'
    elif (user_ch['name'] == 'Paper' and comp_ch['name'] == 'Spock'):
        print_outcome(paper, 'spock')
        player_score += 1
        return 'You Win!'
    elif (user_ch['name'] == 'Scissors' and comp_ch['name'] == 'Paper'):
        print_outcome(scissors, 'paper')
        player_score += 1
        return 'You Win!'
    elif (user_ch['name'] == 'Scissors' and comp_ch['name'] == 'Lizard'):
        print_outcome(scissors, 'lizard')
        player_score += 1
        return 'You Win!'
    elif (user_ch['name'] == 'Spock' and comp_ch['name'] == 'Rock'):
        print_outcome(spock, 'Rock')
        player_score += 1
        return 'You Win!'
    elif (user_ch['name'] == 'Spock' and comp_ch['name'] == 'Scissors'):
        print_outcome(spock, 'scissors')
        player_score += 1
        return 'You Win!'
    elif (user_ch['name'] == 'Lizard' and comp_ch['name'] == 'Paper'):
        print_outcome(lizard, 'paper')
        player_score += 1
        return 'You Win!'
    elif (user_ch['name'] == 'Lizard' and comp_ch['name'] == 'Spock'):
        print_outcome(lizard, 'spock')
        player_score += 1
        return 'You Win!'
    else:
        print_outcome(comp_ch, user_ch['name'].lower())
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

def print_outcome(dict, choice):
    print(dict[choice])

#main body        
print( "Welcome to our rock, paper, scissors!")
print(paper['emoji'], rock['emoji'], scissors['emoji'], spock['emoji'], lizard['emoji'])

while True:
    user_choice = play_game()
    comp_choice = random_choice()
    outcome = determine_winner(user_choice, comp_choice)
    print(outcome)
    print(f"Score: {player_score}-{computer_score}")
    still_playing()
   