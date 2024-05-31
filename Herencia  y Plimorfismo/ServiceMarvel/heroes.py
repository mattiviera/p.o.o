from ControllerPersonaje.personaje import Personaje

class HeroeMarvel(Personaje):
    def __init__(self, nombre, edad, genero, habilidad,arma):
        super().__init__(nombre, edad, genero)
        self.habilidad = habilidad
        self.arma = arma
        

    def atacar(self):
        print(f"{self.nombre} está usando su habilidad: {self.habilidad}!, y su arma: {self.arma}")
