#Calculando a hipotenusa do triângulo retângulo
a = int(input("Digite o valor de a (Cateto Oposto): "))
b = int(input("Digite o valor de b (Cateto Adjacente): "))

hipotenusa = (a**2 + b**2) ** 0.5

print(f"Hipotenusa do triângulo: {hipotenusa}")
