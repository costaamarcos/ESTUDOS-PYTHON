'''Exercício Resolvido 11.1
Enunciado: Escreva um programa que permaneça em laço lendo números inteiros até que seja digitado 0. Todos
os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha'''

arquivo = open("C:/Users/estev/ESTUDOS-PYTHON/arquivos/Exercicios Resolvidos/saida_resolvido01.txt", "w" ) #abre o arquivo

A = int(input("Digite um número inteiro: "))

while A != 0:
    arquivo.write(f"{A}\n")
    A = int(input("Digite um número inteiro: "))

arquivo.close() #fecha o arquivo

print("Fim!")