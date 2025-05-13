# Proyecto empezado el 07/05/25
# 13-05-25, 12:07p.m

from datetime import datetime

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

def agregar_libro():
    try:
        #Validar title:
        title = input("Ingrese el título: ")
        while True:
            if not title:
                print("El titulo no debe estar vacio")
                title = input("> Ingrese el título nuevamente: ")
            else:
                break

        #Validar author
        author = input("Agrege el autor: ")
        while not author.replace(" ", "").isalpha():
            print("El autor no debe estar vacio y solo tener letras")
            author = input("> Agrege el autor nuevamente: ")

        #Validar year_publication
        current_year = datetime.now().year
        year_publication = input("Ingrese el año de publicación: ")
        while True:
            if year_publication.isdigit() and 1300 <= int(year_publication) <= current_year:
                year_publication = int(year_publication)
                break
            else:
                print(f"El año debe estar entre 1300 y {current_year}")
                year_publication = input("> Ingrese el año de publicación nuevamente: ")

        # Validar que el genero no esté vacío
        genre = input("Ingrese el género: ")
        while not genre or not genre.isalpha():
            print("El género no debe estar vacio ni tampoco tener letras")
            genre = input("> Ingrese el género nuevamente: ")

        #Validar available
        available = input("Ingrese disponibilidad (SI o NO): ").strip().lower()
        while available not in ["si", "no"]:
            available = input("Error: sólo responda -> 'SI' ó 'NO': ").strip().lower()
        available = (available == "si")

        new_book = Book(title, author, year_publication, genre, available)
        catalogo.append(new_book)
        print(f"\u2705 Libro '{title}' añadido exitosamente!")
    
    except Exception as e:
        print(f"Error inesperado: {e}. Intente nuevamente.")


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
        1. Agregar nuevo libro
        2. Ver catálogo completo  
        3. Buscar libros por género  
        4. Prestar un libro  
        5. Devolver un libro  
        6. Salir 
        ''')
        try:       
            option = int(input(">>> "))
            if option == 1:
                agregar_libro() 
            elif option == 2:
                ver_catálogo_completo()
            elif option == 3:
                buscar_libros_genero()
            elif option == 4:
                prestar_libro()
            elif option == 5:
                devolver_libro()
            elif option == 6:
                salir()
                break
            else:
                print("Opción no válida. Ingrese 1-6.")
        except Exception as error:
            print("Ingrese una opción válida: ", error)

# Ejecutar el programa:
if __name__ == '__main__':
    main()
