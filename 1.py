"""
@Author: Marco A. Gallegos
@Date: 2020/10/15
@Version: python 3.8
@Description: 
    numero primo , el objetivo no es ser eficiente si no rapido (al codear) y cool ( ͡° ͜ʖ ͡°)
"""

numero = int(input("dame un numero: "))

def es_primo(num:int):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

if es_primo(numero):
    print("el numero es primo")
else:
    print("el numero no es primo")