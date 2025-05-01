import random, sys
purse = 5000
while True: 
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot) 
            break  
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print('    EVEN or  ODD ?')
    while True:
        bet = input('> ').upper()
        if bet != 'EVEN' and bet != 'ODD':
            print('Please enter either "EVEN" or "ODD".')
            continue
        else:
            break
    print('The dealer lifts the cup to reveal:')
    print('    ', dice1, '-', dice2)
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'EVEN'
    else:
        correctBet = 'ODD'
    playerWon = bet == correctBet
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot  
        print('The house collects a', pot // 10, 'mon fee.')
        purse = purse - (pot // 10)  
    else:
        purse = purse - pot  
        print('You lost!')
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
