import tkinter as tk
from PIL import ImageTk, Image

class Vechiculo:
    def __init__(self, placa):
        self.placa = placa

class ParkingLot:
    def __init__(self):
        self.capacity = 60  # Capacidad del parking
        self.slots = [None] * self.capacity  # Inicializar todos los slots como vacíos

    def hash_function(self, placa):
        """
        Función de hash que determina el índice para almacenar un vehículo en la tabla hash.
        Utiliza la suma de los caracteres ASCII de la placa y aplica una operación módulo para obtener el índice.
        """
        total = sum(ord(char) for char in placa)
        return total % self.capacity

    def insert_Vechiculo(self, Vechiculo):
        """
        Inserta un vehículo en el parqueadero utilizando una tabla hash con manejo de colisiones.
        """
        index = self.hash_function(Vechiculo.placa)

        if self.slots[index] is None:
            self.slots[index] = Vechiculo
            print(f"Vehículo con placa {Vechiculo.placa} estacionado en el puesto {index}.")
        else:
            # Manejo de colisiones mediante búsqueda lineal
            i = index + 1
            while i != index:
                if i >= self.capacity:
                    i = 0  # Volver al principio del array

                if self.slots[i] is None:
                    self.slots[i] = Vechiculo
                    print(f"Vehículo con placa {Vechiculo.placa} se estaciono en el puesto {i}.")
                    return
                i += 1

            print("El parking está lleno. No se puede estacionar el vehículo.")

    def find_Vechiculo(self, placa):
        """
        Busca un vehículo en el parqueadero dado su número de placa.
        """
        index = self.hash_function(placa)

        if self.slots[index] is not None and self.slots[index].placa == placa:
            return index
        else:
            # Búsqueda lineal
            i = index + 1
            while i != index:
                if i >= self.capacity:
                    i = 0

                if self.slots[i] is not None and self.slots[i].placa == placa:
                    return i
                i += 1

        return None

    def remove_Vechiculo(self, placa):
        """
        Remueve un vehículo del parqueadero dado su número de placa.
        """
        index = self.find_Vechiculo(placa)

        if index is not None:
            self.slots[index] = None
            print(f"Vehículo con placa {placa} acaba de salir del parqueadero y ahora el puesto: {index} se encuentra disponible.")
        else:
            print("El vehículo no está estacionado en el parqueadero.")

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

# Crear la ventana principal
root = tk.Tk()
root.title("Navegador de Imágenes")

# Crear una instancia del navegador de imágenes
image_browser = ImageBrowser(root)

# Ejecutar la aplicación
root.mainloop()