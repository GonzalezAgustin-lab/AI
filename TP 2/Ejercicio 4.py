"""1 - Variables cualitativas ordinales y nominales:
Las variables cualitativas se refieren a características o atributos que no se pueden medir en términos numéricos y se clasifican en dos categorías principales:
ordinales y nominales.

Variables cualitativas ordinales: Estas variables tienen categorías o niveles con un orden o jerarquía definida. El orden o la jerarquía entre las categorías 
es importante, pero la diferencia entre las categorías no es necesariamente uniforme. Ejemplos:

a) Nivel educativo: Puede ser categorizado como "primaria", "secundaria" y "terciaria". Existe un orden claro, donde la educación primaria es básica, seguida 
de la secundaria y luego la terciaria.

b) Escala de calificación: Una escala de calificación puede tener categorías como "excelente", "bueno", "regular" y "deficiente". Estas categorías tienen un 
orden implícito donde "excelente" es superior a "bueno", "regular" y "deficiente".

Variables cualitativas nominales: Estas variables tienen categorías sin un orden o jerarquía específica. Las categorías son distintas y no se pueden clasificar
 en un orden lógico. Ejemplos:

a) Color de ojos: Las categorías pueden ser "azul", "verde", "marrón" y "negro". Estas categorías no tienen un orden lógico ni una jerarquía.

b) Estado civil: Las categorías pueden ser "soltero", "casado", "divorciado" y "viudo". Estas categorías son distintas y no tienen un orden específico.
"""
import pandas as pd

# Creamos un DataFrame de ejemplo
data = {
    'Animal': ['Perro', 'Gato', 'Elefante', 'Jirafa', 'León'],
    'Tamaño': ['Pequeño', 'Pequeño', 'Grande', 'Mediano', 'Grande'],
    'Color': ['Blanco', 'Negro', 'Gris', 'Amarillo', 'Marrón']
}

df = pd.DataFrame(data)

# Codificación de variable ordinal 'Tamaño'
tamaño_mapping = {
    'Pequeño': 1,
    'Mediano': 2,
    'Grande': 3
}

df['Tamaño_codificado'] = df['Tamaño'].map(tamaño_mapping)

# Codificación de variable nominal 'Color' con dummy variables
color_dummies = pd.get_dummies(df['Color'], prefix='Color')

# Agregamos las dummy variables al DataFrame original
df = pd.concat([df, color_dummies], axis=1)

# Imprimimos el resultado
print(df)