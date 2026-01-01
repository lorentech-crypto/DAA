"""
Define la estructura de datos del grafo dirigido ponderado
utilizado en el problema de planificación de rutas con drones.
Cada arista tiene un peso vectorial:
w = <distancia, riesgo, consumo de batería>
"""

from typing import Tuple
import networkx as nx


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
