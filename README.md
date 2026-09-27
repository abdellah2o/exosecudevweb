# Exercices pour m'entrainer à la sécurité en dev web

## Intro
Ce projet est pour moi un bac à sable pour tester toutes sortes de mesures de sécurité à appliquer sur une application web, l'objectif ici est de se tromper, se tromper, se tromper et réessayer à chaque fois jusqu'à maîtriser les différents concepts de sécurité

---

## Intrastructure
- code: Flask (python)
- bd: SQLite

## Extensions python à installer
Tout d'abord activer le virtual environment python.
### Windows CMD

```cmd
.\.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Copier ensuite le texte ci dessous dans un fichier 'requirements.txt' à placer dans la racine du projet. (liste des packages obtenus avec la commande "pip freeze")
```txt
blinker==1.9.0
click==8.5.0
Flask==3.1.3
Flask-JWT-Extended==4.7.4
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
PyJWT==2.15.0
Werkzeug==3.1.8
```
Puis exécuter la commande.
```bash
python -m pip install -r requirements.txt
```
---
## Schéma BD
Il est important de créer la table SQL user si votre BD ne l'a pas déjà.
``` sql
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);
```
