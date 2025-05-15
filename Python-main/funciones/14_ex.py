#division segura

#objetivo: Dividir entre 2 números y evitar o alertar
#si el usuario quiere dividir entre 0

def division_segura():
    try:
        num1 = int(input("ingresa un número: "))
        num2 = int(input("ingresa otro número: "))
        resultado = num1 / num2
        print("El resultado de la division es:", resultado)
    except ZeroDivisionError:
        print("Lo sentimos, no se puede realizar esta division")
    except ValueError:
        print("Error. Solo debes ingresar números")

division_segura()