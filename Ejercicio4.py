import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def export_to_google_drive(df):
    # Aplicar transformación logarítmica a la columna numérica
    df['columna_numerica'] = df['columna_numerica'].apply(lambda x: math.log(x))

    # Obtener solo las primeras 10 columnas si hay más de 10
    if len(df.columns) > 10:
        df = df.iloc[:, :10]

    # Pasar los nombres de las columnas a lowercase
    df.columns = map(str.lower, df.columns)

    # Transformar la columna ordinal a escala numérica
    ordinal_dict = {'alto': 2, 'medio': 1, 'bajo': 0}
    df['columna_ordinal'] = df['columna_ordinal'].map(ordinal_dict)

    # Exportar el DataFrame a un archivo Excel en Google Drive
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)  # Reemplazar 'credentials.json' con el nombre de tu archivo de credenciales
    client = gspread.authorize(credentials)
    sheet = client.create('Archivo_exportado').sheet1  # Reemplazar 'Archivo_exportado' con el nombre que quieras para tu archivo Excel en Google Drive
    sheet.clear()
    sheet.insert_rows(df.values.tolist(), 2)  # Insertar los datos en la segunda fila para dejar espacio para los nombres de columna

    print('Archivo exportado a Google Drive con éxito.')

# Ejemplo de uso:
# Crear un DataFrame de ejemplo con columnas 'columna_numerica' y 'columna_ordinal'
df = pd.DataFrame({'columna_numerica': [10, 20, 30, 40],
                   'columna_ordinal': ['alto', 'medio', 'bajo', 'alto']})

# Llamar a la función export_to_google_drive pasando el DataFrame como argumento
export_to_google_drive(df)