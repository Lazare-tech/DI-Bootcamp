from curses.ascii import isalpha
from anagram_checker import AnagramChecker
class anagram(AnagramChecker):
    def __init__(self,fileName):
        super().__init__(fileName)
    #method
    def menu(self,mot):
        super(anagram,self).is_valid_word(mot)
        # super(anagram,self).get_anagrams(mot)
def main():
    anagramme=anagram("text.txt")
  
    while True:
        print("\tMain")
        print("(e) Entrer un mot")
        print("(x) quitter")
        rep=input("Choisir:")
        if rep=='e':
            mot=input("Entrer un mot:")
            if mot.isalpha():
                anagramme.menu(mot)
            else:
                print("Entrer un mot avec que des lettres")
        else:
            break        
#
main()