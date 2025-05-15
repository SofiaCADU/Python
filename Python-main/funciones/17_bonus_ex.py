#Repetir hasta que lo hagan bien
#podemos usar bucle junto con un try

def pedir_numero_repetido():
    while True:
        try:
            numero = int(input("Escribe in numero entero:"))
            print("¡Gracias, Tu número es: ", numero)
            break
        except ValueError:
            print("Eso no es un numero valido")

pedir_numero_repetido()