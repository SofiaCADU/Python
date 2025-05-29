# Sofía Cáceres
# 02-04-2025
# ya me estoy estresando conlas ventas y lleva un par de horas de informado

respuesta = input('¿Estas cansado? (si o no): ').strip().lower()

cansado = respuesta == 'si'

if not cansado:
    print(' es hora de programar!!')
else:
    print('Tómate un descanso, lo necesitas')