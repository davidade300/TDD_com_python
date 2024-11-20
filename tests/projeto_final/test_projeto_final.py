import pytest  # noqa: F401
from database_manager import Cliente, DatabaseManager  # noqa: F401


@pytest.fixture
def get_db():
    db = DatabaseManager("tests\\projeto_final\\users.db")
    yield db


# falha a inclusão de forma proposial, datadecadastro errada
def test_inclusao_falha_com_dados_invalidos(get_db):
    cliente = Cliente(
        "david",
        "mail@mail.com",
        "999999999",
        "rua rua",
        "cidade cidade",
        "Estado est",
        "98765-123",
        "dataer",
        "1998-04-22",
    )

    result = get_db.incluir_cliente(cliente)
    assert result == "Falha na validação dos dados do cliente."


# verifica se o cliente está no bd
def test_cliente_existe_no_bd(get_db):
    result = get_db.verificar_cliente(id=1)

    # assert result checa para resultados que sejam "truthy"
    # (qualquer valor que seja equiparado a True quando convertido para um bool)
    assert result


def test_atualizacao_de_clientes(get_db):
    result = get_db.atualizar_cliente(id=1, campo="nome", valor="joãozinho")

    assert result
