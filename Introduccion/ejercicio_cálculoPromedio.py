"""
En este ejercicio, creará un programa que calcule el promedio de una colección de valores ingresados por el usuario. 

El usuario ingresará 0 como valor centinela para indicar que no se proporcionarán más valores. 

Su programa debería mostrar un mensaje de error apropiado si el primer valor ingresado por el usuario es 0.

"""
def calculo_promedio():
    lista = []
    total = 0
    valor = 0
    entrada = int(input("Dame una colección de numeros: "))
    contador = 0
    while entrada != 0:
        contador += 1
        lista.append(entrada)
        entrada = int(input("Dame otro numero: "))
        total = sum(lista)
        valor = (total/contador)
                
    else:
        print("La media de los numeros selecionados son: ", valor)
            

    

calculo_promedio()

