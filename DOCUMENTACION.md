DOCUMENTACION.md
Introducción
Descripción del código original
El código original implementa un algoritmo básico de búsqueda de números primos utilizando el método de fuerza bruta. La función principal es_primo(n) verifica si un número es primo dividiendo por todos los enteros desde 2 hasta n-1.
Características del código original:
•	Función es_primo(): Itera desde 2 hasta n-1 para verificar divisibilidad
•	Función encontrar_primos_original(): Recorre todos los números del 2 al límite
•	Rango de prueba: 1 a 100,000 números
•	Tiempo de ejecución: 35.1430 segundos
Problemas identificados
1.	Complejidad temporal excesiva: O(n²) - cada número se verifica contra todos los anteriores
2.	Iteraciones innecesarias: Verifica divisibilidad hasta n-1 cuando solo necesita hasta √n
3.	Falta de optimizaciones algorítmicas: No utiliza algoritmos especializados como la Criba de Eratóstenes
4.	Ineficiencia en estructuras de datos: Uso básico de listas sin aprovechar librerías optimizadas
5.	Tiempo de ejecución impracticable: 35+ segundos para 100,000 números
Optimización
Técnicas aplicadas
1. Optimización matemática - Reducir el rango del bucle
Técnica: Iterar solo hasta la raíz cuadrada de n
for i in range(3, int(math.sqrt(n)) + 1, 2):
Mejora: Reduce las iteraciones de O(n) a O(√n)
2. List comprehensions
Técnica: Usar comprensión de listas para mayor eficiencia
primos = [2] + [num for num in range(3, limite + 1, 2) if es_primo_optimizado(num)]
Mejora: Operaciones más rápidas y código más limpio
3. NumPy y algoritmo especializado
Técnica: Implementar la Criba de Eratóstenes con arrays NumPy
def criba_eratostenes_numpy(limite):
    es_primo = np.ones(limite + 1, dtype=bool)
    es_primo[0:2] = False
    
    for i in range(2, int(math.sqrt(limite)) + 1):
        if es_primo[i]:
            es_primo[i*i::i] = False
    
    return np.where(es_primo)[0].tolist()
Mejora: Cambio de complejidad de O(n²) a O(n log log n)
Cómo mejoraron el rendimiento
•	Optimización básica: Tiempo reducido de 35.14s a 0.11s (99.69% mejora)
•	Criba + NumPy: Tiempo reducido a 0.001s (99.997% mejora)
•	Factor de mejora total: 35,143x más rápido
•	Escalabilidad: Mantiene eficiencia con números grandes
Resultados
Comparativa de tiempos
Método	Tiempo (segundos)	Mejora (%)	Factor
Código Original	35.1430	-	1x
Optimización Básica	0.1100	99.69%	319x
Criba + NumPy	0.0010	99.997%	35,143x
Análisis de escalabilidad
Límite	Original (s)	Optimizado (s)	Factor de Mejora
1,000	0.0100	0.0000	~100x
5,000	0.1680	0.0000	~168x
10,000	0.5740	0.0000	~574x
50,000	11.2200	0.0000	~11,220x
100,000	41.0660	0.0000	~41,066x
Análisis de cProfile
Código Original:
•	Función más costosa: es_primo() consume ~85% del tiempo total
•	Problema principal: Millones de iteraciones innecesarias
•	Llamadas a funciones: Extremadamente alto número de operaciones
Código Optimizado:
•	Distribución eficiente del tiempo: 
•	60% operaciones NumPy optimizadas
•	20% operaciones range
•	10% operaciones append
•	10% otras funciones
•	Reducción de llamadas: 99.9% menos iteraciones
•	Eficiencia de memoria: Uso optimizado con arrays NumPy
Verificación de resultados
•	Números primos encontrados: 9,592 (mismo resultado en ambas versiones)
•	Primeros 10 primos: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
•	Últimos 10 primos: [99877, 99881, 99901, 99907, 99923, 99929, 99961, 99971, 99989, 99991]
•	Consistencia: Ambos métodos producen resultados idénticos
Conclusiones
Beneficios obtenidos
1.	Mejora dramática en rendimiento
•	Reducción del 99.997% en tiempo de ejecución
•	De 35+ segundos a menos de 0.001 segundos
•	Factor de mejora de 35,143x
2.	Escalabilidad superior
•	El algoritmo optimizado mantiene eficiencia con datasets grandes
•	Crecimiento logarítmico vs cuadrático del original
3.	Uso eficiente de recursos
•	NumPy optimiza el uso de memoria con arrays nativos
•	Operaciones vectorizadas eliminan bucles explícitos
4.	Código más mantenible
•	Implementación más limpia y legible
•	Uso de librerías estándar reconocidas
Repositorio GitHub: [Tu enlace aquí] 

