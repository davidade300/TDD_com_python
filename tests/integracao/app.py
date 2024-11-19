class Produto:
    def __init__(self, nome: str, quantidade: int):
        self.nome = nome
        self.quantidade = quantidade


class Estoque:
    def __init__(self):
        self.produtos: dict = {}

    def adicionar_produto(self, produto: Produto):
        if produto.nome not in self.produtos:
            # acessa o produto pelo nome
            self.produtos[produto.nome] = produto.quantidade
        else:
            self.produtos[produto.nome] += produto.quantidade

    def verifica_quantidade(self, nome_produto: str):
        return self.produtos.get(nome_produto, 0)
