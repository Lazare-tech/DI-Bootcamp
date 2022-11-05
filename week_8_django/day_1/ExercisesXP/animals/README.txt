Des Instructions
Nous allons créer une application Web simple basée sur Django pour gérer les informations sur différents animaux.

Créez un nouveau répertoire pour votre projet avec un nouvel environnement virtuel. Appelez le répertoire animal-info .
Activez votre nouvel environnement virtuel, puis installez Django.
Créez un nouveau projet en utilisant Django appelé animals , puis créez une nouvelle application à l'intérieur appelée info .
Utilisez le fichier json proposé à la fin de cette page. Le fichier contient les dictionnaires suivants :
Animal , aux propriétés :
identifiant
pattes - un nombre entier, le nombre de pattes que l'animal a
poids - le poids moyen d'un animal adulte de ce type
taille - la taille moyenne d'un animal adulte de ce type
vitesse – la vitesse maximale à laquelle cet animal peut se déplacer
famille – le groupe familial auquel appartient cet animal. (Doit référencer le dictionnaire de la famille par identifiant - voir ci-dessous).
Famille , représentant un groupe d'animaux ou "famille", avec des propriétés :
identifiant
Nom

Ajoutez quelques familles au fichier json. Familles recommandées :
mammifère
reptile
insecte
arachnide
amphibie
etc.

Ajoutez quelques animaux à votre fichier json.

Créez 2 vues, correspondant aux URL suivantes :
/family/X , où X est l'ID (clé primaire) de la famille donnée. Devrait afficher une liste de tous les animaux de cette famille.
/animal/X , où X est l'ID (clé primaire) de l'animal donné. Doit afficher toutes les informations sur l'animal donné.

Créez deux modèles rendus par les deux vues ci-dessus
