def tableroVacio():
    return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
def contenidoColumna(nro_columna, tablero):
    columna = []
    for fila in tablero:
        celda = fila[nro_columna - 1]
        columna.append(celda) 
    return columna

def todasColumnas(tablero):
    for x in range (1, 8):
        columna = []
        columna = contenidoColumna(x, tablero)
        print(columna)
    return
    
def todasFilas(tablero):
    print(tablero)

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

def dibujarTablero(tablero): # pragma: no cover
    cont = 0
    for x in tablero:
        print("|",x,"|") # Ignoro dibujarTablero en coverage debido a que no hay forma aparente de testear que funcione bien
        cont = cont + 1
        if(cont == 6):
            print("+-----------------------+")
        
def verificarSecuencia(secuencia):
    validez = 1
    for x in secuencia:
        if x < 1 or x > 7:
            validez = 0
    return validez

secuencia = [1, 2, 3, 1, 3]
tablero = []
if verificarSecuencia(secuencia) == 1:
    tablero = completarTableroenOrden(secuencia, tableroVacio())
    dibujarTablero(tablero)
    todasColumnas(tablero)
    todasFilas(tablero)

else:
    print("Al menos uno de los numeros de la secuencia de jugadas es inválido")
