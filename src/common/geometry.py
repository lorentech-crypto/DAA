"""
Funciones geométricas para comprobar restricciones espaciales.
Se utilizan para:
- Detectar intersecciones con zonas no-fly
- Validar aristas del grafo
"""
from shapely.geometry import LineString, Polygon
from typing import Tuple, List

def segmento_intersecta_poligono(
    p1: Tuple[float, float],
    p2: Tuple[float, float],
    poligono: Polygon
) -> bool:
    """
    Comprueba si un segmento corta un polígono.

    Implementa los tests de intersección vistos en el Tema 7.
    """
    segmento = LineString([p1, p2])
    return segmento.intersects(poligono)


def segmento_valido(
    p1: Tuple[float, float],
    p2: Tuple[float, float],
    zonas_no_fly: List[Polygon]
) -> bool:
    """
    Devuelve True si el segmento NO intersecta ninguna zona prohibida.
    """
    for poligono in zonas_no_fly:
        if segmento_intersecta_poligono(p1, p2, poligono):
            return False
    return True
