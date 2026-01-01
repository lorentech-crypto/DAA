import argparse
from pathlib import Path

from src.common.io import cargar_instancia
from src.common.graph import construir_grafo_desde_instancia


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    args = parser.parse_args()

    instancia = cargar_instancia(Path(args.instance))
    grafo = construir_grafo_desde_instancia(instancia)

    print("Instancia cargada correctamente")
    print("Número de nodos:", grafo.graph.number_of_nodes())
    print("Número de aristas:", grafo.graph.number_of_edges())


if __name__ == "__main__":
    main()
