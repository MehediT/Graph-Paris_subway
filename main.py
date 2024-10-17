# Exemple d'utilisation
from module.draw_graph import draw_metro_graph
from module.read_file import read_file_metro

v_lines, e_lines = read_file_metro("res/metro.txt")
draw_metro_graph(v_lines, e_lines)