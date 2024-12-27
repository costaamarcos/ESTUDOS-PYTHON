print("MÉTODOS DICIONÁRIO")

D = {120: "Queijo", 134: "Arroz", 117: "Farinha"}
print(D)

print("\n\n** ADIÇÃO DE ELEMENTOS **")
D[125] = "Açucar"
print(D)
D[133] = "Macarrão"
print(D)
print(len(D))

print("\n** LIMPAR DICIONÁRIO **")
D.clear()
print(D)

print("\n** COPIAR UM DICIONÁRIO **")
D = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}
A = D.copy()
print(A)
print(id(A))
print(id(D))

print("\n** NOVO NOME QUE APONTA PRO LUGAR ORIGINAL **")
A = D
print(id(A))
print(id(D))

print("\n** GET **")
print(A.get(134))
X = A.get(134)
print(X)
X = A[125]
print(X)

print("\n** FROMKEYS **")
# RETORNA UM PAR DE CHAVE DE VALOR DE UM INTERAVEL, E O VALOR ESPECIFICADO
D = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}
A = D.copy()
codigos =(111,139,143,157)
A.fromkeys(codigos)
print(A.fromkeys(codigos))
print(A)
print(A.fromkeys(codigos, "Algo"))
del(A)
A = {}.fromkeys(codigos, " ")
print(A)
A[111] = "Vinagre"
print(A)

print("\n** POP **")
D = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão', 111: "Vinagre"}
print(D)
X = D.pop(111)
print(X)
print(D)

print("\n** POPITEM **")
D = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão', 111: "Vinagre"}
X = D.popitem()
print(X)
print(D)
print(type(X))
X = D.popitem()
print(X)
print(D)
X = D.popitem()
print(X)
print(D)
X = D.popitem()
print(X)
print(D)

print("\n** SET **")
# SE O ELEMENTO JA ESTÁ NA LISTA COM A CHAVE, ELE RETORNA O VALOR QUE ESTÁ ASSOCIADO A CHAVE E SE NÃO ESTIVER NA LISTA, ELE ADICIONA O NOVO VALOR A COM A CHAVE E RETORNA O NOVO VALOR
D = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão', 111: "Vinagre"}
print(D)
R = D.setdefault(144, "Feijão")
print(R)
print(D)
R = D.setdefault(117, "Feijão")
print(R)

print("\n** UPDATE **")
# TEM QUE SER LISTA OU TUPLA
D = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão', 111: "Vinagre"}
D.update( ( (177, "Cebola" ),(217, "Maça"), (185, "Abacate") ) )
print(D)

print("\n** KEYS **")
chave = D.keys()
print(chave)
print(type(chave))

print("\n** VALUE **")
vl = D.values()
print(vl)
print(type(vl))
    
print("\n** ITEMS **")
item = D.items()
print(item)
print(type(item))

D = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão', 111: 'Vinagre', 177: 'Cebola', 217: 'Maça', 185: 'Abacate'}
for k in D.items():
    print(k)
print("\n")
for k in D.keys():
    print(k)
print("\n")
for k in D.values():
    print(k)