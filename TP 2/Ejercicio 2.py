import math
import matplotlib.pyplot as plt

def pearson_correlation(points):
    n = len(points)
    sum_x = sum_y = sum_xy = sum_x2 = sum_y2 = 0

    for x, y in points:
        sum_x += x
        sum_y += y
        sum_xy += x * y
        sum_x2 += x ** 2
        sum_y2 += y ** 2

    numerator = (n * sum_xy) - (sum_x * sum_y)
    denominator = math.sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))
    correlation = numerator / denominator

    return correlation

# Parte 1: Cálculo de la correlación para un conjunto de puntos dados

# Ejemplo de entrada
points = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
correlation = pearson_correlation(points)
print(f"Correlación: {correlation}")

# Gráfico X vs Y
x = [point[0] for point in points]
y = [point[1] for point in points]
plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico X vs Y')
plt.show()

# Parte 2: Prueba de correlación lineal para Y = 2X + 3

# Generar 50 pares (x, y) utilizando la ecuación de la recta Y = 2X + 3
points_linear = [(x, 2 * x + 3) for x in range(1, 51)]
correlation_linear = pearson_correlation(points_linear)
print(f"Correlación (lineal): {correlation_linear}")

# Gráfico X vs Y
x_linear = [point[0] for point in points_linear]
y_linear = [point[1] for point in points_linear]
plt.scatter(x_linear, y_linear)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico X vs Y (lineal)')
plt.show()

# Parte 3: Prueba de correlación para puntos en un círculo de radio 1 centrado en el origen

# Generar 50 pares ordenados en el círculo de radio 1 centrado en el origen
points_circle = []
for theta in range(0, 360, int(360 / 50)):
    x = math.cos(math.radians(theta))
    y = math.sin(math.radians(theta))
    points_circle.append((x, y))

correlation_circle = pearson_correlation(points_circle)
print(f"Correlación (círculo): {correlation_circle}")

# Gráfico X vs Y
x_circle = [point[0] for point in points_circle]
y_circle = [point[1] for point in points_circle]
plt.scatter(x_circle, y_circle)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico X vs Y (círculo)')
plt.show()

#1. Para la parte 1, como los puntos están perfectamente alineados en una relación 1:1, la correlación será 1. 
#El gráfico mostrará una línea diagonal perfecta.

#2. Para la parte 2, dado que los puntos se generan siguiendo una relación lineal Y = 2X + 3, la correlación será 1, 
#ya que hay una relación lineal perfecta. El gráfico mostrará una línea recta ascendente.

#3. Para la parte 3, dado que los puntos se generan en un círculo de radio 1 centrado en el origen, no hay una relación lineal 
#entre X e Y. Por lo tanto, la correlación será cercana a 0. El gráfico mostrará una dispersión de puntos alrededor del círculo.