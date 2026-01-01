"""
Operadores de vecindad para metaheurísticas.
"""

import random


def operador_swap(ruta):
    """
    Intercambia dos nodos de la ruta.
    """
    i, j = random.sample(range(len(ruta)), 2)
    ruta[i], ruta[j] = ruta[j], ruta[i]
    return ruta
