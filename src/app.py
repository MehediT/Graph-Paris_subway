from entity.Graphe import Graphe
from service.read_file import read_file_metro, read_pospoint_file
from service.algorithme import chemin_le_plus_court, prim

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bonus')
def bonus():
   return render_template("bonus.html")

@app.route('/get_lines', methods=['GET'])
def get_lines():
    return jsonify({'lines': graphe.get_lines()})

@app.route('/get_graph', methods=['GET'])
def get_graph():
    sommets = []
    for sommet in graphe.sommets:
        sommets.append({
            'name': sommet.nom_sommet,
            'numeros': [station.num_sommet for station in sommet.stations],
            'posx': sommet.pos[0][0],
            'posy': sommet.pos[0][1],
            'description': graphe.get_info_for_sommet(sommet),
        })
    aretes = []
    for arete in graphe.aretes:
        aretes.append({
            'source': arete.num_station1,
            'target': arete.num_station2,
            'couleur': graphe.get_color_for_station(arete.num_station1),
            'distance': arete.time_sec,
        })

    return jsonify({'sommets': sommets, 'aretes': aretes})

@app.route('/get_stations', methods=['GET'])
def get_stations():
    return jsonify(graphe.getStationVm())

@app.route('/acpm', methods=['GET'])
def acpm():
    acpm = prim(graphe, random_sommet= graphe.get_sommet_by_name("Châtelet"))
    aretes = []
    for arete in acpm:
        aretes.append({
            'source': arete.num_station1,
            'target': arete.num_station2,
            'couleur': graphe.get_color_for_station(arete.num_station1),
            'distance': arete.time_sec,
        })
    return jsonify({"aretes" :aretes})

@app.route('/pcc', methods=['GET'])
def pcc():
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

@app.route('/pcc2', methods=['GET'])
def pcc2():
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
            'x': sommet.pos[0][0],
            'y': sommet.pos[0][1],
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
    click_x = float(request.args.get('x'))
    click_y = float(request.args.get('y'))
    
    sommet = graphe.get_sommet_for_pos(click_x, click_y)
    lines = graphe.get_info_for_sommet(sommet)

    if sommet is not None:
        return jsonify({'name': sommet.nom_sommet, 'lines': lines})
    else:
        return jsonify({'name': 'Aucune zone', 'lines': []})

if __name__ == '__main__':
    sommets, aretes = read_file_metro("src/res/metro.txt")
    positions = read_pospoint_file("src/res/pospoints.txt")
    graphe = Graphe()
    graphe.ajouter_sommets(sommets)
    graphe.ajouter_aretes(aretes)
    graphe.ajouter_positions(positions)

    app.run(debug=True, host='0.0.0.0', port=8080)
