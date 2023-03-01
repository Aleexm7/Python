""" Escribe un programa que pida por teclado dos números enteros. A continuación, el
programa debe calcular su división, escribiendo el cociente entero, en caso de que el resto
no sea cero, habrá que mostrar también el valor del resto entero. """""

num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el segundo numero: "))
cociente = num1//num2
resto = num1 % num2
variable = num1 / num2

print(variable)

if num1 == 0:
    print("La division es igual a 0")
else:
    cociente = num1//num2
    resto = num1 % num2
    if resto == 0:
        print(f"El resultado es exacto y el cociente es {cociente}")
    else:
        print(f"El cociente es {cociente} y el resto es {resto}")