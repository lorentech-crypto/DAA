"""
geo_solver.py
--------------
Heurística geométrica para rutas de drones.

Genera rutas factibles evitando zonas no-fly, visitando todos los destinos
una sola vez y volviendo al hub.
"""

from typing import List, Tuple
from src.common.graph import DroneGraph
from src.common.objectives import distancia_total, riesgo_total, consumo_bateria


class GeometricSolver:
    def __init__(self, graph: DroneGraph):
        """
        Inicializa el solver con un grafo ya construido.

        Parameters
        ----------
        graph : DroneGraph
            Grafo dirigido ponderado con nodos y aristas
        """
        self.graph = graph

    def solve(self) -> List[int]:
        """
        Genera una ruta factible usando heurística geométrica.

        Returns
        -------
        ruta : List[int]
            Lista de IDs de nodos en el orden visitado
        """
        # -----------------------------------------------------------------
        # 1. Identificar el hub y los destinos
        # -----------------------------------------------------------------
        hub = None
        destinos = []

        for n, attr in self.graph.graph.nodes(data=True):
            if attr["kind"] == "hub":
                hub = n
            elif attr["kind"] == "destino":
                destinos.append(n)

        if hub is None:
            raise ValueError("No se encontró un hub en el grafo")

        # -----------------------------------------------------------------
        # 2. Construir ruta usando vecino más cercano
        # -----------------------------------------------------------------
        ruta = [hub]
        nodos_por_visitar = set(destinos)
        nodo_actual = hub

        while nodos_por_visitar:
            vecinos = self.graph.graph[nodo_actual]
            # Filtrar vecinos que todavía no se visitaron
            vecinos_validos = {v: data for v, data in vecinos.items() if v in nodos_por_visitar}

            if not vecinos_validos:
                # Si no hay vecinos directos, tomar el destino más cercano (ignorando no-fly)
                min_dist = float("inf")
                siguiente = None
                for v in nodos_por_visitar:
                    peso = self.graph.graph.get_edge_data(nodo_actual, v, default=None)
                    if peso is not None:
                        dist = peso["weight"][0]
                        if dist < min_dist:
                            min_dist = dist
                            siguiente = v
                if siguiente is None:
                    raise ValueError("No se puede construir ruta factible con el grafo")
            else:
                # Elegir vecino con menor distancia
                siguiente = min(vecinos_validos.items(), key=lambda x: x[1]["weight"][0])[0]

            ruta.append(siguiente)
            nodos_por_visitar.remove(siguiente)
            nodo_actual = siguiente

        # -----------------------------------------------------------------
        # 3. Volver al hub
        # -----------------------------------------------------------------
        ruta.append(hub)

        return ruta

    # -----------------------------------------------------------------
    # 4. Evaluación de la ruta
    # -----------------------------------------------------------------
    def evaluar_ruta(self, ruta: List[int]) -> Tuple[float, float, float]:
        """
        Calcula los objetivos de la ruta: distancia, riesgo y batería.

        Parameters
        ----------
        ruta : List[int]
            Lista de IDs de nodos

        Returns
        -------
        objetivos : Tuple[float, float, float]
            (distancia_total, riesgo_total, consumo_bateria)
        """
        pesos = []
        for i in range(len(ruta) - 1):
            u = ruta[i]
            v = ruta[i + 1]
            peso = self.graph.graph[u][v]["weight"]
            pesos.append(peso)

        dist = distancia_total(pesos)
        riesgo = riesgo_total(pesos)
        bateria = consumo_bateria(pesos)

        return dist, riesgo, bateria
