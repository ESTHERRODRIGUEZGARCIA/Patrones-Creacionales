from abc import ABC, abstractmethod
import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import pandas as pd

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
        # Agrupa los eventos por categoría y cuenta cuántos hay por cada mes.
        results = defaultdict(int)
        for evento in datos:
            fecha = pd.to_datetime(evento["FECHA"])
            categoria = evento["TIPO"]
            results[categoria] += 1

        return dict(results)

class ConcreteProductA2(AbstractProductA):
    def realizar_analisis(self, datos):
        print("Análisis personalizado")

class AbstractProductB(ABC):
    @abstractmethod
    def generar_visualizacion(self, datos):
        pass

class ConcreteProductB1(AbstractProductB):
    def generar_visualizacion(self, datos):
        # Crea un histograma de distribución de eventos por mes.
        months = [pd.to_datetime(evento["FECHA"]).month for evento in datos]
        plt.hist(months, bins=12, edgecolor='k')
        plt.xlabel("Mes")
        plt.ylabel("Cantidad de Eventos")
        plt.title("Distribución de Eventos por Mes")
        plt.show()

class ConcreteProductB2(AbstractProductB):
    def generar_visualizacion(self, datos):
        # Crea un gráfico de barras que muestra la cantidad de eventos por categoría.
        categories = [evento["TIPO"] for evento in datos]
        data = pd.Series(categories).value_counts()
        data.plot(kind="bar")
        plt.xlabel("Categoría")
        plt.ylabel("Cantidad de Eventos")
        plt.title("Cantidad de Eventos por Categoría")
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
    product_a = factory.crear_analisis_de_datos()
    results_a = product_a.realizar_analisis(datos)
    print("Producto A (Análisis de Datos):")
    print(results_a)

    factory = FabricaConcreta2()
    product_b = factory.crear_visualizacion_de_datos()
    print("Producto B (Visualización de Datos):")
    product_b.generar_visualizacion(datos)



