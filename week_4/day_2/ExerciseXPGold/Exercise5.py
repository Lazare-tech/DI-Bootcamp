# The Alphabet
# Instructions

#     Create a string of all the letters in the alphabet
#     Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.
alphabet="abcdefghijklmnopqrstuvwxyz"
for i in range(1,26):
    if(alphabet[i]=='a' or alphabet[i]=='i' or alphabet[i]=='o' or alphabet[i]=='u' or alphabet[i]=='y' or alphabet[i]=='e'):
        print("Voyelle:",alphabet[i])
    else:
        print("Consonne:",alphabet[i])
        