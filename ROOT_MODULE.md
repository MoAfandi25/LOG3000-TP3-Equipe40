# Module Racine - Logique Métier et Application

## Raison d'être

Le module racine contient la logique métier principale de l'application Flask et les opérations mathématiques de base. Il orchestre le traitement des requêtes HTTP, le parsing des expressions mathématiques, et coordonne l'interaction entre les différents modules (templates, static, operators).

## Fichiers principaux

### `app.py`
**Responsabilité** : Point d'entrée principal de l'application Flask. Gère les routes HTTP, le parsing des expressions mathématiques, et la coordination entre la logique métier et l'interface utilisateur.

**Fonctionnalités principales** :
- **Initialisation Flask** : Création de l'instance de l'application Flask
- **Dictionnaire OPS** : Mapping des opérateurs vers leurs fonctions correspondantes pour le parsing
- **Fonction `calculate(expr: str)`** : Parse et évalue une expression mathématique simple au format "nombre1 opérateur nombre2"
  - Valide le format de l'expression
  - Extrait l'opérateur et les opérandes
  - Délègue le calcul aux fonctions du module `operators`
  - Gère les erreurs de validation et de format
- **Route `index()`** : Route principale (`/`) qui gère les requêtes GET (affichage) et POST (traitement)
  - GET : Affiche le formulaire de calculatrice
  - POST : Traite l'expression soumise et retourne le résultat ou un message d'erreur

**Contraintes de parsing** :
- Un seul opérateur par expression
- Format strict : "nombre1 opérateur nombre2"
- Les espaces sont ignorés
- Les opérandes doivent être des nombres valides

### `operators.py`
**Responsabilité** : Module contenant les fonctions mathématiques de base utilisées par l'application. Fournit une couche d'abstraction pour les opérations arithmétiques.

**Fonctions** :
- `add(a, b)` : Additionne deux nombres
- `subtract(a, b)` : Soustrait le premier nombre du deuxième (b - a)
- `multiply(a, b)` : Élève le premier nombre à la puissance du deuxième (a ** b)
- `divide(a, b)` : Effectue la division entière du premier nombre par le deuxième (a // b)

**Note** : Les implémentations actuelles de `multiply` et `divide` utilisent respectivement l'exponentiation (`**`) et la division entière (`//`), ce qui peut différer des attentes standards pour une calculatrice.

## Dépendances

### Dépendances externes
- **Flask** : Framework web pour gérer les routes HTTP et le rendu des templates
- **Python 3.x** : Version de Python requise (utilisation de type hints et syntaxe moderne)

### Dépendances internes
- **Module `templates/`** : `app.py` utilise `render_template()` pour générer les réponses HTML
- **Module `static/`** : Les templates référencent les fichiers CSS depuis ce module
- **Module `operators`** : `app.py` importe les fonctions mathématiques depuis `operators.py`

## Hypothèses

- Flask est configuré pour servir automatiquement les fichiers statiques depuis `static/` et chercher les templates dans `templates/`
- Les expressions mathématiques sont limitées à deux opérandes et un seul opérateur
- Les erreurs sont capturées et affichées à l'utilisateur plutôt que de faire échouer l'application
- Le mode debug est activé (`debug=True`) pour le développement (à désactiver en production)
- Les opérandes sont convertis en `float`, permettant les nombres décimaux
- Le serveur Flask est lancé directement via `python app.py` (pas de déploiement WSGI pour le moment)

## Structure des données

- **Expressions** : Chaînes de caractères au format "nombre1 opérateur nombre2"
- **Résultats** : Nombres flottants (`float`)
- **Erreurs** : Chaînes de caractères au format "Error: {message}"
