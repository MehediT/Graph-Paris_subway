from entity.Sommet import Sommet
from entity.Station import Station
from entity.Arete import Arete

class Graphe:
    def __init__(self, sommets = {}, aretes = []):
        self.sommets = []
        self.aretes = []

    def ajouter_sommets(self, liste_sommets):
        """Ajoute plusieurs sommets au graphe"""
        for sommet in liste_sommets:
            self.sommets.append(sommet)

    def ajouter_aretes(self, liste_aretes):
        """Ajoute plusieurs aretes au graphe"""
        for arete in liste_aretes:
            self.aretes.append(arete)

    def ajouter_positions(self, positions):
        """Ajoute les positions des sommets"""
        # nb_added = []
        # nb_not_added = []

        for sommet in self.sommets:
            for x, y, nom_sommet in positions:
                if sommet.nom_sommet == nom_sommet:
                    sommet.pos.append((x, y))
                    # nb_added.append((x, y, nom_sommet))
                    
        # if len(nb_added) != len(positions):
        #     print("Erreur : toutes les positions n'ont pas été ajoutées")
        #     for x, y, nom_sommet in positions:
        #         if (x, y, nom_sommet) not in nb_added:
        #             nb_not_added.append((x, y, nom_sommet))
        # return nb_not_added

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
    
    def get_sommet_for_pos(self, x, y):
        """Renvoie le sommet à la position donnée"""
        for sommet in self.sommets:
            if sommet.is_within(x, y, 20, 20):
                return sommet
        return None
    
    # ICI ça a été donné par Chatgpt et Copilot

    def get_sommet_by_name(self, nom_sommet):
        """Renvoie le sommet avec le nom donné"""
        for sommet in self.sommets:
            if sommet.nom_sommet == nom_sommet:
                return sommet
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