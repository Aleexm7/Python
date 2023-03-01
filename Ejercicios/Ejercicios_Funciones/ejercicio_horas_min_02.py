"""
Escribir una función que reciba dos horas en formato "hh:mm:ss"
Debe devolver la diferencia entre ellas en formato "hh:mm:ss"
"""
from ejercicio_horas_min import horas_segundos #Esto es para importar una funcion de otro archivo distinto para reutilizarla


def dif_horas(inicio,fin):
    diferencia = abs(horas_segundos(fin) - horas_segundos(inicio)) #ABS sirve para pasar las horas restantes que salgan en negativo a positivo
    h = diferencia // 3600
    m = diferencia % 3600 // 60
    s = diferencia % 3600 % 60
    
    return f"{h:02d}:{m:02d}:{s:02d}"

print(dif_horas("23:56:21","20:33:10"))