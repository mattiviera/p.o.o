from ControllerPersonaje.personaje import Personaje

class HeroeDC(Personaje):
    def __init__(self, nombre, edad, genero, habilidad):
        super().__init__(nombre, edad, genero)
        self.habilidad = habilidad

    def atacar(self):
        print(f"{self.nombre} está usando su habilidad: {self.habilidad}!")
