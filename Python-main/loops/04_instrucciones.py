# Instrucciones else
contador = 0

while contador < 10:
    print(contador)
    contador += 1

else:
    print('dejo de contar')

# Instrucciones break
contador = 0
while contador < 5:
    contador += 1

    if (contador == 4):
        print('Se rompio el bucle')
        break

    print(contador)

# Instrucciones continue
contador = 0

while contador < 5:
    contador += 1
    if (contador == 3):
        continue
    print(contador)