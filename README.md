# Patrones-Creacionales

## Ejercicio 1: Análisis Modular de las Activaciones del SAMUR-Protección Civil en Madrid con Abstract Factory

Contexto:

El SAMUR-Protección Civil es el servicio de atención a urgencias y emergencias sanitarias extrahospitalarias en el municipio de Madrid. Su labor es esencial para garantizar la seguridad y el bienestar de los ciudadanos en situaciones de emergencia. A lo largo del año, el SAMUR lleva a cabo múltiples "activaciones" en respuesta a diversas situaciones, desde accidentes de tráfico hasta emergencias médicas.

La ciudad de Madrid, en su compromiso con la transparencia y la apertura de datos, publica un registro detallado de estas activaciones en formato CSV. Este registro incluye información como la fecha, hora, tipo de emergencia, y otros detalles relevantes de cada activación.

Objetivo:

Tu tarea es desarrollar un programa en Python que haga uso del patrón de diseño "Abstract Factory" para modularizar y estandarizar el análisis de estos datos. En específico:

1. Lectura de Datos: Acceda y lea el archivo CSV directamente desde el enlace proporcionado: Activaciones del SAMUR-Protección Civil. A continuación, te dejo un código que realiza la lectura del archivo CSV:

````

import pandas as pd

URL = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"

#Leer CSV desde la URL

data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

print(data.head())  #Mostrar las primeras filas para visualizar los datos

````

2. Modelado de Datos: Modela y estructura la información para su análisis.

3. Abstract Factory:
   * Diseña un "Abstract Factory" que permita crear diferentes tipos de análisis o representaciones de los datos. Por ejemplo:
   * Una fábrica que genere análisis estadísticos (media, moda, mediana).
   * Una fábrica que produzca visualizaciones gráficas (histogramas, gráficos de barras).
   * Cada fábrica debe tener al menos dos productos concretos (e.g., histograma de activaciones por tipo de emergencia, gráfico de barras de activaciones por mes).

4. Análisis y Representación: Utiliza las fábricas creadas para generar distintos análisis y representaciones de los datos. Muestra la media de activaciones por día, y un histograma de las activaciones

Recomendaciones:

El objetivo principal es demostrar una correcta implementación y uso del patrón "Abstract Factory". Asegúrate de definir claramente las interfaces (productos abstractos) y las implementaciones concretas (productos concretos).
Utiliza pandas para la manipulación de datos y, si decides incluir visualizaciones, considera matplotlib o seaborn.

#### Rúbrica:

Comprensión del Patrón Abstract Factory: Demuestra una completa comprensión del patrón, implementando correctamente las factories abstractas y concretas.

Lectura y Manipulación de Datos: Lee y procesa el archivo CSV de manera eficiente y sin errores. Los datos se estructuran adecuadamente para su análisis.

Implementación de Productos Concretos (Análisis): Implementa productos concretos (ej., análisis estadístico) de manera correcta y útil. Los análisis son relevantes y significativos.

Implementación de Productos Concretos (Visualización): Crea visualizaciones claras y útiles que aportan información valiosa sobre los datos.

Calidad del Código: El código es limpio, bien organizado, y sigue buenas prácticas. Es fácil de entender y modificar.

Documentación y Comentarios: El código está bien documentado con comentarios claros y útiles. Las funciones y clases tienen descripciones adecuadas.
