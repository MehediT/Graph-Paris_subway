from entity.Arete import Arete
from entity.Station import Station
from entity.Sommet import Sommet

def read_file_lines(src):
    """Affiche les lignes du fichier pour déboguer"""
    # Open the file in read mode
    with open(src, 'r') as file:
        # Read each line in the file
        for line in file:
            print(line.strip())

def read_file_metro(src):
    v_lines = []  # Liste des sommets
    e_lines = []  # Liste des arêtes

    # Open the file in read mode
    with open(src, 'r') as file:
        # Read each line in the file
        for line in file:
            # Traitement des sommets
            if line.strip().startswith('V'):
                v_lines = parse_sommet_line(v_lines,line.strip())

    with open(src, 'r') as file:
        # Read each line in the file
        for line in file:
            # Traitement des arêtes
            if line.strip().startswith('E'):
                arete = parse_arete_line(v_lines, line.strip())
                e_lines.append(arete)

    return v_lines, e_lines

def read_pospoint_file(src):
    """
    Lit le fichier pospoint.txt et extrait les positions des stations en pixels
    et les noms des stations.
    """
    positions = []  # Liste pour stocker les positions et noms des stations

    with open(src, 'r') as file:
        for line in file:
            # Suppression des espaces superflus et sauts de ligne
            line = line.strip()

            # Découper la ligne par le caractère ' ; '
            parts = line.split(';')

            if len(parts) == 3:
                # Extraire les coordonnées x, y
                x = int(parts[0])
                y = int(parts[1])

                # Remplacer les '@' par des espaces dans le nom de la station
                station_name = parts[2].replace('@', ' ')

                # Ajouter les données à la liste des positions
                positions.append((x, y, station_name))

    # Affiche ou retourne les positions
    return positions

def parse_sommet_line(sommets,line):
    """Extrait les données de la ligne V et retourne un objet Sommet"""
    # Exemple de format : "V 0069 Châtelet ;14 ;False 0"

    try:
        # On enlève le 'V' au début, puis on découpe la ligne en deux parties par ' ; '
        main_parts = line.split(';')

        if len(main_parts) < 3:
            raise ValueError(f"Ligne mal formatée : {line}")

        # Première partie avant le premier ' ; ' (num_sommet et nom_sommet)
        sommet_parts = main_parts[0].strip().split(maxsplit=2)

        if len(sommet_parts) < 3:
            raise ValueError(f"Ligne mal formatée pour le sommet : {main_parts[0]}")

        num_sommet = int(sommet_parts[1])  # Numéro du sommet
        nom_sommet = sommet_parts[2]  # Nom du sommet (peut contenir des espaces)

        # Deuxième partie pour le numéro de ligne
        numero_ligne = main_parts[1].strip()

        # Troisième partie (False 0) pour si_terminus et branchement
        terminus_br = main_parts[2].strip().split()

        if len(terminus_br) != 2:
            raise ValueError(f"Ligne mal formatée pour terminus et branchement : {main_parts[2]}")

        si_terminus = terminus_br[0].lower() == 'true'  # Terminus ou non (booléen)
        branchement = int(terminus_br[1])  # Branchement (0, 1, 2, ...)

        _match = next((sommet for sommet in sommets if sommet.nom_sommet == nom_sommet), None)
        if _match is None:
            _match = Sommet(nom_sommet=nom_sommet)
            sommets.append(_match)

        _match.stations.append(Station(num_sommet, numero_ligne, si_terminus, branchement))
        
        return sommets

    except ValueError as ve:
        print(f"Erreur de parsing dans la ligne : {line}. Détails : {ve}")
        return None  # Ou tu peux lever une exception selon ton besoin

def parse_arete_line(sommets, line):
    """Extrait les données de la ligne E et retourne un objet Arete"""
    # Ex : "E 105 296 42"

    parts = line.split()  # Séparer les parties par des espaces
    num_sommet1 = int(parts[1])  # Numéro du premier sommet
    num_sommet2 = int(parts[2])  # Numéro du deuxième sommet
    temps_en_secondes = int(parts[3])  # Temps de parcours en secondes

    match_sommet1 = next((sommet for sommet in sommets if sommet.asStation(num_sommet1)), None)
    match_sommet2 = next((sommet for sommet in sommets if sommet.asStation(num_sommet2)), None)
    
    if(match_sommet1 is None):
        raise ValueError(f"Sommet {num_sommet1} non trouvé dans la liste des sommets")
    if(match_sommet2 is None):
        raise ValueError(f"Sommet {num_sommet1} non trouvé dans la liste des sommets")

    # Création d'un objet Arete avec les données extraites
    return Arete(num_sommet1, num_sommet2, temps_en_secondes, match_sommet1, match_sommet2)

# # Exemple d'utilisation
# read_pospoint_file("../res/pospoints.txt")
# # Exemple d'utilisation
# read_file_metro("../res/metro.txt")