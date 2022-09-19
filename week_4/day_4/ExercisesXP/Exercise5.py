# 🌟 Exercise 5 : Let’s create some personalized shirts !
# Instructions

#     Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
#     The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
#     Call the function make_shirt().

#     Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
#     Make a large shirt with the default message
#     Make medium shirt with the default message
#     Make a shirt of any size with a different message.

#     Bonus: Call the function make_shirt() using keyword arguments.
def  make_shirt(size,text):
    if size<16:
        print("The size of the shirt is ",size,"and the text is ",text)
    elif size>=16 and size<=22:
           print("The size of the shirt is ",size,"and the text is ",text)
    else:
        text="I love Django"
        print("The size of the shirt is ",size,"and the text is ",text)

make_shirt(size=12,text="I love python") 
#function modifed
