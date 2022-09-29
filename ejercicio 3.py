# Ejercicio 3:
# Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, 
# pero no debe repetirse ningún elemento en la nueva lista: 
# lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o'] lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

'''
lista = [1,2,3,3,2,1]
conjunto = set(lista)
lista = list(conjunto)
print(lista)
'''
'''
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

lista_1 = list(set(lista_1))
lista_2 = list(set(lista_2))
print(lista_1)
print(lista_2)
'''

# Ejercicio 3:
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

def caracteres_repetidos(lista_1,lista_2):
    lista_caracteres_repetidos = []
    for i in lista_1:
        for j in lista_2:
            if i == j:
                lista_caracteres_repetidos.append(i)
    lista_caracteres_repetidos = list(set(lista_caracteres_repetidos))
    print(lista_caracteres_repetidos)

caracteres_repetidos(lista_1, lista_2)


