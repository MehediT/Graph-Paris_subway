from entity.Graphe import Graphe
from service.read_file import read_file_metro, read_pospoint_file
from service.algorithme import bellman_ford, chemin_le_plus_court

from flask import Flask, jsonify, render_template, request  # Importez 'request' ici

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_lines', methods=['GET'])
def get_lines():
    return jsonify({'lines': graphe.get_lines()})

@app.route('/get_stations', methods=['GET'])
def get_stations():
    return jsonify(graphe.getStationVm())

# /prim?station1=selectedStation1&station2=selectedStation2
@app.route('/prim', methods=['GET'])
def prim():
    num1 = int(request.args.get('station1'))
    num2 = int(request.args.get('station2'))

    sommet1 = graphe.get_sommet_by_station(num1)
    sommet2 = graphe.get_sommet_by_station(num2)

    station1 = graphe.get_station_by_num(num1)
    station2 = graphe.get_station_by_num(num2)

    chemin_station, temps = chemin_le_plus_court(graphe, station1, station2)
    if chemin_station is None:
        return jsonify({'error': temps})

    st_station = graphe.get_info_for_station_num(num1), 
    end_station = graphe.get_info_for_station_num(num2), 
    
    chemin = [st_station]
    points = [
        {
            'x': sommet1.get_x(num1),
            'y': sommet1.get_y(num1),
        }
    ]
    for	num_station, sommet in chemin_station:
        station = graphe.get_info_for_station_num(num_station), 
        chemin.append(station)
        points.append({
            'x': sommet.get_x(num_station),
            'y': sommet.get_y(num_station),
        })

    result = {
        'st_station': sommet1.nom_sommet,
        'end_station': sommet2.nom_sommet,
        'chemin': chemin,
        'points': points,
        'time': temps,
    }

    return jsonify(result)

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
