class Arete:
    def __init__(self, num_station1, num_station2, time_sec, sommet1 = None, sommet2=None):
        self.num_station1 = num_station1
        self.num_station2 = num_station2
        self.time_sec = time_sec

        self.sommet1 = sommet1
        self.sommet2 = sommet2

class Station:
    def __init__(self, num_sommet, numero_ligne, si_terminus=False, branchement=0):
        self.num_sommet = num_sommet # Numéro du sommet
        self.numero_ligne = numero_ligne  # Numéro de la ligne
        self.si_terminus = si_terminus  # Si la station est un terminus (booléen)
        self.branchement = branchement  # Indicateur de branchement (0, 1, 2, etc.)
    
class Sommet:
    def __init__(self, nom_sommet, x=0, y=0):
        self.nom_sommet = nom_sommet  # Nom de la station de métro

        self.stations = []  # Numéro du sommet
        self.x = x # En pixel sur la map
        self.y = y # En pixel sur la map

    def get_station(self, num_station):
        for station in self.stations:
            if station.num_sommet == num_station:
                return station
        return None
    
class Graphe:
    def __init__(self, sommets = [], aretes = []):
        self.sommets = sommets
        self.aretes = aretes

    def get_sommet_by_station(self, station_num):
        """Renvoie le sommet contenant la station donnée"""
        for sommet in self.sommets:
            for station in sommet.stations:
                if station.num_sommet == station_num:
                    return sommet
        return None

import networkx as nx
import matplotlib.pyplot as plt

def afficher_graphe(graph):
    """Affiche le graphe en utilisant NetworkX et Matplotlib"""
    G = nx.Graph()

    # Ajouter les sommets
    for sommet in graph.sommets:
        G.add_node(sommet.nom_sommet, pos=(sommet.x, sommet.y))

    # Ajouter les arêtes
    for arete in graph.aretes:
        G.add_edge(arete.sommet1.nom_sommet, arete.sommet2.nom_sommet, weight=arete.time_sec)

    # Positionner les sommets avec plus d'espacement
    pos = nx.spring_layout(G, seed=1)

    # Ajuster la taille de la figure
    plt.figure(figsize=(50, 50))

    # Dessiner les sommets avec des labels (nom de station)
    node_labels = {sommet.nom_sommet: sommet.nom_sommet for sommet in graph.sommets}
    nx.draw(G, pos, with_labels=False, node_color='lightgreen', node_size=800)

    # Ajouter les labels des sommets (noms des stations)
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8)

    # Dessiner les arêtes avec des poids (temps de trajet)
    edge_labels = {(arete.sommet1.nom_sommet, arete.sommet2.nom_sommet): f"{arete.time_sec} sec" for arete in graph.aretes}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    # Afficher le graphe
    plt.title("Graphe du Métro")
    plt.show()