"""
Implementa el algoritmo exacto Branch & Bound
para el circuito Hamiltoniano multiobjetivo.
"""


class BranchAndBoundSolver:
    def __init__(self, graph):
        self.graph = graph
        self.mejor_solucion = None
        self.mejor_coste = float("inf")

    def solve(self):
        """
        Método principal del algoritmo.
        Explora el espacio de soluciones con poda.
        """
        # TODO: backtracking + poda por cotas
        return self.mejor_solucion
