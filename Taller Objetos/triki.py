# Clases y Objetos - PROBLEMA III y IV


class triki:

    def __init__(self):
        self.tablero = [["a", "a", "a"],
                        ["a", "a", "a"],
                        ["a", "a", "a"]]

    def marcarCasilla(self, simbolo, fila, columna):
        self.tablero[fila][columna] = simbolo

    def verificarGanador(self):
        ganadores = (
                        [(0, 0), (0, 1), (0, 2)],
                        [(1, 0), (1, 1), (1, 2)],
                        [(2, 0), (2, 1), (2, 2)],
                        [(0, 0), (1, 0), (2, 0)],
                        [(0, 1), (1, 1), (2, 1)],
                        [(0, 2), (1, 2), (2, 2)],
                        [(0, 0), (1, 1), (2, 2)],
                        [(0, 2), (1, 1), (2, 0)],
                    )

        for indexes in ganadores:
            fila = [self.tablero[f][c] for f, c in indexes]
            if all(cell == "X" for cell in fila):
                return "Ganador: X"
            if all(cell == "O" for cell in fila):
                return "Ganador: O"

        return "No hay ganadores"

    def verificarCasilla(self, fila, columna):
        return self.tablero[fila][columna]


x = triki()

print(x.tablero)
x.marcarCasilla("X",2,2)
x.marcarCasilla("X",1,2)
x.marcarCasilla("X",0,2)
print(x.tablero)
print(x.verificarGanador())
print(x.verificarCasilla(2,2))
