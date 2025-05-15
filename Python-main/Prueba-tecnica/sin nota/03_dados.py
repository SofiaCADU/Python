#Sofía Cáceres
#30-04-2025
#Tengo sueño

import random

total = random.randint(1,6)+ random.randint(1,6)

adivinanza = int(input("¿Cual es el total (2-12)?: "))

while adivinanza != total:
    print(int(input("¿Cual es el total (2-12)?: ")))

print("Lo adivinaste")