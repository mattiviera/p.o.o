from service.luz import ApagarTodo

class ApagarLuz:
    def __init__(self):
        self.luz = ApagarTodo()

    def apagar_luz(self):
        return self.luz.apagar()