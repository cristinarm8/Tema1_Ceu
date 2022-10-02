'''
Ejercicio 4

Durante la planificación de un proyecto se han acordado una lista de tareas. 
Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).
¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?
Sugerencia
Para ordenar automáticamente una lista es posible utilizar el método .sort(), deberias probarlo.

'''

from collections import deque

def imprimir_tareas_ordenadas(tareas):

    tareas_ordenadas = {}
    claves_ordenadas = sorted(tareas, key=tareas.get)

    for i in claves_ordenadas:
        tareas_ordenadas[i] = tareas[i]
    print(f"\nLista de tareas ordenadas por prioridad: {tareas_ordenadas.keys()}")

    lista_claves = list(tareas_ordenadas.keys())
    #print(type(lista_claves))
    #lista_claves = list(lista_claves)
    #print(type(lista_claves))

    cola = deque(lista_claves)
    print("Ahora lo mostramos como una estructura de tipo cola: ")
    for i in cola:
        print(i, end=" ")

tareas_1 = {"Identificar": 5, "Investigacion": 2,"Evaluacion": 7, "Metodologia":3, "Objetivo": 1, "Comunicacion" : 6, "Planificar":4}
imprimir_tareas_ordenadas(tareas_1)








