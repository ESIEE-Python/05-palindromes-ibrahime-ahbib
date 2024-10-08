"""
Ce module contient des fonctions pour vérifier si une chaîne de caractères
ou un nombre est un palindrome.
"""

#### Fonction secondaire

def ispalindrome(p):
    """
    Vérifie si une chaîne de caractères ou un nombre est un palindrome.

    La fonction ignore les espaces, les accents, la casse et les caractères non alphabétiques.
    """
    # Version avec table de correspondance
    table = str.maketrans("éèêëàâùûçôîïÉÈÊËÀÂÙÛÇÔÎÏ", "eeeeaauucoiiEEEEAAUUCOII")
    p = p.translate(table)  # On remplace les caractères accentués par leur équivalent non accentué

    p = p.lower()

    # On garde uniquement les lettres de l'alphabet et les chiffres
    p = "".join([c for c in p if c.isalnum()])

    # Version simple
    # if p == p[::-1]:
    #     return True

    for i in range(len(p) // 2):
        # On compare le premier caractère avec le dernier, le deuxième avec l'avant dernier, etc.
        if p[i] != p[-i - 1]:
            return False

    return True

#### Fonction principale

def main():
    """
    Fonction principale pour tester des chaînes de caractères prédéfinies.
    """
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
