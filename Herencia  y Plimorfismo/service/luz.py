class Luz:
    def encender(self):
        raise NotImplementedError("Las subclases deben implementar este método.")

    def apagar(self):
        raise NotImplementedError("Las subclases deben implementar este método.")

class LuzBlanca(Luz):
    def encender(self):
        if not self.funciona():
            raise LuzNoFuncionaException("La luz blanca no funciona.")
        return "Luz blanca encendida."

    def apagar(self):
        return "Luz blanca apagada."
    
    def funciona(self):
        return True

class LuzNoFuncionaException(Exception):
    pass
    
class LuzRoja(Luz):
    def encender(self):
        return "Luz roja encendida."

    def apagar(self):
        return "Luz roja apagada."
    
    
class LuzPatio(Luz): 
    def encender(self):
        return "Luz Patio de entrada encendida."
    
    def encender(self):
        return "Reflectores del frente encendidos."
    
    def apagar(self):
        return "Luces del patio trasero apagadas."
    
class ApagarTodo(Luz):
    def apagar(self):
        return "Se apagaron todas las luces."

