#c) Faça um programa que verifica se uma pessoa pode dirigir com base na idade.

idade = int(input("Digite a idade da pessoa: "))

if idade >= 18:
    print(f"A pessoa com {idade} anos poderá dirigir")
else:
    print(f"A pessoa com {idade} anos não poderá dirigir")    