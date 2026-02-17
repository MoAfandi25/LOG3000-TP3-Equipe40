"""
Tests unitaires pour l'application Flask de calculatrice (app.py).

Ce module vérifie l'exhaustivité des chemins d'exécution de la fonction
calculate() ainsi que les routes HTTP GET et POST de l'application.

Chemins couverts dans calculate() :
  - Chemin 1 : expression vide ou non-chaîne → ValueError("empty expression")
  - Chemin 2 : plusieurs opérateurs détectés → ValueError("only one operator is allowed")
  - Chemin 3 : opérateur absent, en début ou en fin → ValueError("invalid expression format")
  - Chemin 4 : opérandes non numériques → ValueError("operands must be numbers")
  - Chemin 5 : expression valide → appel de la fonction opérateur et retour du résultat

Chemins couverts dans index() :
  - GET  / : affichage du formulaire vide
  - POST / : expression valide → result = calculate(expression)  (ligne 85)
  - POST / : expression invalide → result = f"Error: {e}"        (lignes 87-88)

Note :
  La ligne `app.run(debug=True)` (bloc __main__, ligne 91) est exclue du
  coverage via `# pragma: no cover` dans app.py, car son exécution en test
  démarrerait un vrai serveur HTTP et sortirait du cadre des tests unitaires.
"""

import sys
import types

import pytest
from unittest.mock import patch, MagicMock

# ---------------------------------------------------------------------------
# Le module `operators` est mocké le temps de l'import de app.py, puis
# retiré de sys.modules pour ne pas polluer les autres fichiers de tests
# (notamment test_operators.py qui importe le vrai module).
# ---------------------------------------------------------------------------
_faux_operators = types.ModuleType("operators")
_faux_operators.add      = lambda a, b: a + b
_faux_operators.subtract = lambda a, b: a - b
_faux_operators.multiply = lambda a, b: a * b
_faux_operators.divide   = lambda a, b: a / b

_module_reel = sys.modules.get("operators")
sys.modules["operators"] = _faux_operators

from app import app, calculate

if _module_reel is not None:
    sys.modules["operators"] = _module_reel
else:
    del sys.modules["operators"]


# ===========================================================================
# Fixture
# ===========================================================================

@pytest.fixture()
def client():
    """Retourne un client de test Flask avec le mode TESTING activé."""
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


# ===========================================================================
# calculate() — Chemin 1 : expression vide ou de type invalide
# ===========================================================================

def test_chaine_vide():
    """
    Vérifie que calculate() lève ValueError lorsque l'expression est une
    chaîne vide, couvrant le premier branchement de validation du type.
    """
    with pytest.raises(ValueError, match="empty"):
        calculate("")


def test_type_non_chaine():
    """
    Vérifie que calculate() lève ValueError lorsque l'argument n'est pas
    une chaîne de caractères (ici un entier), couvrant la garde isinstance().
    """
    with pytest.raises(ValueError, match="empty"):
        calculate(42)


# ===========================================================================
# calculate() — Chemin 2 : plusieurs opérateurs dans l'expression
# ===========================================================================

def test_plusieurs_operateurs():
    """
    Vérifie que calculate() lève ValueError dès qu'un second opérateur est
    détecté, couvrant le branchement « op_pos != -1 » dans la boucle.
    """
    with pytest.raises(ValueError, match="only one operator is allowed"):
        calculate("1 + 2 + 3")


# ===========================================================================
# calculate() — Chemin 3 : format d'expression invalide
# ===========================================================================

def test_aucun_operateur():
    """
    Vérifie que calculate() lève ValueError quand aucun opérateur n'est
    trouvé (op_pos reste à -1), couvrant la condition de format invalide.
    """
    with pytest.raises(ValueError, match="invalid expression format"):
        calculate("42")


def test_operateur_en_debut():
    """
    Vérifie que calculate() lève ValueError quand l'opérateur se trouve en
    position 0 (op_pos <= 0), couvrant la vérification de placement.
    """
    with pytest.raises(ValueError, match="invalid expression format"):
        calculate("+5")


def test_operateur_en_fin():
    """
    Vérifie que calculate() lève ValueError quand l'opérateur se trouve en
    dernière position (op_pos >= len(s) - 1), couvrant l'autre borne.
    """
    with pytest.raises(ValueError, match="invalid expression format"):
        calculate("5+")


# ===========================================================================
# calculate() — Chemin 4 : opérandes non numériques
# ===========================================================================

def test_operandes_non_numeriques():
    """
    Vérifie que calculate() lève ValueError quand float() échoue sur l'un
    des opérandes, couvrant le bloc except ValueError de la conversion.
    """
    with pytest.raises(ValueError, match="operands must be numbers"):
        calculate("a + b")


# ===========================================================================
# calculate() — Chemin 5 : expression valide, appel de l'opérateur
# ===========================================================================

