"""
Gestión de réplicas estocásticas.
"""


def ejecutar_repeticiones(solver, n=5):
    return [solver.solve() for _ in range(n)]
