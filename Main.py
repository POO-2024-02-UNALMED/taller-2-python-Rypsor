
class Asiento:
    def __init__(self, color, registro):
        self.color = color
        self.registro = registro

    def cambiarColor(self, color_elegido):
        if color_elegido in ("rojo","verde","amarillo","negro","blanco"):
            self.color = color_elegido


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, reg):
        self.registro = reg

    def asignarTipo(self, tip):
        if tip == "electrico":
            self.tipo = tip
        elif tip == "gasolina":
            self.tipo = tip
        else:
            pass


class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        contador = 0
        for i in self.asientos:
            if isinstance(i,Asiento):
                contador += 1
        return contador
    
    def verificarIntegridad(self):
        reg_auto = self.registro
        if reg_auto != self.motor.registro:
            return "Las piezas no son originales"
            
        else:
            verificador = 0
            for asiento in self.asientos:
                if asiento.registro != reg_auto:
                    verificador = 1
            if verificador == 0:
                return "Auto original"
            else:
                return "Las piezas no son originales"

        





