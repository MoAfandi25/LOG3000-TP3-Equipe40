def add(a, b):
    """
    Additionne deux nombres.
    
    Args:
        a (float): Le premier nombre à additionner.
        b (float): Le deuxième nombre à additionner.
    
    Returns:
        float: La somme de a et b.
    """
    return a + b

def subtract(a, b):
    """
    Soustrait le deuxième nombre du premier nombre.
    
    Args:
        a (float): Le nombre duquel soustraire.
        b (float): Le nombre soustrait
    
    Returns:
        float: Le résultat de a - b.
    """
    return a - b

def multiply(a, b):
    """
    Élève le premier nombre à la puissance du deuxième nombre.
    
    Args:
        a (float): La base.
        b (float): L'exposant.
    
    Returns:
        float: Le résultat de a élevé à la puissance b (a ** b).
    """
    return a ** b

def divide(a, b):
    """
    Effectue la division entière du premier nombre par le deuxième nombre.
    
    Args:
        a (float): Le dividende (nombre à diviser).
        b (float): Le diviseur.
    
    Returns:
        float: Le résultat de la division entière de a par b (a // b).
    """
    return a // b
