from entity.Graphe import Graphe
from service.read_file import read_file_metro, read_pospoint_file
from flask import Flask, jsonify, render_template, request  # Importez 'request' ici

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_lines', methods=['GET'])
def get_lines():
    return jsonify({'lines': graphe.get_lines()})

@app.route('/get_zone', methods=['GET'])
def get_zone():
    # Récupérez les coordonnées de clic à partir de la requête
    click_x = float(request.args.get('x'))
    click_y = float(request.args.get('y'))
    
    sommet = graphe.get_sommet_for_pos(click_x, click_y)
    lines = graphe.get_info_for_sommet(sommet)

    if sommet is not None:
        return jsonify({'name': sommet.nom_sommet, 'lines': lines})
    else:
        return jsonify({'name': 'Aucune zone', 'lines': []})

if __name__ == '__main__':
    sommets, aretes = read_file_metro("res/metro.txt")
    positions = read_pospoint_file("res/pospoints.txt")
    graphe = Graphe()
    graphe.ajouter_sommets(sommets)
    graphe.ajouter_aretes(aretes)
    graphe.ajouter_positions(positions)
    app.run(debug=True, host='0.0.0.0', port=8080)
