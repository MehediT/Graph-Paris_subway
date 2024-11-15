class Station:
    def __init__(self, num_sommet, numero_ligne, si_terminus=False, branchement=0):
        self.num_sommet = num_sommet
        self.numero_ligne = numero_ligne 
        self.si_terminus = si_terminus
        self.branchement = branchement
    
    def get_info(self):
        """Renvoie les informations de la station"""
        return {
            'num_sommet': self.num_sommet,
            'numero_ligne': self.numero_ligne,
            'si_terminus': self.si_terminus,
            'branchement': self.branchement
        }

    def __str__(self):
        """Pour afficher la station sous forme de chaîne de caractères"""
        string = f"{self.num_sommet} : ligne - {self.numero_ligne}, terminus - {self.si_terminus}, branchement - {self.branchement})"
        return string