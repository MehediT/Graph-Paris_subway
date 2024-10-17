class Graphe:
    def __init__(self, sommets= {}, aretes = []):
        self.sommets = {}
        self.aretes = []

    def ajouter_sommet(self, sommet):
        """Ajoute un sommet au graphe"""
        self.sommets[sommet.num_sommet] = sommet

    def ajouter_sommets(self, liste_sommets):
        """Ajoute plusieurs sommets au graphe"""
        for sommet in liste_sommets:
            self.ajouter_sommet(sommet)

    def ajouter_arete(self, arete):
        """Ajoute une arête au graphe et vérifie que les sommets existent"""
        if arete.num_sommet1 in self.sommets and arete.num_sommet2 in self.sommets:
            self.aretes.append(arete)
        else:
            raise ValueError("Un des sommets de l'arête n'existe pas dans le graphe.")

    def ajouter_aretes(self, liste_aretes):
        """Ajoute plusieurs aretes au graphe"""
        for arete in liste_aretes:
            self.ajouter_arete(arete)

    def voisins(self, num_sommet):
        """Renvoie la liste des sommets voisins d'un sommet donné"""
        voisins = []
        for arete in self.aretes:
            if arete.num_sommet1 == num_sommet:
                voisins.append(arete.num_sommet2)
            elif arete.num_sommet2 == num_sommet:
                voisins.append(arete.num_sommet1)
        return voisins