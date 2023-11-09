import tkinter as tk
from tkinter import ttk
from builder import PizzaBuilder, CustomerBuilder
from menu_personalizada import save_customer_data, load_pizza_menu

class PizzaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Delizioso Pizzeria")
        self.root.geometry("800x600")

        self.label = ttk.Label(self.root, text="¡Bienvenido a Delizioso Pizzeria!", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        self.customer_builder = CustomerBuilder()
        self.pizza_builder = PizzaBuilder()

        # Crear elementos de la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Botón para elegir pizza del menú
        pizza_button = ttk.Button(self.root, text="Elegir Pizza del Menú", command=self.choose_menu_pizza, style="Bold.TButton")
        pizza_button.pack(pady=20)

        # Botón para personalizar pizza
        customize_button = ttk.Button(self.root, text="Personalizar Pizza", command=self.customize_pizza, style="Bold.TButton")
        customize_button.pack(pady=20)

        # Botón para salir
        exit_button = ttk.Button(self.root, text="Salir", command=self.root.destroy, style="Bold.TButton")
        exit_button.pack(pady=20)

        # Configurar el estilo
        style = ttk.Style()
        style.configure("Bold.TButton", font=("Arial", 14, "bold"))

    def choose_menu_pizza(self):
        menu = load_pizza_menu("datos/pizza_types.csv")

        # Crear una nueva ventana para mostrar el menú
        menu_window = tk.Toplevel(self.root)
        menu_window.title("Menú de Pizzas")

        # Crear una lista para mostrar las opciones del menú
        pizza_listbox = tk.Listbox(menu_window)
        pizza_listbox.pack()

        # Llenar la lista con las opciones del menú
        for pizza in menu:
            pizza_listbox.insert(tk.END, pizza['name'])

        # Función para manejar la selección del usuario
        def on_select():
            selected_pizza_index = pizza_listbox.curselection()
            if selected_pizza_index:
                selected_pizza = menu[selected_pizza_index[0]]
                self.pizza_builder.set_name(selected_pizza['name'])
                pizza_to_serve = self.pizza_builder.build()
                self.serve_pizza(pizza_to_serve)
                menu_window.destroy()

        # Función para mostrar los ingredientes al hacer clic en una pizza
        def show_ingredients():
            selected_pizza_index = pizza_listbox.curselection()
            if selected_pizza_index:
                selected_pizza = menu[selected_pizza_index[0]]
                ingredients = selected_pizza['ingredients']
                ingredients_label.config(text=f"Ingredientes: {', '.join(ingredients)}")

        # Botón para seleccionar la pizza
        select_button = ttk.Button(menu_window, text="Seleccionar", command=on_select, style="Bold.TButton")
        select_button.pack()

        # Etiqueta para mostrar los ingredientes
        ingredients_label = ttk.Label(menu_window, text="")
        ingredients_label.pack()

        # Botón para mostrar los ingredientes
        show_ingredients_button = ttk.Button(menu_window, text="Mostrar Ingredientes", command=show_ingredients, style="Bold.TButton")
        show_ingredients_button.pack()

    def customize_pizza(self):
        # Crear una nueva ventana para personalizar la pizza
        customize_window = tk.Toplevel(self.root)
        customize_window.title("Personalizar Pizza")

        # Etiqueta de recomendaciones
        recommendations_label = ttk.Label(
            customize_window,
            text="RECOMENDACIÓN:\nTop 5 mejores pizzas servidas por nosotros:\n"
                 "1. Pizza con setas, queso fresco, jamón ibérico y trufa\n"
                 "2. Pizza con ricota, jamón y pesto de cebollino\n"
                 "3. Pizza de verduras (sin tomate), aguacate y jamón ibérico\n"
                 "4. Pizza de berenjena, kale y jamón\n"
                 "5. Pizza de calabaza, queso y jamón\n\n"
                 "En cuanto a vinos:\n"
                 "1. Borsao Joven Selección 2021\n"
                 "2. Marqués de Cáceres Verdejo 2022\n"
                 "3. Viña Zorzal Rosado Garnacha 2022\n\n"
                 "Si prefieres refresco, disponemos de gran variedad.",
            font=("Arial", 12),
            justify=tk.LEFT
        )
        recommendations_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Crear etiquetas y cuadros de entrada para la personalización
        labels = ["Tipo de masa", "Salsa base", "Ingredientes", "Técnica de cocción", "Presentación", "Bebida", "Extras"]
        entries = []

        for i, label_text in enumerate(labels):
            label = ttk.Label(customize_window, text=label_text)
            entry = ttk.Entry(customize_window)
            label.grid(row=i + 1, column=0, sticky=tk.W, padx=10, pady=5)
            entry.grid(row=i + 1, column=1, padx=10, pady=5)
            entries.append(entry)

        # Función para manejar la personalización
        def on_customize():
            for i, entry in enumerate(entries):
                value = entry.get()
                method_name = f"set_{labels[i].replace(' ', '_').lower()}"
                setattr(self.customer_builder, method_name, value)

            customer = self.customer_builder.build()
            self.serve_pizza(customer)
            customize_window.destroy()

        # Botón para personalizar la pizza
        customize_button = ttk.Button(customize_window, text="Personalizar", command=on_customize, style="Bold.TButton")
        customize_button.grid(row=len(labels) + 1, columnspan=2, pady=10)

    def serve_pizza(self, pizza):
        # Simplemente imprime la información de la pizza por ahora
        print("Pizza Servida:")
        print(pizza)
        save_customer_data("datos/datos_clientes.csv", pizza)

if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaApp(root)
    root.mainloop()
