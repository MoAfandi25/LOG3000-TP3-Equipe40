# Module Tests

## Raison d'être

Le module `tests/` contient tous les tests unitaires et d'intégration de l'application. Ces tests garantissent la qualité du code, vérifient le bon fonctionnement des fonctionnalités, et facilitent la détection de régressions lors des modifications futures. Les tests suivent les pratiques de test-driven development (TDD) et couvrent les chemins d'exécution critiques de l'application.

## Fichiers principaux

### `test_operators.py`
**Responsabilité** : Tests unitaires pour le module `operators.py`. Vérifie l'exhaustivité des cas possibles de chaque fonction arithmétique.

**Fonctions testées** :
- `add(a, b)` : Tests avec entiers positifs, négatifs, décimaux, zéro
- `subtract(a, b)` : Tests avec différents types de nombres et cas limites
- `multiply(a, b)` : Tests de la multiplication (a * b) avec différents scénarios
- `divide(a, b)` : Tests de la division décimale (a / b) avec cas normaux et limites, y compris ZeroDivisionError

**Couverture** :
- Cas nominaux (nombres positifs)
- Cas limites (nombres négatifs, zéro, décimaux)
- Gestion des erreurs (ZeroDivisionError pour divide)
- Vérification des résultats attendus pour chaque opération

### `test_app.py`
**Responsabilité** : Tests unitaires et d'intégration pour l'application Flask (`app.py`). Vérifie les chemins d'exécution de la fonction `calculate()` et les routes HTTP.

**Fonctionnalités testées** :
- **Fonction `calculate(expr: str)`** :
  - Chemin 1 : Expression vide ou non-chaîne → `ValueError("empty expression")`
  - Chemin 2 : Plusieurs opérateurs détectés → `ValueError("only one operator is allowed")`
  - Chemin 3 : Opérateur absent, en début ou en fin → `ValueError("invalid expression format")`
  - Chemin 4 : Opérandes non numériques → `ValueError("operands must be numbers")`
  - Chemin 5 : Expression valide → Appel de la fonction opérateur et retour du résultat

- **Route `index()`** :
  - GET `/` : Affichage du formulaire vide
  - POST `/` : Expression valide → `result = calculate(expression)`
  - POST `/` : Expression invalide → `result = f"Error: {e}"`

**Tests Flask** :
- Utilise le client de test Flask (fixture `client`) pour simuler les requêtes HTTP
- Vérifie les codes de statut HTTP (200 pour succès)
- Vérifie le contenu des réponses HTML
- Utilise des mocks pour isoler les tests (mock de `operators`, `calculate`, `render_template`)
- Utilise `@pytest.mark.parametrize` pour tester plusieurs cas avec une seule fonction de test

## Dépendances

### Dépendances externes
- **pytest** : Framework de test utilisé pour exécuter les tests
- **Flask** : Nécessaire pour les tests d'intégration de l'application web

### Dépendances internes
- **Module `operators`** : `test_operators.py` importe les fonctions depuis `operators.py`
- **Module `app`** : `test_app.py` importe l'application Flask depuis `app.py`

## Hypothèses

- Les tests sont exécutés avec `pytest` (pas `unittest`)
- Les tests doivent être isolés et indépendants (pas de dépendances entre tests)
- Les tests couvrent les chemins d'exécution critiques mais ne sont pas exhaustifs pour tous les cas possibles
- Le client de test Flask est utilisé pour simuler les requêtes HTTP sans démarrer un serveur réel
- Les tests peuvent être exécutés en parallèle sans conflits

## Exécution des tests

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

### Lancer avec couverture de code
```bash
pytest --cov=. --cov-report=html
```

### Lancer en mode watch (si installé)
```bash
pytest-watch
```

## Structure des tests

Chaque fichier de test suit cette structure :
1. **Imports** : Import des modules à tester et des dépendances de test
2. **Tests unitaires** : Tests isolés pour chaque fonction
3. **Tests d'intégration** : Tests qui vérifient l'interaction entre composants
4. **Fixtures** (si nécessaire) : Données de test réutilisables

## Bonnes pratiques

- Nommer les tests de manière descriptive : `test_nom_fonction_cas_testé()`
- Un test = une assertion principale
- Utiliser des docstrings pour expliquer le but de chaque test
- Tester les cas limites et les cas d'erreur, pas seulement les cas nominaux
- Maintenir les tests à jour lors des modifications du code
