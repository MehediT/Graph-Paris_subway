class Arete:
    def __init__(self, num_station1, num_station2, time_sec, sommet1=None, sommet2=None):
        self.num_station1 = num_station1
        self.num_station2 = num_station2
        self.time_sec = time_sec

        self.sommet1 = sommet1
        self.sommet2 = sommet2

    def __repr__(self):
        """Pour afficher l'arête sous forme de chaîne de caractères"""
        if self.sommet1 is not None and self.sommet2 is not None:
            return f"Arete({self.num_station1}/{self.sommet1.nom_sommet}, {self.num_station2}/{self.sommet2.nom_sommet}, {self.time_sec})"
        return f"Arete({self.num_station1}, {self.num_station2}, {self.time_sec})"
