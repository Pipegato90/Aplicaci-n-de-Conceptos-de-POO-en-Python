# Clase base: Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        # Atributos encapsulados (privados)
        self.__marca = marca  # Encapsulación: __marca no es accesible directamente desde fuera de la clase
        self.__modelo = modelo  # Encapsulación: __modelo no es accesible directamente desde fuera de la clase

    # Método público para obtener la marca (getter)
    def get_marca(self):
        return self.__marca

    # Método público para obtener el modelo (getter)
    def get_modelo(self):
        return self.__modelo

    # Método para mostrar información del vehículo
    def mostrar_info(self):
        return f"Vehículo: {self.__marca} {self.__modelo}"


# Clase derivada: Coche (hereda de Vehiculo)
class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        # Llamada al constructor de la clase base
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas  # Atributo adicional de la clase derivada

    # Sobrescritura del método mostrar_info (Polimorfismo)
    def mostrar_info(self):
        # Llama al método de la clase base y añade información adicional
        return f"{super().mostrar_info()}, Puertas: {self.num_puertas}"


# Función para demostrar polimorfismo con argumentos múltiples
def mostrar_informacion_vehiculo(vehiculo):
    print(vehiculo.mostrar_info())


# Creación de instancias y demostración de funcionalidad
if __name__ == "__main__":
    # Instancia de la clase base (Vehiculo)
    mi_vehiculo = Vehiculo("Toyota", "Corolla")
    print(mi_vehiculo.mostrar_info())  # Salida: Vehículo: Toyota Corolla

    # Instancia de la clase derivada (Coche)
    mi_coche = Coche("Ford", "Mustang", 2)
    print(mi_coche.mostrar_info())  # Salida: Vehículo: Ford Mustang, Puertas: 2

    # Demostración de polimorfismo
    print("\nDemostración de polimorfismo:")
    mostrar_informacion_vehiculo(mi_vehiculo)  # Llama al método de la clase base
    mostrar_informacion_vehiculo(mi_coche)  # Llama al método sobrescrito de la clase derivada

    # Acceso a atributos encapsulados (usando getters)
    print("\nAcceso a atributos encapsulados:")
    print(f"Marca del vehículo: {mi_vehiculo.get_marca()}")
    print(f"Modelo del vehículo: {mi_vehiculo.get_modelo()}")