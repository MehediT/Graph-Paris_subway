class Arete:
    def __init__(self, num_sommet1, num_sommet2, temps_en_secondes):
        self.num_sommet1 = num_sommet1
        self.num_sommet2 = num_sommet2
        self.temps_en_secondes = temps_en_secondes

    def __repr__(self):
        """Pour afficher l'arête sous forme de chaîne de caractères"""
        return (f"Arete(Sommet1: {self.num_sommet1}, "
                f"Sommet2: {self.num_sommet2}, Temps: {self.temps_en_secondes}s)")

# Exemple d'utilisation :
# a1 = Arete(105, 296, 42)
# print(a1)
