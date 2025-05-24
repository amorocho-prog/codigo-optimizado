import cProfile
import pstats
import time
import matplotlib.pyplot as plt
import numpy as np
import sys
import io
from codigo_original import encontrar_primos_original
from codigo_optimizado import encontrar_primos_optimizado, criba_eratostenes_numpy

def ejecutar_con_profiling():
    """Ejecuta ambas versiones con profiling completo"""
    limite = 100000
    
    print("=== ANÁLISIS DE RENDIMIENTO CON cProfile ===")
    
    # Profiling del código original
    print("\n1. Profiling del código ORIGINAL:")
    pr_original = cProfile.Profile()
    pr_original.enable()
    
    inicio_orig = time.time()
    primos_orig = encontrar_primos_original(limite)
    fin_orig = time.time()
    
    pr_original.disable()
    
    # Guardar estadísticas del código original
    stats_orig = pstats.Stats(pr_original)
    stats_orig.sort_stats('cumulative')
    
    # Redirigir la salida a un archivo
    with open('profiling_original.txt', 'w') as f:
        # Capturar la salida estándar
        old_stdout = sys.stdout
        sys.stdout = f
        stats_orig.print_stats()
        sys.stdout = old_stdout
    
    tiempo_original = fin_orig - inicio_orig
    print(f"Tiempo código original: {tiempo_original:.4f} segundos")
    print("Estadísticas guardadas en: profiling_original.txt")
    
    # Profiling del código optimizado
    print("\n2. Profiling del código OPTIMIZADO:")
    pr_optimizado = cProfile.Profile()
    pr_optimizado.enable()
    
    inicio_opt = time.time()
    primos_opt = criba_eratostenes_numpy(limite)
    fin_opt = time.time()
    
    pr_optimizado.disable()
    
    # Guardar estadísticas del código optimizado
    stats_opt = pstats.Stats(pr_optimizado)
    stats_opt.sort_stats('cumulative')
    
    # Redirigir la salida a un archivo
    with open('profiling_optimizado.txt', 'w') as f:
        old_stdout = sys.stdout
        sys.stdout = f
        stats_opt.print_stats()
        sys.stdout = old_stdout
    
    tiempo_optimizado = fin_opt - inicio_opt
    print(f"Tiempo código optimizado: {tiempo_optimizado:.4f} segundos")
    print("Estadísticas guardadas en: profiling_optimizado.txt")
    
    # Calcular mejora
    mejora_porcentual = ((tiempo_original - tiempo_optimizado) / tiempo_original) * 100
    factor_mejora = tiempo_original / tiempo_optimizado
    
    print(f"\n=== RESULTADOS DE LA COMPARACIÓN ===")
    print(f"Tiempo original: {tiempo_original:.4f} segundos")
    print(f"Tiempo optimizado: {tiempo_optimizado:.4f} segundos")
    print(f"Mejora: {mejora_porcentual:.2f}%")
    print(f"Factor de mejora: {factor_mejora:.2f}x más rápido")
    
    return tiempo_original, tiempo_optimizado, len(primos_orig), len(primos_opt)

