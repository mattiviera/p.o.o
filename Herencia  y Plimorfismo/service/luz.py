class Luz:
    def encender(self):
        raise NotImplementedError("Las subclases deben implementar este método.")

    def apagar(self):
        raise NotImplementedError("Las subclases deben implementar este método.")

class LuzBlanca(Luz):
    def encender(self):
        return "Luz blanca encendida."

    def apagar(self):
        return "Luz blanca apagada."

