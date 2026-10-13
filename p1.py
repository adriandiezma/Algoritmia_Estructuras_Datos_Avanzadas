import time # Para la función time_measure. Entender código dado.
import matplotlib.pyplot as plt # Para imprimir gráficas. Entender código dado.
import random # Puede usarse random.randint(n, m) para generar listas aleatorias de enteros en las funciones dataprep.
import numpy as np 


# Funciones DATAPREP

def dataprep_sum_pair_hit(n):
    """Genera un caso donde SÍ existe un par que suma target.
    Devuelve una tupla (lista, target)
    """
    data_list = []
    target = random.randint(2, 2 * 10 * n)

    for _ in range(n-1):
        value = random.randint(1, 10 * n)
        data_list.append(value)
    sum_number = target - value
    data_list.append(sum_number)  

    random.shuffle(data_list)  
    
    return (data_list, target)


def dataprep_sum_pair_miss(n):
    """Genera un caso donde NO existe ningún par (Caso peor).
    Devuelve una tupla (lista, target)
    """
    data_list = []
    target = random.randint(2, 2 * 10 * n)
    vistos = set()

    for _ in range(n):
        # Queremos ver si exste un elemento "search" en el set que sumado 
        # con "value" dé "target" -> value + search = target -> search = target - value
        while(True):
            value = random.randint(1, 10 * n)
            data_list.append(value)
            search = target - value

            if(search not in vistos):
                vistos.add(value)
                break
            else:
                data_list.pop()
            

    return (data_list, target)


def dataprep_rle(n):
    """Genera una lista con rachas repetidas de dimensión n.
    Devuelve una lista.
    """
    data_list = []
    
    while len(data_list) < n:
        val = random.randint(1, 100)

        # Elegimos cuántas veces repetir el valor.
        racha = random.randint(2, 5)

        # Añadimos "racha" veces el elemento "val" al final de la lista.
        for _ in range(racha):
            data_list.append(val)

    # Recortamos la lista a tamaño n por si nos pasamos de elementos.
    return data_list[:n]


# I.A.1 Medición de tiempos de ejecución
def time_measure(f, dataprep, Nlist, Nrep=1000, Nstat=100):
    """Mide la media y varianza del tiempo de ejecución de la función f
    para cada tamaño n presente en Nlist.
    """
    res = []
    for n in Nlist:
        partial = []
        for _ in range(Nstat):
            data = dataprep(n)
            t1 = time.perf_counter()
            for _ in range(Nrep):
                f(data)
            t2 = time.perf_counter()
            t_elem = (t2 - t1) / float(Nrep)
            partial.append(t_elem)

        mean_val = sum(partial) / float(Nstat)
        var_val = sum((x - mean_val) ** 2 for x in partial) / float(Nstat)
        res.append((mean_val, var_val))
    return res


# I.A.2 Búsqueda de duplicados manteniendo orden de aparición
def find_duplicates(lst):
    """Devuelve los elementos que aparecen más de una vez en lst,
    preservando el orden de su primera repetición y sin duplicados.
    """
    vistos = set()
    duplicados_set = set()
    duplicados = []
    
    for ele in lst:
        if ele in vistos:
            if ele not in duplicados_set:
                duplicados_set.add(ele)
                duplicados.append(ele)
        else:
            vistos.add(ele)

    return duplicados


# I.A.3 Búsqueda de par que suma target con complejidad O(n)
def has_sum_pair(par):
    """Dada una tupla (lst, target), devuelve True si existen dos elementos
    distintos en lst que sumen target; de lo contrario devuelve False.
    """
    lst, target = par
    
    vistos = set()

    # Queremos ver si exste un elemento "search" en el set que sumado con "elem" dé "target" -> elem + search = target -> search = target - elem
    for elem in lst:
        search = target - elem
        if search in vistos: 
            return True
        vistos.add(elem)
    
    return False


# I.B.1 RLE Naive / Ingenuo
def rle_encode_naive(lst):
    """Codificación RLE utilizando operador + concatenador de listas."""
    if not lst:
        return []
    
    lst_final = []
    count = 1
    # Guardo el primer valor de la lista para empezar a comparar a partir del 2º elemento (posición 1).
    aux = lst[0] 

    # Se empieza desde la segunda posición de la lista.
    for i in range(1, len(lst)):
        elem = lst[i]
        if elem == aux:
            count += 1

        else:
            lst_final = lst_final + [(aux, count)]
            count = 1
            aux = elem

    # Añadimos el último caso tras salir del bucle.
    lst_final = lst_final + [(aux, count)]

    return lst_final


