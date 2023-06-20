def soma(a,b):
    return a+b
def subtracao(a,b):
    return a-b
def multiplicacao(a,b):
    return a*b
def divisao(a,b):
    return a/b


operacao = input("Digite a operação [+][-][*][/]:\n")
calc = int(input("Digite o valor de a: "))
calc2 = int(input("Digite o valor de b: "))

if operacao == '+':
    resultado = soma(calc,calc2)
    print(resultado)

if operacao == '-':
    resultado = subtracao(calc,calc2)
    print(resultado)

if operacao == '*':
    resultado = multiplicacao(calc,calc2)
    print(resultado)

if operacao == '/':
    if calc2 != 0:
        resultado = divisao(calc,calc2)
        print(resultado)
    else:
        print("Divisão por 0!")        



'''
def epar(x):
    return x % 2 == 0
'''