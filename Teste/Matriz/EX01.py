#a) Escreva um programa que soma duas matrizes de ordem 3x3.
# Definindo as matrizes
matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matriz2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

# Criando a matriz resultante
resultado = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

# Somando as matrizes
for i in range(3):
    for j in range(3):
        resultado[i][j] = matriz1[i][j] + matriz2[i][j]

# Imprimindo a matriz resultante
for linha in resultado:
    print(linha)
