# LOG3000 - TP3 - Équipe 40

## Description du projet

### But

Flask Calculator est une application web de calculatrice développée dans le cadre du cours LOG3000. Elle permet d'effectuer des opérations mathématiques basiques (addition, soustraction, multiplication, division) via une interface web simple et intuitive.

### Portée

L'application prend en charge :

- **Opérations supportées** : addition (+), soustraction (-), multiplication (*), division (/)
- **Format des expressions** : une expression par calcul, au format `nombre1 opérateur nombre2`
- **Interface** : calculatrice visuelle avec boutons et affichage du résultat
- **Validation** : gestion des erreurs (expression invalide, opérateurs multiples, opérandes non numériques)

**Limitations actuelles** : une seule opération binaire par expression ; pas de chaînage d'opérations ni de calculs plus complexes.

---

## Installation

### Prérequis

- **Python 3.7 ou supérieur**  
  Vérification :
  ```bash
  python --version
  # ou
  python3 --version
  ```
- **pip** (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le dépôt**
   ```bash
   git clone <url-du-depot>
   cd TP3---LOG3000-main
   ```

2. **Créer un environnement virtuel (recommandé)**
   ```bash
   python -m venv venv
   ```
   - **Windows** :
     ```bash
     venv\Scripts\activate
     ```
   - **Linux / macOS** :
     ```bash
     source venv/bin/activate
     ```

3. **Installer les dépendances**
   ```bash
   pip install flask
   ```

4. **Optionnel : créer un `requirements.txt`**  
   Pour faciliter les prochaines installations :
   ```bash
   pip freeze > requirements.txt
   ```
   Puis, sur un autre environnement :
   ```bash
   pip install -r requirements.txt
   ```

---

## Utilisation

### Lancer l'application

1. Depuis la racine du projet (avec l'environnement virtuel activé si nécessaire) :
   ```bash
   python app.py
   ```

2. Ouvrir un navigateur et aller à :
   ```
   http://127.0.0.1:5000
   ```

3. La calculatrice s'affiche et est prête à l'emploi.

### Utiliser la calculatrice

1. **Composer une expression**  
   Utiliser les boutons 0–9 et +, -, *, / pour former une expression du type `5 + 3` ou `10 - 2`.

2. **Obtenir le résultat**  
   Cliquer sur le bouton `=` pour envoyer l'expression au serveur et afficher le résultat.

3. **Effacer l'écran**  
   Cliquer sur `C` pour vider l'affichage et saisir une nouvelle expression.

4. **En cas d'erreur**  
   Un message du type `Error: ...` s'affiche si l'expression est invalide (plusieurs opérateurs, opérateur mal placé, opérandes non numériques, etc.).

### Exemples d'expressions valides

- `2 + 3`
- `10 - 4`
- `5 * 2`
- `8 / 2`

---

## Tests

Le projet inclut une suite complète de tests unitaires et d'intégration dans le répertoire `tests/`.

### Prérequis pour les tests

```bash
pip install pytest
```

### Lancer tous les tests

```bash
pytest
```

### Lancer avec verbosité

```bash
pytest -v
```

### Lancer un fichier de test spécifique

```bash
pytest tests/test_operators.py
pytest tests/test_app.py
```

### Lancer les tests avec couverture

```bash
pytest --cov=. --cov-report=html
```

### Structure des tests

- **`tests/test_operators.py`** : Tests unitaires pour les fonctions mathématiques (add, subtract, multiply, divide)
- **`tests/test_app.py`** : Tests d'intégration pour l'application Flask (routes HTTP, fonction calculate)

Pour plus de détails, consultez `tests/README.md`.

---

## Structure du projet

```
TP3---LOG3000-main/
├── app.py              # Point d'entrée Flask, routes, logique de calcul
├── operators.py        # Fonctions mathématiques (add, subtract, multiply, divide)
├── static/
│   ├── style.css       # Styles de l'interface
│   └── README.md       # Documentation du module static
├── templates/
│   ├── index.html      # Page principale de la calculatrice
│   └── README.md       # Documentation du module templates
├── tests/
│   ├── test_operators.py  # Tests unitaires pour operators.py
│   ├── test_app.py       # Tests d'intégration pour app.py
│   └── README.md         # Documentation du module tests
├── ROOT_MODULE.md      # Documentation du module racine
└── README.md           # Ce fichier
```

---

## Contribution

### Flux de travail (branches, PR, issues)

1. **Issues**  
   Ouvrir une issue pour signaler un bug ou proposer une fonctionnalité.

2. **Branches**
   - Créer une branche depuis `main` :
     ```bash
     git checkout -b feature/ma-fonctionnalite
     # ou
     git checkout -b fix/correction-bug
     ```
   - Convention de nommage : `feature/`, `fix/`, `docs/`, etc.

3. **Pull requests**
   - Commiter et pousser votre branche vers le dépôt distant.
   - Ouvrir une Pull Request vers `main`.
   - Décrire les changements et lier les issues concernées.
   - Attendre la revue et la validation.

4. **Conventions**
   - Messages de commit clairs et explicites.
   - Mettre à jour la documentation si nécessaire.
   - Assurer que les tests passent avant de merger.

---

## Licence et crédits

Projet réalisé dans le cadre du cours LOG3000 - Polytechnique Montréal.
