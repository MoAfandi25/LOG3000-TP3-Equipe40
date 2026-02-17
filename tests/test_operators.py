"""
Tests unitaires pour le module operators.py.

Ce module vérifie l'exhaustivité des cas possibles de chaque
fonction arithmétique : add, subtract, multiply et divide.
"""

import pytest
from operators import add, subtract, multiply, divide


# ===========================================================================
# add() — addition de deux nombres
# ===========================================================================

def test_add_entiers_positifs():
    """
    Vérifie que add() retourne la somme correcte pour deux entiers positifs,
    couvrant le chemin nominal de la fonction.
    """
    assert add(2, 3) == 5


def test_add_avec_negatifs_et_zero():
    """
    Vérifie que add() gère correctement les opérandes négatifs et nuls,
    couvrant les cas limites de la fonction.
    """
    assert add(-1, 2) == 1
    assert add(2,-3) == -1
    assert add(0, 0) == 0


# ===========================================================================
# subtract() — soustraction de deux nombres
# ===========================================================================

def test_subtract_resultat_positif():
    """
    Vérifie que subtract() retourne la différence correcte quand le résultat
    est positif, couvrant le chemin nominal de la fonction.
    """
    assert subtract(3, 2) == 1
    assert subtract(5, 2) == 3


def test_subtract_resultat_negatif_ou_nul():
    """
    Vérifie que subtract() gère correctement les cas où le résultat est
    négatif ou nul, couvrant les cas limites de la fonction.
    """
    assert subtract(-1, 1)  == -2
    assert subtract(-1, -1) ==  0
    assert subtract(1, -1)  ==  2


# ===========================================================================
# multiply() — multiplication de deux nombres
# ===========================================================================

def test_multiply_entiers_positifs():
    """
    Vérifie que multiply() retourne le produit correct pour deux entiers
    positifs, couvrant le chemin nominal et la commutativité.
    """
    assert multiply(2, 3) == 6
    assert multiply(3, 2) == 6


def test_multiply_par_zero_ou_negatif():
    """
    Vérifie que multiply() gère correctement la multiplication par zéro
    et par un entier négatif, couvrant les cas limites de la fonction.
    """
    assert multiply(5, 0)  == 0
    assert multiply(5, -1) == -5


# ===========================================================================
# divide() — division de deux nombres
# ===========================================================================

def test_divide_resultat_decimal_et_entier():
    """
    Vérifie que divide() retourne le quotient correct pour une division
    avec résultat décimal et pour une division exacte, couvrant le chemin
    nominal et le cas du dividende nul.
    """
    assert divide(5, 2) == 2.5
    assert divide(9, 3) == 3
    assert divide(0, 3) == 0


def test_divide_par_zero():
    """
    Vérifie que divide() lève ZeroDivisionError quand le diviseur est nul,
    couvrant le chemin d'erreur de la fonction.
    """
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)