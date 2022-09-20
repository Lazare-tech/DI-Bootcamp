# Chiens
# Des Instructions
# Créez une classe appelée Dog.
# Dans cette classe, créez une __init__méthode qui prend deux paramètres : nameet height. Cette fonction instancie deux attributs, dont les valeurs sont les paramètres.
# Créez une méthode appelée barkqui imprime la chaîne suivante " <dog_name>va woof!".
# Créez une méthode appelée jumpqui imprime la chaîne suivante " <dog_name>saute <x>en cm de haut!". xest le height*2.
# En dehors de la classe, créez un objet appelé davids_dog. Le nom de son chien est « Rex » et sa taille est de 50 cm.
# Affichez les détails de son chien (c'est-à-dire nameet height) et appelez les méthodes barket jump.
# Créez un objet nommé sarahs_dog. Le nom de son chien est "Teacup" et sa taille est de 20 cm.
# Imprimez les détails de son chien (c'est-à-dire nameet height) et appelez les méthodes barket jump.
# Créez une instruction if en dehors de la classe pour vérifier quel chien est le plus grand. Imprimez le nameplus gros chien.
class Dog:
    def __init__(self,name,height):
        self.name=name
        self.height=height
    #
    def bark(self):
        print("{} va woof!!!".format(self.name))
    #
    def jump(self):
        print("{} saute de {} cm de haut".format(self.name,self.height*2))
        print("")

#method en dehors d la classe
def plus_grand():
    if davids_dog.height>sarahs_dog.height:
        print("Le plus gros chien est ",davids_dog.name)
    else:
        print("Le plus gros chien est ",sarahs_dog.name)
davids_dog=Dog("Rex",50)
davids_dog.bark()
davids_dog.jump() 
#objet sarah dog
sarahs_dog=Dog('Teacup',20)
#apel des methods
sarahs_dog.bark()
sarahs_dog.jump()       
plus_grand()
        