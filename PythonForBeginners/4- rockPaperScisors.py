import random

options = ['rock', 'paper', 'scissors']
user_input = input('Choose one (rock, paper, scissors): ').lower()
computer_choice = random.choice(options)

if user_input in options:
    user_choice = user_input
    print(f'You chose: {user_choice}')
    print(f'Computer chose: {computer_choice}')
else:
    print('Invalid choice. Please choose rock, paper, or scissors.')

if (user_choice == computer_choice):
    print('Its a tie')
elif (user_choice == 'rock' and computer_choice == 'scissors'):
    print('You win')
elif (user_choice == 'scissors' and computer_choice == 'paper'):
    print('You win')
elif (user_choice == 'paper' and computer_choice == 'rock'):
    print('You win')
else:
    print('You lose')
