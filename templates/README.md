# Module Templates

## Raison d'être

Le module `templates/` contient tous les fichiers de templates HTML utilisés par Flask avec le moteur de template Jinja2. Ces fichiers définissent la structure et la présentation de l'interface utilisateur de l'application web. Flask utilise automatiquement ce répertoire pour localiser les templates lors de l'appel à `render_template()`.

## Fichiers principaux

### `index.html`
**Responsabilité** : Template principal de l'application qui définit l'interface complète de la calculatrice.

**Structure** :
- **En-tête HTML** : Métadonnées, titre, lien vers le CSS
- **Formulaire** : Formulaire POST pour envoyer les expressions au serveur
- **Champ d'affichage** : Champ texte en lecture seule (`readonly`) pour afficher les résultats
- **Grille de boutons** : Interface de la calculatrice avec boutons numériques (0-9) et opérateurs (+, -, *, /)
- **JavaScript intégré** : Fonctions pour gérer l'interaction utilisateur côté client

**Fonctionnalités JavaScript** :
- `appendToDisplay(value)` : Ajoute des caractères au champ d'affichage
- `clearDisplay()` : Efface le contenu du champ d'affichage

**Variables Jinja2 utilisées** :
- `{{ result }}` : Résultat du calcul ou message d'erreur, injecté par Flask depuis `app.py`
- `{{ url_for('static', filename='style.css') }}` : Génération de l'URL vers le fichier CSS

## Dépendances

- **Flask** : Flask doit être configuré pour utiliser Jinja2 (comportement par défaut)
- **Module static** : Le template référence `style.css` depuis le répertoire `static/`
- **Module app** : Le template reçoit la variable `result` depuis la fonction `index()` dans `app.py`
- **Navigateurs** : Compatible avec les navigateurs supportant HTML5 et JavaScript ES5+

## Hypothèses

- Flask cherche automatiquement les templates dans le répertoire `templates/` à la racine du projet
- Le template utilise la syntaxe Jinja2 pour l'injection de variables
- Les formulaires utilisent la méthode POST pour envoyer les données au serveur
- Le JavaScript est intégré directement dans le template (pas de fichier externe)
- Le champ d'affichage est en lecture seule pour forcer l'utilisation des boutons et garantir un format valide
