import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QListWidget, QInputDialog

class PizzaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.pizza_menu = [
            {"name": "The Barbecue Pizza"},
            {"name": "The Pesto Pizza"},
            {"name": "The Hawaiian Pizza"},
            {"name": "The Brie Carre Pizza"},
            {"name": "The Calabrese Pizza"},
            {"name": "The Italian Supreme Pizza"},
            {"name": "The Soppressata Pizza"},
            {"name": "The Spicy Italian Pizza"},
            {"name": "The Five Cheese Pizza"},
            {"name": "The Vegetables Pizza"}
        ]

        self.customer_counter = 0

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Delizioso Pizzeria')
        self.setGeometry(300, 300, 400, 300)

        self.layout = QVBoxLayout()

        self.label = QLabel('¡Bienvenido a Delizioso Pizzeria!', self)
        self.layout.addWidget(self.label)

        menu_button = QPushButton('Elegir una pizza del menú', self)
        menu_button.clicked.connect(self.display_pizza_menu)
        self.layout.addWidget(menu_button)

        customize_button = QPushButton('Personalizar tu pizza', self)
        customize_button.clicked.connect(self.display_recommendations)
        self.layout.addWidget(customize_button)

        exit_button = QPushButton('Salir', self)
        exit_button.clicked.connect(self.close)
        self.layout.addWidget(exit_button)

        self.setLayout(self.layout)

    def display_pizza_menu(self):
        items = [f"{i + 1}. {pizza['name']}" for i, pizza in enumerate(self.pizza_menu)]
        item, ok_pressed = QInputDialog.getItem(self, "Elegir una pizza", "Selecciona una pizza:", items, 0, False)
        if ok_pressed and item:
            pizza_number = int(item.split(".")[0])
            print(f"Has elegido la pizza {pizza_number}: {self.pizza_menu[pizza_number - 1]['name']}")

    def display_recommendations(self):
        self.customer_counter += 1
        custom_pizza_builder = CustomPizzaBuilder(self.customer_counter)
        recommendations_label = QLabel(self)
        recommendations_label.setText(self.get_recommendations_text())
        custom_pizza_builder.get_pizza_info()

    def get_recommendations_text(self):
        return (
            "RECOMENDACIÓN:\n\nTop 5 mejores pizzas servidas por 'Delizioso Pizzeria':\n"
            "1. Pizza con setas, queso fresco, jamón ibérico, trufa\n"
            "2. Pizza con ricota, jamón, pesto de cebollino\n"
            "3. Pizza de verduras (sin tomate), aguacate, jamón ibérico\n"
            "4. Pizza de berenjena, kale, jamón\n"
            "5. Pizza de calabaza, queso, jamón\n\n"
            "En cuanto a vinos:\n"
            "1. Borsao Joven Selección 2021\n"
            "2. Marqués de Cáceres Verdejo 2022\n"
            "3. Viña Zorzal Rosado Garnacha 2022\n\n"
            "Si prefieres refresco, disponemos de gran variedad."
        )


class CustomPizzaBuilder:
    def __init__(self, customer_number):
        self.customer_number = customer_number

    def get_pizza_info(self):
        print(f"Construyendo pizza para el Cliente {self.customer_number}")
        # Aquí puedes agregar la lógica para recolectar la información de la pizza personalizada
        # y guardarla en tu archivo CSV (datos_clientes.csv)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pizza_app = PizzaApp()
    pizza_app.show()
    sys.exit(app.exec_())
