# 🌟 Exercise 1: Cats
# Instructions
# Using this class

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
        print("{} age {}".format(self.name,self.age))
        
    def ancien(self):    
        if catOne.age>catTwo.age and catOne.age>catFree.age:
            print("Le chat le plus age est {} et a ".format(catOne.name,catOne.age))
        elif (catTwo.age>catOne.age and catTwo.age>catFree.age):
            print("Le chat le plus age est {} et a {}".format(catTwo.name,catTwo.age))
        else:
                print("Le chat le plus age est {} et a {}".format(catFree.name,catFree.age))


catOne= Cat("miuous",12)
catTwo=Cat("Chip",24)
catFree=Cat("Sirt",31)
catOne.ancien()