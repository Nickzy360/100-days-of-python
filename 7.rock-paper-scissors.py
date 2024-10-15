import random
choice_list = ['rock', 'paper','scissors']
print("let's play rock, paper, scissors.")
choice = random.choice(choice_list)
player = input("input your choice: rock, paper or scissors? ")
if player == 'rock' and choice == 'scissors' or player == 'paper' and choice == 'rock' or player == 'scissors' and choice == 'paper':
    print("You win")
elif player == choice:
    print("Tie")
elif player == 'scissors' and choice == 'rock' or player == 'rock' and choice == 'paper' or player == 'paper' and choice == 'scissors':
    print('You lost')
print("I chose", choice)    