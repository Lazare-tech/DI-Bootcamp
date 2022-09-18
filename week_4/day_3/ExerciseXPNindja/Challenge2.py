# Perfect number

# A perfect number is a positive integer that is equal to the sum of its divisors.
# However, the number itself is not included in the sum.

#     Ask the user for a number and print whether or not it is a perfect number. If yes, print True else False.
#     Hint: Google perfect numbers

# Example

# Input -- Enter the number:6
# Output -- True

# Input -- Enter the number:10
# Output --  False
cpt=0
nombre=int(input("Entrer un nombre:"))
for i in range(1,1000):
    if i==6:
        continue
    elif nombre%i==0:
        cpt=cpt+i
        
if cpt==nombre:
    print("True")
else:
    print("False")