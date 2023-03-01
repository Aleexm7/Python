#Escribe un programa que pida por teclado dos números y que indique cuál de ellos es el menor
#y cuál el mayor o bien si ambos números son iguales.
num1 = int(input("Escribe un numero: "))
num2 = int(input("Escribe otro numero: "))

if num1 == num2:
    print("Ambos numeros son iguales")
else:
    if num1<num2:
        print(f"El numero menor es {num1} y el numero mayor es {num2}")
    else:
        if num2<num1:
            print(f"El numero menor es {num2} y el numero mayor es {num1}")