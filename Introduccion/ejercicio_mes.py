""" La duración de un mes varía de 28 a 31 días. 
En este ejercicio, creará un programa que lea el nombre de un mes del usuario como una cadena. 
Entonces su programa debería mostrar el número de días en ese mes. 
Muestre "28 o 29 días" para febrero para que se aborden los años bisiestos. """


mes = str(input("Introduce un mes para mostrar los días de ese mes: "))

def meses(dias):   
    if dias == "febrero":
        return "28 o 29 días"
    elif dias in ("abril","junio","septiembre","noviembre"):
        return "30 días"
    elif dias in ("enero","marzo","mayo","julio","agosto","octubre","diciembre"):
        return "31 dias"
    else:
        return f"{dias}, No se reconoce como mes"
    
print(meses(mes))