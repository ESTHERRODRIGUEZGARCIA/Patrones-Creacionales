# Patrones-Creacionales

## Ejercicio 1: Análisis Modular de las Activaciones del SAMUR-Protección Civil en Madrid con Abstract Factory


Objetivo:

Desarrollar un programa en Python que haga uso del patrón de diseño "Abstract Factory" para modularizar y estandarizar el análisis de estos datos. En específico:

1. Lectura de Datos: Acceda y lea el archivo CSV directamente desde el enlace proporcionado: Activaciones del SAMUR-Protección Civil. 

2. Modelado de Datos: Modela y estructura la información para su análisis.

3. Abstract Factory:
   * Diseña un "Abstract Factory" que permita crear diferentes tipos de análisis o representaciones de los datos. Por ejemplo:
     * Una fábrica que genere análisis estadísticos (media, moda, mediana).
     * Una fábrica que produzca visualizaciones gráficas (histogramas, gráficos de barras).
     * Cada fábrica debe tener al menos dos productos concretos (e.g., histograma de activaciones por tipo de emergencia, gráfico de barras de activaciones por mes).

4. Análisis y Representación: Utiliza las fábricas creadas para generar distintos análisis y representaciones de los datos. Muestra la media de activaciones por día, y un histograma de las activaciones.

##Resolución del ejercicio

La resolución del ejercicio implica varios pasos para diseñar e implementar un programa en Python utilizando el patrón de diseño "Abstract Factory". 

1. Organización del Proyecto:
Se organiza el proyecto en carpetas y archivos según una estructura que facilite la comprensión y mantenimiento del código. Se crean las carpetas EJERCICIO1, CSV, y se colocan los archivos necesarios (archivo.csv, limpieza.py, archivo_limpio.csv, etc.) en las ubicaciones correspondientes.

2. Creación de las Clases y Módulos:
Se crean tres módulos principales:

  - bien_factories.py: Define las clases relacionadas con las fábricas (Abstract Factory).

  - bien_analisis_productos.py: Contiene las clases relacionadas con los productos de análisis (Concrete Product A).

  - bien_visualizacion_productos.py: Contiene las clases relacionadas con los productos de visualización (Concrete Product B).

En cada módulo se define una interfaz (AbstractFactory), y clases concretas (FabricaConcreta1, FabricaConcreta2, ConcreteProductA1, ConcreteProductA2, ConcreteProductB1, ConcreteProductB2).

3. Función para Cargar Datos desde CSV:
Se implementa la función cargar_datos_desde_csv en el archivo principal (bien_main.py). Esta función utiliza la biblioteca csv para leer datos desde un archivo CSV y devuelve una lista de diccionarios.

4. Función de Código Cliente:
Se define la función client_code en el archivo principal (bien_main.py). Esta función toma una fábrica concreta como parámetro, crea instancias de productos de análisis y visualización, realiza el análisis de datos y muestra los resultados.

5. Ejecución del Código Principal:
En el bloque _ _ main _ _, se carga los datos utilizando la función cargar_datos_desde_csv. Luego, se ejecuta el código cliente con dos fábricas concretas (FabricaConcreta1 y FabricaConcreta2). Se muestra la salida en la consola, indicando que se está probando el código cliente con los productos de análisis y visualización.

6. Resultados y Salida:
En la función client_code, se realizan los análisis de datos y visualización utilizando los productos concretos correspondientes. La salida del programa incluye los resultados del análisis de datos y la visualización de datos.

7. Pruebas y Verificación:
Se ejecuta el código para verificar que el diseño y la implementación son correctos. Se observa la salida en la consola y se ajusta según sea necesario.

8. Comentarios y Documentación:
Se agregan comentarios en el código para explicar su funcionamiento y se proporciona documentación si es necesario para entender la lógica y la estructura del programa.

Conclusión:

La solución del ejercicio se adhiere a fundamentos esenciales de programación, como la modularidad, la reutilización de código y la implementación de un diseño basado en el patrón Abstract Factory. La organización estructurada del proyecto contribuye a una mayor claridad y facilidad de mantenimiento.

En términos generales, el código refleja el cumplimiento de los principios SOLID. La estructura modular, la implementación de interfaces y la jerarquía bien definida posibilitan la ampliación y el mantenimiento del código de manera eficiente. La aplicación de estos principios promueve un desarrollo sostenible y la adaptabilidad del sistema a posibles cambios o extensiones futuras.

Indicaciones:
ejecutar bien_main.py

Client: Testing client code with the first factory type: Producto A (Análisis de Datos):
Analisis de Datos:
{'/contenido/actividades/ActividadesDeportivas/CarrerasMaratones': 5, '/contenido/actividades/ActividadesDeportivas': 6, '/contenido/actividades/ActividadesDeportivas/Ciclismo': 4, '': 1, '/contenido/actividades/ActividadesDeportivas/Hipica': 1}   
Visualización de Datos:


Client: Testing client code with the second factory type: Producto B (Visualización de Datos):
Analisis de Datos:
{'2023-11-12': 2, '2023-10-08': 1, '2023-11-19': 2, '2023-09-01': 7, '2023-11-09': 1, '2023-11-24': 1, '2023-11-26': 1, '2023-10-02': 2}
Visualización de Datos:

