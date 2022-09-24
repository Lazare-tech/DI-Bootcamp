# Exercice 5 : Temps Restant Jusqu'au 1er Janvier
# Des Instructions
# Créez une fonction qui affiche le temps restant jusqu'au 1er janvier.
# ( Exemple : le 1er janvier est dans 10 jours et 10:34:01heures).
from datetime import date

def dateNaiss(date1,date2):
    n= (date2-date1).days
    min=n*1330
    return min
#date de user
date1= date(2018, 12, 13)
#calcul a partir de lannee actuelle
date2 = date(2022, 1, 1)
print("Vous avez vecu",dateNaiss(date1, date2), "minutes")    