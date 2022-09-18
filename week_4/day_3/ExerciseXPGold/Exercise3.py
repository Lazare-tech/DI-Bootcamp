# Add Your Own Birthday
# Instructions

#     Add this new code: before asking the user to input a person’s name to look up, ask the user to add a new birthday:
#         Ask the user for a person’s name – store it in a variable.
#         Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
#         Now add this new data into your dictionary.
#     Make sure that if the user types any name that exists in the dictionary – including the name that he entered himself – the corresponding birthday is found and displayed.
birthdays={'jean':'1997/02/14',
           'pierre':'2000/12/25',
           'luc':'1997/03/15',
           'audrey':'2000/05/26',
           'el':'2001/04/16'}

name=input("Entrer votre nom:")
birth=input("Entrer votre date d'anniverssaire yyy/mm/dd:")
birthdays[name]=birth
for cle in birthdays.keys():
    if name==cle:
        print("L'anniverssaire correspondant est trouve: ",birthdays[name])
        break
    else:
        birthdays[name]=birth
        print(birthdays)
