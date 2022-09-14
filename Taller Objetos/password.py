# Clases y Objetos - PROBLEMA II

# Crear la clase Contrase~na que tenga como atributos Longitud (por
# defecto ser ́a 8) y Contrase~na (String). El constructor debe recibir
# la longitud y generar una contrase ̃na aleatoria con dicha longitud.
# La clase debe tener los siguientes m ́etodos:

import random
import string
import re


class contraseña:

    def __init__(self, longitud=8, clave=None):
        self.longitud = longitud
        self.clave = ''.join(random.choices(string.ascii_letters + string.digits, k=self.longitud))


    @classmethod
    def at_least_one_upper_or_lower_case(cls, clave):
        compiler = "^(?=.*?[A-Z])(?=.*?[a-z]).{8,}$"

        return re.fullmatch(compiler, clave)


    @classmethod
    def number_of_digits(cls, clave):
        return len(re.sub("[^0-9]", "", clave))


    def esFuerte(self):
        if  self.at_least_one_upper_or_lower_case(self.clave) and self.number_of_digits(self.clave) > 5:
            return True
        else:
            return False


    def cambiarContraseña(self, nuevaclave):
        self.longitud = len(nuevaclave)
        self.clave=nuevaclave

    def toString(self):
        return "Longitud: {0} \nClave: {1}".format(
            self.longitud,
            self.clave
        )


x  = contraseña(20)

print(x.toString())
print(x.esFuerte())
x.cambiarContraseña("Ab12345678")
print(x.toString())
print(x.esFuerte())