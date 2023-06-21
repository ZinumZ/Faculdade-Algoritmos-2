#Crie uma função que receba um inteiro positivo e verifique se ele é um número primo

def primo(valor):
    if valor <= 1:
        return False

    for i in range(2, valor):
        if valor % i == 0:
            return False
    return True

num = int(input("Digite um número inteiro positivo: "))

if primo(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")
