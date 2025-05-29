class Libro:
    #inicializar sin inicializar
    # titulo = "Sin titulo"
    # autor = "Desconocido"
    # paginas = 0
    # genero = "Indefinido"
    # Copias_disponibles = 0

    def __init__(self, titulo, autor, paginas, genero, copias_disponibles):  #
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.genero = genero
        self.Copias_disponibles = copias_disponibles

    def atributos(self):
        print(self.titulo, ":" , sep="")
        print("*Autor:", self.autor) 
        print("*Páginas:", self.paginas)
        print("*Género:", self.genero)
        print("*Copias disponibles:", self.Copias_disponibles)
    
    def incrementar_copias(self, nuevas_copias):
        self.Copias_disponibles = self.Copias_disponibles + nuevas_copias
    
    def esta_disponible(self):
        self.Copias_disponibles > 0

    def agotado(self):
        self.Copias_disponibles == 0
        print(self.titulo, "está agotado")

    def prestar(self, copias = 1):
        if self.Copias_disponibles >= copias:
            self.Copias_disponibles -= copias
            print(f"Se han prestado {copias} copia(s) de '{self.titulo}'.")
        else:
            print(f"No hay suficientes copias disponibles de '{self.titulo}' para prestar.")








mi_libro = Libro("El principito", "Antoine de Saint-Exupéry", 154, "cuento", 5)  #Haci se crea un objeto de la clase Libro

print("n ===Prestar copias===")
mi_libro.prestar(2)  #Haci se presta 2 copias del libro
mi_libro.atributos() 

# mi_libro.atributos()
# mi_libro.agotado()  #Haci se llama al método agotado, que verifica si el libro está agotado
# print("¿Esta disponible?", mi_libro.esta_disponible())  #Haci se llama al método esta_disponible, que verifica si el libro está disponible

# mi_libro.incrementar_copias(300)  #Haci se incrementa las copias disponibles
# print("\n -----------------------")
# print("Atributos despues de incremento")
# mi_libro.atributos()  #Vuelve a mostrar los atributos del libro con las copias actualizadas

# mi_libro.titulo = "Principito"  #Haci se modifica los atributos
# mi_libro.autor = "Antoine de Saint-Exupéry"  #Haci se modifica los atributos

# print("\n -----------------------")
# print(mi_libro)
# print("El título del libro es:", mi_libro.titulo) #Este llama al atributo título
# print("El autor del libro es:", mi_libro.autor)  #y este al atributo autor

   