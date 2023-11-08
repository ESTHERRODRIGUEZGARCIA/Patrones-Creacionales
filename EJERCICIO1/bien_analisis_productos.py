from bien_factories import AbstractFactory
from abc import ABC, abstractmethod
import pandas as pd

# Clase abstracta para productos de análisis
class AbstractProductA(ABC):
    @abstractmethod
    def realizar_analisis(self, datos):
        pass

# Producto de análisis concreto A1
class ConcreteProductA1(AbstractProductA):
    def realizar_analisis(self, datos):
        # Agrupar los eventos por categoría y contar cuántos hay por cada mes.
        results = defaultdict(int)
        for evento in datos:
            categoria = evento["TIPO"]
            results[categoria] += 1

        return dict(results)


# Producto de análisis concreto A2
class ConcreteProductA2(AbstractProductA):
    def realizar_analisis(self, datos):
        results = defaultdict(int)
        for evento in datos:
            fecha = pd.to_datetime(evento["FECHA"]).strftime("%Y-%m-%d")
            results[fecha] += 1

        return dict(results)
        #resultado = agrupar_eventos_por_fecha(datos)
        #print(resultado)