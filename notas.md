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
    @pytest.mark.parametrize
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
