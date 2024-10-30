# Exemple d'utilisation
from entity.Graphe import Graphe
from service.draw_graph import draw_metro_graph
from service.read_file import read_file_metro
from service.algorithme import bfs, dfs, chemin_le_plus_court


# Exemple d'appel après avoir lu les sommets et arêtes
sommets, aretes = read_file_metro("res/metro.txt")
# v_lines, e_lines = sample_metro()
# Affichage ou autre traitement des sommets et arêtes
print("Sommets : ", sommets)
print("Arêtes : ", aretes)
print()

# Visualisation du graphe
# draw_metro_graph(sommets, aretes)

graphe = Graphe()
graphe.ajouter_sommets(sommets)
graphe.ajouter_aretes(aretes)

# num_sommet = graphe.sommets[0].num_sommet

bfs = bfs(graphe,363)
dfs = dfs(graphe,363)
sizeOfBFSList = len(bfs)
sizeOfDFSList = len(dfs)
sizeOfList = len(sommets)
print()

### 3.1 Connexité
# DFS à partir du sommet 0363 Villejuif louis aragon
print("BFS\n\tListe des sommets atteignable via Villejuif louis aragon : ", bfs)
print("Nb sommet :",sizeOfList," Nb sommet atteignable : ",sizeOfBFSList)
print("Via BFS Le graphe ", "est connexe." if sizeOfList == sizeOfBFSList else "n'est pas connexe.")

print()
# BFS à partir du sommet 0363 Villejuif louis aragon
print("DFS\n\tListe des sommets atteignable via Villejuif louis aragon : ", dfs)
print("Nb sommet :",sizeOfList," Nb sommet atteignable : ",sizeOfDFSList)
print("Via DFS Le graphe ", "est connexe." if sizeOfList == sizeOfDFSList else "n'est pas connexe.")

### 3.2 Le plus court chemin
print()
# Calculer le chemin le plus court entre la Station A (1) et la Station D (4)
# chemin, distance = chemin_le_plus_court(graphe,363, 181)
chemin, temps = chemin_le_plus_court(graphe,48, 365)
print("Chemin")
[print(arrete.num_sommet, '-', arrete.nom_sommet, '(', arrete.numero_ligne, ')') for arrete in chemin]
if temps >= 60 :
      print(f"Le meilleur itinéraire prend environ {int(temps / 60)} minutes.")
else :
      print(f"Le meilleur itinéraire prend environ {int(temps / 60)} secondes.")


### 3.2 Le plus court chemin
