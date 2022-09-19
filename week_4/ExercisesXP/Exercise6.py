# Magicians …
# Instructions

#     Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
#     Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
#     Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
#     Call the function make_great().
#     Call the function show_magicians() to see that the list has actually been modified.
newList=[]
def  show_magicians(liste):
    print(liste)
def make_great(liste):
    c="the great"
    for i in range(3):
        newList.append(liste[i]+" "+c)
    print(newList)
    
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
show_magicians(magician_names)
make_great(magician_names)
show_magicians(magician_names)
