# Sofía Cáceres
# 15-04-2025

# 1) Basico
for i in range(101):
    print(i)
# Este código imprime los números del 0 al 99 en la consola.

# 2) Multiples de 2
for par in range(2, 501, 2):
    print(par)
# Este código imprime los números pares del 2 al 100 en la consola.

# 3) Contando Vanilla Ice
for vanilla in range(1, 101):
    if vanilla % 10 == 0:
        print('baby')
    elif vanilla % 5 == 0:
        print('ice ice')
    else:
        print(vanilla)
# Este código imprime los números del 1 al 100, pero reemplaza los múltiplos de 5 por "ice ice" y los múltiplos de 10 por "baby".

# 4) Wow. Número gigante a la vista
suma = sum(range(1, 500001, 2))
print(f"la suma total es: {suma}")