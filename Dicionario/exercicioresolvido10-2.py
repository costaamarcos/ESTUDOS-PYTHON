'''
Escreva um programa que leia do teclado o codigo de um produto e seu preço unitario.
O codigo é um string e o preco é real. Acrescente o par código:preço em um dicionario.
O programa deve verificar se o codigo ja esta no dicionario e neste caso deve emitir uma mensagem de erro.
O laço termina quando for fornecido um string vazio para o código.
Ao final, exibir código e preço, um produto em cada linha'''

produtos = {}

codigo = input("Digite o código: ")

while codigo != "":
    preco = input(("Digite o preço: "))    
    if codigo in produtos:
        print("O código ja existe!")
        codigo = input("Digite o código novamente: ")
    else:
        produtos[codigo] = preco
        codigo = input("Digite o código: ")
        

for codigo,preco in produtos.keys():
    print(f"O codigo é {codigo} e o preco é R${preco}")
        
    