"""
@Author: Marco A. Gallegos
@Date: 2020/10/15
@Version: python 3.8
@Description: 
    fibonacci hasta n, el objetivo no es ser eficiente si no rapido (al codear) y cool ( ͡° ͜ʖ ͡°)
"""

limite = int(input("dame el limite de la serie: "))

fibonacci = [0,1]
index = len(fibonacci)
next_number = 1

while next_number < limite:
    fibonacci.append(next_number)
    next_number = fibonacci[index] + fibonacci[index-1]
    index+=1


print(fibonacci)