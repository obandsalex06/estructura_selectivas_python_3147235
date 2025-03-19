'''
if else:
determinar dos caminos de ejecucion basados en la evaluacion de una condicional
sintaxis:
if condicional:
    instruccion1
    instruccion2
else:
    instruccion3
    instruccion4 
'''
#ELABORE UN PROGARAMA EN PYTHON QUE DETERMINE SI UNA PERSONA ES MAYOR O MENOR DE EDAD
#Y POR TANTO HABILITADA PA VOTAR 

edad = int(input("Ingrese su edad: "))
documento = input ("Tiene documento (SI/NO): ")

if edad >= 18 and documento=="SI":
    print ("usted es mayor de edad ")
    print ("puede votar por petro")
else:
    print("usted es menor de edad")
    print("o")
    print("no puede votar por falta de documento")
print("fin programa")