import pytest
from python_tdd.classifica_idade import classifica_idade


@pytest.mark.crianca
def test_for_crianca():
    assert classifica_idade(12) == "Crianca"


@pytest.mark.adolescente
def test_for_adolescente():
    assert classifica_idade(15) == "Adolescente"


@pytest.mark.adulto
def test_for_adulto():
    assert classifica_idade(21) == "Adulto"


@pytest.mark.idoso
def test_for_idoso():
    assert classifica_idade(60) == "Idoso"
