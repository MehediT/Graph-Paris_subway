from entity.Graphe import Graphe
from entity.Sommet import Sommet
from entity.Station import Station
from entity.Arete import Arete


from service.draw_graph import afficher_graphe

def bfs(graph : Graphe, start_sommet : Sommet):
    """Traverse le graphe en utilisant BFS à partir du sommet donné."""
    visited = set()
    queue = [start_sommet]  # Utilisation d'une liste comme file d'attente

    while queue:
        sommet = queue.pop(0)  # Retirer le premier élément de la liste
        if sommet not in visited:
            visited.add(sommet)
            adjacents = graph.get_sommet_adjacents(sommet)
            
            for adjacent in adjacents:
                if adjacent not in visited:
                    queue.append(adjacent)  # Ajouter à la fin de la liste

    return visited

def dfs(graph : Graphe, start_sommet : Sommet):
    """Traverse le graphe en utilisant DFS à partir du sommet donné."""
    visited = set()
    stack = [start_sommet]  # Utilisation d'une liste comme pile

    while stack:
        sommet = stack.pop()  # Retirer le dernier élément de la liste
        if sommet not in visited:
            visited.add(sommet)
            adjacents = graph.get_sommet_adjacents(sommet)
            
            for adjacent in reversed(adjacents):
                if adjacent not in visited:
                    stack.append(adjacent)  # Ajouter à la pile

    return visited

def bellman_ford(graph: Graphe, sommet_depart: Sommet):
    """Algorithme de Bellman-Ford"""
    # Initialiser les distances
    distances = {sommet: float('inf') for sommet in graph.sommets}
    distances[sommet_depart] = 0  # Initialiser la distance du sommet de départ à 0
    
    # Initialiser les prédécesseurs pour reconstruire le chemin
    predecesseur = {sommet: None for sommet in graph.sommets}
    
    # Dans le cours les valeurs finales sont obtenues après n-1 itérations max
    for _ in range(len(graph.sommets) - 1):
        for arete in graph.aretes:
            sommet_depart, sommet_arrive = arete.sommet_depart, arete.sommet_arrive
            poids = arete.poids

            if distances[sommet_depart] + poids < distances[sommet_arrive]:
                distances[sommet_arrive] = distances[sommet_depart] + poids
                predecesseur[sommet_arrive] = sommet_depart
    
    # Pas de poids négatif pas de verif de cycles absorbants
    return distances, predecesseur

def chemin_le_plus_court(graph : Graphe, sommet_depart : Sommet, sommet_arrive: Sommet):
    """Trouve et retourne le chemin le plus court entre deux sommets"""
    distances, predecesseur = bellman_ford(graph, sommet_depart)

    # Reconstruire le chemin depuis sommet_arrive
    chemin = []
    sommet_actuel = sommet_arrive

    if distances[sommet_arrive] == float('inf'):
        return None, "Aucun chemin trouvé."

    while sommet_actuel is not None:
        chemin.append(sommet_actuel)
        sommet_actuel = predecesseur[sommet_actuel]

    chemin.reverse()
    return chemin, distances[sommet_arrive]