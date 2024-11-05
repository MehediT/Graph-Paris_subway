from entity.Graphe import Graphe
from service.read_file import read_file_metro, read_pospoint_file
from flask import Flask, jsonify, render_template, request  # Importez 'request' ici

app = Flask(__name__)

# Exemple de données ou de logique métier
class LineInfo:
    def __init__(self):
        self.lines = [
            "Ligne 1: Lorem ipsum dolor sit amet.",
            "Ligne 2: Consectetur adipiscing elit.",
            "Ligne 3: Sed do eiusmod tempor incididunt."
        ]

    def get_lines(self):
        return self.lines

class Zone:
    def __init__(self, name, x, y, width, height):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def is_within(self, click_x, click_y):
        return self.x <= click_x <= self.x + self.width and self.y <= click_y <= self.y + self.height

# Créez des zones cliquables avec une marge de 10px
zones = [
    Zone("Zone 1", 0, 0, 10, 10),  # (x, y, width, height)
    Zone("Zone 2", 200, 50, 100, 100),
    Zone("Zone 3", 50, 200, 100, 100),
]

line_info = LineInfo()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_lines', methods=['GET'])
def get_lines():
    return jsonify(line_info.get_lines())

@app.route('/get_zone', methods=['GET'])
def get_zone():
    # Récupérez les coordonnées de clic à partir de la requête
    click_x = float(request.args.get('x'))
    click_y = float(request.args.get('y'))
    
    sommet = graphe.get_sommet_for_pos(click_x, click_y)
    if sommet is not None:
        return jsonify({'name': sommet.nom_sommet})
    return jsonify({'name': 'Aucune zone'})


if __name__ == '__main__':
    sommets, aretes = read_file_metro("res/metro.txt")
    positions = read_pospoint_file("res/pospoints.txt")
    graphe = Graphe()
    graphe.ajouter_sommets(sommets)
    graphe.ajouter_aretes(aretes)
    graphe.ajouter_positions(positions)
    app.run(debug=True)
