'''Enunciado:
Escreva um programa que grave o arquivo NUMEROS.TXT com 2.000 números, um em cada linha,
gerados com a função randint() do módulo random no intervalo [1, 5.000].
Variação: Altere este programa substituindo o tamanho fixo de 2.000 por uma quantidade de entrada a ser lida
do teclado.
'''

import random

numero_aleatorio = [random.randint(1,5000) for _ in range (2000)]

arquivo = open('C:/Users/estev/ESTUDOS-PYTHON/arquivos/exercicios_propostos/NUMEROS.TXT', 'w')
for numero in numero_aleatorio:
    arquivo.write(f"{numero}\n")


arquivo.close()

print(numero_aleatorio)

