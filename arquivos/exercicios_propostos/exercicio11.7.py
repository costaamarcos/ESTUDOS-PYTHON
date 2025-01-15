'''Enunciado:
 Escreva um programa para registrar os seguintes dados de uma frota de veículos de uma empresa:
Placa (string – chave – obrigatório todas as letras maiúsculas)
Marca
Modelo
Tipo (caminhão, furgão, automóvel, motocicleta, etc)
Kilometragem
Data da Compra (string no formato AAAAMMDD – ano,mês,dia)
O programa deve ficar em laço enquanto a Placa for digitada. O laço termina quando for digitado FIM
para a placa. Se for digitada uma placa com letras minúsculas o programa deve convertê-las para
maiúsculas com o método .upper().
Para cada veículo leia todos os dados e carregue em um dicionário. Se uma placa já existente for
digitada o programa deve avisar que já existe, mostrar seus dados e se usuário quiser fazer alteração
em algum dado basta digitar o novo valor. Para os campos em que nada for digitado deve ser mantido
o valor já cadastrado.
Ao final do laço grave todos os dados em um arquivo CSV usando o caractere ";" como delimitador.
Detalhe: Este exercício é uma extensão do exercício proposto 10.6, acrescentando a parte referente à
gravação do arquivo'''

import csv

dicionario = {}

while True:
    placa = input("Digite a placa do veículo: ").upper()
    if placa.upper() == "FIM":
        break

    if placa in dicionario:
        print("Placa ja cadastrada, tente novamente!")
        print(dicionario[placa])

        atualizar = input("Deseja atualizar os Dados Existentes? (S/N)").strip().upper()
        if atualizar == "S":
            marca = input(f"Digite a Marca [{dicionario[placa]['Marca']}]: ") or dicionario[placa]['Marca']
            modelo = input(f"Digite o Modelo [{dicionario[placa]['Modelo']}]: ") or dicionario[placa]['Modelo']
            km = input(f"Digite a Kilometragem [{dicionario[placa]['Kilometragem']}]: ") or dicionario[placa][
                'Kilometragem']
            data_compra = input(f"Digite a data de compra [{dicionario[placa]['Data de compra']}]: ") or \
                          dicionario[placa]['Data de compra']

            dicionario[placa] = {"Marca": marca, "Modelo": modelo, "Kilometragem": km, "Data de compra": data_compra}
        else:
            continue
    else:
        marca = input("Digite a Marca: ")
        modelo = input("Digite o Modelo:((caminhão, furgão, automóvel, motocicleta, etc): ")
        km = input("Digite a Kilometragem: ")
        data_compra = input("Digite a data de compra: ")

        dicionario[placa] = {"Marca": marca, "Modelo": modelo, "Kilometragem": km, "Data de compra": data_compra}

with open("frota_veiculos.csv", "w", newline="", encoding="utf-8") as csvfile:
    escritor_csv = csv.writer(csvfile, delimiter=";")
    escritor_csv.writerow(["Placa", "Marca", "Modelo", "Kilometragem", "Data de compra"])
    for placa, dados in dicionario.items():
        escritor_csv.writerow([placa, dados["Marca"], dados["Modelo"], dados["Kilometragem"], dados["Data de compra"]])

print("Dados da frota salvos em 'frota_veiculos.csv'.")
