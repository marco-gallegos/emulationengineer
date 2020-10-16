class Pokemon(object):
    ataque:int
    defensa:int
    velocidad:int
    sonido:str

    def __init__(self, ataque, defensa, velocidad, sonido):
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.sonido = sonido
    
    def roar(self):
        print(self.sonido.lower())

class PKMGEN2(Pokemon):
    def __init__(self, ataque, defensa, velocidad, sonido):
        Pokemon.__init__(self, ataque, defensa, velocidad, sonido)
    
    def roar(self):
        print(self.sonido.upper())

pika = Pokemon(ataque=40, defensa=20, velocidad=80, sonido="Pika CHUUUUUUUUUU")
charizard = Pokemon(ataque=90, defensa=70, velocidad=40, sonido="chariiiiiIIzard")
meow = Pokemon(ataque=100, defensa=100, velocidad=80, sonido="al ataque")

wobbufet = PKMGEN2(ataque=100, defensa=100, velocidad=80, sonido="wobbuuuuuuuuuuuuffet")

pokemones = [pika,charizard,meow,wobbufet]

for pokemon in pokemones:
    pokemon.roar()