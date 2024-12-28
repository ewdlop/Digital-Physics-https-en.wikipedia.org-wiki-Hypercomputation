import scipy.constants as const

# Planck units
planck_length = const.Planck_length
planck_time = const.Planck_time
planck_mass = const.Planck_mass
planck_temperature = const.Planck_temperature

# Conversion example: meters to Planck length
def meters_to_planck_length(meters):
    return meters / planck_length

# Conversion example: seconds to Planck time
def seconds_to_planck_time(seconds):
    return seconds / planck_time

# Conversion example: kilograms to Planck mass
def kilograms_to_planck_mass(kilograms):
    return kilograms / planck_mass

# Conversion example: Kelvin to Planck temperature
def kelvin_to_planck_temperature(kelvin):
    return kelvin / planck_temperature

# Example usage
meters = 1.0
seconds = 1.0
kilograms = 1.0
kelvin = 1.0

print(f"{meters} meters is {meters_to_planck_length(meters)} Planck lengths")
print(f"{seconds} seconds is {seconds_to_planck_time(seconds)} Planck times")
print(f"{kilograms} kilograms is {kilograms_to_planck_mass(kilograms)} Planck masses")
print(f"{kelvin} Kelvin is {kelvin_to_planck_temperature(kelvin)} Planck temperatures")
