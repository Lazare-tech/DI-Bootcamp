# 🌟 Exercice 3 : Qui Est Le Producteur De La Chanson ?
# Des Instructions
# Définissez une classe appelée Song, elle affichera les paroles d'une chanson.
# Sa __init__()méthode doit avoir deux arguments : selfet lyrics(une liste).
# Dans votre classe, créez une méthode appelée sing_me_a_songqui imprime chaque élément de lyricssur sa propre ligne.
# Créez un objet, par exemple :

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


# Ensuite, appelez la sing_me_a_songméthode. La sortie doit être :

# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven
class Song:
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for i in range(3):
            print(self.lyrics[i])
#creation de lobjet        
   
stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()
