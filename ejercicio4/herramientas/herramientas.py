
def celsius_a_fahr(t_celsius: float):
    return t_celsius * (9/5) + 32

def fahr_a_celsius(t_fahr: float):
    return (t_fahr - 32) * (5/9)

def celsius_a_kelvin(t_celsius: float):
    return t_celsius + 273

def kelvin_a_celsius(t_kelvin: float):
    return t_kelvin - 273

def fahr_a_kelvin(t_fahr: float):
    return celsius_a_kelvin(fahr_a_celsius(t_fahr))

def kelvin_a_fahr(t_kelvin: float):
    return celsius_a_fahr(kelvin_a_celsius(t_kelvin))