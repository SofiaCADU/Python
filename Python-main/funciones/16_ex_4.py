#Acceder a un valor en un diccionario 
#sin que se rompa el programa si la clave no existe

def buscar_cantante():
    cantante={
        "nombre" : "Luis Miguel",
        "pais" : "Puerto rico"
    }
    try:
        clave = input("¿Que quieres saber? (Nombre o pais)")
        print("Resultado:", cantante[clave])
    except KeyError:
        print("Esta clave no existe dentro del diccionario")

buscar_cantante()
