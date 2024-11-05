import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from entity.Sommet import Sommet
from entity.Station import Station
from entity.Arete import Arete

from numpy import array

class Graphe:
    def __init__(self, sommets = {}, aretes = []):
        self.sommets = []
        self.aretes = []

    def ajouter_sommet(self, sommet):
        """Ajoute un sommet au graphe"""
        self.sommets.append(sommet)

    def ajouter_sommets(self, liste_sommets):
        """Ajoute plusieurs sommets au graphe"""
        for sommet in liste_sommets:
            self.ajouter_sommet(sommet)

    def ajouter_arete(self, arete):
        """Ajoute une arête au graphe"""
        self.aretes.append(arete)

    def ajouter_aretes(self, liste_aretes):
        """Ajoute plusieurs aretes au graphe"""
        for arete in liste_aretes:
            self.ajouter_arete(arete)

    
    def get_sommet_by_station(self, station_num):
        """Renvoie le sommet contenant la station donnée"""
        for sommet in self.sommets:
            for station in sommet.stations:
                if station.num_sommet == station_num:
                    return sommet
        return None
    
    def get_stations(self):
        """Renvoie les stations du graphe"""
        stations = []
        for sommet in self.sommets:
            stations.extend(sommet.stations)
        return stations



    # ICI ça a été donné par Chatgpt ert Copilot
    def get_sommet_by_name(self, nom_sommet):
        """Renvoie le sommet avec le nom donné"""
        for sommet in self.sommets:
            if sommet.nom_sommet == nom_sommet:
                return sommet
        return None
    
    def get_arete_by_sommets(self, sommet1, sommet2):
        """Renvoie l'arête entre les deux sommets donnés"""
        for arete in self.aretes:
            if (arete.sommet1.nom_sommet == sommet1.nom_sommet and arete.sommet2.nom_sommet == sommet2.nom_sommet) \
                or \
                (arete.sommet1.nom_sommet == sommet2.nom_sommet and arete.sommet2.nom_sommet == sommet1.nom_sommet):
                return arete
        return None
    
    def get_sommet_adjacents(self, sommet):
        """Renvoie les sommets adjacents au sommet donné"""
        sommets_adjacents = []
        for arete in self.aretes:
            if arete.sommet1.nom_sommet == sommet.nom_sommet:
                sommets_adjacents.append(self.get_sommet_by_name(arete.sommet2.nom_sommet))
            elif arete.sommet2.nom_sommet == sommet.nom_sommet:
                sommets_adjacents.append(self.get_sommet_by_name(arete.sommet1.nom_sommet))
        return sommets_adjacents
    
    def get_aretes_adjacentes(self, sommet):
        """Renvoie les arêtes adjacentes au sommet donné"""
        aretes_adjacentes = []
        for arete in self.aretes:
            if arete.sommet1.nom_sommet == sommet.nom_sommet or arete.sommet2.nom_sommet == sommet.nom_sommet:
                aretes_adjacentes.append(arete)
        return aretes_adjacentes
    
    def get_sommet_adjacent_le_plus_proche(self, sommet):
        """Renvoie le sommet adjacent le plus proche du sommet donné"""
        sommets_adjacents = self.get_sommet_adjacents(sommet)
        sommet_adjacent_le_plus_proche = sommets_adjacents[0]
        arete_adjacente_la_plus_proche = self.get_arete_by_sommets(sommet, sommet_adjacent_le_plus_proche)
        for sommet_adjacent in sommets_adjacents:
            arete_adjacente = self.get_arete_by_sommets(sommet, sommet_adjacent)
            if arete_adjacente.temps_en_secondes < arete_adjacente_la_plus_proche.temps_en_secondes:
                sommet_adjacent_le_plus_proche = sommet_adjacent
                arete_adjacente_la_plus_proche = arete_adjacente
        return sommet_adjacent_le_plus_proche, arete_adjacente_la_plus_proche