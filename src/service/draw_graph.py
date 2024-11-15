import networkx as nx
import matplotlib.pyplot as plt
from entity.Graphe import Graphe

def afficher_graphe(graph, title="Graphe du Métro"):
    """Affiche le graphe en utilisant NetworkX et Matplotlib"""
    G = nx.Graph()

    # Ajouter les sommets
    for sommet in graph.sommets:
        G.add_node(sommet.nom_sommet)

    # Ajouter les arêtes
    for arete in graph.aretes:
        G.add_edge(arete.sommet1.nom_sommet, arete.sommet2.nom_sommet)

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
    print(G)
    # Afficher le graphe
    plt.title(title)
    plt.show()

def afficher_acpm(graph, acpm=[]):
    """Affiche le graphe en utilisant NetworkX et Matplotlib"""
    G = nx.Graph()

    # Ajouter les sommets
    for sommet in graph.sommets:
        G.add_node(sommet.nom_sommet)
    # Ajouter les arêtes
    for arete in graph.aretes:
        G.add_edge(arete.sommet1.nom_sommet, arete.sommet2.nom_sommet)

    # Positionner les sommets avec plus d'espacement
    pos = nx.spring_layout(G, seed=1)

    # edges
    map = []
    for arete in acpm:
        map.append((arete.sommet1.nom_sommet, arete.sommet2.nom_sommet))

    edge_colors = ['red' if edge in map else 'black' for edge in G.edges()]

    # Ajuster la taille de la figure
    plt.figure(figsize=(50, 50))

    # Dessiner les sommets avec des labels (nom de station)
    node_labels = {sommet.nom_sommet: sommet.nom_sommet for sommet in graph.sommets}
    nx.draw(G, pos, with_labels=False, edge_color=edge_colors, node_color='lightgreen', node_size=800)

    # Ajouter les labels des sommets (noms des stations)
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8)

    # Dessiner les arêtes avec des poids (temps de trajet)
    edge_labels = {(arete.sommet1.nom_sommet, arete.sommet2.nom_sommet): f"{arete.time_sec} sec" for arete in graph.aretes}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    # Afficher le graphe
    plt.title("Arbre Couvrant de Poids Minimum (ACPM par nous)")
    plt.show()


def afficher_acpm_networkx(graph):
    """Affiche l'arbre couvrant de poids minimum (ACPM) en utilisant Prim"""
    G = nx.Graph()

    # Ajouter les sommets
    for sommet in graph.sommets:
        G.add_node(sommet.nom_sommet)

    # Ajouter les arêtes avec les poids
    for arete in graph.aretes:
        G.add_edge(arete.sommet1.nom_sommet, arete.sommet2.nom_sommet, weight=arete.time_sec)

    # Calculer l'ACPM en utilisant l'algorithme de Prim
    mst = nx.minimum_spanning_tree(G, algorithm='prim')

    # Positionner les sommets pour un espacement optimal
    pos = nx.spring_layout(G, seed=1)

    # Ajuster la taille de la figure
    plt.figure(figsize=(50, 50))

    # Dessiner les sommets avec des labels (nom de station)
    node_labels = {sommet.nom_sommet: sommet.nom_sommet for sommet in graph.sommets}
    nx.draw(mst, pos, with_labels=False, node_color='lightblue', node_size=800)

    # Ajouter les labels des sommets
    nx.draw_networkx_labels(mst, pos, labels=node_labels, font_size=8)

    # Dessiner les arêtes de l'ACPM avec les poids (temps de trajet)
    edge_labels = {(u, v): f"{d['weight']} sec" for u, v, d in mst.edges(data=True)}
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=edge_labels, font_size=8)

    # Afficher l'ACPM
    plt.title("Arbre Couvrant de Poids Minimum (ACPM par NetworkX)")
    plt.show()
