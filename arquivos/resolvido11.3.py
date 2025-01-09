'''Enunciado:
Escreva um programa que permaneça em laço lendo números reais até que seja digitado 0. Todos
os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha, com
três casas decimais. Usar o método .writelines()'''



lista = []
X = float(input("Digite um número real: ")) 
arquivo03 = open("C:/Users/estev/ESTUDOS-PYTHON/arquivos/saida_resolvido03.txt", "w")
while X != 0:    
    lista.append(f"{X:.3f}\n")
    X = float(input("Digite um número real: "))

arquivo03.writelines(lista)
arquivo03.close()
print(lista)
print("FIM")

#posso usar antes ou depois do while, porém antes o arquivo fica aberto durante todo o processamento
# Antes do while: Ideal para gravar dados em tempo real ou quando você trabalha com grandes volumes e quer evitar o uso de muita memória.
# Depois do while: Ideal para acumular e processar os dados primeiro e só depois gravá-los, garantindo consistência.

