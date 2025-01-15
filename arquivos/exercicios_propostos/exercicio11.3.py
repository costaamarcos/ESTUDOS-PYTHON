'''Enunciado: 
Escreva um programa que leia um número inteiro N (10 < N < 10.000) e grave um arquivo com N linhas
com os dados listados na tabela abaixo. O arquivo deve ter o nome 'Estoque.csv e deve usar o
caractere ';' (ponto e vírgula) como delimitador. Não é necessário que o arquivo esteja ordenado.
'''
import random
import csv

n =  random.randint(10,9999)
codigos_dicionarios = set()


with open('C:/Users/estev/ESTUDOS-PYTHON/arquivos/exercicios_propostos/Estoque.csv', 'w', newline='') as arquivo:
          escritor = csv.writer(arquivo, delimiter =';')

          # Escrever o cabeçalho
          escritor.writerow(["Código do Produto", "Quantidade em Estoque", "Preço Unitário de Compra", "Alíquota do ICMS"])
    

        

          for _ in range(n):
              # Gerar código único
              while True:
                  codigo = random.randint(10000,50000)
                  if codigo not in codigos_dicionarios:
                        codigos_dicionarios.add(codigo)
                        break        

              # Gerar os outros valores aleatórios
              quantidade_estoque = random.randint(1,3800)
              preco_compra = random.uniform(1.80,435.90)
              aliquota = random.choice((7,12,18))

              # Escrever a linha no arquivo
              escritor.writerow([codigo,quantidade_estoque,preco_compra,aliquota])

   



