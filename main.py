import random

def play():
    while True:
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors (or 'q' to quit): ")
        
        if user == 'q':
             print("Thanks for playing!")
             break
        if user not in ['r', 'p', 's']:
             print("Invalid choice, please try again")
             continue
        
        computer = random.choice(['r', 'p', 's'])
        print(f"Computer {computer} vs {user} You")
        if user == computer:
            print('Tie\n')
    
        elif is_win(user, computer):
            print('You won!\n')
            
        else:
            print('You lost!\n')

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
            return True
    
play()