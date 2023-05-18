# Función a minimizar
import random

def f(x, y):
    return 3 * x**2 * y**2

# Parámetros iniciales aleatorios entre 0 y 1
x = random.uniform(0, 1)
y = random.uniform(0, 1)

# Proceso iterativo
for i in range(1, 101):
    # Calcular el valor de la función en la posición actual
    funActual = f(x, y)
    
    # Calcular el gradiente de la función en la posición actual
    derivadaX = 6 * x * y**2
    derivadaY = 6 * x**2 * y
    
    # Actualizar las coordenadas en la dirección del gradiente
    x -= 0.05 * derivadaX
    y -= 0.05 * derivadaY
    
    # Imprimir los valores de la función en cada iteración
    print("Iteración:", i, "par(",x, " , ",y,"), Valor funcion f(x, y):", funActual)
    print()