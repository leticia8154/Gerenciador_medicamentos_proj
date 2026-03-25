def validar_medicamento(nome, dose):
    """Valida se os dados do medicamento são aceitáveis."""
    if not nome or len(nome.strip()) < 2:
        raise ValueError("Nome do medicamento inválido.")
    if dose <= 0:
        raise ValueError("A dose deve ser um número positivo.")
    return True

def calcular_estoque(atual, consumo):
    """Calcula quanto resta no estoque após uma dose."""
    if consumo > atual:
        return 0
    return atual - consumo
