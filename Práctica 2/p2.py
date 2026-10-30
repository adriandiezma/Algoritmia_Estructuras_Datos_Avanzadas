"""
Práctica 2: Algoritmos codiciosos.
Algoritmia y Estructuras de Datos Avanzadas.
Curso 2026-27.
"""

from typing import List, Tuple, Dict, Optional
import random

# =============================================================================
# I. Problema del cambio de monedas
# =============================================================================

def greedy_change(coins: List[int], amount: int) -> Tuple[List[int], int]:
    """
    Estrategia codiciosa para el problema del cambio de monedas.
    Selecciona en cada paso la moneda de mayor valor que no supere la cantidad restante.
    """
    # Ordenar las monedas de mayor a menor valor
    sorted_coins = sorted(coins, reverse=True)
    
    selected = []
    remainder = amount
    
    for coin in sorted_coins:
        # Añadir la moneda mientras quepa en la cantidad restante
        while remainder >= coin:
            selected.append(coin)
            remainder -= coin
            
    return selected, remainder
        
    

def optimal_change(coins: List[int], amount: int) -> Optional[List[int]]:
    """
    Solución óptima mediante programación dinámica para el problema del cambio de monedas.
    Determina el menor número de monedas necesario para obtener la cantidad objetivo.
    """
    if amount == 0:
        return []
    
    n = len(coins)
    # Ordenamos las monedas, para que en caso de empate se prioricen las monedas más grandes.
    sorted_coins = sorted(coins)
    
    # Matriz de estados, inicializada con infinitos
    D = [[float('inf')] * (amount + 1) for _ in range(n + 1)]
    
    # Casos base (columna del cero)
    for i in range(n + 1):
        D[i][0] = 0
        
    # Rellenar la matriz de programación dinámica
    for i in range(1, n + 1):
        c_i = sorted_coins[i - 1]  # Valor de la moneda en la fila i
        for a in range(1, amount + 1):
            if a < c_i:
                # No cabe la moneda: copiar solución de la fila superior
                D[i][a] = D[i - 1][a]
            else:
                # Mínimo entre no usar la moneda i y usar al menos una moneda i
                D[i][a] = min(D[i - 1][a], 1 + D[i][a - c_i])
                
    # Si la casilla final sigue siendo infinito, no es posible formar la cantidad
    if D[n][amount] == float('inf'):
        return None
        
    # Reconstrucción del resultado
    selected = []
    i = n
    a = amount
    
    while a > 0:
        c_i = sorted_coins[i - 1]
        # Comprobar si se eligió la Opción B (usar la moneda c_i)
        if a >= c_i and D[i][a] == 1 + D[i][a - c_i]:
            selected.append(c_i)
            a -= c_i  # Restar el valor pagado
        else:
            i -= 1    # No se usó esta moneda: subir a la fila superior
            
    return selected

def compare_change(coins: List[int], max_amount: int) -> Dict[str, List[int]]:
    """
    Evalúa todas las cantidades entre 1 y max_amount, clasifica cada cantidad en
    'optimal', 'suboptimal', 'greedy_failed' o 'impossible'.
    """
    pass

# =============================================================================
# II. Selección de actividades
# =============================================================================

def activity_selection(activities: List[Tuple[str, int, int]]) -> List[Tuple[str, int, int]]:
    """
    Selecciona el máximo número posible de actividades compatibles.
    Ordena por tiempo de finalización ascendente, y en caso de empate por inicio e identificador.
    """
    pass

def generate_activities(n: int, seed: int = 42) -> List[Tuple[str, int, int]]:
    """
    Genera n actividades aleatorias reproducibles.
    start en [0, 10000], duration en [1, 100], end = start + duration.
    """
    pass

# =============================================================================
# III. Planificación de tareas con fechas límite
# =============================================================================

def job_scheduling(jobs: List[Tuple[str, int, int]]) -> Tuple[List[Optional[Tuple[str, int, int]]], int]:
    """
    Planificación de tareas de duración unitaria con fecha límite (deadline).
    Devuelve la secuencia de tareas asignadas (con None para intervalos vacíos) y el beneficio total.
    """
    pass

def generate_jobs(n: int, seed: int = 42) -> List[Tuple[str, int, int]]:
    """
    Genera n tareas aleatorias con fecha límite reproducibles.
    profit en [1, 1000], deadline en [1, max(1, n // 10)].
    """
    pass