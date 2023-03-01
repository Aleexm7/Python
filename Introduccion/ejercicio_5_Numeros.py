"""
Escriba un programa que solicite al usuario que ingrese 5 números, separados por comas.
Calcule la suma de los 5 números y muestre los números ingresados y la suma al usuario

"""
entrada = int(input("Ingresa 5 númeritos: "))
def contador():
    lista_valores = []
    for v in range(5):
        lista_valores.append(int(entrada))
        lista_valores.append(sum(lista_valores))
    lista_valores.append("La suma de los numeros introducido es: ")
    return v

print(contador())
    
