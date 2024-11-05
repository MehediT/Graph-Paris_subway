from service.read_file import read_file_metro,read_pospoint_file
from entity.Graphe import Graphe
sommets, aretes = read_file_metro("res/metro.txt")

graphe = Graphe()
graphe.ajouter_sommets(sommets)
graphe.ajouter_aretes(aretes)

positions = read_pospoint_file("res/pospoints.txt")

graphe.ajouter_positions(positions)