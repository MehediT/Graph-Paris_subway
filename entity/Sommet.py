class Sommet:
    def __init__(self, nom_sommet, x=0, y=0):
        self.nom_sommet = nom_sommet  # Nom de la station de métro

        self.stations = []  # Numéro du sommet
        self.x = x # En pixel sur la map
        self.y = y # En pixel sur la map

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

