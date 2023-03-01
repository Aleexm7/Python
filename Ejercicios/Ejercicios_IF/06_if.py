#Escribe un programa que solicite los coeficientes de una ecuación de primer grado(a*x+b=0)
#y que a continuación calcule y muestre como resultado la solución a la ecuación

a = int(input("Dame un coeficiente: "))
b = int(input("Dame otro coeficiente: "))

if a == 0 and b == 0:
    print("Todos los números son solución")
else:
    if a == 0:
        print("Sin solución")
    else:
        if b == 0:
            print("Sin solución")

        else:
            solucion = -b / a
            print(f"La solución de la ecuación es {solucion}")