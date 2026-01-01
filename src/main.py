from pathlib import Path
import argparse

from src.common.io import cargar_instancia
from src.common.graph import construir_grafo_desde_instancia
from src.geo_heuristic.geo_solver import GeometricSolver
from src.geo_heuristic.visualize import dibujar_ruta


def main():
    # -------------------------------
    # 1. Leer argumentos
    # -------------------------------
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True, help="Ruta al archivo JSON de la instancia")
    args = parser.parse_args()

    # -------------------------------
    # 2. Cargar instancia
    # -------------------------------
    raiz = Path(__file__).resolve().parent.parent
    ruta_instancia = raiz / args.instance
    instancia = cargar_instancia(ruta_instancia)

    print("Instancia cargada correctamente")
    print("Número de nodos:", len(instancia["nodes"]))
    print("Número de zonas no-fly:", len(instancia["no_fly_zones"]))

    # -------------------------------
    # 3. Construir grafo
    # -------------------------------
    grafo = construir_grafo_desde_instancia(instancia)
    print("Grafo construido")
    print("Nodos:", grafo.numero_nodos())
    print("Aristas:", grafo.numero_aristas())

    # -------------------------------
    # 4. Resolver con heurística geométrica
    # -------------------------------
    solver = GeometricSolver(grafo)
    ruta = solver.solve()
    objetivos = solver.evaluar_ruta(ruta)

    print("\n--- Heurística geométrica ---")
    print("Ruta encontrada:", ruta)
    print("Objetivos (distancia, riesgo, batería):", objetivos)

    # -------------------------------
    # 5. Dibujar ruta
    # -------------------------------
    dibujar_ruta(grafo, ruta, titulo="Ruta encontrada por heurística geométrica")


if __name__ == "__main__":
    main()
