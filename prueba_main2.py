# main.py
import time
import csv

from datos.menu_reader import load_pizza_menu
from datos.gestion_archivos import save_customer_data

# pizza.py
class Pizza:
    def __init__(self):
        self.name = None
        self.category = None
        self.ingredients = None

# pizza_builder.py
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_name(self, name):
        self.pizza.name = name
        return self

    def set_category(self, category):
        self.pizza.category = category
        return self

    def set_ingredients(self, ingredients):
        self.pizza.ingredients = ingredients
        return self

    def build(self):
        return self.pizza

# customer.py
class Customer:
    def __init__(self):
        self.customer_number = None
        self.pizza_masa = None
        self.salsa_base = None
        self.ingredientes = None
        self.tecnica_coccion = None
        self.presentacion = None
        self.bebida = None
        self.extras = None

# customer_builder.py
class CustomerBuilder:
    def __init__(self):
        self.customer = Customer()

    def set_customer_number(self, customer_number):
        self.customer.customer_number = customer_number
        return self

    def set_pizza_masa(self, masa):
        self.customer.pizza_masa = masa
        return self

    def set_salsa_base(self, salsa_base):
        self.customer.salsa_base = salsa_base
        return self

    def set_ingredientes(self, ingredientes):
        self.customer.ingredientes = ingredientes
        return self

    def set_tecnica_coccion(self, tecnica_coccion):
        self.customer.tecnica_coccion = tecnica_coccion
        return self

    def set_presentacion(self, presentacion):
        self.customer.presentacion = presentacion
        return self

    def set_bebida(self, bebida):
        self.customer.bebida = bebida
        return self

    def set_extras(self, extras):
        self.customer.extras = extras
        return self

    def build(self):
        return self.customer





def display_pizza_menu(menu):
    print("Menú de pizzas:")
    for i, pizza in enumerate(menu, 1):
        print(f"{i}. {pizza.name} - {pizza.category}")
    print("0. Salir")

def main():
    # Contador de clientes
    customer_counter = 0

    while True:
        print("¡Bienvenido a Delizioso Pizzeria!")
        print("¿Qué deseas hacer?")
        print("1. Elegir una pizza del menú")
        print("2. Personalizar tu pizza")
        print("0. Salir")

        choice = input("Ingresa el número de tu elección: ")

        if choice == "1":
            # Cargar el menú de pizzas desde el archivo CSV
            menu = load_pizza_menu("pizza_types.csv")
            display_pizza_menu(menu)
            pizza_choice = input("Elige el número de la pizza que deseas: ")

            if pizza_choice == "0":
                print("Gracias por visitar Delizioso Pizzeria. ¡Hasta la próxima!")
                break

            if not pizza_choice.isnumeric() or int(pizza_choice) < 1 or int(pizza_choice) > len(menu):
                print("Selección no válida. Inténtalo de nuevo.")
                continue

            # Construir la pizza elegida del menú
            pizza = menu[int(pizza_choice) - 1]
            pizza_builder = PizzaBuilder()
            pizza_builder.set_name(pizza.name)
            pizza_builder.set_category(pizza.category)
            pizza_builder.set_ingredients(pizza.ingredients)
            pizza_to_serve = pizza_builder.build()

        elif choice == "2":
            # Construir una pizza personalizada
            customer_counter += 1
            customer_builder = CustomerBuilder()
            customer_builder.set_customer_number(customer_counter)
            print(f"Construyendo pizza para el Cliente {customer_counter}")

            customer_builder.set_pizza_masa(input("Tipo de masa (fina o gruesa): "))
            customer_builder.set_salsa_base(input("Salsa base (tomate, soja, genovesa): "))
            customer_builder.set_ingredientes(input("Ingredientes separados por comas (queso, pollo, bacon, atún, cebolla): "))
            customer_builder.set_tecnica_coccion(input("Técnica de cocción (horno de piedra o sartén): "))
            customer_builder.set_presentacion(input("Presentación (en caja de cartón o en un plato de metal): "))
            customer_builder.set_bebida(input("Bebida (vino blanco, vino tinto, cocacola, agua, nada): "))
            customer_builder.set_extras(input("Extras (helado, regalo, patatas fritas): "))
            pizza_to_serve = customer_builder.build()

        elif choice == "0":
            print("Gracias por visitar Delizioso Pizzeria. ¡Hasta la próxima!")
            break

        else:
            print("Selección no válida. Inténtalo de nuevo.")
            continue

        print("Construyendo tu pizza...")
        time.sleep(2)
        print("Tu pizza está lista para ser recogida.")

        # Guardar los datos del cliente en el archivo CSV
        customer = customer_builder.get_customer()
        save_customer_data("datos_clientes.csv", customer)

if __name__ == "__main__":
    main()
