'''
Elabore un programa que permita 
calcular el salario neto de un
empleado, despues de descontar
los descuentos por conceptos de:
salud, pension, ARL
1. El problema debe solicitar
    el tipo de empleado:
    a- contrato a termino indefinido
    b- contrato por prestacion de servicios
    c- contrato de aprendizaje
    d- contrato por jornal (Freelane)
'''
'''
=> para el caso de prestacion de servicios 
se debe solicitar:
-valor del contrato
- el numero de meses del contrato
- la antiguedad del empleado (años)
el salario neto en este caso se calcula :
1 - dividir el valor del contrato,
por numero de meses
2 - restar el 15% de valor del contrato, por 
cocncepto de EPS 
3 - restar el 10% de valor del contrato pr concepto
de pension
4 - si el empleado tiene una antiguedad igual o mayor
a 10 años, se le descuenta el 5% por concepto de ARL 

=> para el caso de contrato indefinido 
se debe solicitar:
- antiguedad del empleado (años)
- grado o escalafon (1 - 5)
- el salario neto se calcula de acuerdo a la siguiente tabla:
- grado 1: 1.5 sm
- grado 2: 1.7 sm
- grado 3: 2.0 sm
- grado 4: 2.5 sm
- grado 5: 3.0 sm
la bonificacion estara acorde a los siguientes rangos:
- entre 1 y 5 años: 1% del salario mensual
- entre 6 y 10 años: 2% del salario mensual
- superior a 10 años: 3% del salario mensual
para este caso, los descuentos de ley son:
- 25% por concepto de EPS
- 22% por concepto de pension
- 0.1% por concepto de ARL
'''

contrato = input("ingrese el tipo de contrato: ")
#inicializar variables:
#Dar valor inicial a una variable
#asi no se utilice en el momento
salario_neto = 0
if contrato == "a":
    print("Eligió contrato a termino indefinido")
    antiguedad = int(input("Ingrese la antiguedad del empleado (años): "))
    grado = int(input("Ingrese el grado del empleado (1-5): "))
    sm = int(input("Ingrese el valor del salario minimo: "))
    if grado == 1:
        salario_mensual = sm * 1.5
    elif grado == 2:
        salario_mensual = sm * 1.7
    elif grado == 3:
        salario_mensual = sm * 2.0
    elif grado == 4:
        salario_mensual = sm * 2.5
    elif grado == 5:
        salario_mensual = sm * 3.0
    if antiguedad >= 1 and antiguedad <= 5:
        bonificacion = salario_mensual * 0.01
        print("bonificacion: ", bonificacion)
    elif antiguedad >= 6 and antiguedad <= 10:
        bonificacion = salario_mensual * 0.02
        print("bonificacion: ", bonificacion)
    elif antiguedad > 10:
        bonificacion = salario_mensual * 0.03
        print("bonificacion: ", bonificacion)
    eps = salario_mensual * 0.25
    print("EPS: ", eps)
    pension = salario_mensual * 0.22
    print("Pension: ", pension)
    arl = salario_mensual * 0.001
    print("ARL: ", arl)
    salario_neto = salario_mensual - eps - pension - arl + bonificacion
    print("Salario neto: ", salario_neto)
    

elif contrato == "b":
    print("Eligio contrato a termino indefinido")
    valor_cotrato = int(input("Ingrese el valor del contrato: "))
    numero_meses = int(input("Ingrese el numero de meses del contrato: "))
    antiguedad = int(input("Ingrese la antiguedad del empleado (años): "))
    salario_mensual = valor_cotrato / numero_meses
    eps = salario_mensual * 0.15
    pension = salario_mensual * 0.10
    bonificacion = salario_mensual * 0.05
    salario_neto = salario_mensual - eps - pension
    if antiguedad >= 10:
        salario_neto = salario_neto + bonificacion
    
    
elif contrato =="c":
    print("eligio contrato de aprendizaje")
    salario_minimo = int(input("Ingrese valor del salario minimo: "))
    salario_neto =salario_minimo - (salario_minimo * 0.25)
    
    
elif contrato =="d":
    print("Eligio contrato por jornal")
    #variable que solo se puede utilizar en un bloque  de codigo
    numero_horas = int(input("Ingrese numero de horas: "))
    valor_hora = int(input("Ingrese el valor por hora a pagar: "))
    salario_neto = numero_horas * valor_hora
    
    
else:
    print("El tipo de contrato no existe")
print("El salario neto es: " , salario_neto)
print("Fin del programa")
    
    
    
    