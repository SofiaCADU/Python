
pistas = ("Puerta roja", 221, "Londres", 3.14, "Watson", 7, "Moriarty")

print("🔎¡Bienvenido,detective Holmes!")
print("📜 Se ha encontrado una serie de pistas misteriosas...")
print("🗝️ Pistas encontradas:", pistas)

#📌 Analisis de pistas
print("\n 🕵️ Analizando las pistas...")

print("\n 🕵️ Felicitaciones, detective. ¡Has resuelto el analisis de las pistas!")
print("🔐 Ahora, sigue con las deducciónes para resolver el misterio")


# 1. ¿Cuál es la primera pista?
print(pistas[0])

# 2. ¿Cuál es la última pista?
print(pistas[-1])

# 3. ¿Cuántas pistas hay en total?
print(len(pistas))

# 4. ¿Está la palabra "Londres" en las pistas?
print('Londres' in pistas)

# 5. Desempaqueta las primeras tres pistas
a, b, c, d, e, f, g = pistas
print(a, b, c)

# 6. Crea una nueva tupla con pistas adicionales
pistasAdi = ("3:57", " quinto piso")

# 7. Encuentra la posición de "Watson"
print(pistas.index("Watson"))

# 8. ¿Cuántas veces aparece el número 7 en las pistas?
print(pistas.count("7"))