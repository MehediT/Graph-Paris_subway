from service.read_file import read_file_metro

sommets, aretes = read_file_metro("res/metro.txt")
print("Sommets : ")
for sommet in sommets:
    print(sommet)
print()

print("Arêtes : ")
for arete in aretes:
    print(arete)
    
from entity.Graphe import Graphe
from service.draw_graph import afficher_graphe

graphe = Graphe()
graphe.ajouter_sommets(sommets)
graphe.ajouter_aretes(aretes)

afficher_graphe(graphe)

from service.algorithme import bfs

sizeOfList = len(sommets)
vlf_aragon = graphe.get_sommet_by_name("Villejuif, Louis Aragon")
bfslist = bfs(graphe, vlf_aragon)
sizeOfBFSList = len(bfslist)

print("BFS")
#print("\n\tListe des sommets atteignable via Villejuif louis aragon : ", bfslist)
print("Nb sommet :",sizeOfList," Nb sommet atteignable : ",sizeOfBFSList)
print("Via BFS Le graphe ", "est connexe." if sizeOfList == sizeOfBFSList else "n'est pas connexe.")

from service.algorithme import dfs

sizeOfList = len(sommets)
vlf_aragon = graphe.get_sommet_by_name("Villejuif, Louis Aragon")

dfs_list = dfs(graphe,vlf_aragon)
sizeOfDFSList = len(dfs_list)

print("DFS")
#print("\n\tListe des sommets atteignable via Villejuif louis aragon : ", dfs_list)
print("Nb sommet :",sizeOfList," Nb sommet atteignable : ",sizeOfDFSList)
print("Via DFS Le graphe ", "est connexe." if sizeOfList == sizeOfDFSList else "n'est pas connexe.")

from entity.Graphe import Graphe
from service.algorithme import bellman_ford, chemin_le_plus_court

carrefour_pleyel = "Carrefour Pleyel"
start_sommet = graphe.get_sommet_by_name(carrefour_pleyel)
station_start = start_sommet.stations[0]

distances, predecesseur = bellman_ford(graphe, station_start)

for station, poids in distances.items():
	sommet = graphe.get_sommet_by_station(station)
	print(sommet.nom_sommet, ":", poids)

vlf_pvc = "Villejuif, P. Vaillant Couturier"
sommet_end = graphe.get_sommet_by_name(vlf_pvc)
station_end = sommet_end.stations[0]

chemin, temps = chemin_le_plus_court(graphe, station_start, station_end)

print("\nBellman Ford")
print("Vous êtes aux :", carrefour_pleyel)
for	num_station, sommet in chemin:
	station = sommet.get_station(num_station)

	print("ligne : ", station.numero_ligne, end=" ")
	if station.branchement != 0:
		print("branchement : ", station.branchement, end="")
	print("\n   ", sommet.nom_sommet)
	
time_minutes = int(temps / 60)
sec_minutes = int(temps % 60)

print("Vous êtes à :", vlf_pvc, "en", time_minutes, "minutes et ", sec_minutes, "secondes")

from entity.Graphe import Graphe
from service.algorithme import prim
from service.read_file import read_file_metro

sommets, aretes = read_file_metro("res/metro.txt")

graphe = Graphe()
graphe.ajouter_sommets(sommets)
graphe.ajouter_aretes(aretes)

prim(graphe)
