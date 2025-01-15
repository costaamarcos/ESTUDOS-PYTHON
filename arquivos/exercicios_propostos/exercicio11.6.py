
entrada = int(input("Digite um valor inteiro: "))

lista = []

arquivo = open('C:/Users/estev/ESTUDOS-PYTHON/arquivos/exercicios_propostos/UNICOS.TXT', 'w')
for _ in entrada:    
    arquivo.write(f"{entrada}")

lista.append(arquivo)
set(lista)
lista.sort()

arquivo.close()
