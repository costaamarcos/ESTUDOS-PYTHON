from tabulate import tabulate

estoque = {}

for linha in open('C:/Users/estev/ESTUDOS-PYTHON/arquivos/entrada11.6.txt', 'r'):
   lista = linha.rstrip().split(";")   

   cod = int(lista[0])
   qtde = int(lista[1])
   pcunit = float(lista[2])
   estoque[cod] = (qtde, pcunit)

print("\nValores carregador no dict\n")


# Preparando os dados para exibição
tabela = []
for cod, (qtde, pcunit) in estoque.items():
    tabela.append([cod, qtde, pcunit])

# Exibindo os dados em formato de tabela
headers = ["Código", "Quantidade", "Preço Unitário"]
print(tabulate(tabela, headers=headers, tablefmt="grid"))