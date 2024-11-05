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

def bellman_ford(graph, source):
        # Initialisation des distances et du prédécesseur
        # distances = {sommet: float('inf') for sommet in graph.sommets}
        # distances[source] = 0
        # predecesseur = {sommet: None for sommet in graph.sommets}

        distances = {station.num_sommet: float('inf') for station in graph.get_stations()}
        for station in source.stations:
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

def chemin_le_plus_court(graph : Graphe, sommet_depart : Station, sommet_arrive: Sommet):
    """Trouve et retourne le chemin le plus court entre deux sommets"""
    distances, predecesseur = bellman_ford(graph, sommet_depart)

    # Reconstruire le chemin depuis sommet_arrive
    for station in sommet_arrive.stations:
        if distances[station.num_sommet] == float('inf'):
            return None, "Aucun chemin trouvé."

    chemin = []

    sommet_actuel = sommet_arrive
    num_station_actuel = sommet_actuel.stations[0].num_sommet

    for station in sommet_actuel.stations:
        if distances[station.num_sommet] < distances[num_station_actuel]:
            num_station_actuel = station.num_sommet

    while sommet_actuel is not sommet_depart:
        chemin.append((num_station_actuel, sommet_actuel))
        num_station_actuel , sommet_actuel = predecesseur[num_station_actuel]

    chemin.reverse()
    return chemin, distances[sommet_arrive.stations[0].num_sommet]
