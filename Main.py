class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color_elegido):
        """
        Cambia el color del asiento solo si es un color permitido.
        """
        if color_elegido in ("rojo", "verde", "amarillo", "negro", "blanco"):
            self.color = color_elegido


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, reg):
        """
        Cambia el registro del motor.
        """
        self.registro = reg

    def asignarTipo(self, tip):
        """
        Cambia el tipo del motor a 'electrico' o 'gasolina'. Otros valores son ignorados.
        """
        if tip in ("electrico", "gasolina"):
            self.tipo = tip


class Auto:
    cantidadCreados = 0  # Atributo de clase para contar los autos creados

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        if not isinstance(motor, Motor):
            raise TypeError("motor debe ser una instancia de la clase Motor")
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos  # Lista de objetos Asiento o None
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        """
        Retorna la cantidad de objetos Asiento válidos en la lista de asientos.
        """
        return sum(1 for asiento in self.asientos if isinstance(asiento, Asiento))

    def verificarIntegridad(self):
        """
        Verifica que el registro del auto, motor y cada asiento sea el mismo.
        Retorna 'Auto original' si todos coinciden, de lo contrario, 'Las piezas no son originales'.
        """
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"

        for asiento in self.asientos:
            if asiento and asiento.registro != self.registro:
                return "Las piezas no son originales"

        return "Auto original"
        