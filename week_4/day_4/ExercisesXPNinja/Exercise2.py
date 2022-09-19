# From English to Morse
# Instructions

#     Write a function that converts English text to morse code and another one that does the opposite.
#     Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /
morse = { 'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'J':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..'
                }
#
francais = { '.-':'a', '-...':'b',
                    '-.-.':'c', 'd':'-..', '.':'e',
                    '..-.':'f', 'g':'--.', '....':'h',
                    'i':'..', '.---':'j', '-.-':'k',
                    '.-..':'l', '--':'m', '-.':'n',
                    '---':'o', '.--.':'p', '--.-':'q',
                    '.-.':'r', '...':'s', '-':'t',
                    '..-':'u', '...-':'v', '.--':'w',
                    '-..-':'x', '-.--':'y', '--..':'z'
                }
text=input("Enter an english test:")
liste=[]
for i in range(len(text)):
    for cle in morse.keys():
        if text[i] == cle:
            chaine=morse[cle]
            liste=chaine.split(" ")
            print(" ".join(liste),end=" ")
print(" ")
txt=input("Enter a morse code:")
liste2=[]
for i in range(len(txt)):
    for cle in francais.keys():
        if txt[i] == cle:
            chaine=francais[cle]
            liste2=chaine.split(" ")
            print(" ".join(liste2),end=" ")
