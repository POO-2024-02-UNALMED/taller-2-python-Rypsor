class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
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
        if self.registro == self.motor.registro:
            for elemento in self.asientos:
                if elemento.registro != self.registro:
                    return("Las piezas no son originales")
                else:
                    return("Auto original")
        #Como el if no fue verdad, entonces retorne el siguiente texto
        return("Las piezas no son originales")

        