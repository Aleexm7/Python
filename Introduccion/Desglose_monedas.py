dinero = int(input('Dime cuánto dinero queres: '))
billete_quiniento = dinero // 500
restobqui = dinero % 500

billete_dos = restobqui // 200
restobdos = billete_dos % 200

billete_cien = restobdos // 100
restobci = billete_cien % 100

billete_cincuenta = restobci // 50
restobcin = billete_cincuenta % 50

billete_veinte = restobcin // 20
restobvein = billete_veinte % 20

billete_diez = restobvein // 10
resbdiez = billete_diez % 10

billete_cinco = resbdiez // 5
restobcinc = billete_cinco % 5 

moneda_dos = restobcinc // 2
restomondos = moneda_dos % 2

moneda_uno = restomondos // 1
print(f'Te corresponden {billete_quiniento} billetes de 500, {billete_dos} billetes de 200, {billete_diez} billetes de 100, {billete_cincuenta} billetes de 50, {billete_veinte} billetes de 20, {billete_diez} billetes de 10, {billete_cinco} billetes de 5, {moneda_dos} monedas de 2 euros y {moneda_uno} monedas de un euro')
