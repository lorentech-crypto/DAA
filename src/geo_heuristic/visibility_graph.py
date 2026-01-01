"""
Construcción del grafo de visibilidad evitando zonas no-fly.
"""

from typing import List
from shapely.geometry import Polygon
from src.common.geometry import segmento_valido


def construir_grafo_visibilidad(nodos, zonas_no_fly: List[Polygon]):
    """
    Crea aristas solo entre nodos visibles.
    """
    aristas = []
    for i in nodos:
        for j in nodos:
            if i != j:
                if segmento_valido(i["coord"], j["coord"], zonas_no_fly):
                    aristas.append((i["id"], j["id"]))
    return aristas
