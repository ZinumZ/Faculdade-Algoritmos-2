#Faça um programa que receba o lado de um quadrado e calcule a área do quadrado

def quadrado(a):
    return a * a

usuario = int(input("Digite o lado do quadrado: \n"))
resultado = quadrado(usuario)

print(f"A área do quadrado: {resultado}")