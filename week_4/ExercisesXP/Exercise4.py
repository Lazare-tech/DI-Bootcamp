
    # Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
    # Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

import random
def rand(number):
    n=random.randint(1,100)
    if(number>=0 and number<=100 and n==number):
        print("Weldone!!!!")
    else:
        print("Loser!!!!")
rand(45)