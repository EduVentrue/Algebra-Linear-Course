import numpy as np
#Exemplo resolvido
v = np.array([2, 4])
w = np.array([7, 18])

print(f"Soma: {v + w}")
print(f"Subtração: {v - w}")
print(f"Escalar: {2 * v}")

#Exercício 1: Crie dois vetores e faça a soma e a subtração
a = np.array([8, 10])
b = np.array([6, 8])
print(f"Soma: {a + b}")
print(f"Subtração: {a - b}")

#Exercício 2: Crie um vetor e multiplique por 3
c = np.array([1, 2, 3])
print(f"Multiplicando por 3: {3 * c}")

#Exercício 3: Tente somar vetores de tamanhos diferentes e verifique o erro
d = np.array([1, 2])
e = np.array([1, 2, 3])
try:
    print(f"Soma: {d + e}")
except ValueError as erro:
    print("Erro de dimensão:", erro)
    