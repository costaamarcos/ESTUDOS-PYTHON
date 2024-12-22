
#1. Remoção de Duplicatas
#Conjuntos automaticamente eliminam elementos duplicados, o que é útil para limpar listas ou outras coleções. '''


# Python
lista = [1, 2, 3, 1, 2, 4]
conjunto = set(lista)
print(conjunto)  # Saída: {1, 2, 3, 4}


#2. Checagem Rápida de Pertencimento
# Checar se um elemento está em um conjunto é mais eficiente do que em listas, devido à sua implementação baseada em tabelas hash.


# Python
conjunto = {1, 2, 3, 4}
print(3 in conjunto)  # Saída: True
print(5 in conjunto)  # Saída: False



#3. Operações Matemáticas
# Conjuntos suportam operações como união, interseção, diferença e diferença simétrica.


# Python
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

# União
print(conjunto_a | conjunto_b)  # Saída: {1, 2, 3, 4, 5}

# Interseção
print(conjunto_a & conjunto_b)  # Saída: {3}

# Diferença
print(conjunto_a - conjunto_b)  # Saída: {1, 2}

# Diferença Simétrica
print(conjunto_a ^ conjunto_b)  # Saída: {1, 2, 4, 5}


# 4. Garantir Elementos Únicos em Coleções
# Se você quer armazenar itens únicos, como IDs ou nomes sem duplicatas, conjuntos são ideais.

# Python
ids = {"abc123", "def456", "ghi789"}
ids.add("abc123")  # Não será adicionado pois já existe
print(ids)  # Saída: {'abc123', 'def456', 'ghi789'}



# 5. Comparação de Conjuntos
#   Conjuntos permitem verificar subconjuntos, superconjuntos e igualdade entre coleções.

# Python
a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))  # Saída: True
print(b.issuperset(a))  # Saída: True
print(a == b)  # Saída: False



# 6. Processamento de Dados
# Conjuntos são usados para resolver problemas como identificação de valores exclusivos, filtros e cálculos rápidos.

# Python
palavras = "Python é divertido e Python é poderoso".split()
unicas = set(palavras)
print(unicas)  # Saída: {'é', 'poderoso', 'divertido', 'Python', 'e'}