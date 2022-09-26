# Des Instructions :
# Le but de l'exercice est de créer une classe qui vous aidera à analyser un texte spécifique. Un texte peut être juste une simple chaîne, comme "Aujourd'hui, c'est un jour heureux" ou il peut s'agir d'un fichier texte externe.



# Première Partie
# Tout d'abord, nous analyserons une chaîne simple, comme "Un bon livre coûterait parfois autant qu'une bonne maison".

# Créez une classe appelée Textqui prend une chaîne comme argument et stockez le texte dans un attribut.
# Astuce : Vous devez copier-coller manuellement le texte, directement dans le code

# Implémentez les méthodes suivantes :
# une méthode pour renvoyer la fréquence d'un mot dans le texte (en supposant que les mots sont séparés par des espaces) return Noneou un message significatif.
# une méthode qui renvoie le mot le plus courant dans le texte.
# une méthode qui renvoie une liste de tous les mots uniques dans le texte.


# Partie II
# Ensuite, nous analyserons un texte provenant d'un fichier texte externe. Téléchargez le fichier_inconnu.txt .

# Implémentez a classmethodqui renvoie une Textinstance mais avec un fichier texte :

#     >>> Text.from_file('the_stranger.txt')
# Astuce : Vous devez ouvrir et lire le texte du fichier texte.


# Maintenant, utilisez le the_stranger.txtfichier fourni et essayez d'utiliser la classe que vous avez créée ci-dessus.



# Prime:
# Créez une classe appelée TextModificationqui hérite de Text.

# Implémentez les méthodes suivantes :
# une méthode qui renvoie le texte sans aucune ponctuation.
# une méthode qui renvoie le texte sans aucun mot vide en anglais (regardez ce que c'est !!).
# une méthode qui renvoie le texte sans aucun caractère spécial.
# Remarque : N'hésitez pas à implémenter/créer n'importe quel attribut, méthode ou fonction nécessaire pour que cela fonctionne, soyez créatif :)
from typing import Counter


class Text:
    def __init__(self,chaine):
        self.chaine=chaine
    #method
    def frequency(self):
        str=self.chaine.split(' ')
        str2=[]
        for i in str:
            if i not in str2:
                str2.append(i)
        for i in range(0,len(str2)):
            print("Frequence de ",str2[i],'de:',str.count(str2[i]))
    #method
    def current_word(self):
        str=self.chaine.split(' ')
        f=Counter(str)
        max=0
        word=[]
        for i in f:
            if(f[i]>max):
                max=f[i]
                word=i
        print("Mot le plus courant:",word)
    #method
    def unique_word(self):
        str=self.chaine.split(' ')
        str2=[]
        for i in str:
            if i not in str2:
                str2.append(i)
        print("Mot dans doublons:",end=" ")
        for i in range(0,len(str2)):
            print(str2[i],end=" ")
        print("")
    @classmethod
    def from_file(cls,nom_fichier):
        with open(nom_fichier,"r") as file:
            print(file.read())
            
#instance
text=Text("al so me lo al me me me")
text.frequency()
text.current_word()
text.unique_word()
# file=Text()
# file.from_file('theStranger_text_W5D4PY/the_stranger.txt')
Text.from_file('theStranger_text_W5D4PY/the_stranger.txt')