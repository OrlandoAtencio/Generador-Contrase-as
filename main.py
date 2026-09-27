# main.py
# Archivo principal para ejecutar la aplicación.

from tkinter import Tk
from interfaz import InterfazGenerador

def main():
    # Instanciamos la ventana principal de Tkinter
    root = Tk()
    
    # Le pasamos la ventana a nuestra clase de interfaz
    app = InterfazGenerador(root)
    
    # Arrancamos el bucle de eventos (a la espera de los clics del usuario)
    root.mainloop()

if __name__ == "__main__":
    main()