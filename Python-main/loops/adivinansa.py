# Sofía Cáceres
# 07-04-2025

adivinanza = 0

intentos = 0

while adivinanza != 6 and intentos < 5:
    adivinanza = int(input("Adivina el número: "))
    intentos += 1
if adivinanza != 6:
    print("Te quedaste sin intentos")
else:
    print("Adivinaste el número")
    print("Felicitaciones")