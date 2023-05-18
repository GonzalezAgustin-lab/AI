import math

entrada1 = [2, 3, 4, 5, 6, 1, 1, 1, 1, 2, 3, 4, 6, 9]
entrada2 = [2, 3, 2, 3, 2, 3]
entrada3 = [2,3,4,4,4,4,4,4,4,4, 99, 99, 1, -5, -99]

def estandarizarDatos(array):
    media = sum(array) / len(array)
    acum = 0
    for n in array:
        acum += pow((n - media), 2)
    desviacionEstandar = math.sqrt(acum / (len(array) - 1))
    i = 0
    for n in array:
        array[i] = (array[i] - media)/desviacionEstandar
        i += 1
    return array

print(estandarizarDatos(entrada1))