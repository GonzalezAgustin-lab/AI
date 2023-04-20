import random
import time

# Crear un array aleatorio de 10,000 elementos
maxNumRandom = 10
array = random.sample(range(maxNumRandom), 10)
n = 73
k = 3

# Computar el anillo y medir el tiempo acumulado
tiempos = []
tiempoTotal = 0
for i in range(len(array)):
    inicio = time.time()
    valorAnillo = n % k
    tiempo = time.time() - inicio
    tiempoTotal += tiempo
    tiempos.append(tiempo)

# Graficar el tiempo acumulado en cada iteración
import matplotlib.pyplot as plt
plt.plot(range(len(array)), tiempos)
plt.xlabel('Número de iteración')
plt.ylabel('Tiempo acumulado (segundos)')
plt.show()