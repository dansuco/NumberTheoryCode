#Tenemos codificado el teorema de gauss de que en una sussecion de enteros positivos solo hay un ...
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

