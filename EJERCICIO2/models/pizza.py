#class Pizza que represente una pizza, aquí estaran las 7 cosas que lleva cada pizza
class Pizza:
    def __init__(self):
        self.name = None
        self.category = None
        self.ingredients = None

    def __str__(self):
        return f"Nombre: {self.name}, Categoría: {self.category}, Ingredientes: {self.ingredients}"
