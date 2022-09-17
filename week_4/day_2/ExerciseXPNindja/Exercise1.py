#  Formula
# Instructions

#     Write a program that calculates and prints a value according to this given formula:
#     Q = Square root of [(2 * C * D)/H]
#     Following are the fixed values of C and H:
#         C is 50.
#         H is 30.
#     Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results

# For example, if the user inputs: 100,150,180
# The output should be:

# 18,22,24
import math
tabNombre=[]
q=[]
C=50
H=30
nombre=input("Entrer trois nombres separes par des virgules:")
tabNombre=nombre.split(',')
intNombre=list(map(int,tabNombre))
print(intNombre)
for i in range(len(tabNombre)):
    res=(2*C*intNombre[i])//H
    q=math.sqrt(res)
    print(q)