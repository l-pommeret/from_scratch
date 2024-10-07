import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_function(f, x_range=(-10, 10), y_range=(-10, 10), num_points=100, title=None):
    """
    Trace un graphique 3D pour une fonction à deux variables.
    
    :param f: Fonction à deux variables à tracer
    :param x_range: Tuple (min, max) pour la plage de x
    :param y_range: Tuple (min, max) pour la plage de y
    :param num_points: Nombre de points dans chaque dimension
    :param title: Titre du graphique (optionnel)
    """
    # Création d'une grille de points
    x = np.linspace(x_range[0], x_range[1], num_points)
    y = np.linspace(y_range[0], y_range[1], num_points)
    X, Y = np.meshgrid(x, y)
    
    # Calcul des valeurs de la fonction pour chaque point de la grille
    Z = f(X, Y)
    
    # Création de la figure et de l'axe 3D
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Création du graphique de surface
    surface = ax.plot_surface(X, Y, Z, cmap='viridis')
    
    # Ajout d'une barre de couleur
    fig.colorbar(surface, shrink=0.5, aspect=5)
    
    # Étiquettes des axes
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    
    # Titre du graphique
    if title:
        ax.set_title(title)
    else:
        ax.set_title('Graphique 3D de f(x, y)')
    
    # Affichage du graphique
    plt.show()

# # Exemple d'utilisation
# def w(x, y):
#     return x**2 + y**2

# plot_3d_function(w, title="Graphique 3D de f(x, y) = x^2 + y^2")