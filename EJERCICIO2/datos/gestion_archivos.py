#funciones para manejar la lectura y escritura de datos de clientes en un archivo CSV llamado "datos_clientes.csv".

import csv

def save_customer_data(filename, customer):
    try:
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            # Escribe los datos del cliente en el archivo CSV
            writer.writerow([
                customer.customer_number,
                customer.pizza_masa,
                customer.salsa_base,
                customer.ingredientes,
                customer.tecnica_coccion,
                customer.presentacion,
                customer.bebida,
                customer.extras
            ])
    except Exception as e:
        print(f"Error al guardar datos del cliente: {str(e)}")

def load_customer_data(filename):
    customers = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                customer = {
                    "customer_number": int(row[0]),
                    "pizza_masa": row[1],
                    "salsa_base": row[2],
                    "ingredientes": row[3],
                    "tecnica_coccion": row[4],
                    "presentacion": row[5],
                    "bebida": row[6],
                    "extras": row[7]
                }
                customers.append(customer)
    except Exception as e:
        print(f"Error al cargar datos de clientes: {str(e)}")
    return customers
