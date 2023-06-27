arquivo = open ("numeros.txt", "a")
for linha in range (1,101):
    arquivo.write(f"{linha}\n")

arquivo.close()


"""
ARQUIVOS
r = leitura
w = escrita, apaga o conteúdo se existir
a = escrita, conserva o conteúdo se existir
b = modo binário
+ = atualização (leitura e escrita)

"""