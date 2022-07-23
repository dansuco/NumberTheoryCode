def main():
    print("TEOREMA:")
    print("Dados m numeros enteros consecutivos a, a+1, a+2, ... a+m-1 y se A otro entero")
    print("entonces existe un unico elemento de la sucesion que es congruente con A al modulo de m\n")
    print("compruebelo: ")
    m = int(input("cantidad de elementos (m): "))
    a = int(input("primer elemento de la sucesion de enteros (a): "))
    A = int(input("otro entero (A): "))
    numeros = [(i-A)/m for i in range(a, a+m)]
    congruentes = list(filter(lambda x: ((x*m)+A)%m ==A%m,numeros))
    print("en el intervalo : ({}, {}), el numero que es congruente con {} modulo {} es {}".format(a, a+m,A, m, congruentes[0]*m+A))

if __name__=="__main__":
    main()