![image](https://github.com/ESTHERRODRIGUEZGARCIA/Patrones-Creacionales/assets/91721860/8fb4ce1c-a4cf-4495-bd50-03bd428833e9)

![image](https://github.com/ESTHERRODRIGUEZGARCIA/Patrones-Creacionales/assets/91721860/10524a40-b6f1-40fe-ba0e-2f72d05aaa3d)



## Ejercicio 2: Sistema Integral de Creación y Gestión de Pizzas Gourmet con Almacenamiento en CSV utilizando el Patrón Builder

Objetivos:

  * Diseñar un sistema que permita a los clientes construir su pizza paso a paso utilizando el patrón Builder.
  * Asegurar que cada elección sea validada para ser compatible con las selecciones previas del cliente.
  * Incorporar un sistema de recomendaciones que sugiera ingredientes, técnicas y maridajes basados en las elecciones previas del cliente.
  * Desarrollar un módulo que guarde cada pizza personalizada en un archivo CSV, almacenando cada detalle, desde los ingredientes hasta el maridaje recomendado.
  * Crear una funcionalidad que lea del archivo CSV y pueda reconstruir la pizza para su visualización, edición o reorden.
  * Garantizar la flexibilidad del sistema para futuras adiciones o modificaciones, ya que la pizzería está en constante innovación.
  * Desarrollar una interfaz de usuario amigable que guíe al cliente en el proceso de creación, ofreciendo información relevante sobre cada elección y facilitando la toma de decisiones.
  * Implementar medidas de seguridad para garantizar la integridad de los datos almacenados y la privacidad de las elecciones de los clientes.

Características a considerar:
  * Tipo de masa: Variedades premium desde masas delgadas hasta masas fermentadas por 48 horas, con opciones de ingredientes especiales.
  * Salsa base: Desde salsas clásicas hasta salsas de autor, incluyendo opciones veganas y de edición limitada.
  * Ingredientes principales: Una gama que abarca desde ingredientes locales hasta importados de especialidad, todos categorizados por su origen, tipo y rareza.
  * Técnicas de cocción: Diversidad que abarca desde hornos tradicionales hasta técnicas modernas de cocina molecular.
  * Presentación: Opciones que van desde estilos clásicos hasta presentaciones que son verdaderas obras de arte.
  * Maridajes recomendados: Una base de datos con cientos de opciones de vinos, cervezas y cocteles, con recomendaciones basadas en las elecciones de los ingredientes de la pizza.
  * Extras y finalizaciones: Desde bordes especiales hasta acabados con ingredientes gourmet como trufas y caviar.



### Patrón Builder

El patrón Builder desempeña un papel fundamental en la construcción flexible y personalizada de pizzas y clientes en este código. Al emplear el patrón Builder, se logra separar la construcción de objetos complejos, como `Pizza` y `Customer`, de su representación, encapsulando los pasos de construcción en las clases `PizzaBuilder` y `CustomerBuilder`. Esto posibilita la creación variable de pizzas y clientes sin necesidad de modificar el código principal, gracias a la capacidad del patrón Builder de permitir la construcción paso a paso y adaptarse fácilmente a diferentes configuraciones. Además, las ventajas clave de este enfoque incluyen la independencia del código principal de las clases concretas, cumpliendo con el principio SOLID, y la asignación de una única responsabilidad a cada clase, facilitando así la comprensión y el mantenimiento del código. La reutilización de los builders en distintos contextos fortalece la modularidad del sistema, permitiendo la creación de pizzas y clientes en otras partes si es necesario. La implementación efectiva del patrón Builder a través de las clases en "builder.py" y "pizza_customer.py" confiere una estructura modular y bien organizada al proyecto, facilitando la construcción y personalización de pizzas con alta cohesión y flexibilidad para futuras expansiones.

Resolución del ejercicio 2:

La estructura del proyecto EJERCICIO2 se organiza de manera clara y modular, con distintas carpetas y archivos que desempeñan funciones específicas. La carpeta "datos" almacena archivos CSV esenciales para la información de pizzas y clientes, donde "datos_clientes.csv" registra los detalles de los clientes y "pizza_types.csv" contiene tipos de pizzas predefinidos. El módulo "app_qt.py" se encarga de la interfaz de usuario utilizando PyQt5, mientras que "builder.py" define las clases del patrón Builder para la construcción de pizzas. El módulo principal, "main.py", implementa la lógica del programa y la interacción a través de la consola. Adicionalmente, "menu_personalizada.py" contiene funciones relacionadas con la personalización del menú, y "pizza_customer.py" define el builder específico para la construcción de pizzas personalizadas, contribuyendo así a una arquitectura organizada y modular del proyecto.




La interfaz de usuario, implementada con PyQt5, se centra en la clase "PizzaApp" en el archivo "app_qt.py". Esta clase define la estructura de la interfaz, proporcionando botones que permiten al usuario elegir pizzas del menú, personalizar su elección y salir. Los métodos clave, como "display_pizza_menu()" para seleccionar pizzas predefinidas, "customize_pizza()" para la personalización guiada y "save_customer_data()" para almacenar los detalles del cliente en un archivo CSV, constituyen las funciones principales de la interfaz. El flujo de ejecución inicia cargando el menú de pizzas desde un archivo CSV. En el menú principal, ya sea en la consola o en PyQt5, se presenta al usuario con opciones para elegir, personalizar o salir. La elección del menú implica mostrar las pizzas predefinidas, mientras que la personalización guía al usuario con recomendaciones y permite la modificación opcional. En ambos casos, los detalles de la pizza se registran en "datos_clientes.csv", y la opción de salir finaliza el programa. Este enfoque proporciona una experiencia de usuario clara y accesible, facilitando tanto la elección de pizzas estándar como la personalización a medida.


**Conclusiones:**
- Se ha logrado implementar un sistema modular que utiliza el patrón Builder para la construcción de pizzas paso a paso.
- La aplicación es flexible y extensible, cumpliendo con los principios SOLID.
- Se ha creado una interfaz de usuario amigable para guiar a los clientes en el proceso de creación de pizzas.




