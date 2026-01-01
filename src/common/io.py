"""
Carga y guardado de instancias y resultados.
"""

import json
from pathlib import Path


def cargar_instancia(path: Path) -> dict:
    """Carga una instancia del problema desde JSON."""
    with open(path, "r") as f:
        return json.load(f)


def guardar_resultados(path: Path, datos: dict):
    """Guarda resultados en formato JSON."""
    with open(path, "w") as f:
        json.dump(datos, f, indent=2)
