import numpy as np

#Exercício 1: Calcule o produto escalar de dois vetores
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
resultado = np.dot(a, b)
print(f"O produto escalar é: {resultado}")

#Exercício 2: Crie dois vetores e calcule o produto escalar com np.dot()
c = np.array([2, 5, 9, 7, 8])
d = np.array([5, 8, 10, 4, 9])
resultado1 = np.dot(c, d)
print(f"O produto escalar é: {resultado1}")

#Exercício 3: Teste com vetores diferentes: v = [1, 0] e w = [0, 1]. Veja o resultado e interprete
v = np.array([1, 0])
w = np.array([0, 1])
resultado2 = np.dot(v, w)
print(f"O produto escalar é: {resultado2}")
