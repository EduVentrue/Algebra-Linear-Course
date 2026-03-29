#Aula de Exemplo 1:
import numpy as np
#criando vetores
v = np.array([2, 3])
w = np.array([1, 4])
print("v:", v)
print("w:", w)
#dimensão
print("dimensão de v:", v.shape)

#Exercício 1: Crie um vetor com idade, altura e peso
p = np.array([30, 1.85, 71])

#Exercício 2: Crie um vetor com 5 números aleatórios
i = np.random.randint(0, 100, 5)
print(f"Elementos de i: {i}")
#Exercício 3: Mostre a dimensão de um vetor com 5 elementos
print(f"Dimensão de i: {i.shape}")
