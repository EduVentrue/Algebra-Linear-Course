import numpy as np

pessoa1 = np.array([30, 1.85, 72])
pessoa2 = np.array([17, 1.62, 62])
resultado = np.dot(pessoa1, pessoa2)
print(f"O produto escalar é: {resultado}")
#O produto escalar pode indicar semelhança, mas não é confiável sozinho



#Desafio extra
pessoaA = np.array([17, 1.62, 62])
pessoaB = np.array([19, 1.68, 70])
pessoaC = np.array([21, 1.40, 60])
resultado1 = np.dot(pessoaA, pessoaB)
resultado2 = np.dot(pessoaA, pessoaC)
resultado3 = np.dot(pessoaB, pessoaC)

resultados = {
    "A - B": resultado1,
    "A - C": resultado2,
    "B - C": resultado3
}

mais_semelhante = max(resultados, key=resultados.get)
print(f"O mais semelhante é: {mais_semelhante}")
print(f"O resultado entre a pessoa A e a pessoa B é: {resultado1}")
print(f"O resultado entre a pessoa A e a pessoa B é: {resultado2}")
print(f"O resultado entre a pessoa B e a pessoa C é: {resultado3}")
