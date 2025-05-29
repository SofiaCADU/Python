matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"}

]

ciudades = {

   "México": ["Ciudad de México", "Guadalajara", "Cancún"],

   "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}

coordenadas = [

   {"latitud": 8.2588997, "longitud": -84.9399704}

]

# Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]

matriz [1] [0] = 6
print(matriz)

# Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”

cantantes [0] ["nombre"] = "Enrique Martin Morales"
print(cantantes)

# En ciudades, cambia “Cancún” por “Monterrey”

ciudades ["México"] [2] = "Monterrey"
print(ciudades)

# En las coordenadas, cambia el valor de “latitud” por 9.9355431

coordenadas [0] ["latitud"] = 9.9355431
print(coordenadas)

print("\n Ejercicio 2.")
cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]

def iterarDiccionario(lista):
    for diccionario in lista:
        print("," .join(f"{key} - {value}" for key, value in diccionario.items()))
    
iterarDiccionario(cantantes)

print("\n Ejercicio 3.")
def iterarDiccionario2(artista, nac):
    for diccionario in nac:
        if artista in diccionario:
            print(diccionario[artista])
# ejemplo de uso
iterarDiccionario2("nombre", cantantes)
iterarDiccionario2("pais", cantantes)

print("\n Ejercicio 4.")
costa_rica = {

   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}

def iterarDiccionario3(diccionario):
    for clave, valores in diccionario.items():
        print(f"{len(valores)} {clave.upper()}")
        for valor in valores:
            print(valor)

print("\n Iterar a través de un diccionario con valores de la lista")
iterarDiccionario3(costa_rica)