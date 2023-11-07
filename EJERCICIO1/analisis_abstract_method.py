from abc import ABC, abstractmethod

# Fábrica abstracta para análisis
class FabricaAnalisis(ABC):
    @abstractmethod
    def crear_analisis_estadistico(self):
        pass

    @abstractmethod
    def crear_analisis_personalizado(self):
        pass

# Fábrica abstracta para visualización
class FabricaVisualizacion(ABC):
    @abstractmethod
    def crear_histograma(self):
        pass

    @abstractmethod
    def crear_grafico_de_barras(self):
        pass

# Producto abstracto para análisis estadístico
class AnalisisEstadistico(ABC):
    @abstractmethod
    def realizar_analisis(self, datos):
        pass

# Producto abstracto para análisis personalizado
class AnalisisPersonalizado(ABC):
    @abstractmethod
    def realizar_analisis_personalizado(self, datos):
        pass

# Producto abstracto para histograma
class Histograma(ABC):
    @abstractmethod
    def generar_histograma(self, datos):
        pass

# Producto abstracto para gráfico de barras
class GraficoDeBarras(ABC):
    @abstractmethod
    def generar_grafico_de_barras(self, datos):
        pass
