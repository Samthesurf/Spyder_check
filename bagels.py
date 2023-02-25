import random as rn
print('Bagels, a deductive logic game.\nBy Samuel Ukpai')
guess = input('''\nI am thinking of a 3-digit number. Try to guess what it is.\n Here are some clues
 When I say:    That means: \n  Pico        One digit is correct but in the wrong position.
  Fermi       One digit is correct and in the right position. \n  Bagels      No digit is correct.\n
 I have thought of a number.\n You have 10 guesses for it.\n Guess # ''')

def bagels(x):
    list_3d = [y for y in range(100,1000)]
    x = str(rn.randrange(100,1000,1))
    for i in x:
        if guess == x:
            print('Pico')
        else:
            print('Bagels')
bagels(guess)