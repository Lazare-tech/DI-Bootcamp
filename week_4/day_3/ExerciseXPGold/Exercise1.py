#  Birthday Look-up
# Instructions

#     Create a variable called birthdays. Its value should be a dictionary.
#     Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.
#     Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”“
#         Ask the user to give you a person’s name and store the answer in a variable.
#         Get the birthday of the name provided by the user.
#         Print out the birthday with a nicely-formatted message.
birthdays={'jean':'1997/02/14',
           'pierre':'2000/12/25',
           'luc':'1997/03/15',
           'audrey':'2000/05/26',
           'el':'2001/04/16'}
print("Bievenue,vous pouvez voir les anniverssaires des personnes dans la liste ci-dessous")
print(birthdays)
name=input("Entrer un nom:")
for cle in birthdays.keys():
    if name==cle:
        print("The birthday of ",cle)
        print("-------",birthdays[name],"------")
        print("--------------------------------")
    else:
        print("Ce nom n'est pas dans notre dictionnaire")