#implementa la lógica principal de tu programa, incluida la bienvenida, 
# la presentación del menú, 
# la construcción de pizzas 
# y la personalización. 
# SOLID: cada clase o módulo tenga una sola razón para cambia

import time
import csv
from builders.pizza_builder import PizzaBuilder
from builders.customer_builder import CustomerBuilder
from models.pizza import Pizza
from models.customer import Customer
from datos.menu_reader import load_pizza_menu
from datos.gestion_archivos import save_customer_data

def display_pizza_menu(menu):
    print("Menú de pizzas:")
    for i, pizza in enumerate(menu, 1):
        print(f"{i}. {pizza.name} - {pizza.category}")
    print("0. Salir")

def main():
    # Cargar el menú de pizzas desde el archivo CSV
    menu = load_pizza_menu("pizza_types.csv")

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
