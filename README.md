# Flappy Bird

## Description
Flappy Bird est une version simple du célèbre jeu où le joueur contrôle un oiseau qui doit passer entre des tuyaux pour marquer des points. Le but est de marquer le plus de points possible sans toucher les tuyaux ou le sol.

## Fonctionnalités
- Contrôle de l'oiseau avec la touche espace.
- Génération aléatoire des tuyaux.
- Score incrémenté à chaque passage réussi entre les tuyaux.
- Gestion des collisions avec les tuyaux et les bords de l'écran.

## Structure du Projet
Le projet est organisé en plusieurs fichiers Python pour une meilleure gestion et modularité :

- **main.py** : Point d'entrée de l'application.
- **application.py** : Classe abstraite `Application`.
- **flappy_bird_app.py** : Classe pour l'application Flappy Bird.
- **game.py** : Contient la logique du jeu `Game`.
- **bird.py** : Classe `Bird` représentant l'oiseau.
- **pipe.py** : Classe `Pipe` représentant les tuyaux.

## Prérequis
- Python 3.x
- Pygame

### Installation des dépendances
Assurez-vous d'avoir installé `pygame` pour exécuter le jeu. Vous pouvez l'installer via pip :

```sh
pip install pygame

Assets

Les images nécessaires pour le jeu doivent être placées dans le dossier assets :

    bird.png : L'image de l'oiseau.
    background.png : L'image de fond.
    pipe_top.png : L'image du tuyau supérieur.
    pipe_bottom.png : L'image du tuyau inférieur.