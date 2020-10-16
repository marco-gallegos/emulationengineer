"""
@Author: Marco A. Gallegos
@Date: 2020/10/15
@Version: python 3.8
@Description: 
    obtener dos maximos y minimos de una lista de numeros , el objetivo no es ser eficiente si no rapido (al codear) y cool ( ͡° ͜ʖ ͡°)
"""

lista = [100,55,66,2345,56,234,67,66]

def mayores_menores(lista:list)->dict:
    lista.sort()
    return {
        "mayores": lista[0:2],
        "menores": lista[::-1][0:2]
    }

data = mayores_menores(lista)

print(lista)
print(data)