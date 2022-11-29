lista1 = ['A1','A2','A3','A4','A5','A6','A7']
lista2 = ['B1','B2','B3','B4','B5','B6','B7']
lista3 = ['C1','C2','C3','C4','C5','C6','C7']


print("A  B  C")
for i in range(0,7):
    print(lista1[i],lista2[i],lista3[i])

escolha1 = input("Escolha uma Carta e digite a coluna que ela esta'A, B ou C': ")

if escolha1 == 'a':
    rodada1 = lista2+lista1+lista3
elif escolha1 == 'b':
    rodada1 = lista1+lista2+lista3
elif escolha1 == 'c':
    rodada1 = lista1+lista3+lista2

n = 3
rodada2 = [rodada1[i::n] for i in range(7)]

lista1 =rodada2[0]
lista2 =rodada2[1]
lista3 =rodada2[2]
print("A  B  C")
for i in range(0,7):
    print(lista1[i],lista2[i],lista3[i])

escolha2 = input("Em qual coluna esta a sua 'Carta'?: ")

if escolha2 == 'a':
    rodada3 = lista2+lista1+lista3
elif escolha2 == 'b':
    rodada3 = lista1+lista2+lista3
elif escolha2 == 'c':
    rodada3 = lista1+lista3+lista2

n = 3
rodada4 = [rodada3[i::n] for i in range(7)]


lista1 = rodada4[0]
lista2 = rodada4[1]
lista3 = rodada4[2]
print("A  B  C")
for i in range(0,7):
    print(lista1[i],lista2[i],lista3[i])

escolha3 = input("Em qual coluna esta a sua 'Carta'?: ")
print("A, B ou C?")
if escolha3 == 'A' or escolha3 == 'a':
    rodada5 = lista2+lista1+lista3
elif escolha3 == 'B' or escolha3 == 'b':
    rodada5 = lista1+lista2+lista3
else:
    rodada5 = lista1+lista3+lista2

resultado = {rodada5[10]}
print(f'Você escolheu > {resultado} <')
