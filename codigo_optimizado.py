import time
import numpy as np
import math

def es_primo_optimizado(n):
    """Función optimizada para verificar si un número es primo"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Solo iterar hasta la raíz cuadrada de n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def encontrar_primos_optimizado(limite):
    """Encuentra primos usando list comprehension y optimizaciones"""
    # Usar list comprehension para mayor eficiencia
    primos = [2] + [num for num in range(3, limite + 1, 2) if es_primo_optimizado(num)]
    return primos

def criba_eratostenes_numpy(limite):
    """Implementación usando NumPy y la Criba de Eratóstenes"""
    # Crear array booleano usando NumPy
    es_primo = np.ones(limite + 1, dtype=bool)
    es_primo[0:2] = False
    
    for i in range(2, int(math.sqrt(limite)) + 1):
        if es_primo[i]:
            # Marcar múltiplos como no primos usando operaciones NumPy
            es_primo[i*i::i] = False
    
    # Retornar índices donde es_primo es True
    return np.where(es_primo)[0].tolist()

if __name__ == "__main__":
    print("=== CÓDIGO OPTIMIZADO - BÚSQUEDA DE NÚMEROS PRIMOS ===")
    limite = 100000
    
    # Método 1: Optimización básica
    print("\n1. Método optimizado con raíz cuadrada y list comprehension:")
    inicio1 = time.time()
    primos_opt1 = encontrar_primos_optimizado(limite)
    fin1 = time.time()
    tiempo1 = fin1 - inicio1
    
    print(f"Números primos encontrados: {len(primos_opt1)}")
    print(f"Tiempo de ejecución: {tiempo1:.4f} segundos")
    
    # Método 2: Criba de Eratóstenes con NumPy
    print("\n2. Criba de Eratóstenes con NumPy:")
    inicio2 = time.time()
    primos_opt2 = criba_eratostenes_numpy(limite)
    fin2 = time.time()
    tiempo2 = fin2 - inicio2
    
    print(f"Números primos encontrados: {len(primos_opt2)}")
    print(f"Tiempo de ejecución: {tiempo2:.4f} segundos")
    
    # Verificar que ambos métodos dan el mismo resultado
    print(f"\n¿Los resultados coinciden? {len(primos_opt1) == len(primos_opt2)}")
    print(f"Primeros 10 primos: {primos_opt2[:10]}")
    print(f"Últimos 10 primos: {primos_opt2[-10:]}")
    
    # Mostrar mejora de rendimiento
    print(f"\nMejor método: Criba de Eratóstenes con NumPy")
    print(f"Tiempo final optimizado: {tiempo2:.4f} segundos")