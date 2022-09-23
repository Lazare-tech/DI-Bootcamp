#  Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.
class Dog:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
    #method
    def bark(self):
        return '{} is barking'.format(self.name)
    #method
    def run_speed(self):
        # print("{} running speed {}".format(self.name,self.weight/self.age*10))
        n=self.weight/self.age*10
        return n
    #method
    def fight(self,other_dog):
        weight1=self.weight*self.run_speed()
        weight2=other_dog.weight*self.run_speed()
        if weight1>weight2:
            print("{} est le plus fort".format(self.name))
        elif(weight1<weight2):
            print("{} est le plus fort ".format(other_dog.name))
       
        
      

#instance
dogOne=Dog("moul",22,10)
dogTwo=Dog("milou",20,12)
dogFree=Dog("Berk",30,16) 
dogOne.run_speed()
dogTwo.run_speed()
dogOne.fight(dogTwo)
n=dogOne.bark()
print(n)