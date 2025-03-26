'''
if anidados:
if dentro de otro if
syntax:
if condicion1:
    if condicion2:
        print("mensaje1")
    if condicion3:
        print("mensaje2")
    if condicion4:
        print("mensaje3")
    elif condicion5:
        print("mensaje4")
    elif condicion6:
        print("mensaje5")
    else:
        print("mensaje6")
NO confundir con elif (if en cascada)
'''

#ejemplo 1:
#modifique el ejercicio de la edad para las siguientes condiciones
#1. si es mayor de 18 años
#   pero no tiene documento, no puede votar
#   de lo contrario, si puede votar
#2. si es menor de 18 años
#   no puede votar
#   utilice estructura de if anidados
edad = int(input("Cual es su edad?: "))
if edad >= 18:
    documento = input("Tiene documento? (si/no): ")
    if documento == "si":
        print("Puede votar")
    else:
        print("No puede votar, no tiene documento")
else: 
    print("No puede votar, es menor de edad")