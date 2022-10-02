'''
Ejercicio 1

Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. 
¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?
Nombre Apellido ha sacado un Nota de nota.
Ayuda
Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]
cadena = "zeréP nauJ, 01"

'''

cadena = "zeréP nauJ, 01"

# Método 1:

#cadena_girada = cadena[::-1]
#print(cadena_girada)
#print(cadena_girada[4:], "ha sacado un", cadena_girada[:2], "de nota")

# Método 2, con función: 

def formatear_cadena(cadena):

    nombre_girado = cadena[0:cadena.find(",")][::-1]
    #print(nombre_girado)
    nota_girada = cadena[cadena.find(",") + 2:][::-1]
    return (f"{nombre_girado} ha sacado un {nota_girada} de nota")

cadena_formateada = formatear_cadena(cadena)
print(cadena_formateada)