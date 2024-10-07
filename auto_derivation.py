import math

class AutoDiff:
    def __init__(self, value, derivatives):
        self.value = value
        self.derivatives = derivatives

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return AutoDiff(self.value + other, self.derivatives)
        return AutoDiff(self.value + other.value, [d1 + d2 for d1, d2 in zip(self.derivatives, other.derivatives)])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return AutoDiff(self.value * other, [d * other for d in self.derivatives])
        new_derivatives = [self.value * d2 + d1 * other.value for d1, d2 in zip(self.derivatives, other.derivatives)]
        return AutoDiff(self.value * other.value, new_derivatives)

    def __pow__(self, power):
        new_value = self.value ** power
        new_derivatives = [power * self.value ** (power - 1) * d for d in self.derivatives]
        return AutoDiff(new_value, new_derivatives)

    def sin(self):
        return AutoDiff(math.sin(self.value), [math.cos(self.value) * d for d in self.derivatives])

    def cos(self):
        return AutoDiff(math.cos(self.value), [-math.sin(self.value) * d for d in self.derivatives])

def gradient(func, *args):
    n = len(args)
    results = []
    for i in range(n):
        derivatives = [1 if j == i else 0 for j in range(n)]
        auto_diff_args = [AutoDiff(arg, derivatives) if j == i else AutoDiff(arg, [0] * n) for j, arg in enumerate(args)]
        result = func(*auto_diff_args)
        results.append(result.derivatives[i])
    return results

# # Exemple d'utilisation
# def f(x, y):
#     return x * y.sin() + x ** 2 + y ** 2

# x, y = 2.0, 1.0
# grad = gradient(f, x, y)
# print(f"Le gradient de f(x, y) = x * sin(y) + x^2 + y^2 en (x, y) = ({x}, {y}) est : {grad}")

# # Fonction à trois variables
# def g(x, y, z):
#     return x * y + y * z.cos() + z ** 2

# x, y, z = 1.0, 2.0, 0.5
# grad_g = gradient(g, x, y, z)
# print(f"Le gradient de g(x, y, z) = x * y + y * cos(z) + z^2 en (x, y, z) = ({x}, {y}, {z}) est : {grad_g}")