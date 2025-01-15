'''Enunciado: 
Escreva um programa que leia um número inteiro N (10 < N < 10.000) e grave um arquivo com N linhas
com os dados listados na tabela abaixo. O arquivo deve ter o nome 'Estoque.csv e deve usar o
caractere ';' (ponto e vírgula) como delimitador. Não é necessário que o arquivo esteja ordenado.
'''
import random
import csv
from tabulate import tabulate

# Gerar um número aleatório para N
n = random.randint(11, 9999)  # Garantir que 10 < N < 10.000

# Criar um conjunto para evitar códigos repetidos
codigos_dicionarios = set()

# Criar a tabela em memória
tabela = [["Código do Produto", "Quantidade em Estoque", "Preço Unitário de Compra", "Alíquota do ICMS"]]

# Gerar as linhas para a tabela
for _ in range(n):
    # Gerar código único
    while True:
        codigo = random.randint(10000, 50000)
        if codigo not in codigos_dicionarios:
            codigos_dicionarios.add(codigo)
            break

    # Gerar os outros valores aleatórios
    quantidade_estoque = random.randint(1, 3800)
    preco_compra = round(random.uniform(1.80, 435.90), 2)  # Arredondar para duas casas decimais
    preco_formatado = f"R$ {preco_compra:,.2f}".replace('.', ',')  # Formatar como moeda brasileira
    aliquota = random.choice((7, 12))  # Escolher entre 7% e 12%
    aliquota_formatada = f"{aliquota}%"  # Adicionar o símbolo %

    # Adicionar a linha na tabela
    tabela.append([codigo, quantidade_estoque, preco_formatado, aliquota_formatada])

# Exibir a tabela formatada no terminal com tabulate
print(tabulate(tabela[:20], headers="firstrow", tablefmt="grid"))  # Exibe apenas as 20 primeiras linhas

# Salvar a tabela no arquivo CSV
with open('C:/Users/estev/ESTUDOS-PYTHON/arquivos/exercicios_propostos/Estoque.csv2', 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo, delimiter=';')
    escritor.writerows(tabela)

   



