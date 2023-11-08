from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def crear_analisis_de_datos(self):
        pass

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
        print("Analisis estadistico")
        #quiero que me recoja los datos del csv y me agrupe los eventos por tipo y contar cuántos hay en cada categoría
        #y que me devuelva un diccionario con los resultados

class ConcreteProductA2(AbstractProductA):
    def realizar_analisis(self, datos):
        print("Analisis personalizado")

class AbstractProductB(ABC):
    @abstractmethod
    def generar_visualizacion(self, datos):
        pass

class ConcreteProductB1(AbstractProductB):
    def generar_visualizacion(self, datos):
        print("Histograma")

class ConcreteProductB2(AbstractProductB):
    def generar_visualizacion(self, datos):
        print("Grafico de barras")

def client_code(factory):
    product_a = factory.crear_analisis_de_datos()
    product_b = factory.crear_visualizacion_de_datos()

    print(f"{product_a.realizar_analisis('datos')}")

    print(f"{product_b.generar_visualizacion('datos')}")

if __name__ == "__main__":
    client_code(FabricaConcreta1())
    client_code(FabricaConcreta2())
    print("EJERCICIO 1")