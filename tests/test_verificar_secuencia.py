from src.prueba import verificarSecuencia

def test_verificar_secuencia():
    secuencia = [1,2,3,4,5,6]
    secuencia2 = [-1,0,4,5,7,2,4,3]
    secuencia3 = [1,4,5,2,3,2,5,2,6,2,7,8,1]

    assert 1 == verificarSecuencia(secuencia)
    assert 0 == verificarSecuencia(secuencia2)
    assert 0 == verificarSecuencia(secuencia3)