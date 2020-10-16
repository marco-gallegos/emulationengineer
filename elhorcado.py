"""
@Author: Marco A. Gallegos
@Date: 2020/10/15
@Version: python 3.8
@Description: 
    mi juegito del "horcado" decia mi abuelo, el objetivo no es ser eficiente si no rapido (al codear) y cool ( ͡° ͜ʖ ͡°)
"""


palabra_adivinar = ""
palabra_lista = list(palabra_adivinar)
palabra_lista_original = []
palabra_lista_avance = []


while len(palabra_lista)==0:
    palabra_adivinar = str(input("dame la palabra a adivinar amigo :D : "))
    palabra_lista = list(palabra_adivinar)
palabra_lista_original = list(palabra_lista)
palabra_lista_avance = ["_" for x in palabra_lista]


finalizar_partida = False
intentos = 5
letra = ""
status_partida = True

recuento =list()
filename_recuento = "resultP.txt"


def update_avance(original:list, faltantes:list, avance:list, actual:str)->list:
    """actualiza la lista de avance

    Args:
        original (list): lista con la palabra original
        faltantes (list): lista de faltantes actuales
        avance (list): lista de caracteres que representan el avance actual
        actual (str): letra actual

    Returns:
        list: avance actualizado
    """
    if len(original) != len(avance):
        print("no es la misma longitud el avance y la original")
        return avance

    new_avance_list = avance
    for index in range(0,len(original)):
        # me dio toc no validar si aun existia
        if actual in faltantes:
            return avance
        if actual == original[index]:
            new_avance_list[index] = actual

    return new_avance_list

def imprime_list(avance:list)->bool:
    """solo imprime el list en bonito formato

    Args:
        avance (list): la lista con el avance

    Returns:
        bool: solo por si tenemos algun excepcion
    """
    for letra in avance:
        print(f"{letra}", end=',')
    print()
    print("="*120)


while not finalizar_partida:
    imprime_list(palabra_lista_avance)
    letra = str(input("cual letra crees que si esta en la palabra??? : "))
    if len(letra) == 0:
        continue
    letra = str(letra[0])

    existe = True if letra in palabra_lista else False

    if existe:
        print(f"Acierto '{letra}' si esta")
        palabra_lista = list(filter(lambda a: a != letra, palabra_lista))
        palabra_lista_avance = update_avance(original= palabra_lista_original, faltantes=palabra_lista,  avance=palabra_lista_avance, actual=letra)
    else:
        print(f"Fallo '{letra}' no esta")
        intentos -= 1

    if len(palabra_lista) == 0 or intentos <= 0:
        finalizar_partida = True
    recuento.append({
        "fallos": 5 - intentos,
        "restantes": "".join(palabra_lista)
    })

status_partida = True if len(palabra_lista) == 0 and intentos > 0 else False

if status_partida:
    print("Ganaste")
    imprime_list(avance=palabra_lista_avance)
else:
    print("Vuelve a Jugar")


status_file = open(filename_recuento, 'w')
for dict_avance in recuento:
    row_csv = f"{dict_avance['fallos']},{dict_avance['restantes']}\n"
    status_file.write(row_csv)

status_file.close()