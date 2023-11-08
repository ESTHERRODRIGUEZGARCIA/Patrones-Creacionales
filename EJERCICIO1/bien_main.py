from bien_factories import FabricaConcreta1, FabricaConcreta2
import csv

def cargar_datos_desde_csv(ruta_csv):
    datos = []
    with open(ruta_csv, "r") as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            datos.append(fila)
    return datos

def client_code(bien_factory):
    product_a = bien_factory.crear_analisis_de_datos()
    product_b = bien_factory.crear_visualizacion_de_datos()

    print("Analisis de Datos:")
    analisis_datos = product_a.realizar_analisis(datos)
    print(analisis_datos)

    print("Visualización de Datos:")
    product_b.generar_visualizacion(datos)


if __name__ == "__main__":
    datos = cargar_datos_desde_csv("EJERCICIO1/CSV/archivo_limpio.csv")
    print("Client: Testing client code with the first factory type: Producto A (Análisis de Datos):")
    client_code(FabricaConcreta1())
    print("\n")
    print("Client: Testing client code with the second factory type: Producto B (Visualización de Datos):")
    client_code(FabricaConcreta2())

