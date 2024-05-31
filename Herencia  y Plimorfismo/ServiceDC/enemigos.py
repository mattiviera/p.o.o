from ControllerPersonaje.personaje import Personaje

class EnemigoDC(Personaje):
    def __init__(self, nombre, edad, genero, habilidad, frase):
        super().__init__(nombre, edad, genero)
        self.habilidad = habilidad
        self.frase = frase

    def atacar(self):
        print(f"{self.nombre} está atacando con su habilidad: {self.habilidad}!")
        print(f"{self.nombre} no podras derrotarme yo soy: {self.frase}!!!")
