import pytest


def soma_dobro(numeros):
    return sum(x * 2 for x in numeros)


@pytest.fixture
def lista():
    return [1, 2, 3, 4, 5, 6]


def test_soma_dobro(lista):
    resultado = soma_dobro(lista)
    assert resultado == 42


def test_soma_dobro_quando_lista_vazia(lista):
    lista.clear()
    resultado = soma_dobro(lista)
    assert resultado == 0, "a soma dos dobros de uma lista vazia deve ser 0"
