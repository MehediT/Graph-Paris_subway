from entity.Arete import Arete


class Sommet:
    def __init__(self, nom_sommet):
        self.nom_sommet = nom_sommet  # Nom de la station de métro

        self.stations = []  # Numéro du sommet
        self.pos = []  # Coordonnée x et y du sommet
        
    def get_station(self, num_station):
        for station in self.stations:
            if station.num_sommet == num_station:
                return station
        return None
    
    def get_station_by_arete(self, arete : Arete):
        for station in self.stations:
            if station.num_sommet == arete.sommet1.nom_sommet and arete.sommet1.nom_sommet != self.nom_sommet:
                return station
            elif station.num_sommet == arete.sommet2.nom_sommet and arete.sommet2.nom_sommet != self.nom_sommet:
                return station
        return None

    def asStation(self, station_num):
        for station in self.stations:
            if station.num_sommet == station_num:
                return True
        return False

    def __repr__(self):
        """Pour afficher le sommet sous forme de chaîne de caractères"""
        string = f"Sommet({self.nom_sommet}, {self.x}, {self.y})"
        string += "\n\tStations :"
        for station in self.stations:
            string += "\n\t" + str(station)
        return string

def number_to_color(n):
    colors = {
        1: "red",
        2: "blue",
        3: "green",
        4: "yellow",
        5: "orange",
        6: "purple",
        7: "pink",
        8: "brown",
        9: "black",
        10: "white",
        11: "gray",
        12: "cyan",
        13: "magenta",
        14: "lime",
        15: "indigo",
        16: "violet"
    }

    return colors.get(n, "Invalid number")

