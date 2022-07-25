def sort_numbers(a: int,b: int):
    if a>b and a!=0 and b!=0:
        a1, b1 = a,b
    elif b>a and a!=0 and b!=0:
        a1, b1 = b,a
    elif a == b and a!=0  :
        return "{a}, =, {b}, * 1, + 0".format(a=a, b=b) +"\n" + "el maximo comun divisor de {} y {} es {}".format(a, b, a) 
    elif a > b and b == 0 :
        return "{a}, =, {b}, * 1, +, {a}".format(a=a, b=b) +"\n" + "el maximo comun divisor de {} y {} es {}".format(a, b, a)
            
    elif b > a and a == 0 :
        return "{b} = {a}* 1 + {b})".format(a=a, b=b) +"\n" + "el maximo comun divisor de {} y {} es {}".format(a, b, b)
    else:
        return "no nulos simultaneos"
    return a1,b1

def main():
    print("En este codigo usaremos el algoritmo de Euclidea para hallar el máximo común divisor de dos numeros no nulos simultaneos a,b ")
    a = int(input("Primer numero (a): "))
    b = int(input("Segundo numero (b): "))
    a1,b1 = sort_numbers(a,b)
    
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


if __name__ == "__main__":
    main()
    