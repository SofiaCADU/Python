
class Personaje:
    # nombre = "Default"
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0
    #Primer
    def __init__ (self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    #Segundo
    def atributos (self):
        print(self.nombre, ";", sep = "")
        print("fuerza:", self.fuerza)
        print("inteligencia:", self.inteligencia)
        print("defensa:", self.defensa)
        print("vida:", self.vida)
    #Tercero
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    #Cuarto
    def esta_vivo(self):
        return self.vida > 0
    #Quinto
    def __morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
    #SextoF
    def daño (self, enemigo):
        return self.fuerza - enemigo.defensa
    #Septimo
    def atacar (self, enemigo):
        daño = self.daño (enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        # print("la vida de", enemigo.nombre, "es de", enemigo.vida)
        if enemigo.esta_vivo():  #muestra si el enemigo esta o no muerto.
            print("La vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()
    def get_fuerza(self):
        return self.fuerza
    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("Error. La fuerza no puede ser negativa")
        else:
            self.fuerza = fuerza

class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Mata dragones, daño  10: "))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Ingresa una opcion valida")
    def atributos(self):
        super().atributos()
        print("Espada:", self.espada)
        def daño (self, enemigo):
            return self.fuerza * self.espada - enemigo.defensa
        
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
        def atributos(self):
            super().atributos()
            print("Libro:", self.libro)
        def daño (self, enemigo):
            return self.inteligencia * self.libro - enemigo.defensa



Kaldrogo = Guerrero("Kalrogo", 20, 30, 20, 100, 5)
mi_personaje = Personaje("Sofía", 10, 20, 10, 100)
Gandalf = Mago("Gandalf", 20, 30, 20, 100, 5)


mi_personaje.atacar(Kaldrogo)
Kaldrogo.atacar(Gandalf)
Gandalf.atacar(mi_personaje)

Kaldrogo.atributos()
print("_________________________________________")
mi_personaje.atributos()
print("_________________________________________")
Gandalf.atributos()
print("_________________________________________")


# Kaldrogo.cambiar_arma
# Kaldrogo.atributos()
# print(Kaldrogo.espada)

# mi_personaje = Personaje("Sofía", 10, 20, 10, 100)
# mi_enemigo = Personaje("Tiempo", 8, 5, 3, 5)
# mi_personaje.atributos()














# mi_personaje.atributos() # muestra los datos por default
# mi_personaje.subir_nivel(1,2,0)
# mi_personaje.nombre = "aionliz"
# mi_personaje.fuerza = 20
# print(mi_personaje)
# print("el nombre del jugador es: ", mi_personaje.nombre)
# print("la fuerza del jugador es: ", mi_personaje.fuerza)
# mi_personaje.atributos() #muestra los datos actualizados
# mi_enemigo.atributos()
# print(mi_personaje.esta_vivo())
# mi_personaje.morir()
# print(mi_personaje.daño(mi_enemigo))
# # mi_personaje.atacar(mi_enemigo)
# # mi_personaje.atributos()
# # mi_enemigo.atributos()
# # mi_personaje.fuerza = 0
# # mi_personaje.atributos()
# # mi_personaje.morir()
# mi_personaje.atacar(mi_enemigo)
# print(mi_personaje.get_fuerza(-5))
