'''Enunciado:
Escreva um programa que leia dois números reais e calcule as 4 operações aritméticas entre eles
usando uma função. Exiba o resultado com duas casas decimais.'''

def numReais (a,b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b
    return  soma, subtracao, multiplicacao, divisao

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

resultado = numReais(valor1, valor2)

print("Resultados!")
print(f"A soma é: {resultado[0]}")
print(f"A subtração é : {resultado[1]}")
print(f"A multiplicação é: {resultado[2]}")
print(f"A divisão é: {resultado[3]}")
