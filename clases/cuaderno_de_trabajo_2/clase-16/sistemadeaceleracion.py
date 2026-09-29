#Haz un sistema de aceleracion usando funciones donde cada vez
#presiones el acelerador aumenta a 10 km

def acelerar(velocidad_inicial):
    nueva_velocidad = velocidad_inicial + 10
    return nueva_velocidad

def desacelerar(velocidad_actual):
    nueva_velocidad = velocidad_actual - 10
    # Validacion para que la velocidad no sea negativa
    if nueva_velocidad < 0:
        nueva_velocidad = 0
    return nueva_velocidad


# Pedimos la velocidad inicial al usuario
velocidad = int(input("Ingrese su velocidad inicial: "))

# Acelerar
velocidad = acelerar(velocidad)
print("Después de acelerar tu velocidad es:", velocidad, "km/h")

# Desacelerar
velocidad = desacelerar(velocidad)
print("Después de desacelerar tu velocidad es:", velocidad, "km/h")