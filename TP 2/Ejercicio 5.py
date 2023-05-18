from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df_titanic = pd.read_csv('./content/test.csv')

# Identificar datos ausentes en datos tabulares
print(f"Identificar ausentes en datos tabulares:\n {df_titanic.isnull().sum()}")

print(f"Eliminar muestras o caracteristicas con valores ausentes:\n{df_titanic.dropna()}")

imr = SimpleImputer(strategy="most_frequent")
imr = imr.fit(df_titanic.values)
imputed_data = imr.transform(df_titanic.values)

print(f"Imputar datos ausentes:\n{imputed_data}")

sex_mapping = { label:idx for idx, label in enumerate(np.unique(df_titanic['Sex']))}
df_titanic['Sex'] = df_titanic['Sex'].map(sex_mapping)
embarked_mapping = { label:idx for idx, label in enumerate(np.unique(df_titanic['Embarked']))}
df_titanic['Embarked'] = df_titanic['Embarked'].map(embarked_mapping)

# Con este codigo códicariamos la caracteristicas ordinales
# pclass_mapping = {
#     "First class": 1, 
#     "Second class": 2,
#     "Third Class": 3
# }

# df_titanic['PClass'] = df_titanic['PClass'].map(pclass_mapping)


#codificacion
print(f"Codificar etiquetas de clase\n: ${df_titanic}")

datosCodificados = pd.get_dummies(df_titanic['Embarked'])

df_titanic = pd.concat([df_titanic, datosCodificados], axis=1)

print(f"Realizar una codificación en caliente sobre características nominales\n: ${df_titanic}")

# Eliminar columnas no numéricas irrelevantes
df_titanic = df_titanic.drop(['Name', 'Ticket', 'Cabin'], axis=1)

# Cálculo de la matriz de correlación
correlation_matrix = df_titanic.corr()

# Visualización de la matriz de correlación
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de correlación')
plt.show()

# Análisis de la matriz de correlación
print("Matriz de correlación:")
print(correlation_matrix)