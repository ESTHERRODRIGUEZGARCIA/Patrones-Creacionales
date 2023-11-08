import csv
import pandas as pd
import matplotlib.pyplot as plt

def cargar_datos_desde_csv(ruta_csv):
    datos = []
    with open(ruta_csv, "r") as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            datos.append(fila)
    return datos

def generar_grafico_de_barras(datos):
    categorias = [evento["TIPO"] for evento in datos]
    data = pd.Series(categorias).value_counts()
    data.plot(kind="bar")
    plt.xlabel("Categoría")
    plt.ylabel("Cantidad de Eventos")
    plt.title("Cantidad de Eventos por Categoría")
    plt.show()

def generar_linea_de_tiempo(datos):
    fechas = [pd.to_datetime(evento["FECHA"]) for evento in datos]
    nombres_eventos = [evento["TITULO"] for evento in datos]

    # Ordena las fechas y los nombres de los eventos en función de las fechas
    fechas, nombres_eventos = zip(*sorted(zip(fechas, nombres_eventos)))

    plt.figure(figsize=(10, 5))
    plt.plot(fechas, range(1, len(fechas) + 1), marker='o', linestyle='-', markersize=2)
    plt.yticks(range(1, len(fechas) + 1), nombres_eventos)
    plt.xlabel("Fecha")
    plt.ylabel("Eventos")
    plt.title("Línea de Tiempo de Eventos (Ordenada)")
    plt.gca().invert_yaxis()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    datos = cargar_datos_desde_csv("EJERCICIO1/CSV/archivo_limpio.csv")

    print("Generando gráfico de barras...")
    generar_grafico_de_barras(datos)

    print("Generando línea de tiempo ordenada...")
    generar_linea_de_tiempo(datos)
