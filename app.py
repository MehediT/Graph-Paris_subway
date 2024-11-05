from flask import Flask, jsonify, render_template, request

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

line_info = LineInfo()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_lines', methods=['GET'])
def get_lines():
    return jsonify(line_info.get_lines())

if __name__ == '__main__':
    app.run(debug=True)
