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
Total = bill + tip
Total = str(Total)
print ("bill + tip = " + Total)
Total = float (Total)
personas = input ("Entre cuantos ? ")
personas = int(personas)
TxPersona = Total / personas
TxPersona = round(TxPersona,2)
TxPersona = str(TxPersona)
print("A cada persona le toca : " + TxPersona)