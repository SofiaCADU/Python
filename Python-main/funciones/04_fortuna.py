# Sofía Cáceres
# 14-04-2025

import random

opciones = ['No pérsigas la felicidad, créala.',
           'Todas las cosas son dificiles antes de ser felices.',
           'El pajaro madrugador consige el gusano, pero el segundo raton se lleva el quedo.',
           'alguen en tu vida necesita una carta de tu parte.',
           'no solo pienses, ¡actua!',
           'Tu corazon se acelera',
           'La galleta que buscas esta en otra galleta'
           '¡Ayuda! ¡Estoy prisionero en una panaderia china!']


def fortuna():
    fortuna = random.randint(0, len(opciones)-1)
    print(opciones[fortuna])

fortuna()