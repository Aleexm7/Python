"""Escribe un programa que pida por teclado dos números enteros. A continuación, el
programa debe calcular su división, escribiendo el cociente entero, en caso de que el resto
no sea cero, habrá que mostrar también el valor del resto entero."""

"""
n1=int(input('Escribe el dividendo'))
n2=int(input('Escribe el divisor'))
div=(n1/n2)
divstr=str(div)
divno=divstr[0:]
ti=len(divstr)
rest=(divstr[1:])
if ti > 0:
    print(f'El resultado no es entero, es {divno} y el resto es {rest}')
else:
    print(f'El resultado es entero, es {div}')

"""

n1=int(input('Escribe el dividendo'))
n2=int(input('Escribe el divisor'))
if n2 == 0:
    print('No se puede hacer la división')
else:
    co=n1//n2
    rest=n1%n2
    if rest == 0:
        print(f'El resultado es entero, el cociente es {co}')
    else:
        print(f'El resultado no es entero, el cociente es {co} y el resto es {rest}')