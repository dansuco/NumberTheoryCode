print("En este codigo usaremos el algoritmo de Euclidea para hallar el máximo común divisor de dos numeros no nulos simultaneos a,b ")
a = int(input("Primer numero (a): "))
b = int(input("Segundo numero (b): "))

if a>b and a!=0 and b!=0:
    a1, b1 = a,b
elif b>a and a!=0 and b!=0:
    a1, b1 = b,a
elif a == b and a!=0  :
    print(a, "=", b, "* 1", "+ 0")
    print("el maximo comun divisor de {} y {} es {}".format(a, b, b)) 
elif a > b and b == 0 :
    print(a, "=", b, "* 1", "+", a)
    print("el maximo comun divisor de {} y {} es {}".format(a, b, a))    
elif b > a and a == 0 :
    print(b, "=", a, "* 1", "+", b)
    print("el maximo comun divisor de {} y {} es {}".format(a, b, b))    
else:
    print("no nulos simultaneos")
if a!=b and a!=0 and b!=0 and a1%b1 !=0 :
    while b1 != 0 and a1%b1 >=0:
        mod = a1%b1
        x = (a1-mod)/b1
        print(a1, "=", b1, "*", int(x), "+", mod)
        a1,b1 = b1, mod
    print("el maximo comun divisor de {} y {} es {}".format(a, b, a1))
elif a!=b and a!=0 and b!=0 and a1%b1 == 0 :
    mod = a1%b1
    x = (a1-mod)/b1
    print(a1, "=", b1, "*", int(x), "+ 0")
    print("el maximo comun divisor de {} y {} es {}".format(a, b, b))    


