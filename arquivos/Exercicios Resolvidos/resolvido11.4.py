'''Escreva um programa que permaneça que leia um arquivo de entrada, sabendo que esse arquivo
tem um número inteiro em cada linha. Todos os números lidos devem ser mostrados na tela. Mostrar
também a soma dos valores, a quantidade, a média aritmética, o menor valor e o maior valor.
Usar um laço while e na leitura usar o método .readline()'''

lista = []
arquivo04 = open('C:/Users/estev/ESTUDOS-PYTHON/arquivos/Exercicios Resolvidos/entrada11.4.txt', 'r')

linha = arquivo04.readline()
while linha != "":
    lista.append(int(linha))
    linha = arquivo04.readline()
 
arquivo04.close()
print("Lista lida do arquivo")
print(lista)

Soma = sum(lista)
print(f"A soma dos valores da lista é: {sum(lista)}")
Quantidade = len(lista)
print(f"A quantidade de itens da lista é: {Quantidade}")
print(f"A média dos valores da lista é: {Soma/Quantidade}")
print(f"O menor valor da lista é : {min(lista)}")
print(f"O maior valor da lista é : {max(lista)}")
print("FIM")