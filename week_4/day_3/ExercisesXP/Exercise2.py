# Cinemax
# Instructions

#     A movie theater charges different ticket prices depending on a person’s age.
#         if a person is under the age of 3, the ticket is free.
#         if they are between 3 and 12, the ticket is $10.
#         if they are over the age of 12, the ticket is $15.

#     Given the following object:

#     family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


#     How much does each family member have to pay ?
#     Print out the family’s total cost for the movies.
#     Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
sum=0
somme=0
for i in family.keys():
    if(family[i]>3 and family[i]<12):
        print( i,"doit payer $10")
        sum=sum+10
    elif(family[i]>=12):
        print(i," doit payer $15")
        somme=somme+15
print("Total a payer: ",sum+somme)
#a variabl empty ,nous allons l'appeler newFamily et on reaplique la meme boucle
#ci dessus
newfamily=dict()
newsum=0
newsomme=0
for i in range(2):
    cle=input("Entrer la cle:")
    valeur=int(input("Entrer valeur du cle:"))
    newfamily[cle]=valeur
print(newfamily)
for i in newfamily.keys():
    if(newfamily[i]>3 and newfamily[i]<12):
        print( i,"doit payer $10")
        newsum=newsum+10
    elif(newfamily[i]>=12):
        print(i," doit payer $15")
        newsomme=newsomme+15
print("Total a payer: ",newsum+newsomme)    