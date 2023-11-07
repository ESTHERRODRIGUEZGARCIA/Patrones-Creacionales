from abc import ABC, abstractmethod

# Fábrica abstracta para análisis
class AnalysisFactory(ABC):
    @abstractmethod
    def create_statistical_analysis(self):
        pass

    @abstractmethod
    def create_custom_analysis(self):
        pass

# Fábrica abstracta para visualización
class VisualizationFactory(ABC):
    @abstractmethod
    def create_histogram(self):
        pass

    @abstractmethod
    def create_bar_chart(self):
        pass

# Producto abstracto para análisis estadístico
class StatisticalAnalysis(ABC):
    @abstractmethod
    def perform_analysis(self, data):
        pass

# Producto abstracto para análisis personalizado
class CustomAnalysis(ABC):
    @abstractmethod
    def perform_custom_analysis(self, data):
        pass

# Producto abstracto para histograma
class Histogram(ABC):
    @abstractmethod
    def generate_histogram(self, data):
        pass

# Producto abstracto para gráfico de barras
class BarChart(ABC):
    @abstractmethod
    def generate_bar_chart(self, data):
        pass
