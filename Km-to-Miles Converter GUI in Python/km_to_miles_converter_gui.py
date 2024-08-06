import tkinter as tk
from tkinter import ttk

# Función para convertir kilómetros a millas
def convert():
    """
    Función para convertir kilómetros a millas
    """
    try:
        # Recuperar el valor del widget km_entry y convertirlo a float
        km = float(km_entry.get())
        # Convertir el valor de kilómetros a millas usando el factor de conversión
        miles = km * 0.621371
        # Actualizar el valor de millas con el valor convertido, formateado a 2 decimales
        miles_value.set(f"{miles:.2f}")
    except ValueError:
        # Si la entrada no es válida (por ejemplo, no numérica), mostrar un mensaje de error
        miles_value.set("Invalid input")

root = tk.Tk()
root.title("Kilometers to Miles Converter") # Establecer el título de la ventana
root.geometry("300x100") # Establecer las dimensiones de la ventana

# Crear una etiqueta para el campo de entrada de kilómetros
km_label = ttk.Label(root, text="Kilometers:")
km_label.grid(column=0, row=0, padx=10, pady=10) # Posicionar la etiqueta en la cuadrícula

# Crear un widget de entrada para la entrada del usuario (kilómetros)
km_entry = ttk.Entry(root)
km_entry.grid(column=1, row=0, padx=10, pady=10) # Posicionar la entrada en la cuadrícula

# Crear una etiqueta para el campo de salida de millas
miles_label = ttk.Label(root, text="Miles:")
miles_label.grid(column=0, row=1, padx=10, pady=10) # Posicionar la etiqueta en la cuadrícula

# Crear una variable para almacenar el valor convertido en millas
miles_value = tk.StringVar()
# Crear un widget de entrada para mostrar el valor convertido en millas (solo lectura)
miles_entry = ttk.Entry(root, textvariable=miles_value, state="readonly")
miles_entry.grid(column=1, row=1, padx=10, pady=10) # Posicionar el widget de entrada en la cuadrícula

# Crear un botón para activar el proceso de conversión
convert_button = ttk.Button(root, text="Convert", command=convert)
convert_button.grid(column=0, row=2, columnspan=2, pady=10) # Posicionar el botón en la cuadrícula

root.mainloop()