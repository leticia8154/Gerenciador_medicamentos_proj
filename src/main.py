# src/main.py
import requests
from src.core import validar_medicamento

def buscar_cep(cep):
    """Integração com a API ViaCEP"""
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        if "erro" in dados:
            return None
        return f"{dados['logradouro']}, {dados['bairro']} - {dados['localidade']}/{dados['uf']}"
    except:
        return "Erro na conexão com a API."

def principal():
    print("="*30)
    print("GERENCIADOR MELHOR IDADE v2.0")
    print("="*30)
    
    nome = input("Nome do Medicamento: ")
    try:
        dose = float(input("Dose (mg): "))
        if validar_medicamento(nome, dose):
            print(f"✅ {nome} validado!")
            
            # Nova funcionalidade da Etapa Intermediária:
            op = input("\nDeseja validar CEP para entrega? (s/n): ")
            if op.lower() == 's':
                cep = input("Digite o CEP: ")
                endereco = buscar_cep(cep)
                print(f"📍 Endereço: {endereco if endereco else 'CEP inválido.'}")
                
    except ValueError as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    principal()
