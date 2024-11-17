from python_tdd.funcoes import dividir_com_raise
import pytest


def test_dividir_por_zero():
    with pytest.raises(ZeroDivisionError):
        dividir_com_raise(10, 0)


def test_dividir_por_zero_2():
    with pytest.raises(ZeroDivisionError) as exec_info:
        dividir_com_raise(10, 0)
    assert "Não é possível dividir por zero." in str(exec_info)
