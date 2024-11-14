import pytest


class Pessoa:
    def __init__(
        self, nome: str, data_de_nascimento: str, sexo: str, altura: float
    ):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.sexo = sexo
        self.altura = altura

    def nome(self):
        return self.nome

    def data_de_nascimento(self):
        return self.data_de_nascimento

    def sexo(self):
        return self.sexo

    def altura(self):
        return self.altura


@pytest.fixture
def pessoa():
    return Pessoa(
        nome="adera",
        data_de_nascimento="19980422",
        sexo="masculino",
        altura="1,74",
    )


def test_pessoa(pessoa):
    assert pessoa.nome == "adera"
    assert pessoa.data_de_nascimento == "19980422"
    assert pessoa.sexo == "masculino"
    assert pessoa.altura == "1,74"
