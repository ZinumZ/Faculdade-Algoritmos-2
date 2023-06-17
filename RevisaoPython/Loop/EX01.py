#Faça um programa que escreva a tabuada de 1 a 10, usando estrutura de repetição


for i in range(1, 11):
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")

        if j == 10:
            print("\n")

