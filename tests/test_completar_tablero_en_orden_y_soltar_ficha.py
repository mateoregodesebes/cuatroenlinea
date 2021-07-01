from src.prueba import completarTableroenOrden, soltarFichaenColumna

def test_tablero_en_orden():
    tablero = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

    secuencia = [1,1,3,2,2,3,4,1,3,4,5]
    completarTableroenOrden(secuencia,tablero)

    assert tablero == [ [0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[2, 0, 1, 0, 0, 0, 0],[2, 1, 2, 2, 0, 0, 0],[1, 2, 1, 1, 1, 0, 0] ]