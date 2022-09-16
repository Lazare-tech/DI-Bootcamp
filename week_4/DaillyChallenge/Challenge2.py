
#     Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

# Examples

# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"
chaine=input("Entrer une chaine:")
taille=len(chaine)
cpt=0
newChaine=[]
for i in range(taille):
    c=chaine[i]
    if chaine[i]==c:
        cpt=cpt+1
        if(cpt>2):
            
            newChaine=chaine[i]
            print(newChaine)
