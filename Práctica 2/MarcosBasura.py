
def greedy_change(coins: List[int], amount: int) -> Tuple[List[int], int]:
    """
    Estrategia codiciosa para el problema del cambio de monedas.
    Selecciona en cada paso la moneda de mayor valor que no supere la cantidad restante.
    """
    if not coins:
        return ([], amount)

    selected = []

    # Primer caso: se empieza a buscar desde el mayor valor en la lista.
    current_max = max(coins)

    # Mientras haya dinero, se va restando la cantidad máxima en cada momento (que no sobrepase el dinero disponible)
    while amount > 0 and current_max > 0:
        if current_max <= amount:
            amount -= current_max
            selected.append(current_max)

        # Cambio de moneda: se busca la máxima disponible para la cantidad de dinero restante
        else:
            current_max = 0
            for val in coins:
                if (val > current_max and val <= amount):
                    current_max = val
            # Si current_max = 0 aquí, se ha terminado y se calcula el resto.

    return (selected, amount)