#crea un constructor para las personalizaciones de los clientes.
from models.customer import Customer

class CustomerBuilder:
    #me permite construir objetos customer
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

    def get_customer(self):
        return self.customer
