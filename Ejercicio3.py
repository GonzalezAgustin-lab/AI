import numpy as np
import time
import matplotlib.pyplot as plt

def calcular_valor_en_anillo(k):
    valor_en_anillo = k % 3
    return valor_en_anillo

# Prueba del código con n = 73 y k = 3
n = 73
k = 3
resultado = calcular_valor_en_anillo(k, n)
print("Resultado para n = 73 y k = 3:", b  )

# Creación de un array aleatorio de 10,000 elementos
tamano_array = 10000
array_aleatorio = np.random.randint(1, 1000, size=tamano_array) 

# Medición del tiempo acumulado en cada iteración
tiempo_acumulado = []
tiempo_total = 0
for i in range(tamano_array):
    tiempo_inicio = time.time()
    calcular_valor_en_anillo(k, n)
    tiempo_fin = time.time()
    tiempo_total += (tiempo_fin - tiempo_inicio)
    tiempo_acumulado.append(tiempo_total)

# Graficación del tiempo acumulado en cada iteración
x = np.arange(tamano_array)
y = np.array(tiempo_acumulado)
plt.plot(x, y)
plt.xlabel('n de iteración')
plt.ylabel('Tiempo acumulado')
plt.title('Costo de Computación en función de n')
plt.grid(True)
plt.show()