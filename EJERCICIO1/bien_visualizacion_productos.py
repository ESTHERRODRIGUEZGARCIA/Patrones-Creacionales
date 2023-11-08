from bien_factories import AbstractFactory
from abc import ABC, abstractmethod

# Clase abstracta para productos de visualización
class AbstractProductB(ABC):
    @abstractmethod
    def generar_visualizacion(self, datos):
        pass

# Producto de visualización concreto B1
class ConcreteProductB1(AbstractProductB):
    def generar_visualizacion(self, datos):
        # Generar línea de tiempo ordenada aquí.
        pass

# Producto de visualización concreto B2
class ConcreteProductB2(AbstractProductB):
    def generar_visualizacion(self, datos):
        # Generar gráfico de barras aquí.
        pass
