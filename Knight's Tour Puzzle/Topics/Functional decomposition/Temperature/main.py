def fahrenheit_to_celsius(temps_f):
    temps_c = (temps_f - 32) * 5 / 9
    return round(temps_c, 2)


def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)


def main():
    """Entry point of the program."""
    temperature, unit = input().split()  # read the input

    if unit == 'F':
        converted_temp = fahrenheit_to_celsius(int(temperature))
        new_unit = 'C'
    elif unit == 'C':
        converted_temp = celsius_to_fahrenheit(int(temperature))
        new_unit = 'F'

    print(converted_temp, new_unit)



