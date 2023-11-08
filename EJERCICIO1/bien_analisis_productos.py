from collections import defaultdict
import pandas as pd
from abc import ABC, abstractmethod

# Clase abstracta para productos de análisis
class AbstractProductA(ABC):
    @abstractmethod
    def realizar_analisis(self, datos):
        pass

# Producto de análisis concreto A1
class ConcreteProductA1(AbstractProductA):
    def realizar_analisis(self, datos):
        # Agrupar los eventos por categoría y los cuenta
        results = defaultdict(int)
        for evento in datos:
            categoria = evento["TIPO"]
            results[categoria] += 1

        return dict(results)


# Producto de análisis concreto A2
class ConcreteProductA2(AbstractProductA):
    def realizar_analisis(self, datos):
        # Agrupar los eventos por fecha y los cuenta
        results = defaultdict(int)
        for evento in datos:
            fecha = pd.to_datetime(evento["FECHA"]).strftime("%Y-%m-%d")
            results[fecha] += 1

        return dict(results)
