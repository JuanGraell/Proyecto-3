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
            print(f"Vehículo con placa {placa} acaba de salir del parqueadero y ahora el puesto: {slot} se encuentra disponible.")
        else:
            print("El vehículo no está estacionado en el parqueadero.")

# Ejemplo de uso
parking = ParkingLot()

# Insertar vehículos
Vechiculo1 = Vechiculo(input("Ingrese la placa del vehiculo: "))
parking.insert_Vechiculo(Vechiculo1)


# Buscar vehículo
slot = parking.find_Vechiculo(input("Ingrese la placa del vehiculo que desea encontrar: "))
if slot is not None:
    print(f"El vehículo se encuentra estacionado en el puesto: {slot}.")
else:
    print("El vehículo no está estacionado en el parqueadero.")

# Remover vehículo
remover=parking.remove_Vechiculo(input("Ingrese la placa del vehiculo que salio del parqueadero: "))
