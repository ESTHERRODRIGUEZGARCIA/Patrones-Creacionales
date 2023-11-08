from bien_factories import FabricaConcreta1, FabricaConcreta2
from bien_analisis_productos import ConcreteProductA1, ConcreteProductA2
from bien_analisis_productos import ConcreteProductB1, ConcreteProductB2
import csv

def cargar_datos_desde_csv(ruta_csv):
    datos = []
    with open(ruta_csv, "r") as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            datos.append(fila)
    return datos

def client_code(factory):
    product_a = factory.crear_analisis_de_datos()
    product_b = factory.crear_visualizacion_de_datos()

    print("Producto A (Análisis de Datos):")
    product_a.realizar_analisis(datos)

    print("Producto B (Visualización de Datos):")
    product_b.generar_visualizacion(datos)

if __name__ == "__main__":
    datos = cargar_datos_desde_csv("EJERCICIO1/CSV/archivo_limpio.csv")

    # Utiliza las fábricas concretas
    client_code(FabricaConcreta1())
    client_code(FabricaConcreta2())
