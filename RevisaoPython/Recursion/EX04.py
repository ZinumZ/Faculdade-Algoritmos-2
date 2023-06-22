#Resolução da 3 com recursividade
def diferenca_num(lista):
    primeiro = lista[0]
    soma_restante = diferenca_num(lista[1:])
    
    if primeiro > 0:
        return primeiro + soma_restante
    elif primeiro < 0:
        return primeiro - soma_restante
    else:
        return soma_restante

# Exemplo de uso
numeros = [2, -5, 10, -3, 0, 8, -1]
diferenca = diferenca_num(numeros)
print("A diferença entre a soma de positivos e a soma de negativos é:", diferenca)
