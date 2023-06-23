#Escreva um programa com uma função que receba um inteiro e diga se o número é perfeito ou não. Em outra função, escreva os números perfeitos até o número n.
def verifica_perfeito(num):
    soma = 0
    for i in range(1, num):
        if num % i == 0:
            soma = soma + i
    if soma == num:
        print(f"{num} é perfeito")    

def numeros_perfeitos(n):
    for i in range (1, n+1):
        if verifica_perfeito(i):
            print(i)

numeros_perfeitos(10000)            