from src.prueba import contenidoColumna

def test_contenido_columna_tres():
    tablero = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
    ]

    assert contenidoColumna(3, tablero) == [2, 1, 2, 1, 2, 1]