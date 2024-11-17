from python_tdd.funcoes import fatorial  # noqa: F401
import pytest  # noqa: F401


@pytest.mark.parametrize("value, expected", [(0, 1), (1, 1), (4, 24), (5, 120)])
def test_fatorial(value, expected):
    assert fatorial(value) == expected


@pytest.mark.parametrize("entrada_negativa", [-1, -2, -10])
def test_negative_fatorial(entrada_negativa):
    with pytest.raises(RecursionError):
        fatorial(entrada_negativa)
