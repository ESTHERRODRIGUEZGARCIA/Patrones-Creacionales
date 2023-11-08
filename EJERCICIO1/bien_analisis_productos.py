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
            fecha = pd.to_datetime(evento["FECHA"])
            categoria = evento["TIPO"]
            # Realizar análisis estadístico aquí.
            results[categoria] += 1

        return dict(results)

# Producto de análisis concreto A2
class ConcreteProductA2(AbstractProductA):
    def realizar_analisis(self, datos):
        def realizar_analisis(self, datos):
        # Agrupar los eventos por fecha (distribución de eventos por fecha).
        fechas = [pd.to_datetime(evento["FECHA"]) for evento in datos]
        # Realizar análisis personalizado aquí.
        return fechas