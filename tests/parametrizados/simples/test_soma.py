import pytest
from python_tdd.soma import soma


# o primeiro argumento é a cobertura dos testes que queremos
# o segundo argumento é a cobertura, os valores são passados através de tuplas
@pytest.mark.parametrize("a,b,esperado", [(1, 2, 3), (4, 5, 9), (10, 20, 30)])
def test_soma(a, b, esperado):
    """
    passamos como string a cobertura dos testes que queremos e como uma
    lista de tuplas os valores que queremos testar, dessa forma, não é
    preciso criar multiplos casos de teste.
    nesse caso queremos afirmar que para 'a' e 'b' o resultado é
    'esperado'
    """
    assert soma(a, b) == esperado
