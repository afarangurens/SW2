# Herencia y Polimorfismo - PROBLEMA I

# Modele mediante el uso de clases y herencia la organización al interior
# de una universidad (profesores, alumnos, directivos, empleados, . . . )
# Utilice la siguiente clase como base para las dem ́as:

class Persona:

    def __init__(self, nombre=None, apellidos=None, edad=0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def __str__(self):
        return "Nombre: {0} \nApellidos: {1} \nEdad: {2}".format(
            self.nombre,
            self.apellidos,
            self.edad
        )


class Estudiante(Persona):
    pass


class Profesor(Persona):
    pass


class Directivo(Persona):
    pass


class Empleado(Persona):
    pass


x = Estudiante("A", "B", 13)
print(x.__str__())
x = Profesor("C", "D", 14)
print(x.__str__())
x = Directivo("E", "F", 15)
print(x.__str__())
x = Empleado("G", "H", 16)
print(x.__str__())

