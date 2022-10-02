'''
Ejercicio 2

Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:
Guarda en una variable numero_magico el valor 12345679 (sin el 8)
Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
Multiplica el numero_usuario por 9 en sí mismo
Multiplica el numero_magico por el numero_usuario en sí mismo
Finalmente muestra el valor final del numero_magico por pantalla

'''
import sys
numero_magico = 12345679

def leer_y_validar_numero():
    while True:
        try:
            numero_usuario = int(input("Introduzca un número entre el 1 y 9: "))

            if numero_usuario < 1 or numero_usuario > 9:
                print("El número debe estar entre 1 y 9")

            else:
                return numero_usuario

        except:
            print("Debe introducir un número válido", file = sys.stderr)
            

def calculo_numero (numero_magico):

    numero_usuario = leer_y_validar_numero()

    numero_usuario *= 9

    numero_magico *= numero_usuario

    return numero_magico

valor_final = calculo_numero(numero_magico)
print(f"El valor final del número mágico es: {valor_final}")



