#Utilizando uma pilha, faça um método que receba um número inteiro positivo e converta esse número para o sistema binário
#EX: 5 => 101; 13 => 1101

pilha = []
pilha2 = []
numero = int(input("Digite um número:"))

while numero > 0:
    if numero % 2 == 1:
        numero = numero - 1
        pilha.append(1)
        numero = numero // 2
    else:
        pilha.append(0)
        numero = numero // 2
    if numero == 0:
        break

contador = len(pilha)
while contador > 0:
    pilha2.append(pilha.pop(-1))
    contador = contador - 1

print(pilha2)