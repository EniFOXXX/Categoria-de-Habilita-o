# Melhor Categoria para Habilitação
# Autor: Enivaldo de Oliveira Souza


print(' Quantidade de Rodas:')
rodas =  int(input())

print(' Peso do Veículo:')
peso =  float(input())

print('Quantidade de Pessoas:')
quant_pessoas = int(input())


if ((rodas >= 4) and (peso > 6000)):
    print(" Categoria E")

elif ((rodas >=4) and (quant_pessoas > 8)) :
        print("Categoria D")

elif((rodas >= 4) and ((peso >= 3500) and (peso <= 6000))):
        print("Categoria C")

elif ((rodas == 4) and ((quant_pessoas <= 8) and ( peso <= 3500))):
        print("Categoria B ")
else:
    print("Categoria A ")




