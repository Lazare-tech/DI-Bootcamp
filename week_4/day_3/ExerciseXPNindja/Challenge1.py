# chaine=input("Entrer chaine")
chaine="You have entered a wrong domain"
conver=[]
conver=chaine.split(' ')
taille=len(conver)
newChaine=[]
print(conver)

while taille!=0:
    newChaine=conver[taille-1]
    print("".join(map(str,newChaine)))
    taille=taille-1