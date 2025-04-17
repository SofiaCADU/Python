# Sofía Cáceres
# 16-04-2025

def calculadora (operacion,    a, b):
    if operacion == 'suma':
        return a + b
    elif operacion == 'resta':
        return a - b
    elif operacion == 'multiplicación':
        return a * b
    elif operacion == 'división':
        return a / b
    elif operacion == 'potencia':
        return a ** b
    else:
        return 'Operación no válida'

respuesta = calculadora('suma', 5, 3)
print(respuesta)

respuesta1 = calculadora('resta', 5, 3)
print(respuesta1)

respuesta2 = calculadora('multiplicación', 5, 3)
print(respuesta2)

respuesta3 = calculadora('división', 5, 3)
print(respuesta3)

respuesta4 = calculadora('potencia', 5, 3)
print(respuesta4)