# Proyecto empezado el 07/05/25

# 06-05-25, 12:07p.m

class Book:
    def __init__(self, title, author, year_publication, genre, available):
        self.title = title
        self.author = author
        self.year_publication = year_publication
        self.genre = genre
        self.available = available

    def show_genre(self):
        return f'{self.genre}'
    
    def show_available(self):
        return self.available

    def show_info(self):
        return f'"{self.title.upper()}" - {self.author} ({self.year_publication}) - Genre: {self.genre} - Available: {"Yes" if self.available else "No"}'

libro1 = Book(
    title="Cien años de soledad",
    author="Gabriel García Márquez",
    year_publication=1967,
    genre="Realismo mágico",
    available=True
)

libro2 = Book(
    title="1984",
    author="George Orwell",
    year_publication=1949,
    genre="Distopía",
    available=False  # Ejemplo de libro prestado
)

libro3 = Book(
    title="Frankenstein",
    author="Mary Shelley",
    year_publication=1818,
    genre="Terror gótico",
    available=True
)

libro4 = Book(
    title="El Principito",
    author="Antoine de Saint-Exupéry",
    year_publication=1943,
    genre="Fábula",
    available=True
)

libro5 = Book(
    title="Dune",
    author="Frank Herbert",
    year_publication=1965,
    genre="Ciencia ficción",
    available=True
)

libro6 = Book(
    title="Guía del Autoestopista Galáctico",
    author="Douglas Adams",
    year_publication=1979,
    genre="Humor",
    available=True
)

libro7 = Book(
    title="Muerte con Pingüino",
    author="Andrei Kurkov",
    year_publication=1996,
    genre="Humor",
    available=True
)


catalogo = [libro1, libro2, libro3, libro4, libro5, libro6, libro7]


def ver_catálogo_completo():
    count = 0
    print("  === Catálogo ===  ")
    for x in catalogo:
        count += 1
        print(f'{count}. {x.show_info()}')
    

def buscar_libros_genero():
    genero = set(libro.genre for libro in catalogo)
    print("Géneros disponibles: " ,  ", ".join(genero))

    gen = input("Ingrese un género: ").strip()
    resultados = [genre for genre in catalogo if gen.lower() == genre.show_genre().lower()]

    if resultados:
        print("=== Resultados ===")
        for genre in resultados:
            print(f'- {genre.title} - {genre.author} ({genre.year_publication})')
    else:   
        print("No hay resultados")

    
def prestar_libro():
    title_book = input("Ingrese el título del libro a prestar: ").strip()
    for book in catalogo:
        if title_book == book.title:
            if book.available:
                print(f'¡Éxito! "{title_book}" ha sido prestado.')
                book.available = False
            else:
                print(f'Lo siento, "{title_book}" ya está prestado.')
            return
    print(f'Error: "{title_book}" no encontrado.')


def devolver_libro():
    title_book = input("Ingrese el título del libro a devolver: ").strip()
    for book in catalogo:
        if title_book == book.title:
            if not book.available:
                print(f'¡Muchas gracias! "{title_book}" ha sido devulto')
                book.available = True
            else:
                print(f'Error: "{title_book}" no estaba prestado.')
            return
    print(f'Error: "{title_book}" no encontrado.')


def salir():
    print("¡Gracias por usar la Biblioteca Python! Hasta pronto.")                


def main():
    while True:
        print(" === Biblioteca Python == ")
        print('''
        1. Ver catálogo completo  
        2. Buscar libros por género  
        3. Prestar un libro  
        4. Devolver un libro  
        5. Salir 
        ''')
        try:       
            option = int(input(">>> ")) 
            if option == 1:
                ver_catálogo_completo()
            elif option == 2:
                buscar_libros_genero()
            elif option == 3:
                prestar_libro()
            elif option == 4:
                devolver_libro()
            elif option == 5:
                salir()
                break
            else:
                print("Opción no válida. Ingrese 1-5.")
        except Exception as error:
            print("Ingrese una opción válida: ", error)

# Ejecutar el programa:
if __name__ == '__main__':
    main()
