# interfaz.py
# Módulo encargado de la interfaz gráfica de usuario (GUI) usando Tkinter.

from tkinter import Tk, Label, BooleanVar, Checkbutton, Scale, Button, Entry, StringVar, messagebox, HORIZONTAL, NORMAL
from generador import generar_password

class InterfazGenerador:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador Seguro de Contraseñas")
        self.root.geometry("380x420")
        self.root.resizable(False, False)

        # Variables booleanas para los checkboxes (Por defecto en True)
        self.var_mayus = BooleanVar(value=True)
        self.var_minus = BooleanVar(value=True)
        self.var_num = BooleanVar(value=True)
        self.var_sim = BooleanVar(value=True)

        # Variable para almacenar y mostrar la contraseña generada
        self.var_password = StringVar()

        # Llamada al método que dibuja la interfaz
        self._crear_widgets()

    def _crear_widgets(self):
        # Etiqueta de Título
        Label(self.root, text="Configuración de Contraseña", font=("Arial", 12, "bold")).pack(pady=15)

        # Barra deslizante (Scale) para la longitud estricta de 10 a 20
        Label(self.root, text="Longitud (10 a 20 caracteres):").pack()
        self.scale_longitud = Scale(self.root, from_=10, to=20, orient=HORIZONTAL, length=200)
        self.scale_longitud.set(15)  # Valor por defecto
        self.scale_longitud.pack(pady=5)

        # Checkboxes (Casillas de verificación)
        Checkbutton(self.root, text="Incluir Mayúsculas (A-Z)", variable=self.var_mayus).pack(anchor="w", padx=80)
        Checkbutton(self.root, text="Incluir Minúsculas (a-z)", variable=self.var_minus).pack(anchor="w", padx=80)
        Checkbutton(self.root, text="Incluir Números (0-9)", variable=self.var_num).pack(anchor="w", padx=80)
        Checkbutton(self.root, text="Incluir Símbolos (@#$%)", variable=self.var_sim).pack(anchor="w", padx=80)

        # Botón de Generar
        Button(self.root, text="Generar Contraseña", command=self.accion_generar, bg="#283593", fg="white", font=("Arial", 10, "bold")).pack(pady=15)

        # Campo de texto de solo lectura para mostrar el resultado
        self.entry_password = Entry(self.root, textvariable=self.var_password, state="readonly", width=25, font=("Courier New", 12), justify="center")
        self.entry_password.pack(pady=5)

        # Botón de portapapeles
        Button(self.root, text="📋 Copiar al portapapeles", command=self.accion_copiar).pack(pady=10)

    def accion_generar(self):
        """Captura los datos de la interfaz y se los envía al módulo generador."""
        longitud = self.scale_longitud.get()
        mayus = self.var_mayus.get()
        minus = self.var_minus.get()
        num = self.var_num.get()
        sim = self.var_sim.get()

        # Ejecutamos la función del archivo generador.py
        resultado = generar_password(longitud, mayus, minus, num, sim)
        
        # Para actualizar un Entry en "readonly", primero hay que pasarlo a NORMAL
        self.entry_password.config(state=NORMAL)
        self.var_password.set(resultado)
        self.entry_password.config(state="readonly")

    def accion_copiar(self):
        """Copia el contenido actual del Entry al portapapeles del sistema operativo."""
        password_actual = self.var_password.get()
        
        # Verificamos que haya una contraseña y que no sea el mensaje de error
        if password_actual and not password_actual.startswith("Error"):
            self.root.clipboard_clear()
            self.root.clipboard_append(password_actual)
            self.root.update()  # Necesario para que el SO registre el portapapeles
            messagebox.showinfo("Copiado", "¡La contraseña se copió al portapapeles con éxito!")
        else:
            messagebox.showwarning("Atención", "No hay una contraseña válida para copiar.")