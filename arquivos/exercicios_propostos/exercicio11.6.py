'''Escreva um programa que leia um arquivo de entrada contendo números inteiros, sendo um por
linha, e os coloque em uma lista. Em seguida pense em alguma forma de remover os valores
repetidos, deixando apenas uma cópia de cada valor.
A lista resultante após a eliminação dos repetidos, deve ser ordenada e salva no arquivo
UNICOS.TXT, um inteiro por linha.'''

import random

lista_numeros = [random.randint(1,2000) for _ in range(5000)]
with open("numeros_aleatorios.txt", "w") as arquivo_lista:
    for numero in lista_numeros:
        arquivo_lista.write(f"{numero}\n")

# Lê os números do arquivo e adiciona à lista
lista = []
with open("numeros_aleatorios.txt", "r") as arquivo_lista:
    for num in arquivo_lista:
       lista.append(int(num.strip()))   # Converte as linhas em inteiros

# Remove os duplicados e ordena a lista
# set(lista): Converte a lista para um conjunto, removendo automaticamente os valores duplicados.
# sorted(set(lista)) : Ordena o conjunto resultante, garantindo que os números fiquem em ordem crescente.
lista_numeros = sorted(set(lista))

print(lista)

# Salva os números únicos e ordenados no arquivo "UNICOS.TXT"
with open("UNICOS.TXT", "w") as arquivo_unicos:
    for numero in lista_numeros:
        arquivo_unicos.write(f"{numero}\n")



