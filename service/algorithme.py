from entity.Graphe import Graphe
from entity.Sommet import Sommet

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

def bellman_ford(graph, sommet_depart):
    """Algorithme de Bellman-Ford pour trouver le plus court chemin depuis sommet_depart

        Pour celui y a eu l'utilisation de Chatgpt pour corriger les bugs
    """
    # Initialiser les distances
    distances = {sommet: float('inf') for sommet in graph.sommets}
    distances[sommet_depart] = 0

    # Initialiser les prédécesseurs pour reconstruire le chemin
    predecesseur = {sommet: None for sommet in graph.sommets}

    # Relaxation des arêtes (|V| - 1 fois)
    for _ in range(len(graph.sommets) - 1):
        for arete in graph.aretes:
            u, v = arete.num_sommet1, arete.num_sommet2

            poids = arete.temps_en_secondes

            # l'arête u → v
            if distances[u] != float('inf') and distances[u] + poids < distances[v]:
                distances[v] = distances[u] + poids
                predecesseur[v] = u

            # l'arête v → u
            if distances[v] != float('inf') and distances[v] + poids < distances[u]:
                distances[u] = distances[v] + poids
                predecesseur[u] = v

    # Vérification des cycles de poids négatifs
    for arete in graph.aretes:
        u, v = arete.num_sommet1, arete.num_sommet2
        poids = arete.temps_en_secondes
        if distances[u] != float('inf') and distances[u] + poids < distances[v]:
            raise ValueError("Le graphe contient un cycle de poids négatif.")

    return distances, predecesseur

def chemin_le_plus_court(graph, sommet_depart, sommet_arrive):
    """Trouve et retourne le chemin le plus court entre deux sommets"""
    distances, predecesseur = bellman_ford(graph, sommet_depart)

    # Reconstruire le chemin depuis sommet_arrive
    chemin = []
    sommet_actuel = sommet_arrive

    if distances[sommet_arrive] == float('inf'):
        return None, "Aucun chemin trouvé."

    while sommet_actuel is not None:
        chemin.append(graph.sommets[sommet_actuel])
        sommet_actuel = predecesseur[sommet_actuel]

    chemin.reverse()
    return chemin, distances[sommet_arrive]
