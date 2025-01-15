'''
Reescreva o programa exercício resolvido 11.6 usando um dicionário aninhado no lugar da tupla
como valor para o dicionário Estoque.
'''



estoque = {}

for linha in open('C:/Users/estev/ESTUDOS-PYTHON/arquivos/Exercicios Resolvidos/entrada11.6.txt', 'r'):
   lista = linha.rstrip().split(";")   
   print(lista)
   cod = int(lista[0])
   qtde = int(lista[1])
   pcunit = float(lista[2])
   estoque[cod] = {"quantidade": qtde, "preço unitario":pcunit}

print("\nValores carregador no dict\n")
print(estoque)

print("\nExibição dos dados em forma de tabela")
TotalGeral = 0
for cod, dados in estoque.items():
   tot = dados["quantidade"] * dados["preço unitario"]
   TotalGeral += tot
   print(f" {cod}: {dados["quantidade"]:5d} x {dados["preço unitario"]:6.2f} = {tot:8.2f}")
print(' ' * 24, f"{TotalGeral:8.2f}")
         
print("\nFIM")

for cod, dados in estoque.items():
    if type(dados) == tuple:
        print(f"O valor para o código {cod} é uma tupla.")
    else:
        print(f"O valor para o código {cod} NÃO é uma tupla.")