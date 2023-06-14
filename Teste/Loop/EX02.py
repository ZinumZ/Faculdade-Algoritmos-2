#b) Crie um programa que calcula a soma de todos os números pares de 1 a 100.
print("Somando todos os números pares de 1 a 100:")

i = 1
soma = 0

for i in range(100):
    if i % 2 == 0:
        soma = soma + i
        print(f"{i}")

print(f"Soma dos números pares: {soma}")    
