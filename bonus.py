import tkinter as tk
from tkinter import messagebox

# Fonction pour afficher une popup avec un message
def show_popup(x, y):
    message = f"Vous avez cliqué à la position : ({x}, {y})\n\nLorem ipsum dolor sit amet, consectetur adipiscing elit."
    messagebox.showinfo("Information", message)

# Fonction appelée lorsque l'utilisateur clique sur l'image
def on_click(event):
    x, y = event.x, event.y
    # Exemple de position spécifique : vous pouvez ajouter plus de points avec des conditions
    if (50 <= x <= 60) and (50 <= y <= 60):
        show_popup(x, y)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Image Click Interface")

# Chargement de l'image (utilisez une image PNG ou un GIF)
image = tk.PhotoImage(file="votre_image.png")

# Création d'un canvas pour afficher l'image
canvas = tk.Canvas(root, width=image.width(), height=image.height())
canvas.pack()

# Affichage de l'image sur le canvas
canvas.create_image(0, 0, anchor=tk.NW, image=image)

# Liaison du clic de souris à la fonction on_click
canvas.bind("<Button-1>", on_click)

# Lancement de la boucle principale
root.mainloop()
