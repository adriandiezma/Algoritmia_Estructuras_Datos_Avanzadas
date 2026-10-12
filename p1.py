import time # Para la función time_measure. Entender código dado.
import matplotlib.pyplot as plt # Para imprimir gráficas. Entender código dado.
import random # Puede usarse random.randint(n, m) para generar listas aleatorias de enteros en las funciones dataprep.
import numpy as np 

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

    for _ in range(n):
        while(True):
            value = random.randint(1, 10 * n)
            data_list.append(value)
            if(has_sum_pair((data_list, target)) == False):
                break
            else:
                data_list.pop()
            

    return (data_list, target)

def dataprep_rle(n):
    """Genera una lista con rachas repetidas de dimensión n.
    Devuelve una lista.
    """
    data_list = []
    bucle = True

    while(bucle):
        value = random.randint(1, 10 * n)
        racha = random.randint(1, n / 5)
        for _ in range(racha):
            data_list.append(value)
            if len(data_list) == n:
                bucle = False
                break
    
    return data_list

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

    if lst == []:
        return []
    
    lst_final = []
    count = 0
    aux = lst[0]

    for elem in lst:
        if elem != aux:
            lst_final = lst_final + [(aux, count)]
            count = 1
            aux = elem
        else:
            count += 1

    lst_final = lst_final + [(aux, count)]

    return lst_final
        
# I.B.2 RLE Optimized / Óptimo
def rle_encode_optimized(lst):
    """Codificación RLE optimizada usando append in-place."""
    pass

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
            filename, format=filename.split(".")[-1], dpi=300
        )  #

    plt.show()  # Muestra la figura

#Nlst = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
#res = time_measure(has_sum_pair, dataprep_sum_pair_miss, Nlst)
#print(res)
#plot_single_curve(Nlst, res)


# II: Conjuntos Disjuntos

def init_cd(n: int)-> np.ndarray:
    """Genera un array de n enteros con todas sus posiciones inicializadas a -1"""
    p_cd = np.full(n, -1, dtype = int)
    return p_cd

def find1(ind: int, p_cd: np.ndarray)-> int:
    """devuelve el representante del índice ind en el conjunto disjunto almacenado en p_cd realizando compresión de caminos"""
    for _ in range(len(p_cd)):
        if(p_cd[ind] == -1):
            return ind
        else:
            ind = p_cd[ind]
    
    return -2

def union(rep_1: int, rep_2: int, p_cd: np.ndarray)-> int:
    """Devuelve el representante del conjunto obtenido como la unión por rangos de los representados 
    por los índices rep_1, rep_2 en el conjunto disjunto almacenado en el array p_cd.
    """
    if rep_1 != rep_2 and p_cd[rep_1] < 0 and p[rep_2] < 0:
        if p_cd[rep_1] < p_cd[rep_2]: # El representante rep_1 es de mayor dimensión que el representante rep_2 -> rep_1 el padre
            p_cd[rep_2] = rep_1
            return rep_1
        else: # El representante rep_2 es de mayor o igual dimensión que el representante rep_1 -> rep_2 el padre
            if p_cd[rep_1] == p_cd[rep_2]:
                p_cd[rep2] = p_cd[rep_2] -1
            p_cd[rep_1] = rep_2
            return rep_2

    return -2

def find(ind: int, p_cd: np.ndarray)-> int:
    """devuelve el representante del índice ind en el conjunto disjunto almacenado en p_cd realizando compresión de caminos"""
    if(p_cd[ind] < 0):
        return ind
    else:
        padre = p_cd[ind]
        rep = find(padre, p_cd)
    p_cd[ind] = rep 
    return rep