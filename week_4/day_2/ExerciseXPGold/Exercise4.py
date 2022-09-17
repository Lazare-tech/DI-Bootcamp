# Greatest Number
# Instructions

#     Ask the user for 3 numbers and print the greatest number.

#     Test Data
#     Input the 1st number: 25
#     Input the 2nd number: 78
#     Input the 3rd number: 87

#     The greatest number is: 87

n=int(input("Entrer le premier nombre:"))
n2=int(input("Entrer le second nombre:"))
n3=int(input("Entrer le troisieme nombre:"))
if(n>n2 and n>n3):
    print("The greatest number is:",n)
elif(n2>n and n2>n3):
    print("The greatest number is:",n2)
else:
     print("The greatest number is:",n3)
        

    