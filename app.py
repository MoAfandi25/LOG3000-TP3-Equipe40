"""
Application Flask pour une calculatrice simple.

Ce module fournit une interface web pour effectuer des calculs mathématiques
basiques (addition, soustraction, multiplication, division) en utilisant
des expressions sous forme de chaînes de caractères.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Utilisé pour identifier l’opérateur dans l’expression et appeler la bonne fonction en un seul passage.
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Calcule le résultat d'une expression mathématique simple.
    
    L'expression doit être au format "nombre1 opérateur nombre2" où l'opérateur
    peut être '+', '-', '*' ou '/'. Les espaces sont ignorés.
    
    Args:
        expr (str): L'expression mathématique à évaluer (ex: "5 + 3", "10-2").
    
    Returns:
        float: Le résultat du calcul.
    
    Raises:
        ValueError: Si l'expression est vide, invalide, contient plusieurs opérateurs,
                   si l'opérateur est mal placé, ou si les opérandes ne sont pas des nombres.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")  # Normaliser pour simplifier le parsing (espaces ignorés).

    op_pos = -1  # Position de l'opérateur dans la chaîne (-1 = non trouvé).
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # Rejeter : opérateur absent, en début ou en fin d’expression (format invalide).
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        # Conversion échouée : les opérandes ne sont pas des nombres valides.
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de l'application qui gère l'affichage et le traitement des calculs.
    
    En GET: Affiche le formulaire de calculatrice.
    En POST: Traite l'expression soumise et retourne le résultat ou une erreur.
    
    Returns:
        str: Le template HTML rendu avec le résultat du calcul ou un message d'erreur.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"  # Afficher l’erreur à l’utilisateur au lieu de faire échouer la page.
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True) # pragma: no cover