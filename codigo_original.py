import time

def es_primo(n):
    """Función básica para verificar si un número es primo (sin optimizaciones)"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def encontrar_primos_original(limite):
    """Encuentra todos los números primos hasta el límite dado"""
    primos = []
    for num in range(2, limite + 1):
        if es_primo(num):
            primos.append(num)
    return primos

if __name__ == "__main__":
    print("=== CÓDIGO ORIGINAL - BÚSQUEDA DE NÚMEROS PRIMOS ===")
    print("Buscando números primos del 1 al 100,000...")
    
    # Medir tiempo de ejecución
    inicio = time.time()
    primos_encontrados = encontrar_primos_original(100000)
    fin = time.time()
    
    tiempo_total = fin - inicio
    
    print(f"Números primos encontrados: {len(primos_encontrados)}")
    print(f"Primeros 10 primos: {primos_encontrados[:10]}")
    print(f"Últimos 10 primos: {primos_encontrados[-10:]}")
    print(f"Tiempo de ejecución: {tiempo_total:.4f} segundos")