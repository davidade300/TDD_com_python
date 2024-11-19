# Notas gerais

- Como executar o pytest de forma recursiva (sem indicar diretório ou quando o diretório não está no caminho de busca):

```bash
python -m pytest
```

## Assert

```python
assert 
```

- a função assert é uma fução python;
- verifica se uma condição é verdadeira;
- se falsa,retorna exceção AssertionError

## Fixtures

- Servem para configurar variáveis, conexões ou qualquer outra coisa que precisa ser usada durante todos os tetes;
- Elimina repetição de código;
- Economiza recursos;
- Pode estar dentro do teste ou em um arquivo de uso compartilhado global
  - Caso esteja em um arquivo de uso compartilhado o nome do arquivo deve, necessariamente, ser:
    - conftest.py
- Fixtures permitem criar um ambiente isolado para cada teste;
- Permitem gerenciar recursos antes e depois do teste;
- Permitem controlar o escopo;

### Setup e teardown com Fixtures

- Fixtures podem ser usadas para:
  - Preparação (setup);
  - Limpeza após testes (teardown);
    - Garante a limpeza dos recursos;
- Utiliza-se yield em fixtures para setup e teardown;

### Yield

- Usado em função para transforma-la em gerador;
- Permite produzir uma série de valores

```python

def contador(máximo):
    n = 0
    while n < maximo:
        yield n
        n += 1

# usando o gerador
for i in contador(5):
    print(i)
```

- Aparantemente utiliza-se yield mantém o estado daquilo que é yielded, por exemplo um arquivo que foi aberto e teve linhas escritas, caso queira em um momento posterior continuar a escrever nesse arquivo, no ponto em que o ponteiro parou, pode ser utilizado o yield (eu acho).

### Escopos de Fixtures

- O escopo define a vida útil de uma fixture (escopo == vida útil)
  - Sua inicialização e destruição(teardown)

- Existem cinco opções de escopo para uma fixture:
  - Function :
    - Padrão, criada e destruida para a função de teste que a utilizar
  - Class:
    - Cria e destroi uma vez para cada instância da Classe.
  - Module:
    - Cria e destroi uma vez para cada módulo ou arquivo de teste
  - Package:
    - Cria e destroi uma vez para cada Package.
  - Session:
    - Toda a seção de testes compartilha a mesma fixture.

## Testes Parametrizados

### Introdução à Parametrização de testes

- Executar testes com diferentes dados;
- Aumenta a cobertura do teste;
- Benefícios da parametrização:
  - Não precisa criar múltiplos casos de teste;
- decorador:

```python
    @pytest.mark.parametrize("a,b,resultado_esperado",[(a,b,resultado_esperado)])
```

## Marcadores

- Permitem organizar testes através de categorias;
- Atribuiímos "etiquetas" aos testes;
- Execução seletiva;

- Teste apenas certas funcionalidades:
  - conexões;
  - Carga de Dados;
  - Transformação;

- Tipos de teste:
  - Testes unitários;
  - Testes de integração;
  - Testes de interface de usuário (UI);
  - Testes de acesso a banco de dados;
  - Testes de API;

- Decorator:

```python
  @pytest.mark.nome_do_marcador
```

- Como executar só testes com marcadores:

```bash
  pytest -m nome_do_marcador
```

- Como executar todos os testes menos os com determinado marcador:

```bash
  pytest -m "no nome_do_marcador"
```

- o marcador -m, para marcadores, aceita operadores lógicos. Exemplo:

```bash
  pytest -m "nome_do_marcador_1 and nome_do_marcador_2"
  # executa testes que tenham dois marcadores (o marcador 1 e o marcador 2)

  pytest -m "nome_do_marcador_1 and not nome_do_marcador_2"
  # executa testes que tenh 
```

- Caso use poetry como gerenciador de pacotes, basta adicionar o seguinte antes do comando pytest:

```shell
  poetry run 
```

### Exemplos

- Sistema de gestão:
  - Emissão da Nota Fiscal;
  - Módulo Contábil;
  - Importação de arquivos

## Testes de exceções

```python
with pytest.raises(exception):
  ...
```

- Garante que o código responde a situações inesperadas;
- Usado em pontos do código que pode gerar exceções;

- Testa se o código gerado dentro da expressão with gera a exceção esperada e, caso gere, o teste passa.

## Plugins

- Adicionam funcionalidades extras ao pytest;
- Devem ser instalados pelo pip/ gerenciador de pacotes;

- Plugins populares:
  - Pytest-cov:
    - Para cobertura de código;
  - Pytest-asyncio:
    - Para testes assíncronos;
  - Pytest-html:
    - para gerar relatórios HTML;

- Comando:

```bash
# para testar tudo
  pytest --cov

# para testar a cobertura de um arquivo específico
  pytest --cov=arquivo_com_funcoes_a_ser_testadas arquivo_com_testes.py 
```

## Boas práticas em Testes

- O nome deve dizer claramente o que o teste faz

- Convenções de nomeação;
  - Test + componente + condição:
    - Ex.

    ```python
    def test_sum_positive_numbers_return_correct_result():
      ...
    ```

### Documentando Testes

- Uso de docstrings:

```python
  def test_sum_with_empty_list_returns_zero():
    """
    Testa se a função sum retorna 0 para uma lista
    vazia.
    """
      assert sum([]) == 0
```

### Testes em código legado

- Código legado normalmente não possui testes;
- Refatorar, caso exista e iniciar onde o risco de problema é maior são boas práticas.

## Testes de integração e End-to-End

- Testes de Unidade:
  - Testam funções isoladamente;
- Testes de Integração:
  - verificam como diferentes unidades de software trabalham juntas;
- Testes End-to-End:
  - Validam o fluxo do aplicativo do início ao fim, imitando o comportamento do usuário. Não necessáriamente a relação entre as funções.

## Introdução ao CI/CD

- Integração Contínua ( Continuos Integration) e Entrega/Implantação Contínua (Continuous Delivery/Deployment)
- Integração do Software com Frequência
- Cada Integração é Testada automaticamente
- benefícios:
  - Detecção precoce de erros;
  - Melhora na qualidade do software;
  - Agilidade no ciclo de lançamento.

### Pyteste no CI/CD

- Cada alteração do código verifica a qualidade automaticamente
- Ferramentas:
  - GitHub Actions;
  - Jenkins.
