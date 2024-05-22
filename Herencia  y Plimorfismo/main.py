import sys
import os

# Asegúrate de que el directorio raíz del proyecto esté en el PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '')))

from Marvel import HeroeMarvel, EnemigoMarvel
from DC import HeroeDC, EnemigoDC

# Ejemplo de uso
if __name__ == "__main__":
    ironman = HeroeMarvel("Iron Man", 40, "Masculino", "Tecnología avanzada")
    loki = EnemigoMarvel("Loki", 1000, "Masculino", "Ego")
    
    batman = HeroeDC("Batman", 35, "Masculino", "Inteligencia")
    joker = EnemigoDC("Joker", 45, "Masculino", "Caos")

    print(ironman)
    ironman.hablar()
    ironman.atacar()

    print(loki)
    loki.hablar()
    loki.atacar()

    print(batman)
    batman.hablar()
    batman.atacar()

    print(joker)
    joker.hablar()
    joker.atacar()
