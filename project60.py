
import sys
win = 0

while True:
    print(f"{win} Wins, 0 Losses, 0 Ties")
    print("Enter your move: (R)ock (P)aper (S)cissors or (Q)uit")
    userMove = input("> ").upper()
    
    if userMove == "Q":
        sys.exit()
    if userMove not in ["R", "P", "S"]:
        print("Type R, P, S, or Q for Quit")
        continue

    if userMove == "R":
        print("ROCK versus...")
    elif userMove == "P":
        print("PAPER versus...")
    elif userMove == "S":
        print("SCISSORS versus...")
    
    print('1...')
    print('2...')
    print('3...')

    if userMove == 'R':
        print('SCISSORS')
    elif userMove == 'P':
        print('ROCK')
    elif userMove == 'S':
        print('PAPER')
    
    print("You win!")
    win += 1