#Escriba un programa que determine el nombre de una forma a partir de su número de lados.
#Lea la cantidad de lados del usuario y luego informe el nombre apropiado como parte de un mensaje significativo. 
#Su programa debe admitir formas con entre 3 y 10 lados (incluidos). 
#Si se ingresa un número de lados fuera de este rango, su programa debería mostrar un mensaje de error apropiado.
entrada1 = int(input("Dame un numero de lados para saber la figura geometrica: "))
def poligonos(lados):
    formas = ["cuadrado","triangulo","heptagono","pentagono","hexagono","octogono","eneagono","decagono"]
    if lados == 3:
        return formas[1]
    elif lados == 4:
         return formas[0]
    elif lados == 5:
         return formas[3]
    elif lados == 6:
        return formas[4]
    elif lados == 7:
        return formas[2]
    elif lados == 8:
        return formas[5]
    elif lados == 9:
        return formas[6]
    elif lados == 10:
            return formas[7]
    if lados < 3 or lados > 10:
        return "No hay figura geometrica"

print(poligonos(entrada1))   