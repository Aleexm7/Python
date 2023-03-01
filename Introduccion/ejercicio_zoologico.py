"""
Un zoológico en particular determina el precio de la entrada según la edad del visitante. 
Los huéspedes de 2 años de edad y menos se admiten sin cargo. 
Niños entre 3 y 12 años cuestan $14.00. 
Las personas mayores de 65 años o más cuestan $ 18.00. 
La entrada para todos los demás invitados es de $23.00.
Cree un programa que comience leyendo las edades de todos los invitados en un grupo del usuario, con una edad ingresada en cada línea. 
El usuario ingresará una línea en blanco para indicar que no hay más invitados en el grupo. 
Luego, su programa debe mostrar el costo de admisión para el grupo con un mensaje apropiado. 
El costo debe mostrarse con dos decimales.
"""

def ticket():
    lista_edades = []
    while True:
        entrada = input("Dime una edad para calcular el precio de tu entrada: ")    
        if entrada == "":
            break
        lista_edades.append(int(entrada))
        
    return lista_edades
    

def valor_edades(lista_edades):
  valor = 0
  lista_precio = []
  for x in range(len(lista_edades)):
    if lista_edades[valor] <= 2:
      lista_precio.append(0)
    if lista_edades[valor] >= 3 and lista_edades[valor] <= 12:
      lista_precio.append(14)
    if lista_edades[valor] > 12 and lista_edades[valor] < 65:
      lista_precio.append(23)
    if lista_edades[valor] >= 65:
        lista_precio.append(18)
    valor += 1
  
  return lista_precio

def suma(lista_precio):
    valor = 0
    total = 0
    
    for x in range(len(lista_precio)):
        total += lista_precio[valor]
        valor += 1
        
    return total

def main():
    lista_edades = ticket()
    lista_precio = valor_edades(lista_edades)
    total = suma(lista_precio)
    print(f"El total de la entrada es {total:.2f}, aplicándose los descuentos por la edad")

main()
