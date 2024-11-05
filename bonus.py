import tkinter as tk
from tkinter import messagebox
from entity.Graphe import Graphe
from service.read_file import read_file_metro, read_pospoint_file

sommets, aretes = read_file_metro("res/metro.txt")
positions = read_pospoint_file("res/pospoints.txt")

graphe = Graphe()
graphe.ajouter_sommets(sommets)
graphe.ajouter_aretes(aretes)
graphe.ajouter_positions(positions)
import tkinter as tk
def show_lines():
    lines_window = tk.Toplevel()
    lines_window.title("Lignes")
    
    text = """Ligne 1: Lorem ipsum dolor sit amet,
Ligne 2: consectetur adipiscing elit,
Ligne 3: sed do eiusmod tempor incididunt."""
    
    # Ajouter du texte
    label = tk.Label(lines_window, text=text, justify=tk.LEFT)
    label.pack(padx=10, pady=10)

# Fonction pour afficher une popup avec du texte et un bouton
def show_popup(x, y):
    popup = tk.Toplevel()
    popup.title("Information")
    
    # Créer un Frame pour organiser le texte et les boutons côte à côte
    frame = tk.Frame(popup)
    frame.pack(padx=10, pady=10)

    # Ajouter un texte à gauche
    label = tk.Label(frame, text=f"Vous avez cliqué à la position : ({x}, {y})\n\nVoulez-vous voir les lignes ?")
    label.pack(side=tk.LEFT, padx=10)

    # Ajouter un bouton à droite
    button = tk.Button(frame, text="Voir les lignes", command=show_lines)
    button.pack(side=tk.LEFT, padx=10)

# Fonction appelée lorsque l'utilisateur clique sur l'image
def on_click(event):
    x, y = event.x, event.y
    # Exemple de position spécifique : vous pouvez ajouter plus de points avec des conditions
    show_popup(x, y)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Image Click Interface")

# Chargement de l'image (utilisez une image PNG ou un GIF)
image = tk.PhotoImage(file="res/metrof_r.png")

# Création d'un canvas pour afficher l'image
canvas = tk.Canvas(root, width=image.width(), height=image.height())
canvas.pack()

# Affichage de l'image sur le canvas
canvas.create_image(0, 0, anchor=tk.NW, image=image)

# Liaison du clic de souris à la fonction on_click
canvas.bind("<Button-1>", on_click)

# Lancement de la boucle principale
root.mainloop()
