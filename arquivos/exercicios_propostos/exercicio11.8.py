'''Enunciado:
Escreva um programa para ler o arquivo CSV gerado no exercício proposto 11.7 com os dados de
uma frota de veículos de uma empresa:

Placa (string - chave)
Marca
Modelo
Tipo (caminhão, furgão, automóvel, motocicleta, etc)
Kilometragem
Data da Compra (string no formato AAAAMMDD – ano,mês,dia)

O programa deve ler o arquivo, carregar um dicionário e exibir os dados na tela com um layout legível.'''

from tabulate import tabulate

# Abrir o arquivo para leitura
with open("frota_veiculos.csv", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()  # Lê todas as linhas do arquivo

# Processar os dados do arquivo
dados = [linha.strip().split(";") for linha in linhas]

# Separar o cabeçalho e os dados
cabecalho = dados[0]  # Primeira linha é o cabeçalho
conteudo = dados[1:]  # Restante são os dados

# Exibir os dados em formato tabular
print(tabulate(conteudo, headers=cabecalho, tablefmt="grid"))
