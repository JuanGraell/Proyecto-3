import tkinter as tk
from PIL import ImageTk, Image

class Vehiculo:
    def __init__(self, placa):
        self.placa = placa

class ParkingLot:
    def __init__(self):
        self.capacity = 60
        self.slots = [None] * self.capacity

    def hash_function(self, placa):
        total = sum(ord(char) for char in placa)
        return total % self.capacity

    def insert_Vehiculo(self, vehiculo):
        index = self.hash_function(vehiculo.placa)

        if self.slots[index] is None:
            self.slots[index] = vehiculo
            return f"Vehículo con placa {vehiculo.placa} estacionado en el puesto {index}."
        else:
            i = index + 1
            while i != index:
                if i >= self.capacity:
                    i = 0

                if self.slots[i] is None:
                    self.slots[i] = vehiculo
                    return f"Vehículo con placa {vehiculo.placa} se estacionó en el puesto {i}."
                i += 1

            return "El parking está lleno. No se puede estacionar el vehículo."

    def find_Vehiculo(self, placa):
        index = self.hash_function(placa)

        if self.slots[index] is not None and self.slots[index].placa == placa:
            return index
        else:
            i = index + 1
            while i != index:
                if i >= self.capacity:
                    i = 0

                if self.slots[i] is not None and self.slots[i].placa == placa:
                    return i
                i += 1

        return None

    def remove_Vehiculo(self, placa):
        index = self.find_Vehiculo(placa)

        if index is not None:
            self.slots[index] = None
            return f"Vehículo con placa {placa} acaba de salir del parqueadero y ahora el puesto {index} se encuentra disponible."
        else:
            return "El vehículo no está estacionado en el parqueadero."

class ImageBrowser:
    def __init__(self, root):
        self.root = root
        self.current_image_index = 0
        self.images = [
            "piso1.png",
            "piso2.png",
            "piso3.png"
        ]

        self.load_image()
        self.create_buttons()

    def load_image(self):
        image_path = self.images[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((800, 600))
        self.photo = ImageTk.PhotoImage(image)

        if hasattr(self, "canvas"):
            self.canvas.destroy()

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        self.canvas.pack()

    def create_buttons(self):
        if hasattr(self, "button_frame"):
            self.button_frame.destroy()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side=tk.BOTTOM, pady=10)

        if self.current_image_index != 0:
            prev_button = tk.Button(self.button_frame, text="Piso {}".format(self.current_image_index), command=self.previous_image)
            prev_button.pack(side=tk.LEFT)

        if self.current_image_index != len(self.images) - 1:
            next_button = tk.Button(self.button_frame, text="Piso {}".format(self.current_image_index + 2), command=self.next_image)
            next_button.pack(side=tk.RIGHT)

    def previous_image(self):
        if self.current_image_index != 0:
            self.current_image_index -= 1
        self.load_image()
        self.create_buttons()

    def next_image(self):
        if self.current_image_index != len(self.images) - 1:
            self.current_image_index += 1
        self.load_image()
        self.create_buttons()

class ParkingGUI:
    def __init__(self, root):
        self.root = root
        self.parking_lot = ParkingLot()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Ingrese la placa del vehículo:")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.insert_button = tk.Button(self.root, text="Estacionar vehículo", command=self.insert_vehicle)
        self.insert_button.pack()

        self.remove_button = tk.Button(self.root, text="Retirar vehículo", command=self.remove_vehicle)
        self.remove_button.pack()

        self.message_label = tk.Label(self.root, text="")
        self.message_label.pack()

    def insert_vehicle(self):
        placa = self.entry.get()
        vehicle = Vehiculo(placa)
        message = self.parking_lot.insert_Vehiculo(vehicle)
        self.message_label.config(text=message)

    def remove_vehicle(self):
        placa = self.entry.get()
        message = self.parking_lot.remove_Vehiculo(placa)
        self.message_label.config(text=message)

# Crear la ventana principal
root = tk.Tk()
root.title("Parking Lot")

# Crear una instancia del navegador de imágenes
image_browser = ImageBrowser(root)

# Crear una instancia de la interfaz del parqueadero
parking_gui = ParkingGUI(root)

# Ejecutar la aplicación
root.mainloop()
