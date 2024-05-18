from service.luz import LuzPatio

class LuzControllerPatio:
    def __init__(self):
        self.luz = LuzPatio()
        
    def encender_luz(self):
        return self.luz.encender()
    
    def apagar_luz(self):
        return self.luz.apagar()