""""
Escriba un programa que lea una posición del usuario. 
Use una declaración if para determinar si la columna comienza con un cuadrado negro o un cuadrado blanco. 
Luego usa la aritmética modular para informar el color del cuadrado en esa fila. 
Por ejemplo, si el usuario ingresa a1, su programa debería informar que el cuadrado es negro. 
Si el usuario ingresa d5, su programa debe informar que el cuadrado es blanco. 
Su programa puede suponer que siempre se ingresará una posición válida. 
No es necesario realizar ninguna comprobación de errores.

"""

def tablero():
    columna = posicion[0].lower()
    fila = int(posicion[1])
    letras = "aceg"    
    if columna in letras:
        columnaNegro = True
    else:
        columnaBlanco = False
            
    if columnaNegro:
        if fila % 2 == 0:
            columnaBlanco = True
        else:
            columnaBlanco = False
    else:
        if fila % 2 == 0:
            columnaBlanco =  False
        else:
            columnaBlanco = True
                
    if columnaBlanco:
        print("La posicion que has insertado es blanca")
    else:
        print("La posicion que has insertado es negra")
    
posicion = input("Dime una posicion: ")            
tablero()
            
     
          
    
    
    


    
    