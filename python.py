print ("Tips Program")
'''
    bill = 150
    porcentaje = 12
    operacion = 12 / 100
    tip = operacion * bill
    total = bill + tip
'''
bill = input ("total del bill ? ")
bill = float(bill)
porcentaje = input ("tip % : 10 , 12 o 15 ")
porcentaje = int(porcentaje)
operacion_1 = porcentaje / 100
tip = operacion_1 * bill
subTotal = bill + tip
subTotal = str(subTotal)
print ("bill + tip = " + subTotal)
# personas = input ("Entre cuantos ?")