@pytest.mark.parametrize("expression,attendu", [
    ("3 + 4",   7.0),   # addition
    ("9 - 4",   5.0),   # soustraction
    ("6 * 7",  42.0),   # multiplication
    ("10 / 4",  2.5),   # division
    ("  5  +  5  ", 10.0),  # espaces ignorés
])
def test_expression_valide(expression, attendu):
    """
    Vérifie le chemin nominal pour chaque opérateur : parsing, suppression
    des espaces, conversion float et retour du résultat correct.
    """
    assert calculate(expression) == attendu


@pytest.mark.parametrize("expression,symbole,fonction_attendue,a,b", [
    ("3 + 4",  "+", "add",      3.0, 4.0),
    ("9 - 4",  "-", "subtract", 9.0, 4.0),
    ("6 * 7",  "*", "multiply", 6.0, 7.0),
    ("10 / 4", "/", "divide",  10.0, 4.0),
])
def test_dispatch_operateur_mocke(expression, symbole, fonction_attendue, a, b):
    """
    Vérifie que calculate() appelle la bonne fonction du dictionnaire OPS
    avec les bons arguments float, en isolant complètement le dispatch.
    """
    mock_op = MagicMock(return_value=99)
    with patch.dict("app.OPS", {symbole: mock_op}):
        resultat = calculate(expression)
    mock_op.assert_called_once_with(a, b)
    assert resultat == 99


# ===========================================================================
# index() — GET / : result = "" et render_template appelé (lignes 81, 88)
# ===========================================================================

def test_get_retourne_200(client):
    """
    Vérifie que la route GET / répond avec un statut HTTP 200, couvrant
    le chemin où request.method != 'POST' — le bloc if est ignoré.
    """
    reponse = client.get("/")
    assert reponse.status_code == 200


def test_get_render_template_appele_avec_result_vide(client):
    """
    Vérifie que render_template est appelé avec result="" lors d'un GET —
    couvre la ligne `result = ""` (ligne 81) et l'appel render_template
    (ligne 88) en dehors du bloc POST.
    """
    with patch("app.render_template", return_value="") as mock_render:
        client.get("/")
    mock_render.assert_called_once_with("index.html", result="")


def test_get_aucun_resultat_ni_erreur_affiches(client):
    """
    Vérifie que le bloc `if request.method == 'POST'` est bien ignoré
    en GET : ni résultat de calcul ni message d'erreur dans la réponse.
    """
    reponse = client.get("/")
    assert b"Error" not in reponse.data


# ===========================================================================
# index() — POST / try : result = calculate(expression) (lignes 83-85)
# ===========================================================================

def test_post_expression_lue_depuis_formulaire(client):
    """
    Vérifie que index() lit le champ 'display' via request.form.get et le
    passe à calculate() — couvre la ligne `expression = request.form.get(...)`.
    """
    with patch("app.calculate", return_value=0) as mock_calculate:
        client.post("/", data={"display": "99 + 1"})
    mock_calculate.assert_called_once_with("99 + 1")


def test_post_result_est_le_retour_de_calculate(client):
    """
    Vérifie que result reçoit bien la valeur retournée par calculate() et
    qu'elle est transmise au template — couvre `result = calculate(expression)`
    (ligne 85) et l'appel render_template avec cette valeur (ligne 88).
    """
    with patch("app.render_template", return_value="") as mock_render:
        with patch("app.calculate", return_value=7.0):
            client.post("/", data={"display": "3 + 4"})
    mock_render.assert_called_once_with("index.html", result=7.0)


def test_post_retourne_200_sur_succes(client):
    """
    Vérifie que la route POST retourne HTTP 200 après un calcul réussi,
    confirmant que render_template est atteint sans exception serveur.
    """
    reponse = client.post("/", data={"display": "10 / 2"})
    assert reponse.status_code == 200


# ===========================================================================
# index() — POST / except : result = f"Error: {e}" (lignes 86-87)
# ===========================================================================

def test_post_result_est_le_message_derreur(client):
    """
    Vérifie que result reçoit le message formaté "Error: ..." quand
    calculate() lève une exception — couvre `result = f"Error: {e}"`
    (ligne 87) et l'appel render_template avec cette valeur (ligne 88).
    """
    with patch("app.calculate", side_effect=ValueError("invalid expression format")):
        with patch("app.render_template", return_value="") as mock_render:
            client.post("/", data={"display": "abc"})
    mock_render.assert_called_once_with(
        "index.html", result="Error: invalid expression format"
    )


def test_post_expression_invalide_affiche_erreur(client):
    """
    Vérifie que le préfixe 'Error:' est bien présent dans la réponse HTML
    quand calculate() lève une exception — chemin du bloc except.
    """
    reponse = client.post("/", data={"display": "abc"})
    assert b"Error" in reponse.data


def test_post_retourne_200_sur_erreur(client):
    """
    Vérifie que la route POST retourne HTTP 200 même quand une exception
    est levée — la page ne doit pas planter (pas de 500).
    """
    reponse = client.post("/", data={"display": "1 / 0"})
    assert reponse.status_code == 200