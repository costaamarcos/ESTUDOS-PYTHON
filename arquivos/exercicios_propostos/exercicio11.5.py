# import random

# quantidade = int(input("Digite a quantidade e números a segrem gerados: "))
# numeros_aleatorios = random.randint(1,5000)

lista = []

arquivo = open('C:/Users/estev/ESTUDOS-PYTHON/arquivos/exercicios_propostos/NUMEROS.TXT', 'r')
for numero in arquivo:
    lista.append(int(numero.strip()))

#ordena a lista
lista.sort()

arquivo_saida = open('C:/Users/estev/ESTUDOS-PYTHON/arquivos/exercicios_propostos/ORDENADOS.TXT', 'w')
for numero2 in lista:
    arquivo_saida.write(f"{numero2}\n")
arquivo_saida.close()
arquivo.close()