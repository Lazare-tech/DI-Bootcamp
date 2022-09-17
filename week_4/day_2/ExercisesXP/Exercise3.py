# List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print("List complet ",basket)
del basket[0]
print("Banane est suprimer",basket)
del basket[2]
print("Blueberries est surpimier ",basket)
basket.append("kiwi")
print("kiwi est ajouter en fin de liste ",basket)
basket.insert(0,"Apples")
print("Apples est ajoute en debut de liste ",basket)
n=basket.count("Apples")
print("Apples aparait {} fois dans la liste".format(n))
basket.clear()
print(basket)