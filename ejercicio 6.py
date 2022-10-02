'''
Ejercicio 6

Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. 
La primera con los números pares y la segunda con los números impares. 
Por ejemplo: pares, impares = separar([6,5,2,1,7]) print(pares) print(impares) [2, 6] [1, 5, 7] 
Sugerencia Para ordenar una lista automáticamente puedes utilizar el método .sort().

'''
lista_separar = [6,5,2,1,7]

def separar(lista):

    pares = []
    impares = []

    for i in lista:
        if i % 2 == 0:
            pares.append(i)
            pares.sort()
        else:
            impares.append(i)
            impares.sort()
    return pares, impares

pares, impares = separar(lista_separar)
print(f"Los números pares son los siguientes: {pares}")
print(f"Los números impares son los siguientes: {impares}")



