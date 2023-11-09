# define funciones para leer el menú desde el archivo CSV "pizza_types.csv". 
# Esto te ayudará a mostrar las opciones disponibles al cliente.

import csv
from models.pizza import Pizza


def load_pizza_menu(filename):
    menu = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader, 1):
                pizza_name = row['name']
                print(f"{i}. {pizza_name}")
                menu.append(pizza_name)
    except Exception as e:
        print(f"Error al cargar el menú de pizzas: {str(e)}")
    return menu
