from abc import ABC, abstractmethod
import csv
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict

class AbstractFactory(ABC):
    @abstractmethod
    def crear_analisis_de_datos(self):
        pass

    @abstractmethod
    def crear_visualizacion_de_datos(self):
        pass

class FabricaConcreta1(AbstractFactory):
    def crear_analisis_de_datos(self):
        return ConcreteProductA1()

    def crear_visualizacion_de_datos(self):
        return ConcreteProductB1()

class FabricaConcreta2(AbstractFactory):
    def crear_analisis_de_datos(self):
        return ConcreteProductA2()

    def crear_visualizacion_de_datos(self):
        return ConcreteProductB2()

class AbstractProductA(ABC):
    @abstractmethod
    def realizar_analisis(self, datos):
        pass

class ConcreteProductA1(AbstractProductA):
    def realizar_analisis(self, datos):
        # Analizar eventos por categoría y contar por mes
        resultados = defaultdict(lambda: defaultdict(int))
        for evento in datos:
            fecha = pd.to_datetime(evento["FECHA"])
            categoria = evento["TIPO"]
            resultados[categoria][fecha.month] += 1

        return dict(resultados)

class ConcreteProductA2(AbstractProductA):
    def realizar_analisis(self, datos):
        # Analizar eventos por mes
        resultados = defaultdict(int)
        for evento in datos:
            fecha = pd.to_datetime(evento["FECHA"])
            mes = fecha.strftime("%B %Y")
            resultados[mes] += 1

        return dict(resultados)

class AbstractProductB(ABC):
    @abstractmethod
    def generar_visualizacion(self, datos):
        pass

class ConcreteProductB1(AbstractProductB):
    def generar_visualizacion(self, datos):
        # Crear un gráfico de barras para eventos por categoría
        analisis = ConcreteProductA1().realizar_analisis(datos)
        categorias = analisis.keys()
        eventos_por_mes = {mes: [analisis[categoria][mes] for categoria in categorias] for mes in range(1, 13)}

        width = 0.2
        x = list(range(1, 13))

        for i, categoria in enumerate(categorias):
            plt.bar([pos + width * i for pos in x], eventos_por_mes[categoria], width=width, label=categoria)

        plt.xlabel("Mes")
        plt.ylabel("Cantidad de Eventos")
        plt.title("Eventos por Categoría y Mes")
        plt.xticks([pos + width for pos in x], x)
        plt.legend(categorias)
        plt.show()

class ConcreteProductB2(AbstractProductB):
    def generar_visualizacion(self, datos):
        # Crear una línea de tiempo con todas las fechas de los eventos
        fechas = [pd.to_datetime(evento["FECHA"]) for evento in datos]
        fechas_ordenadas = sorted(fechas)
        nombres_eventos = [evento["TITULO"] for evento in datos]

        plt.figure(figsize=(10, 5))
        plt.plot(fechas_ordenadas, range(1, len(fechas_ordenadas) + 1), marker='o', linestyle='-', markersize=2)
        plt.yticks(range(1, len(fechas_ordenadas) + 1), nombres_eventos)
        plt.xlabel("Fecha")
        plt.ylabel("Eventos")
        plt.title("Línea de Tiempo de Eventos")
        plt.gca().invert_yaxis()
        plt.grid()
        plt.show()

def cargar_datos_desde_csv(ruta_csv):
    datos = []
    with open(ruta_csv, "r") as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            datos.append(fila)
    return datos

if __name__ == "__main__":
    datos = cargar_datos_desde_csv("EJERCICIO1/CSV/archivo_limpio.csv")

    factory = FabricaConcreta1()
    product_a1 = factory.crear_analisis_de_datos()
    results_a1 = product_a1.realizar_analisis(datos)
    
    print("Producto A1 (Análisis de Datos - Eventos por Categoría y Mes):")
    print(results_a1)

    factory = FabricaConcreta2()
    product_b1 = factory.crear_visualizacion_de_datos()

    print("Producto B1 (Visualización de Datos - Gráfico de Barras por Categoría):")
    product_b1.generar_visualizacion(datos)

    factory = FabricaConcreta2()
    product_b2 = factory.crear_analisis_de_datos()
    results_a2 = product_b2.realizar_analisis(datos)

    print("Producto A2 (Análisis de Datos - Eventos por Mes):")
    print(results_a2)
