"""
Visualización de fronteras de Pareto.
"""

import matplotlib.pyplot as plt


def dibujar_pareto(frentes):
    for frente in frentes:
        x = [p[0] for p in frente]
        y = [p[1] for p in frente]
        plt.scatter(x, y)
    plt.xlabel("Distancia")
    plt.ylabel("Riesgo")
    plt.show()
