import random
print('Feel free to stop the game at anytime by typing [q]')
#choices for game rock, paper, or scissors
choices=['r','p','s']
#computers random choice
computer = random.choice(choices)
#loop to start the game
while True:
    #users input
    user=input('choose your weapon; [r]ock, [p]aper, [s]cissors: ').lower()
    #multiple if statments that represent possible outcomes and the actions that should happen
    if user == 'r' and computer =='p':
        print('Sorry try again :(')
    elif user == 'r' and computer =='s':
        print('congrats you won!')
        print('Play again?')
        user=input('[y]es, [n]o: ')
        if user == 'y':
            continue
        elif user == 'n':
            break
        elif user == 'q':
            print('Thanks for playing')
            break
    elif user == 'r' and computer =='r':
        print('I\'ts a draw')
    elif user == 'p' and computer =='s':
        print('Sorry try again :(')
    elif user == 'p' and computer =='r':
        print('congrats you won!')
        print('Play again?')
        user=input('[y]es, [n]o: ')
        if user == 'y':
            continue
        elif user == 'n':
            break
        elif user == 'q':
            print('Thanks for playing')
            break
    elif user == 'p' and computer =='p':
        print('I\'ts a draw')
    elif user == 's' and computer =='r':
        print('Sorry try again :(')
    elif user == 's' and computer =='p':
        print('congrats you won!')
        print('Play again?')
        user=input('[y]es, [n]o: ')
        if user == 'y':
            continue
        elif user == 'n':
            break
        elif user == 'q':
            print('Thanks for playing')
            break
    elif user == 's' and computer =='s':
        print('I\'ts a draw')
    else:
        if user == 'q':
            print('Thanks for playing')
            break 