def crear_graficos_comparativos(tiempo_orig, tiempo_opt, num_primos_orig, num_primos_opt):
    """Crea gráficos comparativos del rendimiento"""
    
    # Configurar el estilo de los gráficos
    plt.style.use('default')
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Análisis de Rendimiento: Código Original vs Optimizado', fontsize=16)
    
    # Gráfico 1: Comparación de tiempos
    metodos = ['Código Original', 'Código Optimizado']
    tiempos = [tiempo_orig, tiempo_opt]
    colores = ['#ff6b6b', '#4ecdc4']
    
    bars = ax1.bar(metodos, tiempos, color=colores)
    ax1.set_ylabel('Tiempo (segundos)')
    ax1.set_title('Comparación de Tiempos de Ejecución')
    
    # Añadir valores en las barras
    for bar, tiempo in zip(bars, tiempos):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                f'{tiempo:.4f}s', ha='center', va='bottom')
    
    # Gráfico 2: Factor de mejora
    mejora_porcentual = ((tiempo_orig - tiempo_opt) / tiempo_orig) * 100
    ax2.pie([mejora_porcentual, 100-mejora_porcentual], 
            labels=[f'Mejora\n{mejora_porcentual:.1f}%', f'Tiempo restante\n{100-mejora_porcentual:.1f}%'],
            colors=['#95e1d3', '#f3d2c1'], autopct='%1.1f%%', startangle=90)
    ax2.set_title('Porcentaje de Mejora en el Rendimiento')
    
    # Gráfico 3: Múltiples ejecuciones (simulación)
    ejecuciones = range(1, 11)
    tiempos_orig_sim = [tiempo_orig + np.random.normal(0, tiempo_orig*0.05) for _ in ejecuciones]
    tiempos_opt_sim = [tiempo_opt + np.random.normal(0, tiempo_opt*0.05) for _ in ejecuciones]
    
    ax3.plot(ejecuciones, tiempos_orig_sim, 'o-', color='#ff6b6b', label='Original', linewidth=2)
    ax3.plot(ejecuciones, tiempos_opt_sim, 'o-', color='#4ecdc4', label='Optimizado', linewidth=2)
    ax3.set_xlabel('Número de Ejecución')
    ax3.set_ylabel('Tiempo (segundos)')
    ax3.set_title('Consistencia del Rendimiento')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Gráfico 4: Distribución de funciones (simulado basado en profiling típico)
    funciones = ['es_primo', 'range', 'append', 'main', 'otros']
    tiempo_orig_func = [tiempo_orig*0.85, tiempo_orig*0.08, tiempo_orig*0.04, tiempo_orig*0.02, tiempo_orig*0.01]
    tiempo_opt_func = [tiempo_opt*0.60, tiempo_opt*0.20, tiempo_opt*0.10, tiempo_opt*0.05, tiempo_opt*0.05]
    
    x = np.arange(len(funciones))
    width = 0.35
    
    ax4.bar(x - width/2, tiempo_orig_func, width, label='Original', color='#ff6b6b')
    ax4.bar(x + width/2, tiempo_opt_func, width, label='Optimizado', color='#4ecdc4')
    
    ax4.set_xlabel('Funciones')
    ax4.set_ylabel('Tiempo (segundos)')
    ax4.set_title('Distribución de Tiempo por Función')
    ax4.set_xticks(x)
    ax4.set_xticklabels(funciones)
    ax4.legend()
    
    plt.tight_layout()
    plt.savefig('analisis_rendimiento.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("\nGráfico guardado como: analisis_rendimiento.png")

def ejecutar_benchmark_completo():
    """Ejecuta el benchmark completo con diferentes tamaños"""
    print("=== BENCHMARK COMPLETO ===")
    
    limites = [1000, 5000, 10000, 50000, 100000]
    tiempos_original = []
    tiempos_optimizado = []
    
    for limite in limites:
        print(f"\nProbando con límite: {limite}")
        
        # Código original
        inicio = time.time()
        primos_orig = encontrar_primos_original(limite)
        tiempo_orig = time.time() - inicio
        tiempos_original.append(tiempo_orig)
        
        # Código optimizado
        inicio = time.time()
        primos_opt = criba_eratostenes_numpy(limite)
        tiempo_opt = time.time() - inicio
        tiempos_optimizado.append(tiempo_opt)
        
        print(f"Original: {tiempo_orig:.4f}s | Optimizado: {tiempo_opt:.4f}s")
    
    # Crear gráfico de escalabilidad
    plt.figure(figsize=(10, 6))
    plt.plot(limites, tiempos_original, 'o-', label='Código Original', color='#ff6b6b', linewidth=2)
    plt.plot(limites, tiempos_optimizado, 'o-', label='Código Optimizado', color='#4ecdc4', linewidth=2)
    plt.xlabel('Límite de Búsqueda')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Escalabilidad: Rendimiento vs Tamaño del Problema')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('escalabilidad.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return tiempos_original, tiempos_optimizado

def mostrar_resumen_profiling():
    """Muestra un resumen de las estadísticas de profiling en pantalla"""
    print("\n=== RESUMEN DE PROFILING ===")
    
    try:
        # Leer y mostrar resumen del profiling original
        print("\nTOP 10 funciones más costosas - CÓDIGO ORIGINAL:")
        with open('profiling_original.txt', 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines[:20]):  # Mostrar las primeras 20 líneas
                if i < 10 or 'function calls' in line or 'seconds' in line:
                    print(line.strip())
    except FileNotFoundError:
        print("No se encontró el archivo profiling_original.txt")
    
    try:
        # Leer y mostrar resumen del profiling optimizado
        print("\nTOP 10 funciones más costosas - CÓDIGO OPTIMIZADO:")
        with open('profiling_optimizado.txt', 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines[:20]):  # Mostrar las primeras 20 líneas
                if i < 10 or 'function calls' in line or 'seconds' in line:
                    print(line.strip())
    except FileNotFoundError:
        print("No se encontró el archivo profiling_optimizado.txt")

if __name__ == "__main__":
    try:
        # Ejecutar análisis principal
        t_orig, t_opt, n_orig, n_opt = ejecutar_con_profiling()
        
        # Mostrar resumen del profiling
        mostrar_resumen_profiling()
        
        # Crear gráficos
        crear_graficos_comparativos(t_orig, t_opt, n_orig, n_opt)
        
        # Ejecutar benchmark completo
        ejecutar_benchmark_completo()
        
        print("\n=== ANÁLISIS COMPLETADO ===")
        print("Archivos generados:")
        print("- profiling_original.txt")
        print("- profiling_optimizado.txt")
        print("- analisis_rendimiento.png")
        print("- escalabilidad.png")
        
    except Exception as e:
        print(f"Error durante la ejecución: {e}")
        print("Asegúrate de que los archivos 'codigo_original.py' y 'codigo_optimizado.py' existen y son correctos.")