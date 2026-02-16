# Module Static

## Raison d'être

Le module `static/` contient tous les fichiers statiques servis directement au client par Flask. Ces fichiers ne sont pas traités par le moteur de template Jinja2 et sont servis tels quels au navigateur. Ce module centralise les ressources CSS, JavaScript, images et autres assets nécessaires à l'interface utilisateur.

## Fichiers principaux

### `style.css`
**Responsabilité** : Définit tous les styles CSS de l'application web de calculatrice.

**Contenu** :
- Styles globaux pour le body (centrage, fond)
- Styles de la calculatrice (conteneur principal)
- Styles de l'affichage (champ de texte pour les résultats)
- Styles des boutons (grille, couleurs, états hover/active)
- Distinction visuelle entre boutons numériques et opérateurs

**Caractéristiques** :
- Utilise CSS Grid pour organiser les boutons en grille 4x4
- Thème sombre avec accents orange pour les opérateurs
- Transitions CSS pour améliorer l'expérience utilisateur
- Design responsive avec largeur maximale de 600px

## Dépendances

- **Flask** : Flask sert automatiquement les fichiers de ce répertoire via la route `/static/`
- **Templates** : Les templates HTML doivent référencer les fichiers statiques via `url_for('static', filename='...')`
- **Navigateurs** : Compatible avec les navigateurs modernes supportant CSS Grid et Flexbox

## Hypothèses

- Les fichiers CSS sont servis avec le type MIME `text/css`
- Le répertoire `static/` est accessible publiquement (pas de restrictions d'accès)
- Les styles sont appliqués de manière globale à l'application
- Aucun préprocesseur CSS (SASS, LESS) n'est utilisé - CSS pur uniquement
