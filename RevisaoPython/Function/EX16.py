#Faça uma função chamada SomaImposto. A função recebe dois parâmetros: taxaimposto, quantidade de imposto sobre as vendas expressa em porcentagem e o custo que é o valor de custo de um item. A função deve retornar o preço final do produto em reais. Imposto minimo: 12%
def SomaImposto(taxaimposto, custo):
    if taxaimposto >= 12:
        imposto = custo * (taxaimposto / 100)
        final = custo + imposto
    else:
        return "Baixa taxa de imposto"
    return final

custo = float(input("Digite o valor do produto:"))
taxaimposto = float(input("Digite a taxa do produto em porcentagem:"))

print(f"Valor do produto com o imposto: {SomaImposto(taxaimposto,custo)}")