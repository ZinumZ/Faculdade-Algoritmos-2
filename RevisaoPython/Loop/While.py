fim = int(input("Defina o fim do while:\n"))
x = 1
while x < fim:
    print(x)
    x = x + 1

'''
fim = int(input("Defina o fim do while:\n"))    -> A variável fim fica inútil no final das contas
x = 1
while True:
    print(x)
    x = x + 1
    if x==1000:
        break
'''