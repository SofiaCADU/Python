tareas = ["🏦 Sacar dinero del banco.",
          "🪣 Hacer la colada.",
          "🌳 Dar un paseo.",
          "💈 Cortarse el pelo.",
          "🍵 Preparar un té.",
          "💻 Terminar el capitulo de Listas.",
          "💖 Llamar a mamá.",
          "📺 Ver Mi Héroe Academia."]

#Desbloquear la primera misión
print(tareas[0])

#Encontrar la tarea oculta
print(tareas[1])

#Recuperar la sección oculta
print(tareas[1:4])

#Error detectado, crea un error
indice = tareas.index("Pasear al perro")

#Desafio extra "el haquer de la lista"
tareas.insert(1,"Pasear al perro")
print(tareas)