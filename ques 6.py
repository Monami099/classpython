fahrenheit_temps = [32, 68, 77, 86, 104]
celsius_temps = [(f - 32) * 5 / 9 for f in fahrenheit_temps]
print("Temperatures in Fahrenheit:", fahrenheit_temps)
print("Equivalent Temperatures in Celsius:", celsius_temps)

Output:
Temperatures in Fahrenheit: [32, 68, 77, 86, 104]
Equivalent Temperatures in Celsius: [0.0, 20.0, 25.0, 30.0, 40.0]
