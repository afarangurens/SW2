# Herencia y Polimorfismo - PROBLEMA II

# Usando el concepto de herencia, diseñe una superclase que sirva como
# base para los elementos que contiene una biblioteca. Pista: Piense en
# que caracteristicas tienen en comun los libros, revistas, articulos y
# demas elementos presentes en cualquier biblioteca.


class Item:

    def __init__(self, titulo=None, descripcion=None):
        self.titulo = titulo
        self.descripcion = descripcion

    def ver_descripcion(self):
        return


class Libro(Item):
    def __init__(self, titulo, descripcion, autor, isbn):
        super().__init__(titulo, descripcion)
        self.autor = autor
        self.isbn = isbn

    def ver_descripcion(self):
        return "Titulo: {0} \nDescripción: {1} \nAutor: {2} \nISBN: {3}".format(
            self.titulo,
            self.descripcion,
            self.autor,
            self.isbn
        )

libro = Libro("Enigma", "Fiction", "Robert Harris", "978-0099527923")

print(libro.ver_descripcion())