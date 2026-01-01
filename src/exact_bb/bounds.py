"""
Definición de cotas inferiores y superiores.
"""


def cota_inferior(costes_parciales: float) -> float:
    """
    Cota optimista del coste restante.
    """
    return costes_parciales


def cota_superior(coste_heuristico: float) -> float:
    """
    Cota pesimista obtenida por heurística.
    """
    return coste_heuristico
