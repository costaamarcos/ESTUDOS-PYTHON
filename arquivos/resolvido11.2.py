'''Enunciado: 
Escreva um programa que permaneça em laço lendo números reais até que seja digitado 0. Todos
os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha, com
3 casas decimais. Usar o método .write()'''


arquivo02 = open("C:/Users/estev/ESTUDOS-PYTHON/arquivos/saida_resolvido02.txt", "w")

B = float(input("Digite um numero int: "))

while B != 0:
    arquivo02.write(f"{B:.3f}\n")
    B = float(input("Digite um numero int: "))

arquivo02.close()
print("FIM")