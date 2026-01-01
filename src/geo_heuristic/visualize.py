"""
Visualización de rutas de drones sobre el mapa de la ciudad,
incluyendo nodos, zonas no-fly y la ruta generada por la heurística.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPolygon


def dibujar_ruta(grafo, ruta, titulo="Ruta del dron"):
    """
    Dibuja la ruta sobre el grafo con zonas no-fly.

    Parameters
    ----------
    grafo : DroneGraph
        Grafo que contiene nodos y aristas
    ruta : List[int]
        Lista de IDs de nodos visitados en orden
    titulo : str
        Título del gráfico
    """

    fig, ax = plt.subplots(figsize=(8, 6))

    # -----------------------------
    # Dibujar nodos
    # -----------------------------
    colores = {"hub": "red", "destino": "blue", "recarga": "green"}
    for n, attr in grafo.graph.nodes(data=True):
        x, y = attr["coord"]
        ax.scatter(x, y, c=colores.get(attr["kind"], "black"), s=100, label=attr["kind"])
        ax.text(x + 0.1, y + 0.1, str(n), fontsize=9)

    # -----------------------------
    # Dibujar zonas no-fly
    # -----------------------------
    # Asumimos que las zonas ya se encuentran en los atributos del grafo
    if hasattr(grafo, "zonas_no_fly"):
        for pol in grafo.zonas_no_fly:
            patch = MplPolygon(list(pol.exterior.coords), closed=True, color="orange", alpha=0.3)
            ax.add_patch(patch)
    else:
        print("Aviso: No se encontraron zonas no-fly en el grafo para dibujar")

    # -----------------------------
    # Dibujar ruta
    # -----------------------------
    coords = [grafo.graph.nodes[n]["coord"] for n in ruta]
    xs, ys = zip(*coords)
    ax.plot(xs, ys, color="black", linestyle="-", linewidth=2, marker="o", markersize=5, label="Ruta")

    ax.set_title(titulo)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)
    ax.axis("equal")

    # Evitar duplicados en leyenda
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys())

    plt.tight_layout()
    plt.show()
