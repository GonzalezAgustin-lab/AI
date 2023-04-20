import random
import time

def anillo_z(n, k):
    if n < 0:
        return None
    elif n < k:
        return n
    else:
        return n % k

n = 73
k = 3
valor_anillo = anillo_z(n, k)
print(valor_anillo)

# Crear un array aleatorio de 10,000 elementos
arr = [random.randint(0, 10000) for i in range(10000)]

# Computar el anillo y medir el tiempo acumulado
tiempos = []
tiempo_acumulado = 0
for i in range(len(arr)):
    inicio = time.time()
    valor_anillo = anillo_z(arr[i], k)
    fin = time.time()
    tiempo_actual = fin - inicio
    tiempo_acumulado += tiempo_actual
    tiempos.append(tiempo_acumulado)

# Graficar el tiempo acumulado en cada iteración
import matplotlib.pyplot as plt
plt.plot(range(len(arr)), tiempos)
plt.xlabel('Número de iteración')
plt.ylabel('Tiempo acumulado (segundos)')
plt.show()