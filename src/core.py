# src/core.py
def validar_medicamento(nome, dose):
    if not nome or len(nome.strip()) < 2:
        raise ValueError("Nome do medicamento inválido.")
    if dose <= 0:
        raise ValueError("A dose deve ser um número positivo.")
    return True

def g_estoque(atual, consumo):
    if consumo > atual:
        return 0
    return atual - consumo
