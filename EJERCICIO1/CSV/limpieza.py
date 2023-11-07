import pandas as pd

# Cargar el archivo CSV
# Especifica la codificación al abrir el archivo CSV
df = pd.read_csv('EJERCICIO1/CSV/archivo.csv', sep=';', encoding='ISO-8859-1')

# Limpieza de datos: Elimina las columnas que no son necesarias
columns_to_drop = ['PRECIO', 'GRATUITO', 'LARGA-DURACION', 'DIAS-SEMANA', 'DIAS-EXCLUIDOS', 'HORA', 'CONTENT-URL', 'TITULO-ACTIVIDAD', 'URL-ACTIVIDAD', 'URL-INSTALACION', 'NOMBRE-INSTALACION', 'ACCESIBILIDAD-INSTALACION', 'CLASE-VIAL-INSTALACION', 'NOMBRE-VIA-INSTALACION', 'NUM-INSTALACION', 'DISTRITO-INSTALACION', 'BARRIO-INSTALACION', 'CODIGO-POSTAL-INSTALACION', 'COORDENADA-X', 'COORDENADA-Y', 'LATITUD', 'LONGITUD']
df.drop(columns=columns_to_drop, inplace=True)

# Transformación de datos: Convierte la columna 'FECHA' en un objeto de fecha y hora
df['FECHA'] = pd.to_datetime(df['FECHA'])

# Limpieza de caracteres no deseados en la columna 'TITULO'
df['TITULO'] = df['TITULO'].str.replace('�', 'ó')

# Selecciona las columnas relevantes
columns_of_interest = ['ID-EVENTO', 'TITULO', 'FECHA', 'TIPO', 'AUDIENCIA']
df = df[columns_of_interest]

# Guardar el archivo limpio
df.to_csv('EJERCICIO1/CSV/archivo_limpio.csv', index=False)
