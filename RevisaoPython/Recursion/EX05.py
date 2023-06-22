#Faça um programa que receba uma lista e devolva uma lista com o primeiro elemento repetido 1 vez, segundo elemento repetido 2 vezes e assim sucessivamente
#L = [1,2,3,4]
#L = [1,2,2,3,3,3,4,4,4,4]

def listaExponenciada(lista, tamanholista):
    if tamanholista < 1:
        return []
    else:
        listatemporaria = [lista[tamanholista-1]] * tamanholista
        return listaExponenciada(lista,tamanholista-1) + listatemporaria
    
L = [1,2,3,4]
print(listaExponenciada(L,4))    