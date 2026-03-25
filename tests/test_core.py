import pytest
from src.core import validar_medicamento, calcular_estoque

def test_validacao_correta():
    assert validar_medicamento("Dipirona", 500) is True

def test_erro_dose_negativa():
    with pytest.raises(ValueError, match="A dose deve ser um número positivo."):
        validar_medicamento("Aspirina", -10)

def test_calculo_estoque_vazio():
    assert calcular_estoque(5, 10) == 0
