# Sofía Cáceres
# 03-04-2025

altura = int(input('¿Cuál es tu altura? (cm)'))
credito = int(input('¿Cuanto crédito tienes?'))

if altura >= 137 and credito >= 10:
    print('disfruta tu viaje')
elif altura < 137 and credito >= 10:
    print('No tienes la altura suficiente')
elif altura >= 137 and credito < 10:
    print('No tienes el crédito suficiente')
else:
    print('No tienes la altura ni el crédito suficiente')


