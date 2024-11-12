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




