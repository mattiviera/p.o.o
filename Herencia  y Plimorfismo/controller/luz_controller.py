from service.luz import LuzBlanca

class LuzController:
    def __init__(self):
        self.luz = LuzBlanca()

    def encender_luz(self):
        return self.luz.encender()

    def apagar_luz(self):
        return self.luz.apagar()
