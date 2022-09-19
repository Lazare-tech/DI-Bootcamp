chaine=input("Entrer une chaine de caractere separe par des virgules:")
convert=chaine.split(",")
taille=len(convert)
n="*"
c=0
long=0
print(convert)
for i in range(len(convert)):
    if (len(convert[i]) > long):
        long=len(convert[i])
      

print(long)
print("************")
for i in range(len(convert)):
    marge=(long+1)-len(convert[i])
    espace=" "
    print("* "+ convert[i] + espace+"*")


    for i in range(marge):
        espace=espace+" "
     
#   if(convert[i].length>convert[i+1].length){

print("************")





