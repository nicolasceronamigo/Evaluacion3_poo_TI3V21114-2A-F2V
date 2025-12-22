from clases.vehiculo import Vehiculo

cargo_camion = 2000
cargo_camion_hora = 1000
class Camion(Vehiculo):
    def cobrar(self, tiempo):
        return cargo_camion + tiempo * cargo_camion_hora