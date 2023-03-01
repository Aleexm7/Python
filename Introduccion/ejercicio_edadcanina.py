#Comúnmente se dice que un año humano equivale a 7 años caninos. 
"""
Sin embargo, esta simple conversión no reconoce que los perros alcanzan la edad adulta en aproximadamente dos años. 
Como resultado, algunas personas creen que es mejor contar cada uno de los dos primeros años humanos como 10,5 años caninos y luego contar cada año humano adicional como 4 años caninos.
Escriba un programa que implemente la conversión de años humanos a años caninos descrita en el párrafo anterior. 
Asegúrese de que su programa funcione correctamente para conversiones de menos de dos años humanos y para conversiones de dos o más años humanos. 
Su programa debería mostrar un mensaje de error apropiado si el usuario ingresa un número negativo. """


entrada = int(input("Dame un año humano para calcular la conversion a edad canina: "))
def edadcanina():
    edadhumana = entrada
    if edadhumana < 0:
        return "Error de conversion, es un numero negativo"
    elif edadhumana <= 2:
            edadcanina = edadhumana * 10.5
            return f"La edad canina es {edadcanina}"
    else:
         edadcanina = 21 + (edadhumana -2) * 4
         return f" La edad canina es {edadcanina}"   

print(edadcanina())
