#ultimo ejercicio del dia

#no pueden salir de la sala

#aprovechen el tiempo que tienen para avanzar en los 
#proyectos de la feria TP

def funcion(a, b, *args, **kwargs):
    print("a=", a)
    print("b=", b)
    for arg in args:
        print("arg=", arg)
    for key, value in kwargs.items():
        print(key, "=", value)

funcion(1, 2, 14, 21, 24, 36, 37, x="Luis", y = "Sol de mexico", c = "mexico")
