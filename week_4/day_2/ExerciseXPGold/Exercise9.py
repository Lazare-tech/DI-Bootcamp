#  Random number
# Instructions

#     Ask the user to input a number from 1 to 9 (including).
#     Get a random number between 1 and 9. Hint: random module.
#     If the user guesses the correct number print a message that says Winner.
#     If the user guesses the wrong number print a message that says better luck next time.
#     Bonus: use a loop that allows the user to keep guessing until they want to quit.
#     Bonus 2: on exiting the loop tally up and display total games won and lost.
from random import *
print("................................")
print("Pour abandonner le jeu taper -1")
print("................................")
nombre=int(input("Entrer un nombre compris entre 0 et 9:"))
aleatoire=randint(0,9)
print(aleatoire)

while True:
    if(nombre!=aleatoire and nombre!=-1):
        nombre=int(input("Reesayer:"))
    elif(nombre==aleatoire):
        print("Winner")
        break
    elif(nombre== -1):
        break