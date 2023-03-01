entrada1 =input("Escribe un numero entero: ")
entrada2 =input("Dame un numero igual o mayor: ")

if entrada1 > entrada2:
    print(f"¡Te he pedido un numero mayor que {entrada2}")
else:
    for i in range(entrada1,entrada2 +1):
        if i % 2 == 0:
            print(f"El numero {i} es par")
        else:
            print(f"El numero {i} es impar")