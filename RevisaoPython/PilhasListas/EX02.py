prato = 5
pilha = list(range(1,prato+1))
while True:
    print(f"\nExistem {len(pilha)} pratos na pilha")
    print(f"Pilha atual: {pilha}")
    print("Digite E para empilhar um novo prato")
    print("ou D para desempilhar. S para sair.")
    operacao = input("Operação (E,D OU S):")
    if operacao == "D":
        if len(pilha) > 0:
            lavado = pilha.pop(-1) #Tira o último
            print(f"Prato {lavado} lavado")
        else:
            print(f"Pilha vazia! Nada para lavar.") 
    elif operacao == "E":
        prato += 1
        pilha.append(prato)
    elif operacao == "S":
        break
    else:
        print("Operação Inválida! Digite apenas E,D ou S!")    