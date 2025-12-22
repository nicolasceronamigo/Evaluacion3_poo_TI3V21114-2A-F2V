from clases.vehiculo import Vehiculo

cargo_auto = 2000
cargo_auto_hora = 500
class Auto(Vehiculo):
    def cobrar(self, tiempo):
        return cargo_auto + tiempo * cargo_auto_hora