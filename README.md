# LOG3000 – TP3 – Calculatrice Web

## Numéro d’équipe
Équipe 40

## Nom du projet
Calculatrice Web Flask

## Objectif du projet
Ce projet consiste en une application web de calculatrice simple développée avec Flask.
L’objectif est de permettre aux utilisateurs d’effectuer des opérations mathématiques
de base à travers une interface web.

## Prérequis d’installation
- Python 3.10 ou plus récent
- pip
- Git
- Navigateur web moderne

## Instructions d’installation

1. Cloner le dépôt :
git clone https://github.com/MoAfandi25/LOG3000-TP3-Equipe40.git

2. Accéder au dossier du projet :
cd LOG3000-TP3-Equipe40

3. Installer les dépendances :
pip install flask

4. Lancer l’application :
python app.py

5. Ouvrir un navigateur et accéder à :
http://127.0.0.1:5000

## Tests

Des tests unitaires et d'intégration sont fournis pour valider le fonctionnement de la calculatrice.

- `test_operators.py` : teste les fonctions de base (add, subtract, multiply, divide).
- `test_app.py` : teste la logique de parsing/calcul et l'application Flask.

Pour exécuter les tests :

```bash
pip install pytest
pytest
```

## Problèmes/Bugs connus

- La soustraction est inversée (`subtract(a, b)` retourne `b - a`)
- La multiplication est en fait une puissance (`multiply(a, b)` retourne `a ** b`)
- La division est une division entière (`divide(a, b)` retourne `a // b`)
- Les nombres négatifs ne sont pas supportés dans les expressions
- Après une erreur, il faut vider manuellement le champ de saisie
- Les erreurs ne sont pas différenciées (toujours ValueError)
- L'utilisateur ne peut pas entrer plusieurs opérations (pas de support pour des expressions plus complexes)

Voir les fichiers de test pour plus de détails sur la couverture et les cas limites.
