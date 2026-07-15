import json
import os

RUTA_TAREAS = "data/tareas.json"
RUTA_HISTORIAL = "data/historial.json"


def cargar_datos(ruta):
    if not os.path.exists(ruta):
        return []

    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_datos(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


tareas = cargar_datos(RUTA_TAREAS)

usuarios_activos = set()

historial_ia = cargar_datos(RUTA_HISTORIAL)


conocimiento_base = {
    "python": "Python es un lenguaje de programación fácil de aprender.",
    "listas": "Estructura que almacena múltiples valores.",
    "bucles": "Permiten repetir acciones en programación."
}
