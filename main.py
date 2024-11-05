from service.read_file import read_file_metro

sommets, aretes = read_file_metro("res/metro.txt")
# print("Sommets : ")
# for sommet in sommets:
# 	print(sommet)
# print()
# print("Arêtes : ")
# for arete in aretes:
# 	print(arete)


from entity.Graphe import Graphe
from service.draw_graph import afficher_graphe

graphe = Graphe()
graphe.ajouter_sommets(sommets)
graphe.ajouter_aretes(aretes)

# afficher_graphe(graphe)

from entity.Graphe import Graphe
from service.algorithme import bellman_ford, chemin_le_plus_court

carrefour_pleyel = "Carrefour Pleyel"
start_sommet = graphe.get_sommet_by_name(carrefour_pleyel)

distance, predecesseurs = bellman_ford(graphe, start_sommet)
# for station, poids in distance.items():
# 	sommet = graphe.get_sommet_by_station(station)
# 	print(sommet.nom_sommet, ":", poids)

vlf_pvc = "Villejuif, P. Vaillant Couturier"
sommet_end = graphe.get_sommet_by_name(vlf_pvc)

chemin, temps = chemin_le_plus_court(graphe, start_sommet, sommet_end)

print("\nBellman Ford")
print("Vous êtes aux :", carrefour_pleyel)
for	num_station, sommet in chemin:
	station = sommet.get_station(num_station)

	print("ligne : ", station.numero_ligne, end=" ")
	if station.branchement != 0:
		print("branchement : ", station.branchement, end="")
	print("\n   ", sommet.nom_sommet)
