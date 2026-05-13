from src.main import buscar_cep

def test_api_viacep_sucesso():
    # Testa se a API retorna o endereço correto para um CEP real
    resultado = buscar_cep("01001000")
    assert resultado is not None
    assert resultado['localidade'] == "São Paulo"

def test_api_viacep_erro():
    # Testa se o sistema lida com CEP que não existe
    resultado = buscar_cep("00000000")
    assert resultado is None
