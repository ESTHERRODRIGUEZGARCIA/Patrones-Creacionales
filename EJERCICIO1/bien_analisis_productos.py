from bien_factories import AbstractFactory

from abc import ABC, abstractmethod

# Clase abstracta para productos de análisis
class AbstractProductA(ABC):
    @abstractmethod
    def realizar_analisis(self, datos):
        pass

# Producto de análisis concreto A1
class ConcreteProductA1(AbstractProductA):
    def realizar_analisis(self, datos):
        # Realizar análisis estadístico aquí.
        pass

# Producto de análisis concreto A2
class ConcreteProductA2(AbstractProductA):
    def realizar_analisis(self, datos):
        # Realizar análisis personalizado aquí.
        pass
