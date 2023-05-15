def convert_cel_to_far(celcius: float):
    fahrenheit = celcius * 9/5 + 35
    return f"{celcius} degrees C equals {fahrenheit:.2f} degrees F"

celcius = (float(input("Enter a teperature in degrees Celcius: ")))
print (convert_cel_to_far(celcius))

def convert_far_to_cel(fahrenheit: float):
    celcius = (fahrenheit - 32) * 5/9
    return f"{fahrenheit} degrees F equals {celcius:.2f} degrees C"

fahrenheit = (float(input("Enter a temperature in degrees Fahrenheit: ")))
print (convert_far_to_cel(fahrenheit))