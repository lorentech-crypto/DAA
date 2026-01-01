"""
Cálculo de los objetivos del problema multiobjetivo.
"""

from typing import List, Tuple


def distancia_total(pesos: List[Tuple[float, float, float]]) -> float:
    """Suma de las distancias de todas las aristas del recorrido."""
    return sum(p[0] for p in pesos)


def riesgo_total(pesos: List[Tuple[float, float, float]]) -> float:
    """Suma del riesgo acumulado."""
    return sum(p[1] for p in pesos)


def consumo_bateria(pesos: List[Tuple[float, float, float]]) -> float:
    """Consumo total de batería."""
    return sum(p[2] for p in pesos)
