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
    pass

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