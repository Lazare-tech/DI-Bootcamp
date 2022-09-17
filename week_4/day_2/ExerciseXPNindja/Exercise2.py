# List of integers
# Instructions

# Given a list of 10 integers to analyze. For example:

#     [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
#     [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
#     [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
#     [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

#     Store the list of numbers in a variable.
#     Print the following information:
#     a. The list of numbers – printed in a single line
#     b. The list of numbers – sorted in descending order (largest to smallest)
#     c. The sum of all the numbers
#     A list containing the first and the last numbers.
#     A list of all the numbers greater than 50.
#     A list of all the numbers smaller than 10.
#     A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
#     The numbers without any duplicates – also print how many numbers are in the new list.
#     The average of all the numbers.
#     The largest number.
#     10.The smallest number.
#     11.Bonus: Find the sum, average, largest and smallest number without using built in functions.
#     12.Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each number should be added into a variable that you created earlier.
#     13.Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.
#     14.Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
#     15.Bonus: Will the code work when the number of random numbers is not equal to 10?
import math
from random import random
from random import randint
liste=[3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
taille=len(liste)
sum=0
n=[]
print("liste des nombres:",liste)
liste.sort(reverse=True)
print("Trie par odre decroissant:",liste)
for i in range(len(liste)):
    sum=sum+liste[i]
print("Somme liste:",sum)
print("Premier nombre de la liste: {} et le dernier nombre:{}".format(liste[0],liste[taille-1]))
print("Les nombres superieures a 50 de la liste:")
for i in range(taille):
    if(liste[i]>50):
        print(liste[i])    
print("Les nombres inferieures a 10 de la liste:")
for i in range(taille):
    if(liste[i]<10):
        print(liste[i])
print("Racine carre des nombres positifs de la liste:")
for i in range(taille):
    if(liste[i]>0):
        print(math.sqrt(liste[i]))
moyenne=sum/taille
print("Moyenne des nombres de la liste:",moyenne)
print("La plus grande valeur de la liste:",max(liste))
print("La plus petite valeur de la liste:",min(liste))
            #   11.Bonus: Find the sum, average, largest and smallest number without using built in functions.
            #la somme calculer ,la moyenne ci haut nest pas usage dune fonction de  python
            #on calculera la taille
# cpt=0
# for i in range(20):
#     if(liste[i]==''):
#         break
#     else:
        
#         cpt=cpt+1
# print("Taille de la liste est: ",cpt)
min=0
for i in range(taille):
    if(liste[i]>min):
        min=liste[i]
print("La plus grande valeur est :",min)
max=0
for i in range(taille):
    if(liste[i]<max):
        max=liste[i]
print("La plus petite valeur est :",max)
#12BONUS
list2=[]

for i in range(0,9):
    n=int(input("Entrer un nombre compris entre -100 et 100:"))
    list2.append(n)
print("List remplie avec ds nombres saisies par lutilisateur:",list2)

for i in range(0,9):
    n=randint(-100,100)
    list2.append(n)
    break
print("List remplie avec ds nombres aleatoire:",list2)
#Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
for i in range(0,9):
    n=randint(50,100)
    list2.append(n)
print("List remplie avec ds nombres aleatoire:",list2)
    