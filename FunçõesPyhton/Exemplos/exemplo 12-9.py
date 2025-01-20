def Somatoria(*dados):
    r = 0
    for i in dados:
        r += i
    return r
print(Somatoria(3, 6, 9))  # Saída: 18
print(Somatoria(5, 5))     # Saída: 10
print(Somatoria(1, 1, 1, 1, 1, 1, 1, 1, 1, 1))  # Saída: 10


