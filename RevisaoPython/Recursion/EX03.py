#Faça um programa que receba uma lista de números inteiros. Calcule a diferença entre a soma de positivos com a soma de números negativos

def dif_lista(lista):
    soma_pos = 0
    soma_neg = 0

    for item in lista:
        if item >= 0:
            soma_pos = soma_pos + item
        else:
            soma_neg = soma_neg + item
    return soma_pos - soma_neg

lista = [1,2,3,-5-6-7]
print(f"Diferença entre a soma de positivos e negativos: {dif_lista(lista)}")       

