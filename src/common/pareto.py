"""
Herramientas para trabajar con dominancia de Pareto.
"""

from typing import List, Tuple


def domina(a: Tuple[float, ...], b: Tuple[float, ...]) -> bool:
    """
    Devuelve True si la solución a domina a b.
    """
    return all(x <= y for x, y in zip(a, b)) and any(x < y for x, y in zip(a, b))


def frontera_pareto(puntos: List[Tuple[float, ...]]) -> List[Tuple[float, ...]]:
    """
    Filtra los puntos no dominados.
    """
    frontera = []
    for p in puntos:
        if not any(domina(q, p) for q in puntos if q != p):
            frontera.append(p)
    return frontera
