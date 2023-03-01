#Definimos la funcion alumno_notas y dentro de ella aplicamos 3 parámetros que usaremos a continuación
def alumnos_notas(alumno, *asignatura, **notas):
    print(f"El alumno {alumno} se ha matriculado de las asignaturas: ")
    print("--------")
    for a in asignatura:
        print(a) 
    print("-------")
    print("Sus notas son: ")
    
    for k,v in notas.items():
        print(f" {k}: {v}")
alumno = "Miguelito"        
asig = ["Progtamacion", "BBDD", "Sistemas", "Entorno de desarrollo"]
notas = {"Programación":7, "BBDD":2.5, "Sistemas":6, "Entorno de desarrollo":9}
alumnos_notas(alumno, *asig, **notas)
