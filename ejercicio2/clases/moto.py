from clases.vehiculo import Vehiculo

cargo_moto = 1000
cargo_moto_hora = 200
class Moto(Vehiculo):
    def cobrar(self, tiempo):
        return cargo_moto + tiempo * cargo_moto_hora