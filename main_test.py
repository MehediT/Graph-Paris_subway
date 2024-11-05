from entity.Graphe import Graphe
from service.algorithme import prim
from service.read_file import read_file_metro

sommets, aretes = read_file_metro("res/metro.txt")

graphe = Graphe()
graphe.ajouter_sommets(sommets)
graphe.ajouter_aretes(aretes)

prim(graphe)