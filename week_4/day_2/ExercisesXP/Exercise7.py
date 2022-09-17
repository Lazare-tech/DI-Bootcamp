#Favorite fruits
fruits=input("Saisir vos fruits preferees avec des espaces:")
listeFruits=fruits.split(' ')
print(list(listeFruits))
name_fruit=input("Entrer un nom de fruit :")
if(name_fruit in listeFruits):
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")