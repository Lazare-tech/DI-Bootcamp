#  Birthdays Advanced
# Instructions

#     Before asking the user to input a person’s name print out all of the names in the dictionary.
#     If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the birthday information for <person’s name>”)


birthdays={'jean':'1997/02/14',
           'pierre':'2000/12/25',
           'luc':'1997/03/15',
           'audrey':'2000/05/26',
           'el':'2001/04/16'}
print("All bithday:",birthdays)
name=input("Entrer un nom:")
for cle in birthdays.keys():
    if name==cle:
        print("The birthday of ",cle)
        print("-------",birthdays[name],"------")
        print("--------------------------------")
    else:
        print("Sorry, we don't have the birthday information for",name)
        break
        