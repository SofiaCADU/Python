# Sofía Cáceres
# 31-03-2025
# Tengo 8 peluches de rana

import random

respuestas = ["✅ Si, definitivamante.", 
              "⭐ Con toda certeza, que si.", 
              "🔒 Sin lugar a duda.",
              "🤔 Respuesta confusa, inténtalo de nuevo.",
              "🕑 Preguntalo nuevamente más tarde.",
              "🤫 Mejor no dercirte ahora.",
              "✖️  Mis fuentes dicen que no.",
              "🌧️ El panorama no es muy favorable.",
              "🤷‍♂️ Muy dudoso."]

pregunta = input('pregunta:')

respuesta = random.randint(0,8)

if respuesta == 1 :
    print("respuesta:", "✅ Si, definitivamante.")
elif respuesta == 2:
    print("Respuesta:", "⭐ Con toda certeza, que si.")
elif respuesta == 3:
    print("Respuesta:", "🔒 Sin lugar a duda.")
elif respuesta == 4:
    print("Respuesta:", "🤔 Respuesta confusa, inténtalo de nuevo.")
elif respuesta == 5:
    print("Respuesta:", "🕑 Preguntalo nuevamente más tarde.")
elif respuesta == 6:
    print("Respuesta:", "🤫 Mejor no dercirte ahora.")
elif respuesta == 7:
    print("Respuesta:", "✖️  Mis fuentes dicen que no.")
elif respuesta == 8:
    print("Respuesta:", "🌧️ El panorama no es muy favorable.")
else:
    print("Respuesta:", "🤷‍♂️ Muy dudoso.")

