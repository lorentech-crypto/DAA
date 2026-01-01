"""
Funciones auxiliares comunes.
"""

import time
import random
from contextlib import contextmanager


@contextmanager
def temporizador():
    """
    Context manager para medir tiempo de ejecución.
    """
    inicio = time.perf_counter()
    yield lambda: time.perf_counter() - inicio


def fijar_semilla(seed: int):
    """Fija la semilla aleatoria para reproducibilidad."""
    random.seed(seed)
