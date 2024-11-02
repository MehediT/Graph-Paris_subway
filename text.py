
# def bellman_ford2(graph: Graphe, sommet_depart: Sommet):
#     """Algorithme de Bellman-Ford"""
#     # Initialiser les distances
#     distances = {sommet: float('inf') for sommet in graph.sommets}
#     distances[sommet_depart] = 0  # Initialiser la distance du sommet de départ à 0
    
#     # Initialiser les prédécesseurs pour reconstruire le chemin
#     predecesseur = {sommet: None for sommet in graph.sommets}
    
#     # Dans le cours les valeurs finales sont obtenues après n-1 itérations max
#     for _ in range(len(graph.sommets) - 1):
#         for arete in graph.aretes:
#             sommet_depart, sommet_arrive = arete.sommet1, arete.sommet2
#             poids = arete.time_sec

#             if distances[sommet_depart] + poids < distances[sommet_arrive]:
#                 distances[sommet_arrive] = distances[sommet_depart] + poids
#                 predecesseur[sommet_arrive] = sommet_depart

#             if distances[sommet_arrive] + poids < distances[sommet_depart]:
#                 distances[sommet_depart] = distances[sommet_arrive] + poi#ds
#                 predecesseur[sommet_depart] = sommet_arrive
    
#     # Pas de poids négatif pas de verif de cycles absorbants
#     return distances, predecesseur

def bellman_ford(graph: Graphe, sommet: Sommet):
    """Algorithme de Bellman-Ford"""
    # Initialiser les distances

    distances = {}
    predecesseur = {}

    for sommet in graph.sommets:
        for station in sommet.stations:
            distances[station.num_sommet] = float('inf')
            predecesseur[station] = None

    for station in sommet.stations:
        distances[station.num_sommet] = 0  # Initialiser la distance du sommet de départ à 0
    
    # Dans le cours les valeurs finales sont obtenues après n-1 itérations max
    for _ in range(len(distances) - 1):
        for arete in graph.aretes:
            sommet_depart, sommet_arrive = arete.num_station1, arete.num_station2
            poids = arete.time_sec

            if distances[sommet_depart] + poids < distances[sommet_arrive]:
                distances[sommet_arrive] = distances[sommet_depart] + poids
                predecesseur[sommet_arrive] = sommet_depart

            if distances[sommet_arrive] + poids < distances[sommet_depart]:
                distances[sommet_depart] = distances[sommet_arrive] + poids
                predecesseur[sommet_depart] = sommet_arrive
    
    # Pas de poids négatif pas de verif de cycles absorbants
    return distances, predecesseur
