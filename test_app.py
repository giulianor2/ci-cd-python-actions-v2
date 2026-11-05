from app import adicionar, subtrair, multiplicar


def test_adicionar():
    """Verifica se a função adicionar funciona corretamente."""
    assert adicionar(1, 2) == 3
    assert adicionar(-1, 1) == 0
    assert adicionar(0, 0) == 0


def test_subtrair():
    """Verifica se a função subtrair funciona corretamente."""
    assert subtrair(5, 3) == 2
    assert subtrair(10, 20) == -10


def test_multiplicar():
    """Verifica se a função multiplicar funciona corretamente."""
    assert multiplicar(4, 5) == 20
    assert multiplicar(3, 0) == 0
    assert multiplicar(-2, 3) == -6
