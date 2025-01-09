'''Enunciado: 
Escreva um programa que permaneça que leia um arquivo de entrada, sabendo que esse arquivo
tem um número inteiro em cada linha. Todos os números lidos devem ser mostrados na tela. Mostrar
também a soma dos valores, a quantidade, a média aritmética, o menor valor e o maior valor. Usar
aqui o mesmo arquivo de entrada do exercício anterior.
Usar um iterador for e o arquivo como iterável. '''

lista = []

 
for linha in open('C:/Users/estev/ESTUDOS-PYTHON/arquivos/entrada11.4.txt', 'r'):
    lista.append(int(linha))
    

'''linha = arquivo05.readline()
while linha != "":
    lista.append(int(linha))
    linha = arquivo05.readline()'''
 

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