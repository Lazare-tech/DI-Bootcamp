# 🌟 Exercice 1 - Générateur De Phrases Aléatoires
# Des Instructions
# Description : Dans cet exercice, nous allons créer un générateur de phrases aléatoires. Nous le ferons en demandant à l'utilisateur la longueur de la phrase, puis en imprimant la phrase générée.

# Astuce : Les phrases générées n'ont pas à avoir de sens.

# Télécharger cette liste de mots

# Enregistrez-le dans votre répertoire de développement.

# Créez une fonction appelée get_words_from_file. Cette fonction doit lire le contenu du fichier et renvoyer les mots sous forme de collection. Quel est le type de données correct pour stocker les mots ?

# Créez une autre fonction appelée get_random_sentencequi prend un seul paramètre appelé length . Le paramètre de longueur sera utilisé pour déterminer le nombre de mots que la phrase doit contenir. La fonction doit :
# utilisez la liste de mots pour obtenir vos mots au hasard.
# le nombre de mots doit être la valeur du paramètre de longueur .

# Prenez les mots au hasard et créez une phrase (en utilisant une méthode python), la phrase doit être en minuscules.

# Créez une fonction appelée mainqui va :

# Imprimer un message expliquant ce que fait le programme.

# Demandez à l'utilisateur combien de temps il souhaite que la phrase dure. Les valeurs acceptables sont : un entier compris entre 2 et 20. Validez vos données et testez votre validation !
# Si l'utilisateur entre des données incorrectes , imprimez un message d'erreur et terminez le programme.
# Si l'utilisateur saisit des données correctes , exécutez votre code.
from collections import deque
import random
import string
d=deque()
def get_words_from_file():
    with open("mot.txt","r") as file:
        lec=file.read()
        d.extend(lec)
    # print(d,end=" ")   
def get_random_sentence(length):
    str=d
    word=[]
    mot=''.join(random.choice(str) for i in range(0,length))
    mot.lower()
    # mot=' '.join(word)

    return mot
def main():
    """Ce programme permet dafficher un mot de 5 lettres de facon
    aleatoire.Ces mots sont choisis aleatoirement dans un fichier et afficher.
    lutilisateur  ala posssibilitede choisir le nombre de mot quil souhaite afficher"""
        
get_words_from_file() 
print("La chaine aleatoire est :",get_random_sentence(5),end=" ")
print("")       
        
        

