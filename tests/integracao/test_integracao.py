# testes de integração testam a integração entre diferentes componentes
# do sistema (oh rlly?).

from .app import Produto, Estoque


def test_adicionar_verificar_quantidade():
    estoque = Estoque()

    produto1 = Produto("mouse", 10)
    produto2 = Produto("teclado", 5)

    estoque.adicionar_produto(produto1)
    estoque.adicionar_produto(produto2)

    assert estoque.verifica_quantidade("mouse") == 10
    assert estoque.verifica_quantidade("teclado") == 5


def test_adicionar_produto_existente():
    estoque = Estoque()

    produto1 = Produto("mouse", 10)
    estoque.adicionar_produto(produto1)

    produto2 = Produto("mouse", 5)
    estoque.adicionar_produto(produto2)

    assert estoque.verifica_quantidade("mouse") == 15
    # assert estoque.verifica_quantidade("teclado") == 10
