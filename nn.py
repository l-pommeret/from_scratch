from gradient_descent import gradient_descent
from plot import plot_3d_function

def f(x, y):
    return x**2 + y**2 + x*2 + 1

# Utilisation de la fonction plot_3d_function
# plot_3d_function(f, title="Graphique 3D de f(x, y) = x^2 + y^2 + x*2 + 1")

# # Exemple d'utilisation de gradient_descent
# initial_x, initial_y = 0, 0
# result = gradient_descent(f, initial_x, initial_y)
# print("Résultat de la descente de gradient :", result)

def nn(x,y,z):
    return x*2 + y*2 + z*2 

initial_x, initial_y, initial_z = 0, 0, 0
result = gradient_descent(nn, initial_x, initial_y, initial_z)
print("Résultat de la descente de gradient :", result)