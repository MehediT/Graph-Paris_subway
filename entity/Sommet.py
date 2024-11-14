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

    def get_info(self):
        info = []
        for station in self.stations:
            info.append(station.get_info())
        return info

    def asStation(self, station_num):
        for station in self.stations:
            if station.num_sommet == station_num:
                return True
        return False
    
    def is_within(self, click_x, click_y, width, height):
        for x, y in self.pos:
            if x - width <= click_x <= x + width  and y - width <= click_y <= y + height:
                return True
        return False

    def get_x(self, nums_station):
        station = self.get_station(nums_station)
        index = self.stations.index(station)
        if index > len(self.pos) - 1:
            return self.pos[0][0]
        return self.pos[index][0]
    
    def get_y(self, nums_station):
        station = self.get_station(nums_station)
        index = self.stations.index(station)
        if index > len(self.pos) - 1:
            return self.pos[0][1]
        return self.pos[index][1]
    
    def __repr__(self):
        """Pour afficher le sommet sous forme de chaîne de caractères"""
        string = f"Sommet({self.nom_sommet}"
        string += "\n\tStations :"
        for station in self.stations:
            string += "\n\t" + str(station)
        return string


