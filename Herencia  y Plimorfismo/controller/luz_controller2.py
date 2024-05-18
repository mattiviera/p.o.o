from service.luz import LuzRoja 

class LuzControllerDos:
    def __init__(self):
        self.luz = LuzRoja()
        
    def encender_luz(self):
        return self.luz.encender()
    
    def apagar_luz(self):
        return self.luz.apagar()