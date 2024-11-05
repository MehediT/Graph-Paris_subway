import networkx as nx
import matplotlib.pyplot as plt

# Créer un graphe
G = nx.Graph()

# Ajouter des nœuds et des arêtes
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

# Définir les couleurs des arêtes, avec une couleur spécifique pour l'arête (1, 2)
edge_colors = ['red' if edge == (1, 2) or edge == (2, 1) else 'black' for edge in G.edges()]

# Dessiner le graphe avec les couleurs spécifiées
pos = nx.spring_layout(G)  # Définir la disposition des nœuds
nx.draw(G, pos, with_labels=True, edge_color=edge_colors, node_color='lightgrey', node_size=700, font_size=10)

# Afficher le graphe
plt.show()
