"""
Ejecuta benchmarks comparativos.
"""

from src.common.utils import fijar_semilla


def ejecutar_benchmark(instancias):
    resultados = {}
    for inst in instancias:
        fijar_semilla(42)
        resultados[inst] = {}
    return resultados
