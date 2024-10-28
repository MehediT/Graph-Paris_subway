def bfs(graph, sommet_depart):
    """Parcours en largeur (BFS)"""
    visited = set()
    queue = [sommet_depart]
    resultat = []

    while queue:
        sommet_actuel = queue.pop(0)
        if sommet_actuel not in visited:
            visited.add(sommet_actuel)
            resultat.append(sommet_actuel)
            voisins = graph.voisins(sommet_actuel)
            for voisin in voisins:
                if voisin not in visited:
                    queue.append(voisin)

    return resultat

def dfs(graph, sommet_depart):
    """Parcours en profondeur (DFS)"""
    visited = set()
    stack = [sommet_depart]
    resultat = []

    while stack:
        sommet_actuel = stack.pop()
        if sommet_actuel not in visited:
            visited.add(sommet_actuel)
            resultat.append(sommet_actuel)
            voisins = graph.voisins(sommet_actuel)
            for voisin in voisins:
                if voisin not in visited:
                    stack.append(voisin)

    return resultat

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
