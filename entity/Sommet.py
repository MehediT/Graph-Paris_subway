class Sommet:
    def __init__(self, num_sommet, nom_sommet, numero_ligne, si_terminus=False, branchement=0):
        self.num_sommet = num_sommet  # Numéro du sommet
        self.nom_sommet = nom_sommet  # Nom de la station de métro
        self.numero_ligne = numero_ligne  # Numéro de la ligne
        self.si_terminus = si_terminus  # Si la station est un terminus (booléen)
        self.branchement = branchement  # Indicateur de branchement (0, 1, 2, etc.)

    def __repr__(self):
        """Pour afficher le sommet sous forme de chaîne de caractères"""
        return (f"Sommet({self.num_sommet}, '{self.nom_sommet}', "
                f"Ligne {self.numero_ligne}, Terminus: {self.si_terminus}, Branchement: {self.branchement})")

    def est_terminus(self):
        """Retourne vrai si la station est un terminus"""
        return self.si_terminus

    def ajouter_branchement(self, direction):
        """Modifie le nombre de branchements pour la station"""
        self.branchement = direction

    def changer_terminus(self, est_terminus):
        """Permet de définir ou modifier si c'est un terminus"""
        self.si_terminus = est_terminus
# Exemple d'utilisation
# s1 = Sommet(0070, "Châtelet", 7, False, 0)
# s2 = Sommet(0363, "Villejuif, Louis Aragon", 7, True, 2)
#
# print(s1)
# print(s2)

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

