#  Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }

# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)
class Zoo:
    def __init__(self,zoo_name):
        self.zoo_name=zoo_name
        self.animals=[]
        self.name=zoo_name
    #method
    def add_animal(self,new_animal):
        if (new_animal not in self.animals):
            self.animals.append(new_animal)
    #method
    def get_animals(self):
        print("Animals of the zoo:.",self.animals)
    #method
    def sell_animal(self,animal_sold):
        for i in range(len(self.animals)):
            if(animal_sold== self.animals[i]):
                del self.animals[i]
        print("Le {} a ete suprimer ".format(animal_sold))
        print("Nouvelle liste ",self.animals)
    #method
    def sort_animals(self):
        # trie=[]
        liste=sorted(self.animals)
        dico=dict()
        i=0
        for i in range(len(liste)):
            dico[i]=liste[i]
            # nom=self.animals[i]
            # for i in range (len(self.animals)):
            #         if nom[0]==self.animals[i][0] and nom!=self.animals[i]:   
            #             liste.append(self.animals[i])
            #             dico[i]=liste
            #             # liste.append(nom)
            #         # trie=sorted(liste)
            #             # dico[i]=liste
            #         else:
            #             # liste.append(nom)
            #             dico[i]=self.animals[i]
        print(dico)
    #method
    # def get_groups(self):
    #     self.sort_animals()
#object
ramat_gan_safari=Zoo("Gan_Safari")

ramat_gan_safari.add_animal("Girafe")
ramat_gan_safari.add_animal("Chien")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.add_animal("Cougar")


ramat_gan_safari.add_animal("Chat")

ramat_gan_safari.get_animals()
#on retire chat
ramat_gan_safari.sell_animal("Chat")
#trie des animaux
ramat_gan_safari.sort_animals()
# ramat_gan_safari.get_groups()