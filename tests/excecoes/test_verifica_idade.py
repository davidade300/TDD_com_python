import pytest
from python_tdd.funcoes import verificade_idade


def test_verifica_idade_com_erro():
    with pytest.raises(ValueError):
        verificade_idade(17)


def test_verifica_idade_sem_erro():
    assert verificade_idade(20) == "Acesso permitido"
