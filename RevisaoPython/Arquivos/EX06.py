import sys
print(f"Número de parâmetros: {len(sys.argv)}")
nome = sys.argv[0]

arquivo = open(nome, "r")
for linha in arquivo.readlines():
    print(linha)

arquivo.close()