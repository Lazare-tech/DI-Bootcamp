# 🌟 Exercise 2: Random Module
# Instructions
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.
import random
def rand(n):
    m=random.randint(1,100)
    if n==m:
        print("Success!!!!")
    else:
        print("Game over!!!")
        
nombre=int(input("Entrer un nombre:"))
while True:

    if(nombre>=1 and nombre<=100):
        rand(nombre)
        break
    else:
        nombre=int(input("Entrer un nombre compris entre 1 et 100:"))