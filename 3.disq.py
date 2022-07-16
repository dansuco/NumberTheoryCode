print("TEOREMA:")
print("Dados m numeros enteros consecutivos a, a+1, a+2, ... a+m-1 y se A otro entero")
print("entonces existe un unico elemento de la sucesion que es congruente con A al modulo de m")
print()
print("compruebelo: ")
m = int(input("cantidad de elementos (m): "))
a = int(input("primer elemento de la sucesion de enteros (a): "))
A = int(input("otro entero (A): "))
lista = range(a, a+m)
numeros = list()
for i in lista:
    elemento=(i-A)/m
    #print(elemento) esta linea imprime el resultado de (i-A)/m solo va a haber un entero
    numeros.append(elemento)
print()
for j in numeros:
    valor = (j*m) + A
    if valor%m == A%m:
        print("en el intervalo : ({}, {}), el numero que es congruente con {} modulo {} es {}".format(lista[0], lista[0]+m,A, m, valor))

