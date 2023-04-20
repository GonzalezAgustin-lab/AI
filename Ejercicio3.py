import random
import time

# Crear un array aleatorio de 10,000 elementos
maxNumRandom = 10000
array = random.sample(range(maxNumRandom), 10000)
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
    tiempos.append(tiempoTotal)

# Graficar el tiempo acumulado en cada iteración
from matplotlib import pyplot
pyplot.plot(range(len(array)), tiempos)
pyplot.xlabel('Número de iteración')
pyplot.ylabel('Tiempo acumulado (segundos)')
pyplot.show()