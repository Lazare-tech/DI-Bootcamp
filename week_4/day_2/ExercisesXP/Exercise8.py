#Who ordered a pizza ?
n=0
pizza=set ()
while True:
    pizza=input("Entrer des garnitures de pizza:")
    if(pizza=='quit'):
        break
    n = n+ 10+2.5
    print("pizza)
print("Prix total est ",n)