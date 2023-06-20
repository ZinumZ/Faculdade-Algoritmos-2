def soma(a,b):
    return a+b
def subtracao(a,b):
    return a-b
def imprime(a,b,operacao):
    print(operacao(a,b))

imprime(5,4,soma)
imprime(5,4,subtracao)