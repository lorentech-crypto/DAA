"""
graph.py
---------
Define la estructura de datos del grafo dirigido ponderado
utilizado en el problema de planificación de rutas con drones.

Cada arista tiene un peso vectorial:
    w = <distancia, riesgo, consumo de batería>
"""

from typing import Tuple
import math
import networkx as nx
from shapely.geometry import Polygon

from src.common.geometry import segmento_valido


class DroneGraph:
    """
    Grafo dirigido que representa la ciudad y las rutas posibles del dron.
    """

    def __init__(self):
        # Usamos NetworkX para simplificar la gestión del grafo
        self.graph = nx.DiGraph()

    def add_node(self, node_id: int, coord: Tuple[float, float], kind: str):
        """
        Añade un nodo al grafo.

        Parameters
        ----------
        node_id : int
            Identificador del nodo
        coord : (float, float)
            Coordenadas (x, y)
        kind : str
            Tipo de nodo: 'hub', 'destino' o 'recarga'
        """
        self.graph.add_node(node_id, coord=coord, kind=kind)

    def add_edge(self, u: int, v: int, weight: Tuple[float, float, float]):
        """
        Añade una arista dirigida entre dos nodos.

        weight = (distancia, riesgo, consumo_bateria)
        """
        self.graph.add_edge(u, v, weight=weight)

    # ------------------------------------------------------------------
    # FUNCIONES AUXILIARES (NO ROMPEN LA CLASE)
    # ------------------------------------------------------------------

    def numero_nodos(self) -> int:
        """Devuelve el número de nodos del grafo."""
        return self.graph.number_of_nodes()

    def numero_aristas(self) -> int:
        """Devuelve el número de aristas del grafo."""
        return self.graph.number_of_edges()


# ----------------------------------------------------------------------
# CONSTRUCCIÓN DEL GRAFO DESDE UNA INSTANCIA JSON
# ----------------------------------------------------------------------

def distancia_euclidea(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    """
    Calcula la distancia euclídea entre dos puntos.
    """
    return math.dist(a, b)


def construir_grafo_desde_instancia(instancia: dict) -> DroneGraph:
    """
    Construye el grafo dirigido completo a partir de una instancia JSON,
    evitando aristas que crucen zonas no-fly.

    Parameters
    ----------
    instancia : dict
        Diccionario cargado desde el archivo JSON

    Returns
    -------
    DroneGraph
        Grafo completamente construido y listo para usar
    """

    grafo = DroneGraph()

    # -------------------------------------------------------------
    # 1. Construir polígonos de zonas no-fly
    # -------------------------------------------------------------
    zonas_no_fly = [
        Polygon(poligono) for poligono in instancia["no_fly_zones"]
    ]

    # -------------------------------------------------------------
    # 2. Añadir nodos al grafo
    # -------------------------------------------------------------
    for nodo in instancia["nodes"]:
        grafo.add_node(
            node_id=nodo["id"],
            coord=tuple(nodo["coord"]),
            kind=nodo["type"]
        )

    # -------------------------------------------------------------
    # 3. Crear aristas visibles con pesos vectoriales
    # -------------------------------------------------------------
    for u in instancia["nodes"]:
        for v in instancia["nodes"]:

            # No permitimos bucles
            if u["id"] == v["id"]:
                continue

            # Comprobamos si el segmento cruza alguna zona prohibida
            if segmento_valido(
                tuple(u["coord"]),
                tuple(v["coord"]),
                zonas_no_fly
            ):
                # Distancia
                d = distancia_euclidea(u["coord"], v["coord"])

                # Riesgo (modelo simple y explicable en la memoria)
                riesgo = 0.1 * d

                # Consumo de batería proporcional a la distancia
                consumo_bateria = d

                grafo.add_edge(
                    u["id"],
                    v["id"],
                    (d, riesgo, consumo_bateria)
                )

    return grafo
