def tableroVacio():
    return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
def completarTableroenOrden(secuencia, tablero):
    x = 1
    for element in secuencia:
        soltarFichaenColumna(x, element, tablero)
        if x == 1:
            x = 2
        elif x == 2:
            x = 1
    return tablero

def soltarFichaenColumna(ficha, columna, tablero):
    for fila in range (6, 0, -1):
        if tablero[fila - 1][columna - 1] == 0:
            tablero[fila - 1][columna - 1] = ficha
            return

def dibujarTablero(tablero):
    for x in tablero:
        print(x)
        
secuencia = [1, 2, 3, 1]
dibujarTablero(
        completarTableroenOrden(
            secuencia, tableroVacio()
        )
)