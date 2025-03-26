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
contrato = input("ingrese el tipo de contrato: ")
#inicializar variables:
#Dar valor inicial a una variable
#asi no se utilice en el momento
salario_neto = 0
if contrato == "a":
    print("Eligió contrato a termino indefinido")
elif contrato == "b":
    print("Eligio contrato a termino indefinido")
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
    
    
    
    