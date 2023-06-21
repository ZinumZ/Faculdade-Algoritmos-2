import random
def aleat():
    valor = random.randint(1,10)
    while True:
        x = int(input())
        if (x != valor):
            print("Tente novamente")
        else:
            print("Acertou")
            break