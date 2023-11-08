from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import pandas as pd


# Clase abstracta para productos de visualización
class AbstractProductB(ABC):
    @abstractmethod
    def generar_visualizacion(self, datos):
        pass

# Producto de visualización concreto B1
class ConcreteProductB1(AbstractProductB):
    def generar_visualizacion(self, datos):
        # Crea un gráfico de barras que muestra la cantidad de eventos por categoría.
        categorias = [evento["TIPO"] for evento in datos]
        data = pd.Series(categorias).value_counts()
        data.plot(kind="bar")
        plt.xlabel("Categoría")
        plt.ylabel("Cantidad de Eventos")
        plt.title("Cantidad de Eventos por Categoría")
        plt.show()

# Producto de visualización concreto B2
class ConcreteProductB2(AbstractProductB):
    def generar_visualizacion(self, datos):
        # Crea una línea de tiempo con las fechas de los eventos ordenadas.
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
