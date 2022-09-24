# Exercice 7 : Vacances À Venir
# Des Instructions
# Écrivez une fonction qui affiche la date du jour.
# La fonction doit également afficher le temps restant jusqu'aux prochaines vacances à venir et imprimer de quelles vacances il s'agit. ( Exemple : le prochain jour férié est dans 30 jours et 12:03:45 heures).
# Astuce : commencez par coder en dur la date et l'heure et le nom des vacances à venir.

from datetime import date
import datetime
def dateVac(date1,date2):
    d=(date1-date2).days
    heure=219*24
    second=86400*219
    minutes=d*1440
    return "{} jours et dans {}h:{}m:{}s".format(d,heure,minutes,second,"secondes")  
#apel de la fonction
y=datetime.datetime.now().year
m=datetime.datetime.now().month
d=datetime.datetime.now().day  
date1=date(2023,5,1)    
date2=date(y,m,d)
print("Les prochains vacances sont dans :",dateVac(date1,date2))