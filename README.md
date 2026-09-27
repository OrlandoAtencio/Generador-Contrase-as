# 🔐 Generador Seguro de Contraseñas (Python)

Una aplicación de escritorio ligera y modular desarrollada en Python para generar contraseñas criptográficamente seguras. Diseñada con un enfoque en la ciberseguridad, las buenas prácticas de código y la experiencia del usuario (UX).

## 🚀 Características Principales

*   **Seguridad Criptográfica:** Utiliza el módulo `secrets` de Python en lugar de `random` para garantizar que los valores generados sean impredecibles y aptos para la seguridad.
*   **Totalmente Personalizable:**
    *   Longitud ajustable mediante un slider (10 a 20 caracteres).
    *   Selección de conjuntos de caracteres: Mayúsculas, Minúsculas, Números y Símbolos.
*   **Interfaz Gráfica Amigable:** Desarrollada con `tkinter` (Librería estándar de Python), importando estrictamente los módulos necesarios para optimizar el consumo de recursos.
*   **Comodidad (UX):** Incluye un botón para copiar la contraseña generada directamente al portapapeles con confirmación visual.
*   **Arquitectura Modular:** El código está separado por responsabilidades para facilitar su escalabilidad y mantenimiento.

## 📁 Estructura del Proyecto

El proyecto sigue un diseño modular dividido en tres archivos principales:

```text
├── main.py         # Punto de entrada. Inicializa la aplicación.
├── interfaz.py     # Contiene la clase InterfazGenerador (GUI de Tkinter).
└── generador.py    # Lógica central. Maneja el módulo 'secrets' y los strings.
```

## 🛠️ Tecnologías y Herramientas

*   **Lenguaje:** Python 3.x
*   **Librerías Core:** 
    *   `tkinter` (GUI)
    *   `secrets` (Generación segura)
    *   `string` (Constantes de caracteres)

## ⚙️ Instalación y Uso

1.  Clona este repositorio en tu máquina local:
    ```bash
    git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
    ```
2.  Navega a la carpeta del proyecto:
    ```bash
    cd TU_REPOSITORIO
    ```
3.  Ejecuta el archivo principal (no requiere dependencias externas):
    ```bash
    python main.py
    ```
    *(Nota: En algunos sistemas operativos como macOS o Linux puede que necesites usar `python3`)*

## 🧠 Aprendizajes Clave
Este proyecto fue desarrollado poniendo en práctica:
*   Programación Orientada a Objetos (POO) en interfaces gráficas.
*   Modularidad y principio de responsabilidad única.
*   Optimización de importaciones (`from modulo import funcion`).
*   Conceptos básicos de ciberseguridad en la generación de tokens/passwords.