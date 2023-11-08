from bien_factories import FabricaConcreta1, FabricaConcreta2, AbstractFactory
from bien_analisis_productos import ConcreteProductA1, ConcreteProductA2
from bien_visualizacion_productos import ConcreteProductB1, ConcreteProductB2
import csv

#función para cargar los datos del csv
def cargar_datos_desde_csv(ruta_csv):
    datos = []
    with open(ruta_csv, "r") as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            datos.append(fila)
    return datos

#función para realizar el código cliente
def client_code(bien_factory):
    #crea instancias de los productos de análisis y visualización
    product_a = bien_factory.crear_analisis_de_datos()
    product_b = bien_factory.crear_visualizacion_de_datos()

    #realiza el análisis de datos y muestra los resultados
    print("Analisis de Datos:")
    analisis_datos = product_a.realizar_analisis(datos)
    print(analisis_datos)

    print("Visualización de Datos:")
    product_b.generar_visualizacion(datos)


if __name__ == "__main__":
    #carga los datos del csv
    datos = cargar_datos_desde_csv("EJERCICIO1/CSV/archivo_limpio.csv")

    #ejecuta el código cliente con las dos fábricas concretas, producto A y B
    print("Client: Testing client code with the first factory type: Producto A (Análisis de Datos):")
    client_code(FabricaConcreta1())
    print("\n")
    print("Client: Testing client code with the second factory type: Producto B (Visualización de Datos):")
    client_code(FabricaConcreta2())

