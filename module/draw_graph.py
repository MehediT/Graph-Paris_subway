import networkx as nx
import matplotlib.pyplot as plt
from module.read_file import read_file_metro, sample_metro

def draw_metro_graph(sommets, aretes):
    # Créer un graphe vide
    G = nx.Graph()

    # Ajouter les sommets (nœuds) au graphe
    for sommet in sommets:
        G.add_node(sommet.num_sommet, name=sommet.nom_sommet, ligne=sommet.numero_ligne, terminus=sommet.si_terminus)

    # Ajouter les arêtes au graphe avec le temps en tant que poids
    for arete in aretes:
        G.add_edge(arete.num_sommet1, arete.num_sommet2, weight=arete.temps_en_secondes)

    # Positionner les sommets avec plus d'espacement
    pos = nx.spring_layout(G, k=2, seed=1)  # Increase k to spread out nodes more

    # Ajuster la taille de la figure
    plt.figure(figsize=(80, 80))  # Increase the figure size (width, height)

    # Dessiner les sommets avec des labels (nom de station)
    node_labels = {sommet.num_sommet: sommet.nom_sommet for sommet in sommets}
    nx.draw(G, pos, with_labels=False, node_color='lightgreen', node_size=800)

    # Ajouter les labels des sommets (noms des stations)
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8)

    # Dessiner les arêtes avec des poids (temps de trajet)
    edge_labels = {(arete.num_sommet1, arete.num_sommet2): f"{arete.temps_en_secondes} sec" for arete in aretes}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    print("Nb sommets :", G.number_of_nodes())
    print("Nb aretes :", G.number_of_edges())

    # Afficher le graphe
    plt.title("Graphe du Métro")
    plt.show()

# Exemple d'appel après avoir lu les sommets et arêtes
v_lines, e_lines = read_file_metro("../res/metro.txt")
# v_lines, e_lines = sample_metro()
draw_metro_graph(v_lines, e_lines)
