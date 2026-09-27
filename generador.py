# generador.py
# Módulo encargado de la lógica de generación segura de contraseñas.

from secrets import choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

def generar_password(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos):
    """
    Genera una contraseña criptográficamente segura basándose en las preferencias del usuario.
    """
    caracteres_disponibles = ""
    
    # Se construye la "piscina" de caracteres permitidos según las opciones
    if incluir_mayusculas:
        caracteres_disponibles += ascii_uppercase
    if incluir_minusculas:
        caracteres_disponibles += ascii_lowercase
    if incluir_numeros:
        caracteres_disponibles += digits
    if incluir_simbolos:
        caracteres_disponibles += punctuation
        
    # Validación: El usuario debe elegir al menos una opción
    if not caracteres_disponibles:
        return "Error: Selecciona una opción"
        
    # Generación de la contraseña usando secrets.choice para garantizar aleatoriedad segura
    password = ''.join(choice(caracteres_disponibles) for _ in range(longitud))
    
    return password