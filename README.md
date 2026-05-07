# ♟️ Generador de Tableros de Ajedrez con Python 

**Laboratorio 04:** Práctica numero 4.

---

## ¿De qué trata este proyecto?

[cite_start]Este repositorio contiene la implementación paso a paso de un **tablero de ajedrez funcional**En lugar de cargar una imagen estática, el tablero y sus piezas se construyen dinámicamente mediante código, utilizando una clase personalizada `Picture` y la librería gráfica `pygame` para el renderizado.

### Características Principales
*  **Programación Funcional y Estructurada:** Uso intensivo de herramientas nativas como `map`, `lambda`, `zip` y comprensión de listas
*  **Separación de Intereses (Modelo - Vista):** Las estructuras de datos están claramente diferenciadas de la lógica de renderizado gráfico
* **Transformaciones Gráficas:** Implementación de métodos para rotar, espejar (mirror), superponer e invertir colores de las figuras (piezas de ajedrez)

---

### Instalación y Configuración Rápida

Copia y pega los siguientes comandos en tu terminal para clonar el repositorio, configurar el entorno virtual e instalar todas las dependencias necesarias de un solo golpe:

```bash
# 1. Clonar el repositorio
git clone [https://github.com/AlejandroMendozP/LAB04_DAW.git](https://github.com/AlejandroMendozP/LAB04_DAW.git)

# 2. Ingresar a la carpeta del proyecto
cd LAB04_DAW

# 3. Crear el entorno virtual
python3 -m venv venv

# 4. Activar el entorno virtual (Ubuntu / Linux / macOS)
source venv/bin/activate

# 5. Instalar las dependencias
pip install pygame
