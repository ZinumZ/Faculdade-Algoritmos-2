#Construa um método que receba uma lista encadeada de números inteiros e retorne uma lista sem repetições
#Ex: 12,5,-7, 8, 5, 9, 12, 1, 8
# => 12, 5, -7, 8, 9, 1

lista = [12,5,-7,8,6,9,12,1,8]
igual = []
for i in range(len(lista)):
    if lista[i] not in igual:
        igual.append(lista[i])
print(igual)