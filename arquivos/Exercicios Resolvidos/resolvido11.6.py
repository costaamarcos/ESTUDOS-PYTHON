"""Enunciado:
Escreva um programa que leia um arquivo de entrada carregando seus dados em um dicionário e ao
final exibindo-os na tela. A figura 11.1 mostra o do lado esquerdo a natureza dos dados que serão
lidos e do lado direito mostra o formato do arquivo.
Esse formato é conhecido como CSV. Arquivos CSV são muito usados em diversas áreas da
computação, em especial em Análise de Dados. O que caracteriza um arquivo CSV é que cada linha
tem um conjunto de dados de alguma forma relacionados e separados por um caractere
delimitador. No arquivo deste exercício o delimitador é um ponto-e-vírgula ";"
Neste caso, cada linha tem: código de produto (int), a quantidade em estoque (int), preço (float).
Use o código como chave para o dicionário e valor deve ser em formato de tupla.
"""


estoque = {}

for linha in open('C:/Users/estev/ESTUDOS-PYTHON/arquivos/Exercicios Resolvidos/entrada11.6.txt', 'r'):
   lista = linha.rstrip().split(";")   
   print(lista)
   cod = int(lista[0])
   qtde = int(lista[1])
   pcunit = float(lista[2])
   estoque[cod] = (qtde, pcunit)

print("\nValores carregador no dict\n")
print(estoque)

print("\nExibição dos dados em forma de tabela")
TotalGeral = 0
for cod, dados in estoque.items():
   tot = dados[0] * dados[1]
   TotalGeral += tot
   print(f" {cod}: {dados[0]:5d} x {dados[1]:6.2f} = {tot:8.2f}")
print(' ' * 24, f"{TotalGeral:8.2f}")
         
print("\nFIM")