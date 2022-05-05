from random import choice
from Homework7 import get_user_choice, get_computer_choice, get_winner, make_message



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



def main():
    for i in range(1, 4):
        print(f'Try {i}')
        user_choice = get_user_choice()

        computer_choice = get_computer_choice()

        winner = get_winner(user_choice, computer_choice)

        msg = make_message(user_choice, computer_choice, winner)

        print(msg)


main()


