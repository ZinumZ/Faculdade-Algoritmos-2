with open("numeros.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)

#Dessa maneira não precisa fechar o arquivo         