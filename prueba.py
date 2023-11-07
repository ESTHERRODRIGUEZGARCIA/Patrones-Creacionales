import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Abstract Factory
class DataAnalysisFactory:
    def create_data_analysis(self):
        pass

# Concrete Factory 1: Para análisis estadísticos
class StatisticalAnalysisFactory(DataAnalysisFactory):
    def create_data_analysis(self, data):
        return StatisticalDataAnalysis(data)

# Concrete Factory 2: Para visualizaciones gráficas
class VisualAnalysisFactory(DataAnalysisFactory):
    def create_data_analysis(self, data):
        return VisualDataAnalysis(data)

# Abstract Product: Data Analysis
class DataAnalysis:
    def perform_analysis(self):
        pass

# Concrete Product 1: Para análisis estadísticos
class StatisticalDataAnalysis(DataAnalysis):
    def __init__(self, data):
        self.data = data

    def perform_analysis(self):
        # Calcula estadísticas básicas
        mean = np.mean(self.data)
        median = np.median(self.data)
        #mode = np.argmax(np.bincount(self.data)) , Moda: {mode}
        return f"Media: {mean}, Mediana: {median}"

# Concrete Product 2: Para visualizaciones gráficas
class VisualDataAnalysis(DataAnalysis):
    def __init__(self, data):
        self.data = data

    def perform_analysis(self):
        # Crea un histograma de los datos
        sns.histplot(self.data, kde=True)
        plt.xlabel("Valores")
        plt.ylabel("Frecuencia")
        plt.title("Histograma de Activaciones")
        plt.show()

# Lectura de Datos desde el enlace proporcionado
url = "https://datos.madrid.es/egob/catalogo/212504-0-emergencias-activaciones.csv"  # Reemplaza con el enlace real
data = pd.read_csv(url, sep=';', encoding='ISO-8859-1')


# Modelado de Datos: Aquí puedes realizar cualquier preparación de datos necesaria

# Utiliza el Abstract Factory para crear análisis estadísticos
statistical_factory = StatisticalAnalysisFactory()
statistical_analysis = statistical_factory.create_data_analysis(data['PRECIO'])
result_statistical = statistical_analysis.perform_analysis()
print("Análisis Estadístico:")
print(result_statistical)

# Utiliza el Abstract Factory para crear visualizaciones gráficas
visual_factory = VisualAnalysisFactory()
visual_analysis = visual_factory.create_data_analysis(data['PRECIO'])
visual_analysis.perform_analysis()
