import argparse
from pathlib import Path
from src.common.io import cargar_instancia


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    args = parser.parse_args()

    instancia = cargar_instancia(Path(args.instance))
    print("Instancia cargada correctamente:", instancia.keys())


if __name__ == "__main__":
    main()
