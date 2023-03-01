#Escribe un programa que pida por teclado en primer lugar el año actual y después un año
#cualquiera. A continuación, el programa ha de indicar cuántos años faltan para llegar o
#cuantos años han pasado al/desde ese segundo año
num1 = int(input("Escribe el año actual: "))
num2 = int(input("Escribe un año cualquiera: "))

if num1 == num2:
    print(f"Son el mismo año")
else:
    if num1>num2:
        resultado1 = num1 - num2
        print(f"Han pasado {resultado1} años")
    else:
        if num2>num1:
            resultado2 = num2 - num1
            print(f"Faltan {resultado2} años para llegar")