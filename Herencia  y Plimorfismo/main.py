import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '')))

from ServiceMarvel import HeroeMarvel, EnemigoMarvel
from ServiceDC import HeroeDC, EnemigoDC

if __name__ == "__main__":
    thor = HeroeMarvel("Thor", 1000, "Masculino", "Rompe Tormentas", "Mjolnir")
    loki = EnemigoMarvel("Loki", 1000, "Masculino", "Engaño")
    
    batman = HeroeDC("Batman", 35, "Masculino", "Sigilo")
    joker = EnemigoDC("Joker", 45, "Masculino", "Poker", "Invencible")
    
    flash = HeroeDC ("Flash","20", "Masculino", "Super Velocidad")
    reverseflash = EnemigoDC ("Flash Reverso","52", "Masculino", "Tiempo Alterno", "Tu creador Flash")

    print(thor)
    thor.hablar()
    thor.atacar()

    print(loki)
    loki.hablar()
    loki.atacar()

    print(batman)
    batman.hablar()
    batman.atacar()

    print(joker)
    joker.hablar()
    joker.atacar()
    
    print(flash)
    flash.hablar()
    flash.atacar()
    
    print(reverseflash)
    reverseflash.hablar()
    reverseflash.atacar()



