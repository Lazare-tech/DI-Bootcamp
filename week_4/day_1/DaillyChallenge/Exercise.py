# Build up a string
chaine=input("Saisir une chaine de caractere:")
taille=len(chaine)
if(len(chaine)<10):
    print("La chaine est trop courte")
else:
    print("La chaine est trop longue")
print("premier caractere "+chaine[0]+" dernier caractere "+chaine[taille-1])
for i in range(taille+1):
    print(chaine[0:i]+"\n")
    