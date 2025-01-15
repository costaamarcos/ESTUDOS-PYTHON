'''Enunciado: 
Escreva um programa que leia um arquivo CSV de entrada que tenha dois inteiros em
cada linha. O primeiro é um código de produto e o segundo é a quantidade vendida. O
programa deve totalizar quantos itens foram vendidos para cada produto.
Dica: use um dicionário tendo o código como chave e a quantidade como valor. Para
cada código lido do arquivo verifique se ele já existe no dicionário usando o operador
in. Se não existir, inclua; se existir some a quantidade existente com a nova quantidade
lida do arquivo.'''

from tabulate import tabulate


dicionario = {}

for i in open('C:/Users/estev/ESTUDOS-PYTHON/arquivos/exercicios_propostos/dados11.2.txt', 'r'):   
    lista = i.rstrip().split(";") 

    codigo = int(lista[0])
    quantidade = int(lista[1])    

    if codigo in dicionario:   # Verificando se o código já existe no dicionário
        dicionario[codigo] += quantidade  # Somando a quantidade existente com a nova quantidade
    else:
        dicionario[codigo] = quantidade  # Caso o código não exista, adiciona a quantidade

print("\nO Total de vendas por código de produto:")
for codigo, t in dicionario.items():
    print(f"Codigo {codigo}: {t} vendidos")


'''tabela = []
for codigo, total in dicionario.items():
    tabela.append([codigo, total])

print("\nO Total de vendas por código de produto:")
print(tabulate(tabela, headers=["Código", "Total Vendido"], tablefmt="pretty"))'''