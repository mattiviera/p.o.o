#%%
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from controller.luz_controller import LuzController
from controller.luz_controller2 import LuzControllerDos
from controller.luzpatio_controller import LuzControllerPatio
from controller.apagartodo import ApagarLuz
def main():
    controlador = LuzController()
    
    print(controlador.encender_luz())  
    print(controlador.apagar_luz())    

if __name__ == "__main__":
    main()

def main(): 
    controlador2 = LuzControllerDos()
    
    print (controlador2.encender_luz())
    print (controlador2.apagar_luz())
    
if __name__ == "__main__":
    main()
    
def main(): 
    controladorpatio = LuzControllerPatio()
    
    print (controladorpatio.encender_luz())
    print (controladorpatio.apagar_luz())
if __name__ == "__main__":
    main()
    
def main(): 
    controladorapagar = ApagarLuz()
    
    print (controladorapagar.apagar_luz())
if __name__ == "__main__":
    main()


# %%
