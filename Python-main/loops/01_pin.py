# Sofía Cáceres
# 07-04-2025
# Fui a la feria

print('BANCO DEL 4°B')

pin = int(input('Ingresa tu PIN: '))

while pin != 1234:
    pin = int(input('PIN incorrecto. Ingresa tu pin nuevamente: '))

if pin == 1234:
    print('PIN correcto. Bienvenido al banco del 4°B')
    print('Bienvenido a tu cuenta')

