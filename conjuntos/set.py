

set()

c.add(85)
print(c)
c.add(32)
c.add(100)
c.add(76)

print(c)

d = c.copy() # copia mas o ID é diferente ou seja, o elemento é diferente mesmo copiando

print(d)
print(id(c))
print(id(d))

c1 = {26,32,45,58,63}
c2 = {19,34,58,67,82}

print(c1.difference(c2)) #mostra o que tem em c1 e nao tem em c2
c1 = {26,32,45,58,63}
c2 = {19,34,58,67,82}
z = c1.difference_update(c2)
print(z)

c2.discard(58) # remove o elemento
print(c2)
c1 = {26,32,45,58,63}
c2 = {19,34,58,67,82}

print(c1.intersection(c2))  # mostra a interseção