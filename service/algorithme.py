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

def bellman_ford(graph, station):
        # Initialisation des distances et du prédécesseur
        # distances = {sommet: float('inf') for sommet in graph.sommets}
        # distances[source] = 0
        # predecesseur = {sommet: None for sommet in graph.sommets}

        distances = {station.num_sommet: float('inf') for station in graph.get_stations()}
        distances[station.num_sommet] = 0
        predecesseur = {station.num_sommet: None for station in graph.get_stations()}

        # Relaxation des arêtes |V|-1 fois (où |V| est le nombre de sommets)
        for _ in range(len(graph.sommets) - 1):
            for arete in graph.aretes:
                # u = arete.sommet1
                u = arete.num_station1
                # v = arete.sommet2
                v = arete.num_station2

                poids = arete.time_sec

                if distances[u] != float('inf') and distances[u] + poids < distances[v]:
                    distances[v] = distances[u] + poids
                    predecesseur[v] = (u , arete.sommet1)
                
                if distances[v] != float('inf') and distances[v] + poids < distances[u]:
                    distances[u] = distances[v] + poids
                    predecesseur[u] = (v , arete.sommet2)

        return distances, predecesseur

def chemin_le_plus_court(graph : Graphe, station_depart : Station, station_arrive: Station):
    """Trouve et retourne le chemin le plus court entre deux sommets"""
    distances, predecesseur = bellman_ford(graph, station_depart)

    # Reconstruire le chemin depuis sommet_arrive
    if distances[station_arrive.num_sommet] == float('inf'):
        return None, "Aucun chemin trouvé."

    chemin = []

    station_actuel = station_arrive
    sommet_actuel = graph.get_sommet_by_station(station_actuel.num_sommet)
    num_station_actuel = station_actuel.num_sommet

    while station_actuel is not station_depart:
        chemin.append((num_station_actuel, sommet_actuel))
        num_station_actuel , sommet_actuel = predecesseur[num_station_actuel]
        station_actuel = sommet_actuel.get_station(num_station_actuel)

    chemin.reverse()
    return chemin, distances[station_arrive.num_sommet]

import random

def prim(graph: Graphe, random_sommet: Sommet = None) :
    # Prendre n'importe quel sommet comme sommet de départ
    if random_sommet is None:
        random_sommet = random.choice(graph.sommets)
        
    visited = set()
    arete_to_visite = set()
    acpm = []
    
    visited.add(random_sommet)
    current_aretes = graph.get_aretes_adjacentes(random_sommet)

    arete_to_visite.update(current_aretes)

    while len(visited) < len(graph.sommets):
        smallest_weighted_arete = smallest_weight(arete_to_visite)
        
        # Ajouter l'arête la plus petite à l'ACPM
        acpm.append(smallest_weighted_arete)

        # Ajouter les sommets de l'arête à l'ensemble des sommets visités
        visited.add(smallest_weighted_arete.sommet1)
        visited.add(smallest_weighted_arete.sommet2)

        for arete in graph.get_aretes_adjacentes(smallest_weighted_arete.sommet1):
            if arete.sommet1 not in visited or arete.sommet2 not in visited:
                arete_to_visite.add(arete)

        for arete in graph.get_aretes_adjacentes(smallest_weighted_arete.sommet2):
            if arete.sommet1 not in visited or arete.sommet2 not in visited:
                arete_to_visite.add(arete)

        #Retirer l'arête la plus petite de l'ensemble des arêtes à visiter
        arete_to_visite.remove(smallest_weighted_arete)
    
    return acpm

def smallest_weight(aretes) :
    smallest = list(aretes)[0]
    for arete in aretes:
        if arete.time_sec < smallest.time_sec:
            smallest = arete
    return smallest