#Mostrar un elemento de una lista por su posición, manejando si la
#posicion no existe

def mostrar_elementos():
    frutas = ["manzana", "banana", "naranja", "palta"]
    try:
        indice = int(input("elige una posicion (0 a 3): "))
        print("fruta elegida:", frutas[indice])
    except IndexError:
        print("Esta posición no existe en la lista")
    except ValueError:
        print("Porfavor, ingrese solo números")

mostrar_elementos()