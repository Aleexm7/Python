from email.mime import base
import math

entrada1 = input("¿Quieres calcular el area del circulo o del triangulo?")
if entrada1 == "circulo":
    radio = float(input("Dime el radio del circulo: "))
    area_circulo = math.pi * radio ** 2
    print(area_circulo)

elif entrada1 == "triangulo":
        base_triangulo = float(input("Escribe la base del triangulo: "))
        altura_triangulo = float (input("Escribe la altura del triangulo"))
        area_triangulo = base_triangulo * altura_triangulo / 2
        print(area_triangulo)
     
                      
    