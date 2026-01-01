"""
Annealing multiobjetivo.
"""

import math
import random


def simulated_annealing(sol_inicial, temperatura=1000, enfriamiento=0.995):
    """
    Refina soluciones mediante aceptación probabilística.
    """
    sol_actual = sol_inicial
    T = temperatura

    while T > 1e-3:
        # TODO: generar vecino y aceptar/rechazar
        T *= enfriamiento

    return sol_actual
