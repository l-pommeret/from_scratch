from auto_derivation import AutoDiff, gradient

def gradient_descent(f, *args, learning_rate=0.01, iterations=1000):
    current_args = list(args)
    for _ in range(iterations):
        grad = gradient(f, *current_args)
        current_args = [arg - learning_rate * darg for arg, darg in zip(current_args, grad)]
    return current_args

# def f(x, y):
#     return x**3 + y**2

# # Exemple d'utilisation de gradient_descent
# initial_x, initial_y = 0, 0
# result = gradient_descent(f, initial_x, initial_y)
# print("Résultat de la descente de gradient :")
# print(f"Point initial: ({initial_x}, {initial_y})")
# print(f"Point final après 1000 itérations: ({result[0]:.8f}, {result[1]:.8f})")
# print(f"Valeur finale de la fonction: {f(*result):.8f}")
