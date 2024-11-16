import pytest
from python_tdd.classifica_idade import classifica_idade


@pytest.mark.parametrize(
    "idade,categoria_esperada",
    [(10, "Crianca"), (15, "Adolescente"), (30, "Adulto"), (70, "Idoso")],
)
def test_classifica_idade(idade, categoria_esperada):
    assert classifica_idade(idade) == categoria_esperada
