"""
Hacer una funcion que reciba una hora en formato hh:mm:ss.
Debe devolver la cantidad de segundos de dicha hora
"""
def contador(cadena_hora):
    sep_horas = cadena_hora.split(":") #Creamos la variable y le añadimos la funcion split para dividir con dos puntos
    lista = [] #Creamos la lista vacia para ingresar los valores nosotros
    for i in sep_horas:
        i = int(i)
        lista.append(i)
    segundos_horas = lista[0] * 3600
    segundos_minutos = lista [1] * 60
    suma = segundos_horas + segundos_minutos + lista [2]
    return suma
    
    
#print(contador("23:56:21"))

#OTRA FORMA DE HACER CONVERSIONES DE HORAS CON FUNCIONES
def contador2(cadena_hora):
    lista = cadena_hora.split(":")
    h = int(lista[0])
    m = int(lista[1])
    s = int(lista[2])
    return h * 3600 + m *60 + s

#print(contador2("23:56:21"))

#OTRA FORMA DE HACER CONVERSIONES DE HORAS CON FUNCIONES
def horas_segundos(cadena_hora):
    return int(cadena_hora[0:2]) * 3600 + int(cadena_hora[3:5]) * 60 + int(cadena_hora[6:8])

    
    
