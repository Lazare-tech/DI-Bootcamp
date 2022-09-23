# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.
from unicodedata import name
from Exercise2 import Dog
import random
class PetDog(Dog):
    def __init__(self,name,age,weight):
        super().__init__(name,age,weight)
        self.trained=True
    #method
    def train(self,dog):
        super(PetDog,self).bark()
        self.trained=True
    #method
    def play(self,*args):
        print(args)
    #method
    def do_a_trick(self):
        sentence=["does a barrel roll", "stands on his back legs","shakes your hand","plays dead"]
        taille=len(sentence)
        if self.trained==True:
            n=random.randint(0,taille)
            print("{} {}".format(self.name,sentence[n]))
        

    
dogOne=PetDog("moul",22,12)
dogTwo=PetDog("milou",11,20)
dogFree=PetDog("Berk",10,13)         

# dogOne=PetDog("moul")
dogOne.do_a_trick()   
# dogTwo.do_a_trick()     
# petdog.do_a_trick()    