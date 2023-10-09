lista_1 = [1, 2, 3]

lista_dobro = []

for i in lista_1:
    lista_dobro.append(i * 2)

print(lista_dobro)

dobro = map(lambda i: i * 2, lista_1)
print(list(dobro))