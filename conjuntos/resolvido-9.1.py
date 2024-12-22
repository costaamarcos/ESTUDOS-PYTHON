from random import randint

QTDE = int(input("Digite a quantidade: "))

while QTDE > 50:
    print("valor muito alto")
    QTDE = int(input("Digite a quantidade:(max 50):  "))
#criação conjunto vazio
conjunto = set()
while len(conjunto) < QTDE:

    conjunto.add(randint(1,50)) # GERA NÚMEROS ALEATÓRIOS
print(conjunto)
print(f"O conjunto tem {len(conjunto)} elementos")
print("FIM!!")
