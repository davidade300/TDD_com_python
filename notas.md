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