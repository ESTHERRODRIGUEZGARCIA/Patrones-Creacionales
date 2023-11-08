from abc import ABC, abstractmethod

# Clase abstracta para la fábrica
class AbstractFactory(ABC):
    @abstractmethod
    def crear_analisis_de_datos(self):
        pass

    @abstractmethod
    def crear_visualizacion_de_datos(self):
        pass

# Fábrica concreta 1
class FabricaConcreta1(AbstractFactory):
    def crear_analisis_de_datos(self):
        return ConcreteProductA1()

    def crear_visualizacion_de_datos(self):
        return ConcreteProductB1()

# Fábrica concreta 2
class FabricaConcreta2(AbstractFactory):
    def crear_analisis_de_datos(self):
        return ConcreteProductA2()

    def crear_visualizacion_de_datos(self):
        return ConcreteProductB2()

