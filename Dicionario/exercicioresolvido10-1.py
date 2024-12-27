''' Escreva um porgrama que leia do teclado o código de um produto e seu preço unitário.
O codigo é um string e o preço é real. Acrescente o par código:preço em um dicionarrio.
O laço termina quando for fornecido um string vazio para o codigo. Ao final, exibir código e preço, um em cada linha'''

produtos = {}
print("Leitura dos dados")
codigo = input("\nDigite o codigo: ")
while codigo != "":
    preco = float(input("Digite o preço: "))
    produtos[codigo] = preco
    codigo = input("Digite o código: ")

print("FIM LEITURA DOS DADOS!")
print("PREÇO DOS PRODUTOS")
print("\n")

for codigo in produtos.keys():
    print(f" produto {codigo} custa {produtos[codigo]:7.2f}")
    
    
