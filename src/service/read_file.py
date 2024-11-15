from entity.Arete import Arete
from entity.Station import Station
from entity.Sommet import Sommet

def read_file_lines(src):
    """Affiche les lignes du fichier pour déboguer"""
    with open(src, 'r') as file:
        for line in file:
            print(line.strip())

def read_file_metro(src):
    v_lines = []
    e_lines = []

    with open(src, 'r') as file:
        for line in file:
            if line.strip().startswith('V'):
                v_lines = parse_sommet_line(v_lines,line.strip())

    with open(src, 'r') as file:
        for line in file:
            if line.strip().startswith('E'):
                arete = parse_arete_line(v_lines, line.strip())
                e_lines.append(arete)

    return v_lines, e_lines

def read_pospoint_file(src):
    """
    Lit le fichier pospoint.txt et extrait les positions des stations en pixels
    et les noms des stations.
    """
    positions = [] 
    with open(src, 'r') as file:
        for line in file:
            line = line.strip()

            parts = line.split(';')

            if len(parts) == 3:
                x = int(parts[0])
                y = int(parts[1])

                station_name = parts[2].replace('@', ' ')

                positions.append((x, y, station_name))
    return positions

def parse_sommet_line(sommets,line):
    """Extrait les données de la ligne V et retourne un objet Sommet"""
    try:
        main_parts = line.split(';')
        if len(main_parts) < 3:
            raise ValueError(f"Ligne mal formatée : {line}")
        sommet_parts = main_parts[0].strip().split(maxsplit=2)
        if len(sommet_parts) < 3:
            raise ValueError(f"Ligne mal formatée pour le sommet : {main_parts[0]}")
        num_sommet = int(sommet_parts[1])
        nom_sommet = sommet_parts[2]
        numero_ligne = main_parts[1].strip()
        terminus_br = main_parts[2].strip().split()
        if len(terminus_br) != 2:
            raise ValueError(f"Ligne mal formatée pour terminus et branchement : {main_parts[2]}")
        si_terminus = terminus_br[0].lower() == 'true'
        branchement = int(terminus_br[1])
        _match = next((sommet for sommet in sommets if sommet.nom_sommet == nom_sommet), None)
        if _match is None:
            _match = Sommet(nom_sommet=nom_sommet)
            sommets.append(_match)
        _match.stations.append(Station(num_sommet, numero_ligne, si_terminus, branchement))
        
        return sommets

    except ValueError as ve:
        print(f"Erreur de parsing dans la ligne : {line}. Détails : {ve}")
        return None 

def parse_arete_line(sommets, line):
    """Extrait les données de la ligne E et retourne un objet Arete"""
    parts = line.split()
    num_sommet1 = int(parts[1])
    num_sommet2 = int(parts[2])
    temps_en_secondes = int(parts[3])

    match_sommet1 = next((sommet for sommet in sommets if sommet.asStation(num_sommet1)), None)
    match_sommet2 = next((sommet for sommet in sommets if sommet.asStation(num_sommet2)), None)
    
    if(match_sommet1 is None):
        raise ValueError(f"Sommet {num_sommet1} non trouvé dans la liste des sommets")
    if(match_sommet2 is None):
        raise ValueError(f"Sommet {num_sommet1} non trouvé dans la liste des sommets")

    return Arete(num_sommet1, num_sommet2, temps_en_secondes, match_sommet1, match_sommet2)