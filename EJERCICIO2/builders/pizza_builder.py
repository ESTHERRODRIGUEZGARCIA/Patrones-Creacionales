#crea un constructor de pizza que sigue el patrón Builder. Permite a los clientes construir pizzas paso a paso.
from models.pizza import Pizza

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
