# Clases y Objetos - PROBLEMA I

# Crear la clase Persona que tenga como atributos Nombre, Edad,
# Genero (H hombre, M mujer), peso y altura. El constructor debe
# recibir todos los par ́ametros para su inicializaci ́on.
# La clase debe tener los siguientes m ́etodos:
import math

class Persona:

    def __init__(self, nombre=None, edad=0, genero=None, peso=0, altura=0):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.peso = peso
        self.altura = altura

    def calcularIMC(self):
        return round(self.peso/math.pow(self.altura/100, 2), 2)

    def esMayorDeEdad(self):
        return self.edad >= 18

    def toString(self):
        return "Nombre: {0} \nEdad: {1} \nGenero: {2} \nPeso: {3} \nAltura: {4}".format(
                                                                                        self.nombre,
                                                                                        self.edad,
                                                                                        self.genero,
                                                                                        self.peso,
                                                                                        self.altura
                                                                                        )


x = Persona("Turing", 12, "M", 123, 180)

print(x.calcularIMC())
print(x.esMayorDeEdad())
print(x.toString())
