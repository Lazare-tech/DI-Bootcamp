Des Instructions
Partie I - Modèles
Créez et activez un virtualenv, créez un nouveau projet django.

Créez une nouvelle application appelée gifs .

Créez un Modèle Gif avec les champs suivants :
titre (CharField)
URL (URLField)
nom_uploader (CharField)
created_at (DatetimeField, doit être rempli lors de la création).

Créez un modèle de catégorie avec les champs suivants :
nom (CharField)
gifs - (champ plusieurs à plusieurs avec le modèle Gif ). Un Gif peut avoir de nombreuses catégories différentes, et une catégorie peut être partagée entre plusieurs gifs

Remplir les catégories : Ajoutez environ 10 catégories à votre base de données à l'aide du shell django ou de l'administrateur. Vous pouvez trouver quelques idées de catégories gif sur le site giphy - categories


Partie II - Formes Et Vues
Créez un fichier forms.py et ajoutez deux nouveaux formulaires :
GifForm avec les champs
nom_uploader
Titre
url : Vous pouvez utiliser l'url des gifs du site giphy . Cliquez sur le gif que vous voulez, et copiez le lien gif .
categories : rechercher ModelMultipleChoiceField

CategoryForm avec les champs
Nom

Créez des vues :
Vue de la page d' accueil : cette vue affichera tous les gifs de la base de données. Affichez chaque gif dans un imgtag.
Ajoutez une barre de navigation, avec des liens qui redirigent l'utilisateur vers la vue Ajouter un nouveau GIF et vers la vue Ajouter une nouvelle catégorie .

Ajouter une nouvelle vue GIF : cette vue utilisera le GifForm créé ci-dessus, pour ajouter un nouveau gif à la base de données.

Ajouter une nouvelle vue Catégorie : cette vue utilisera le CategoryForm créé ci-dessus, pour ajouter une nouvelle catégorie à la base de données.

Vue catégorie : cette vue accepte un identifiant de catégorie en tant que paramètre et affiche tous les gifs de cette catégorie (c'est-à-dire par exemple tous les gifs "heureux").

Vue catégories : cette vue affichera toutes les catégories existantes de la base de données. Chaque catégorie possède un lien redirigeant l'utilisateur vers la vue Catégorie .

Vue Gif : cette vue accepte un identifiant gif et affiche ces détails gifs spécifiques sur la page. Affichez chaque gif dans un imgtag.

Créez des itinéraires et des modèles conformément aux vues.


Partie III - Conseils
LISEZ LES DOCUMENTS - vous ne pourrez pas tout deviner/souvenir, gardez les documents à portée de main et habituez-vous à les parcourir pour trouver des réponses.

Travailler simultanément sur le GifForm et la vue Ajouter un nouveau GIF vous permettra de voir votre progression.

Découvrez l'héritage des modèles pour désencombrer votre code HTML et arrêter le code répétitif.

Utilisez Bootstrap pour styliser rapidement et (relativement) facilement vos pages.

Vous pensez à une fonctionnalité intéressante ? Essayez et implémentez-le!

