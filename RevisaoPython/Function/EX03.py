#Faça um programa que encontre o maior de 2 números
#Maior numero (5,6) = 6
#Maior numero (3,7) = 7
def maior_numero(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Números iguais"

print("Verificando o maior valor:\n ")
a = float(input("Digite o 1º Número: "))
b = float(input("Digite o 2º Número: "))

resultado = maior_numero(a, b)

print(resultado)
