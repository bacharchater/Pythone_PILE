# Fonction pour créer une pile vide avec un nombre maximum d'éléments donné
def creer_pile(nb_elements):
    """
    Crée une pile avec une capacité maximale de nb_elements.
    L'indice 0 est utilisé pour suivre la position du prochain emplacement libre dans la pile.
    Initialement, P[0] = 1, ce qui signifie que la pile est vide (pas encore d'éléments empilés).
    
    Arguments:
    nb_elements (int): Le nombre maximum d'éléments que la pile peut contenir.

    Retour:
    list: Une liste représentant la pile, avec l'indice 0 comme compteur d'éléments.
    """
    # On crée une liste de taille nb_elements + 1.
    # Le "+1" est nécessaire parce que l'indice 0 est réservé pour suivre la position.
    P = [None] * (nb_elements + 1)
    
    # On initialise l'indice 0 à 1, indiquant que la pile est vide (aucun élément encore empilé).
    P[0] = 1
    return P


# Fonction pour empiler (ajouter) un élément dans la pile
def empiler(P, element):
    """
    Ajoute un élément dans la pile si elle n'est pas pleine.
    
    Arguments:
    P (list): La pile, représentée sous forme de liste.
    element (any): L'élément à empiler dans la pile.

    Retour:
    bool: Renvoie False si la pile est pleine (empilement impossible), True sinon (succès de l'empilement).
    """
    # Si l'indice 0 dépasse la taille maximum de la pile, cela signifie que la pile est pleine
    if P[0] > len(P) - 1:
        return False  # La pile est pleine, on ne peut pas ajouter d'élément
    else:
        # Ajouter l'élément à la position P[0] (qui pointe sur le prochain emplacement libre)
        P[P[0]] = element
        
        # Mettre à jour l'indice 0 pour pointer sur le prochain emplacement libre.
        P[0] += 1
        return True  # L'élément a été ajouté avec succès


# Fonction pour dépiler (retirer) un élément de la pile
def depiler(P):
    """
    Retire un élément de la pile si elle n'est pas vide.
    
    Arguments:
    P (list): La pile, représentée sous forme de liste.

    Retour:
    any: Renvoie l'élément dépilé si la pile n'est pas vide, False sinon (la pile est vide).
    """
    # Si l'indice 0 est à 1, cela signifie que la pile est vide (aucun élément à retirer)
    if P[0] == 1:
        return False  # La pile est vide, on ne peut pas dépiler
    else:
        # Décrémenter l'indice 0 pour revenir à l'élément actuellement au sommet de la pile
        P[0] -= 1
        
        # Récupérer l'élément à dépiler
        element = P[P[0]]
        
        # Remettre l'emplacement dans la pile à None (optionnel, pour "vider" visuellement la pile)
        P[P[0]] = None
        return element  # Renvoie l'élément qui a été dépilé


# Test et exécution des fonctions

# On définit le nombre maximum d'éléments que la pile peut contenir
N = 4  # La pile peut contenir 4 éléments au maximum

# On crée une pile vide
pile = creer_pile(N)
print("Pile initiale:", pile)  # Affiche l'état de la pile avant toute opération

# Essayer d'empiler des éléments
for i in range(1, N + 2):  # On essaie d'empiler 5 éléments dans une pile de 4
    resultat = empiler(pile, i)
    print(f"Empilement de {i}: {resultat}")  # Affiche True si empilement réussi, False sinon
    print("État de la pile:", pile)

# Essayer de dépiler des éléments
for _ in range(N + 1):  # On essaie de dépiler 5 fois (dont 1 fois de trop)
    resultat = depiler(pile)
    print(f"Élément dépilé: {resultat if resultat != False else 'False'}")  # Affiche False si la pile est vide
    print("État de la pile:", pile)
