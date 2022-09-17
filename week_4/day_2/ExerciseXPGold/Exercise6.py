# Words and letters
# Instructions

#     Ask a user for 7 words, store them in a list named words.
#     Ask the user for a single character, store it in a variable called letter.
#     Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
#     If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.

words=[]
i=0
while i<6:
    
    words[i]=input("mot:")
    i=i+1
letter=input("Entrer un caractere:")
print(words)