#Dados m numeros enteros consecutivos a, a+1, a+2, ... a+m-1 y se A otro entero, entonces existe un unico elemento de la sucesion que es congruente con A al modulo de m
lista = range(0, 5)
m = len(lista)
A = -13
print()
print("modulo es: ",m)
print("el intervalo es: ({}, {})".format(lista[0], lista[0]+m))
print()
numeros = list()
for i in lista:
    elemento=(i-A)/m
    print(elemento)
    numeros.append(elemento)
print()
for j in numeros:
    valor = (j*m) + A
    if valor%m == A%m:
        print("el numero es", valor)
print()
numeros2=list()
for i in lista:
    elemento2=(-i-A)/m
    print(elemento2)
    numeros2.append(elemento2)
print(numeros2)
for j in numeros2:
    valor = (j*m) + A
    if valor%m == A%m:
        print("el numero es", valor)

