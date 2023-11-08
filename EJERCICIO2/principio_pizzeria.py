import csv
from abc import ABC, abstractmethod
from typing import List

# Clase Pizza representa el producto final
class Pizza:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def __str__(self):
        return ', '.join(self.ingredients)


# Interfaz del constructor de pizzas (Builder)
class PizzaBuilder(ABC):
    @abstractmethod
    def build_dough(self): #construir masa
        pass

    @abstractmethod
    def build_sauce(self):
        pass

    @abstractmethod
    def build_toppings(self):
        pass

    @abstractmethod
    def build_cooking_technique(self):
        pass

    @abstractmethod
    def build_presentation(self):
        pass

    @abstractmethod
    def build_pairings(self):
        pass

    @abstractmethod
    def build_extras(self):
        pass

    @abstractmethod
    def get_pizza(self) -> Pizza:
        pass


# Constructor concreto para una Pizza Margherita
class MargheritaPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def build_dough(self):
        self.pizza.add_ingredient("Thin crust dough")

    def build_sauce(self):
        self.pizza.add_ingredient("Tomato sauce")

    def build_toppings(self):
        self.pizza.add_ingredient("Mozzarella cheese")
        self.pizza.add_ingredient("Fresh basil")

    def build_cooking_technique(self):
        self.pizza.add_ingredient("Wood-fired oven")

    def build_presentation(self):
        self.pizza.add_ingredient("Classic round shape")

    def build_pairings(self):
        self.pizza.add_ingredient("Chianti wine")

    def build_extras(self):
        self.pizza.add_ingredient("Garlic bread")

    def get_pizza(self) -> Pizza:
        return self.pizza


# Director que orquesta el proceso de construcción de pizzas
class PizzaDirector:
    def __init__(self):
        self.builder = None

    def construct_pizza(self):
        self.builder.build_dough()
        self.builder.build_sauce()
        self.builder.build_toppings()
        self.builder.build_cooking_technique()
        self.builder.build_presentation()
        self.builder.build_pairings()
        self.builder.build_extras()

    def set_builder(self, builder: PizzaBuilder):
        self.builder = builder

    def get_pizza(self) -> Pizza:
        return self.builder.get_pizza()


# Función para guardar una pizza en un archivo CSV
def save_pizza_to_csv(pizza: Pizza, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(pizza.ingredients)


# Función para cargar una pizza desde un archivo CSV
def load_pizza_from_csv(filename):
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        row = next(reader)
        pizza = Pizza()
        pizza.ingredients = row
        return pizza


if __name__ == "__main__":
    # Crear un director de pizzas
    director = PizzaDirector()

    # Usar el constructor de pizzas Margherita
    margherita_builder = MargheritaPizzaBuilder()
    director.set_builder(margherita_builder)

    # Construir una pizza Margherita
    director.construct_pizza()
    pizza = director.get_pizza()

    # Guardar la pizza en un archivo CSV
    save_pizza_to_csv(pizza, "pizza.csv")

    # Cargar la pizza desde el archivo CSV
    loaded_pizza = load_pizza_from_csv("pizza.csv")

    print("Pizza ingredients:", loaded_pizza)
