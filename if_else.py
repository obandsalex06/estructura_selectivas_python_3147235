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

edad = 44
documento = False

if edad >= 18 and documento==True:
    print ("usted es mayor de edad ")
    print ("puede votar por petro")
else:
    print("usted es menor de edad")
    print("o")
    print("no puede votar por chinche")
print("fin programa")