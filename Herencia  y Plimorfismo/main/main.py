import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from controller.luz_controller import LuzController

def main():
    controlador = LuzController()
    
    print(controlador.encender_luz())  
    print(controlador.apagar_luz())    

if __name__ == "__main__":
    main()



