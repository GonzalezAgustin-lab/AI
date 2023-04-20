import pandas as pd
import numpy as np

# Matriz:
estudiantes = {
    'Id': ['64414181e9eab98300feaa7c', '264414181122e51ab86ae23c3', '64414181919390a1c2f6c7c6', '64414181d7290d2fd19e9a44', '644141814cda33213d4a9c4b', '64414181150c2aae76864710'],
    'Index': [0, 1, 2, 3, 4, 5],
    'Height': ['tall', 'short', 'medium', 'tall', 'short', 'medium'],
    'IsActive': ['true', 'false', 'true', 'true', 'true', 'false'],
    'Balance': ['$1,440.09', '$1,667.76', '$1,747.90', '$2,909.78', '$2,861.98', '$3,941.87'],
    'Age': [36, 20, 23, 35, 20, 38],
    'EyeColor': ['brown', 'green', 'blue', 'green', 'blue', 'green'],
    'Name': ['Sears Guy', 'Tyson Butler', 'Cheryl Wheeler', 'Aline Cortez', 'Muriel Porter', 'Herman Rowland'],
    'Gender': ['male', 'male', 'female', 'female', 'female', 'male'],
    'Company': ['MINGA', 'ZOLAREX', 'GEOFORM', 'DIGIRANG', 'TROPOLIS', 'EVENTAGE'],
    'Email': ['searsguy@minga.com', 'tysonbutler@zolarex.com', 'cherylwheeler@geoform.com', 'alinecortez@digirang.com', 'murielporter@tropolis.com', 'hermanrowland@eventage.com'],
}

# Matriz a dataFrame
dataFrame = pd.DataFrame(estudiantes)
print("Dataframe:")
print(f"{dataFrame}\n\n\n")

# Ejercicio 1 - Aplico funcion logaritmica a la columna 'Age'
dataFrame['Age'] = np.log(dataFrame['Age'])

# Ejercicio 2 - Obtengo las 10 primeras columnas
dataFrame = dataFrame.iloc[:, :10]
print(f"DataFrame pero solamente la 10 primeras columnas (sin mail)")
print(f"{dataFrame}\n\n\n")

# Ejercicio 3 - Convertir las columnas a minúscula
dataFrame.columns = dataFrame.columns.str.lower()
print("DataFrame pero las columnas en minúscula:")
print(f"{dataFrame}\n\n\n")

# Ejercicio 4 - Convertir la column 'Height' a enteros
dataFrame['height'] = dataFrame['height'].map({'short': 1, 'medium': 2, 'tall': 3})
print(f"{dataFrame}\n\n\n")

from google.colab import drive
drive.mount('/content/drive')
path = '/content/drive/My Drive/Ejercicio4.csv'
with open(path, 'w', encoding = 'utf-8-sig') as f:
  dataFrame.to_csv(f)