
from typing import List, Tuple
import random

def activity_selection(activities: List[Tuple[str, int, int]]) -> List[Tuple[str, int, int]]:
    """
    Selecciona el máximo número posible de actividades compatibles.
    Ordena por tiempo de finalización ascendente, y en caso de empate por inicio e identificador.
    """
    if not activities:
        return []
    
    # Ordenación por (end, start, identifier) creando una lista nueva
    sorted_activities = sorted(activities, key=lambda act: (act[2], act[1], act[0]))

    # Se incluye la primera actividad, y se guarda su finalización para empezar a comparar
    selected = [sorted_activities[0]]
    last_end = sorted_activities[0][2]

    # Se añade la tupla que empiece después de que acabe la última tarea incluida (o que empiece en el mismo instante)
    for act in sorted_activities[1:]:
        start = act[1]
        if start >= last_end:
            selected.append(act)
            last_end = act[2]

    # Se devuelve la lista óptima, sin modificar la lista original
    return selected

def generate_activities(n: int, seed: int = 42) -> List[Tuple[str, int, int]]:
    """
    Genera n actividades aleatorias reproducibles.
    start en [0, 10000], duration en [1, 100], end = start + duration.
    """
    random.seed(seed)
    activities = []
    
    for i in range(n):
        start = random.randint(0, 10000)
        activities.append(("A"+str(i), start, start + random.randint(1, 100)))
        
    return activities

"""activities = [("A",1,4), ("B",3,5), ("C",0,6), ("D",5,7), ("E",8,9), ("F",7,9)]
print(activity_selection(activities))"""

print(generate_activities(10, ))