# I.B.2 RLE Optimized / Óptimo
def rle_encode_optimized(lst):
    """Codificación RLE optimizada usando append in-place."""

    if not lst:
        return []

    lst_final = []
    
    # Guardo el primer valor de la lista para empezar a comparar a partir del 2º elemento (posición 1).
    aux = lst[0] 
    count = 1

    # Se empieza desde la segunda posición de la lista.
    for i in range(1, len(lst)):
        elem = lst[i]
        if elem == aux:
            count += 1

        else:
            lst_final.append((aux, count))
            aux = elem
            count = 1

    # Añadimos el último caso tras salir del bucle.
    lst_final.append((aux, count))

    return lst_final

# Función auxiliar para generar una gráfica de una serie de datos.
def plot_single_curve(
    x,
    y,
    title="Gráfica de Datos",
    xlabel="Eje X",
    ylabel="Eje Y",
    label=None,
    style="o-",
    color="b",
    grid=True,
    filename=None,
    figsize=(8, 5),
):
    """Genera y muestra/guarda una gráfica limpia para una única serie de datos."""
    plt.figure(figsize=figsize)  # Crea la figura con el tamaño indicado

    # Dibuja la curva
    plt.plot(x, y, style, color=color, label=label)

    # Personalización básica de ejes y título
    plt.title(title)  # Asigna el título
    plt.xlabel(xlabel)  # Etiqueta X
    plt.ylabel(ylabel)  # Etiqueta Y

    if grid:
        plt.grid(True, linestyle="--", alpha=0.6)

    if label:
        plt.legend(
            loc="best"
        )  # Muestra la leyenda si se definió una etiqueta

    plt.tight_layout()

    # Guarda la gráfica en un fichero si se especifica un nombre
    if filename:
        plt.savefig(
            filename, format=filename.split(".")[-1], dpi=1200
        )  #

    plt.show()  # Muestra la figura


# II: CONJUNTOS DISJUNTOS

# II.A.1
def init_cd(n: int)-> np.ndarray:
    """Genera un array de n enteros con todas sus posiciones inicializadas a -1."""
    p_cd = np.full(n, -1, dtype = int)
    return p_cd


# II.A.2
def union(rep_1: int, rep_2: int, p_cd: np.ndarray)-> int:
    """Devuelve el representante del conjunto obtenido como la unión por rangos de los representados 
    por los índices rep_1, rep_2 en el conjunto disjunto almacenado en el array p_cd.
    """
    if p_cd[rep_1] >= 0:
        return p_cd[rep_1]
    if p_cd[rep_2] >= 0:
        return p_cd[rep_2]

    if rep_1 != rep_2:
        if p_cd[rep_1] < p_cd[rep_2]: # El representante rep_1 es de mayor dimensión que el representante rep_2 -> rep_1 el padre
            p_cd[rep_2] = rep_1
            return rep_1
        else: # El representante rep_2 es de mayor o igual dimensión que el representante rep_1 -> rep_2 el padre
            if p_cd[rep_1] == p_cd[rep_2]:
                p_cd[rep_2] = p_cd[rep_2] -1
            p_cd[rep_1] = rep_2
            return rep_2

    return rep_1


# II.A.3
def find(ind: int, p_cd: np.ndarray)-> int:
    """Devuelve el representante del índice ind en el conjunto disjunto almacenado en p_cd realizando compresión de caminos."""
    if(p_cd[ind] < 0):
        return ind
    else:
        padre = p_cd[ind]
        rep = find(padre, p_cd)
    p_cd[ind] = rep 
    return rep


# II.A.4
def cd_2_dict(p_cd: np.ndarray) -> dict:
    """ Devuelve un diccionario cuyas claves son los
        representantes de los subconjuntos del CD y donde el valor de la clave u del dict es una
        lista con los miembros del subconjunto representado por u."""
    res = {}
    n = len(p_cd)

    for i in range(n):
        rep = find(i, p_cd)
        if rep not in res:
            res[rep] = []

        res[rep].append(i)

    return res 


# II.B.1
def ccs(n: int, l: list)-> dict:
    """Recibe un grafo no dirigido y devuelve sus componentes conexas."""
    p_cd = init_cd(n)
    
    for u, v in l:
        rep_u = find(u, p_cd)
        rep_v = find(v, p_cd)
        if rep_u != rep_v:
            union(rep_u, rep_v, p_cd)
            
    return cd_2_dict(p_cd)
