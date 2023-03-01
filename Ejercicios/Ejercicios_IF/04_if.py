#Escribe un programa que pida dos números enteros y que a continucación indique
#si el número mayor es múltiplo del menor.

num1 = int(input("Escribe un número cualquiera: "))
num2 = int(input("Escribe otro número: "))

if num1 == 0 or num2 == 0:
    print("No se puede dividir entre 0")
else:
    if num1 == num2:
        print("Son iguales")
    else:
        if num1>num2:
            div1 = num1 % num2
            if div1 == 0:
                print(f"El numero mayor {num1} es multiplo de {num2}")
            else:
                print(f"El numero mayor {num1} no es multiplo de {num2}")
        else:
            if num2>num1:
                div2 = num2 % num1
                if div2 == 0:
                    print(f"El numero mayor {num2} es multiplo de {num1}")
                else:
                    print(f"El numero mayor {num2} no es multiplo de {num1}")