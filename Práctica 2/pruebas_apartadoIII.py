import time
import matplotlib.pyplot as plt
from p2 import job_scheduling, generate_jobs

def hacer_graficas():
    tamanos = [100, 500, 1000, 5000]
    

    tiempos = []
    beneficios = []
    porcentajes = []

    for n in tamanos:
        jobs = generate_jobs(n)
        
        # --- DATOS PARA GRÁFICA 1 (Tiempo) ---
        inicio = time.perf_counter()
        schedule, total_profit = job_scheduling(jobs)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
        
        # --- DATOS PARA GRÁFICA 2 (Beneficio) ---
        beneficios.append(total_profit)
        
        # --- DATOS PARA GRÁFICA 3 (Porcentaje) ---
        # Contamos cuántos huecos en el schedule NO son None
        tareas_asignadas = sum(1 for slot in schedule if slot is not None)
        porcentaje = (tareas_asignadas / n) * 100
        porcentajes.append(porcentaje)

    # --- Generar y guardar Gráfica 1 ---
    plt.figure(figsize=(8, 5))
    plt.plot(tamanos, tiempos, marker='o', color='blue')
    plt.title('Gráfica 1: Tamaño frente al tiempo')
    plt.xlabel('Número de tareas (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('grafica_1_tiempo.png')
    plt.close()

    # --- Generar y guardar Gráfica 2 ---
    plt.figure(figsize=(8, 5))
    plt.plot(tamanos, beneficios, marker='o', color='green')
    plt.title('Gráfica 2: Tamaño frente al beneficio total')
    plt.xlabel('Número de tareas (n)')
    plt.ylabel('Beneficio Total')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('grafica_2_beneficio.png')
    plt.close()

    # --- Generar y guardar Gráfica 3 ---
    plt.figure(figsize=(8, 5))
    plt.plot(tamanos, porcentajes, marker='o', color='red')
    plt.title('Gráfica 3: Tamaño frente al % seleccionado')
    plt.xlabel('Número de tareas (n)')
    plt.ylabel('Tareas seleccionadas (%)')
    plt.ylim(0, 100)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('grafica_3_porcentaje.png')
    plt.close()

    print("Las tres gráficas se han guardado como PNGs independientes:")
    print("- grafica_1_tiempo.png")
    print("- grafica_2_beneficio.png")
    print("- grafica_3_porcentaje.png")

if __name__ == "__main__":
    hacer_graficas()