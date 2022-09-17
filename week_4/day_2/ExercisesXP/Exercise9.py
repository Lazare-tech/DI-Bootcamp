#: Cinemax
age=int(input("Entrer votre age:"))
movie=["commedie","aventure","fiction","action","romance",'feuilleton']
somme=0
if(age<3):
    somme =somme+0
    print(movie[4])
elif(age>=3 and age<=12):
    somme=somme+10
    print("Vous pouvez suivre ",movie[1:4])
elif (age>12):
    somme=somme+15
    print("Vous pouvez suivre ",movie)

print("Somme a payer ",somme)