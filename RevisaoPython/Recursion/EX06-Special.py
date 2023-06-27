#Faça uma função recursiva que receba uma lista de listas de inteiros e retorne True se verificar que todas as listas da lista tem mais da metade dos seus elementos como zero, senão retorne False
#[[0,0,3,0],[0,5,0],[0,0,0]] = True

def verifica_lista(lista):
    sublista = lista[0]
    cont = 0

    for elemento in sublista:
        if elemento == 0:
            cont += 1

    if cont > len(sublista) / 2:
        return True
    else:
        return verifica_lista(lista[1:])  # Chamada recursiva com a lista restante

lista = [[0, 0, 3, 0], [0, 5, 0], [0, 0, 0]]
print(verifica_lista(lista))


