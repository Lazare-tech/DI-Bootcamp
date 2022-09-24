# Exercice 1 : Fonctions Intégrées
# Des Instructions
# Python a de nombreuses fonctions intégrées.
# Si vous pensez que vous ne savez pas comment les implémenter correctement, consultez la documentation Python en ligne.

# Écrivez un programme qui imprime les résultats des fonctions intégrées python suivantes : abs(), int(), input().
# En utilisant la __doc__méthode dunder créez votre propre documentation qui explique l'exécution de votre code. Jetez un oeil à la méthode doc sur google pour obtenir de l'aide.
import math
def valeur_absolue(n):
    """Ce programme  permet de calculer les valeurs absolues
    il prend un nombre saisie par l'utilisateur,le convertit en entier
    ce nombre est ensuite passer en parametre dans une fonction qui
    retourne la valeur absolue du nombre"""
    return abs(n)

print(valeur_absolue.__doc__)
print("")
nombre=int(input("Entrer un nombre:"))
val=valeur_absolue(nombre)
print("Valeur absolue :",val)
