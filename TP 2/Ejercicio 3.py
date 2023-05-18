import numpy as np
from scipy.stats import spearmanr

def calcularSpearman(x, y):

    # Calcular el coeficiente de correlación de Spearman
    correlacion, __ = spearmanr(x, y)

    return correlacion

x = ['Infantil', 'Primaria', 'Primaria', 'Primaria', 'Secundaria', 'Secundaria', 'Bachillerato', 'Bachillerato', 'Bachillerato', 'Universidad']
y = [2, 5, 6, 4, 9, 8, 6, 12, 13, 17]

# xCuantitativo = []
# for v in x:
#     match v:
#         case 'Infantil':
#             xCuantitativo.append(1)
#         case 'Primaria':
#             xCuantitativo.append(2)
#         case 'Secundaria':
#             xCuantitativo.append(3)
#         case 'Bachillerato':
#             xCuantitativo.append(4)
#         case 'Universidad':
#             xCuantitativo.append(5)
# x = xCuantitativo
#
# print(calcularSpearman(x, y))

print(calcularSpearman(range(len(x)), y))
