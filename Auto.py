from Asiento import Asiento
from Motor import Motor
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

        





# Crear un motor con un registro específico
motor1 = Motor(4, "gasolina", 1234)

# Crear asientos con registros coincidentes o no
asiento1 = Asiento("rojo", 1234)
asiento2 = Asiento("negro", 12434)
asiento3 = Asiento("azul", 1234)  # Este asiento tiene un registro diferente

# Crear un auto con un registro, motor y lista de asientos
auto1 = Auto("Sedán", 25000, [asiento1, asiento2, asiento3], "Toyota", motor1, 1234)

# Testear el método verificarIntegridad
print(auto1.verificarIntegridad())
 # Debería devolver "Las piezas no son originales"