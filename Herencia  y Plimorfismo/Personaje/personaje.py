from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    @abstractmethod
    def atacar(self):
        pass

    def hablar(self):
        print(f"{self.nombre}: ¡Hola! Soy un personaje.")

    def __str__(self):
        return f"{self.nombre} ({self.edad} años, {self.genero})"
