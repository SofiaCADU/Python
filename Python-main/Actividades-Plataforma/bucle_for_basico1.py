# Sofía Cáceres
# 15-04-2025

# 1) Basico
print("\n Ejercicio 1. Basico")
for i in range(101):
    print(i)
# Este código imprime los números del 0 al 99 en la consola.

# 2) Multiples de 2
print("\n Ejercicio 2. Multiple")
for par in range(2, 501, 2):
    print(par)
# Este código imprime los números pares del 2 al 100 en la consola.

# 3) Contando Vanilla Ice
print("\n Ejercicio 3. Vanilla Ice")
for vanilla in range(1, 101):
    if vanilla % 10 == 0:
        print('baby')
    elif vanilla % 5 == 0:
        print('ice ice')
    else:
        print(vanilla)
# Este código imprime los números del 1 al 100, pero reemplaza los múltiplos de 5 por "ice ice" y los múltiplos de 10 por "baby".

# 4) Wow. Número gigante a la vista
print("\n Ejercicio 4. Numero gigante")
suma_total = 0
for i in range(1, 500001, 2):
    suma_total += i
print(suma_total)
# imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.

# 5) Regresame al 3
print("\n Ejercicio 5. Tres")
for i in range(2024, 0, -3):
    print(i)
# imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.

# 6) Contador dinámico
print("\n Ejercicio 6. Multiplo")
numInicial = 3
NumFinal = 10
Multiplo = 2
for i in range(numInicial, NumFinal + 1):
    if i % Multiplo == 0:
        print(i)
# Este código imprime los números entre numInicial y NumFinal que son múltiplos de Multiplo.