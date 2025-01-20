# Criação de uma função
# def <nome da funcao>
#   <codigo>

# EXEMPLO
def ExibeHifens():
    print('-----')
Lista = [10, 20, 30, 40]
for item in Lista:
    print(item)
    ExibeHifens()
print('Fim do Programa')

def LerInteiro():
    n = int(input('Digite um inteiro: '))
    return n
valor = LerInteiro()
print(f'Valor lido com uso da função = {valor}')

