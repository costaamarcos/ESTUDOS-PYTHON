# ALTERAÇÃO DE ELEMENTOS

d = {}
d["A"] = 120
print(d)
d["A"] = 250
print(d)
d["B"] = 521
print(d)

x = d["A"] + d["B"]
print(x)

# d["A"] = d["A"] + 100
d["A"] += 100
print(d["A"])
print(d)

chave = "A"
print(d[chave])

chave = "B"
print(d[chave])

# Cria um novo elemento chave "C" Adiciona valor 0 e print
chave = "C"
d[chave] = 0
print(d)

M = {}
print(type(M))
M[110] = 45.6
print(M)
M[9.2] = "xpto"
print(M)

M[(1, 0, 1)] = 281.9
print(M)