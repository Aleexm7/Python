"""
Un minorista en particular tiene un 60 por ciento de descuento en una variedad de productos descontinuados.

Al minorista le gustaría ayudar a sus clientes a determinar el precio reducido de la mercancía al tener una tabla de descuentos impresa en el estante que muestre los precios originales y los precios después de que se haya aplicado el descuento. 

Escriba un programa que use un bucle para generar esta tabla, que muestre el precio original, el monto del descuento y el nuevo precio para compras de $4.95, $9.95, $14.95, $19.95 y $24.95. 

Asegúrese de que los montos de descuento y los nuevos precios se redondeen a 2 decimales cuando se muestren.

"""

print("La tabla de  descuento es : ")
print("-----------")
print("Precio | Descuento | Total")
def tabla_descuento():
    precio_original = 4.95
    while precio_original <= 24.95:
        descuento = precio_original * 0.60
        precio_final = precio_original - descuento
        print(f"{precio_original:.2f} | {descuento:.2f} | {precio_final:.2f}")
        precio_original = precio_original + 5
    return tabla_descuento
        
print(tabla_descuento())
    