#Faça uma lista com as três notas da disciplina e calcule a média ponderada
lista = [1, 4, 9, 0]

for item in lista:
    print(item)
lista[3] = lista[0] * 0.3 + lista[1] * 0.3 + lista[2] * 0.4
print(f"Média: {lista[3]}")    



'''
lista1 = [1,2,3,4]
lista2=lista
lista2[2] = 0
lista2 = [1,2,0,4]
lista1 = [1,2,0,4]

lista3 = lista[:]
lista3 = [1,2,0,4]
lista3[2] = 3
lista3 = [1,2,3,4]

lista1 = [1,2,0,4]
lista2 = [1,2,0,4]
lista3 = [1,2,3,4]

len(lista)
4

lista1.append(10)
lista1
[1,2,0,4,10]

del lista1[4]
[1,2,0,4]


lista1[0:2]
[1,2]

lista1[:-1]
[1,2]

'''