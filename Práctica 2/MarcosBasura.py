from typing import List, Tuple, Dict, Optional
import random

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

    lst_optimal = []
    lst_suboptimal = []
    lst_greedy_failed = []
    lst_impossible = []

    for i in range(1, max_amount+1):
        greedy = greedy_change(coins, i)
        optimal = optimal_change(coins, i)

        # Caso "impossible"
        if optimal is None:
            lst_impossible.append(i)

        else:    
            remainder_greedy = greedy[1]
            n_optimal = len(optimal)

            # Greedy exacto (optimal/suboptimal)
            if remainder_greedy == 0:
                # Caso suboptimal
                if len(greedy[0]) > n_optimal:
                    lst_suboptimal.append(i)
                # Caso optimal
                else:
                    lst_optimal.append(i)

            # Greedy inexacto (greedy_failed)       
            else:
                lst_greedy_failed.append(i)

    return {"optimal": lst_optimal, "suboptimal": lst_suboptimal, "greedy_failed": lst_greedy_failed, "impossible": lst_impossible}

import time
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. GENERACIÓN DE LA TABLA Y ESTADÍSTICAS
# ---------------------------------------------------------
def generar_estadisticas_sistemas(sistemas, max_amount=500):
    print("="*65)
    print(f"{'SISTEMA DE MONEDAS':<35} | {'OPT':<5} | {'SUB':<5} | {'FAIL':<4} | {'IMP':<3}")
    print("="*65)
    
    for coins in sistemas:
        # Reutilizamos tu función compare_change
        res = compare_change(coins, max_amount)
        
        # Conteos
        n_opt = len(res['optimal'])
        n_sub = len(res['suboptimal'])
        n_fail = len(res['greedy_failed'])
        n_imp = len(res['impossible'])
        total = max_amount
        
        # Porcentajes
        p_opt = (n_opt / total) * 100
        p_sub = (n_sub / total) * 100
        p_fail = (n_fail / total) * 100
        p_imp = (n_imp / total) * 100
        
        # Imprimir fila de la tabla
        sistema_str = str(coins)
            
        print(f"{sistema_str:<35} | {p_opt:>4.1f}% | {p_sub:>4.1f}% | {p_fail:>3.1f}% | {p_imp:>2.1f}%")
        
        # Imprimir desglose para copiar en la memoria
        print(f"  - Optimal:       {n_opt} ({p_opt:.1f}%)")
        print(f"  - Suboptimal:    {n_sub} ({p_sub:.1f}%)")
        print(f"  - Greedy Failed: {n_fail} ({p_fail:.1f}%)")
        print(f"  - Impossible:    {n_imp} ({p_imp:.1f}%)\n")

# ---------------------------------------------------------
# 2. ADAPTACIÓN DE LAS FUNCIONES DE TIEMPO Y GRÁFICAS
# ---------------------------------------------------------
import time
import gc

def time_measure_coin(f, coins, amount_list, Nrep=100, Nstat=10):
    """
    Mide el tiempo mínimo de ejecución desactivando el recolector de basura
    para evitar picos de tiempo irreales.
    """
    res_min = []
    
    for amount in amount_list:
        # 1. Warm-up: Ejecutar una vez sin medir para cargar en caché
        f(coins, amount)
        
        partial = []
        for _ in range(Nstat):
            # 2. Desactivar recolector de basura
            gc.disable()
            
            t1 = time.perf_counter()
            for _ in range(Nrep):
                f(coins, amount)
            t2 = time.perf_counter()
            
            # 3. Reactivar recolector de basura
            gc.enable()
            
            partial.append((t2 - t1) / float(Nrep))

        # 4. Quedarse con la mejor ejecución (el tiempo mínimo)
        best_time = min(partial)
        res_min.append(best_time)
        
    return res_min

def plot_comparison_curves(x, y_greedy, y_optimal, title, filename=None):
    """Grafica ambas curvas en el mismo plano para comparar fácilmente."""
    plt.figure(figsize=(8, 5))
    
    # Dibujar ambas curvas
    plt.plot(x, y_greedy, 'o-', color='b', label='Greedy (Codicioso)')
    plt.plot(x, y_optimal, 's-', color='r', label='Optimal (Dinámica)')

    plt.title(title)
    plt.xlabel("Cantidad Objetivo (amount)")
    plt.ylabel("Tiempo Promedio de Ejecución (s)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(loc="best")
    plt.tight_layout()

    if filename:
        plt.savefig(filename, dpi=300)
    plt.close()

# ---------------------------------------------------------
# 3. EJECUCIÓN DEL EXPERIMENTO
# ---------------------------------------------------------
"""
UNA SOLA TABLA, CON UN SISTEMA MONETARIO ELEGIDO
if __name__ == "__main__":
    sistemas = [
        [200, 100, 50, 20, 10, 5, 2, 1],
        [10, 5, 2, 1],
        [25, 10, 4, 1],
        [4, 3, 1]
    ]
    
    # 1. Mostrar tabla y porcentajes en consola
    generar_estadisticas_sistemas(sistemas, 500)
    
    # 2. Medir y graficar tiempos (usamos saltos para no sobrecargar el PC)
    cantidades_test = list(range(10, 501, 20)) # [10, 30, 50 ... 490]
    
    # Elegimos el tercer sistema para la gráfica de ejemplo
    monedas_test = [25, 10, 4, 1]
    
    print("Midiendo tiempos de Greedy...")
    tiempos_greedy = time_measure_coin(greedy_change, monedas_test, cantidades_test)
    
    print("Midiendo tiempos de DP (puede tardar unos segundos)...")
    tiempos_dp = time_measure_coin(optimal_change, monedas_test, cantidades_test)
    
    # Generar la gráfica comparativa
    plot_comparison_curves(cantidades_test, tiempos_greedy, tiempos_dp, 
                           title="Tiempos de Ejecución: Greedy vs Dinámica",
                           filename="comparativa_tiempos.png")"""

"""UNA TABLA PARA CADA SISTEMA MONETARIO DEL EJEMPLO"""
if __name__ == "__main__":
    sistemas = [
        [200, 100, 50, 20, 10, 5, 2, 1],
        [10, 5, 2, 1],
        [25, 10, 4, 1],
        [4, 3, 1]
    ]
    
    # 1. Mostrar tabla y porcentajes en consola
    generar_estadisticas_sistemas(sistemas, 500)
    
    # 2. Medir y graficar tiempos para CADA sistema
    cantidades_test = list(range(1, 500, 20))
    cantidades_test.append(500)
    
    for i, monedas_test in enumerate(sistemas, start=1):
        print(f"\n--- Procesando Gráfica para el Sistema {i}: {monedas_test} ---")
        
        print("Midiendo tiempos de Greedy...")
        tiempos_greedy = time_measure_coin(greedy_change, monedas_test, cantidades_test)
        
        print("Midiendo tiempos de DP (puede tardar)...")
        tiempos_dp = time_measure_coin(optimal_change, monedas_test, cantidades_test)
        
        # Generar nombres dinámicos para evitar que se sobrescriban
        titulo = f"Tiempos de Ejecución: Greedy vs Dinámica\nSistema: {monedas_test}"
        nombre_archivo = f"comparativa_tiempos_sistema_{i}.png"
        
        # Generar y guardar la gráfica comparativa
        plot_comparison_curves(cantidades_test, tiempos_greedy, tiempos_dp, 
                               title=titulo,
                               filename=nombre_archivo)
        print(f"-> Gráfica guardada como: {nombre_archivo}")