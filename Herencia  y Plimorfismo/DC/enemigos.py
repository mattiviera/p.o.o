from Personaje.personaje import Personaje

class EnemigoDC(Personaje):
    def __init__(self, nombre, edad, genero, debilidad):
        super().__init__(nombre, edad, genero)
        self.debilidad = debilidad

    def atacar(self):
        print(f"{self.nombre} está atacando con su debilidad: {self.debilidad}!")
