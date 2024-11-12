class Asiento:
    def __init__(self, color, registro):
        self.color = color
        self.registro = registro

    def cambiarColor(self, color_elegido):
        if color_elegido in ("rojo","verde","amarillo","negro","blanco"):
            self.color = color_elegido





