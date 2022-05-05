#stone paper scissors
#
from random import choice


# rules
WIN_RULES = {
    'stone': 'scissors',
    'paper': 'stone',
    'scissors': 'paper',
    'lizard': 'spok',
    'spok': 'scissors'
}
#     'stone': 'lizard',
#     'paper': 'spok',
#     'scissors': 'paper',
#     'lizard': 'paper',
#     'spok': 'stone'

# # get data from user
def get_user_choice():
    while True:
        user_choice = input('Enter your choice: stone, paper, scissors, spok or lizard): ')
        if user_choice not in WIN_RULES.keys():
            print('Enter only: stone, paper, scissors, spok or lizard')
            continue
        else:
             return user_choice


 # get data from computer
def get_computer_choice():

    computer_choice = choice(['stone', 'paper', 'scissors', 'lizard', 'spok'])
    return computer_choice

# # define winner
def get_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        msg = 'Draw'
    elif WIN_RULES[user_choice] == computer_choice:
        msg = 'User'
    else:
        msg = 'Computer'

    return msg


# make message
def make_message(user_choice, computer_choice, winner):
    msg = f'User choice is {user_choice}, PC choice is {computer_choice}. Winner is {winner}'
    return msg


def main():
    for i in range(1, 4):
        print(f'Try {i}')
        user_choice = get_user_choice()

        computer_choice = get_computer_choice()

        winner = get_winner(user_choice, computer_choice)

        msg = make_message(user_choice, computer_choice, winner)

        print(msg)


main()



