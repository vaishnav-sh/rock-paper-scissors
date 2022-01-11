actions = ['rock', 'paper', 'scissors'];

import random

user_input = input("Enter 0 for rock, 1 for paper, 2 for scissors: ");
user_action = actions[int(user_input)]
comp_action = random.choice(actions);
print(f'You chose {user_action}, Computer chose {comp_action}');

if user_action == comp_action:
    print("IT'S A DRAW!")
elif user_action == 'rock' and comp_action == 'paper':
    print("YOU WIN!")
elif user_action == 'paper' and comp_action == 'rock':
    print("YOU WIN!")
elif user_action == 'scissors' and comp_action == 'paper': 
    print('YOU WIN!');
elif user_action == 'rock' and comp_action == 'paper':
    print('YOU LOSE!');
elif user_action == 'paper' and comp_action == 'scissors':
    print('YOU LOSE!');
elif user_action == 'scissors' and comp_action == 'rock':
    print('YOU LOSE!');
