import networkx as nx
import matplotlib.pyplot as plt
from entity.Graphe import Graphe

def afficher_graphe(graph):
        """Affiche le graphe en utilisant NetworkX et Matplotlib"""
        G = nx.Graph()

        # Ajouter les sommets
        for sommet in graph.sommets:
            G.add_node(sommet.nom_sommet, pos=(sommet.x, sommet.y))

        # Ajouter les arêtes
        for arete in graph.aretes:
            G.add_edge(arete.nom_sommet1, arete.nom_sommet2, weight=arete.temps_en_secondes)

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
        edge_labels = {(arete.nom_sommet1, arete.nom_sommet2): f"{arete.temps_en_secondes} sec" for arete in graph.aretes}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

        # Afficher le graphe
        plt.title("Graphe du Métro")
        plt.show()