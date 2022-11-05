Des Instructions
Vous avez la liste de dictionnaires suivante :

people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]


Créez un projet Django avec deux vues :
La première vue affiche /peoplela liste des personnes avec le reste des informations dont elles disposent, triées par âge .

La deuxième vue est /people/{id}où id est l'identifiant de la personne. Cette vue présente des informations sur une seule personne.
Assurez-vous que le modèle rendu dans /peoplecontient des liens vers les people/{id}
exigences : utilisez autant de filtres de modèles que possible
