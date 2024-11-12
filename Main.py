
class Asiento:
    def __init__(self, color, registro):
        self.color = color
        self.registro = registro

    def cambiarColor(self, color_elegido):
        if color_elegido in ("rojo", "verde", "amarillo", "negro", "blanco"):
            self.color = color_elegido


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, reg):
        self.registro = reg

    def asignarTipo(self, tip):
        if tip in ("electrico", "gasolina"):
            self.tipo = tip


class Auto:
    cantidadCreados = 0  # Atributo de clase

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos  # Lista de objetos Asiento
        self.marca = marca
        self.motor = motor  # Objeto Motor
        self.registro = registro
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        return sum(1 for asiento in self.asientos if isinstance(asiento, Asiento))

    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"

        for asiento in self.asientos:
            if not isinstance(asiento, Asiento) or asiento.registro != self.registro:
                return "Las piezas no son originales"

        return "Auto original"





