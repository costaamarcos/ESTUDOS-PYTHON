import random

quantidade = int(input("Digite a quantidade desejada de números a serem gerados: "))
numeros_aleatorios = [random.randint(1,5000) for _ in range(quantidade)]

arquivo = open('C:/Users/estev/ESTUDOS-PYTHON/arquivos/exercicios_propostos/NUMEROS.TXT02', 'w')
for numero in numeros_aleatorios:
    arquivo.write(f"{numero}\n")

arquivo.close()