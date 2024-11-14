# Rapport de Projet : « Vas-y dans le métro »

## 1. Introduction
Ce projet utilise la théorie des graphes pour modéliser le réseau de métro parisien. Le réseau est représenté comme un graphe non orienté, et plusieurs algorithmes sont implémentés pour résoudre des problèmes pratiques liés aux trajets et à la structure du réseau. On rappelle que le graph est non orienté bien que certaine ligne possède des orientations notament la ligne 10 qui sera simplifier.

**Langage utilisé** : Python
**Bibliothèques**
- Les bibliothèques standard de Python sont utilisées pour la gestion des structures de données et des algorithmes.
- Pour la partie visualisation en a opté pour NetworkX

---

## 2. Structure des Données
Le réseau de métro est modélisé par les classes suivantes :

### 2.1 Classe `Graphe`
La classe `Graphe` est utilisée pour gérer l'ensemble des sommets (stations) et des arêtes (liaisons entre stations).

```python
class Graphe:
    def __init__(self):
        self.sommets = []  # Liste des sommets
        self.aretes = []   # Liste des arêtes
```

- **Fonction `get_sommet_by_station`** : Cette fonction recherche et retourne un sommet spécifique à partir de son numéro de station.
- **Fonction `get_info_for_station_num`** : Fournit des informations sur une station, telles que le nom de la station et la ligne.

### 2.2 Classe `Sommet`
La classe `Sommet` représente une station de métro avec des stations associées et des coordonnées géographiques.

```python
class Sommet:
    def __init__(self, nom_sommet):
        self.nom_sommet = nom_sommet
        self.stations = []  # Liste des objets Station
        self.pos = []       # Coordonnées (x, y) de la station
```

### 2.3 Classe `Station`
La classe `Station` contient des informations sur une station, y compris si elle est un terminus et les branchements.

```python
class Station:
    def __init__(self, num_sommet, numero_ligne, si_terminus=False, branchement=0):
        self.num_sommet = num_sommet
        self.numero_ligne = numero_ligne
        self.si_terminus = si_terminus
        self.branchement = branchement
```

### 2.4 Classe `Arete`
La classe `Arete` représente une connexion entre deux stations avec le temps de parcours.

```python
class Arete:
    def __init__(self, num_station1, num_station2, time_sec, sommet1=None, sommet2=None):
        self.num_station1 = num_station1
        self.num_station2 = num_station2
        self.time_sec = time_sec
        self.sommet1 = sommet1
        self.sommet2 = sommet2
```

---

## 3. Algorithmes Implémentés
### 3.1 Vérification de la Connexité
L'algorithme de parcours en largeur (BFS) est utilisé pour vérifier que le graphe est connexe. Si un sommet ne peut pas être atteint, des arêtes supplémentaires sont nécessaires pour rendre le graphe connexe.

```python
def bfs(graph: Graphe, start_sommet: Sommet):
    visited = set()
    queue = [start_sommet]
    
    while queue:
        sommet = queue.pop(0)
        if sommet not in visited:
            visited.add(sommet)
            adjacents = graph.get_sommet_adjacents(sommet)
            for adjacent in adjacents:
                if adjacent not in visited:
                    queue.append(adjacent)
    
    return visited
```

### 3.2 Algorithme de Bellman-Ford pour le Plus Court Chemin
L'algorithme de Bellman-Ford est utilisé pour calculer le plus court chemin, tenant compte des temps de parcours entre stations.

```python
def bellman_ford(graph, station):
    distances = {station.num_sommet: float('inf') for station in graph.get_stations()}
    distances[station.num_sommet] = 0
    predecesseur = {station.num_sommet: None for station in graph.get_stations()}

    for _ in range(len(graph.sommets) - 1):
        for arete in graph.aretes:
            u = arete.num_station1
            v = arete.num_station2
            poids = arete.time_sec

            if distances[u] != float('inf') and distances[u] + poids < distances[v]:
                distances[v] = distances[u] + poids
                predecesseur[v] = (u, arete.sommet1)
    
    return distances, predecesseur
```

### 3.3 Arbre Couvrant de Poids Minimum (ACPM) avec l'Algorithme de Prim
L'algorithme de Prim est implémenté pour trouver l'arbre couvrant de poids minimum.

```python
def prim(graph: Graphe):
    random_sommet = random.choice(graph.sommets)
    visited = set()
    arete_to_visite = set()
    acpm = []

    visited.add(random_sommet)
    current_aretes = graph.get_aretes_adjacentes(random_sommet)
    arete_to_visite.update(current_aretes)

    while len(visited) < len(graph.sommets):
        smallest_weighted_arete = smallest_weight(arete_to_visite)
        acpm.append(smallest_weighted_arete)
        visited.add(smallest_weighted_arete.sommet1)
        visited.add(smallest_weighted_arete.sommet2)
        # Mettre à jour les arêtes adjacentes...
    
    return acpm
```

---

## 4. Interface Utilisateur
### 4.1 Affichage Dynamique
- **Affichage de la Carte** : Un module de dessin peut être utilisé pour afficher la carte du métro. L'utilisateur peut cliquer sur les stations pour voir le plus court chemin ou l'ACPM.
- **Bonus** : Affichage interactif de l'itinéraire avec des informations détaillées sur les changements de lignes.

---

## 5. Conclusion
L'implémentation montre une application réussie de la théorie des graphes dans un contexte réel. Les algorithmes et structures de données sont bien utilisés pour répondre aux besoins du projet. Des améliorations possibles incluent l'optimisation de l'affichage graphique et la gestion des cas particuliers dans le réseau de métro.

---

Si vous avez besoin de plus d'explications ou d'une section spécifique développée, n'hésitez pas à demander !