#Escreva um programa que receba o nome de um arquivo via terminal e escreva no terminal o conteúdo do arquivo

arquivo = input("Escreva o nome do arquivo: ")
arquivo = open (arquivo, "r")

for linha in arquivo.readlines():
    print(linha)

arquivo.close()    