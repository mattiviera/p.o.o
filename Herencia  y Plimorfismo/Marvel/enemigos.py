from Personaje.personaje import Personaje

class EnemigoMarvel(Personaje):
    def __init__(self, nombre, edad, genero, habilidad):
        super().__init__(nombre, edad, genero)
        self.habilidad = habilidad

    def atacar(self):
        print(f"{self.nombre} está atacando con su habilidad: {self.habilidad}!")
