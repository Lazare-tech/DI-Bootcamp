#Longest word without a specific character
while True:
    sentence=input("saisir une phrase sans la lettre A:")
    taille=len(sentence)
    if ('a' in sentence):
        print("Reesayer")
    else:
        print("Bravo!!!")
        break
    
