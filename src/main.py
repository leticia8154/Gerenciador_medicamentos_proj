from flask import Flask
app = Flask(__name__)

import requests
from src.core import validar_medicamento

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url, timeout=5)
        dados = response.json()
        return dados if "erro" not in dados else None
    except:
        return None

def principal():
    print("="*40)
    print(" GERENCIADOR DE MEDICAMENTOS - MELHOR IDADE ")
    print("="*40)
    
    nome = input("Nome do Medicamento: ")
    try:
        dose = float(input("Dose (mg): "))
        if validar_medicamento(nome, dose):
            print(f"✅ Medicamento {nome} validado!")
            
            print("\n--- Entrega (API ViaCEP) ---")
            cep = input("Digite seu CEP para entrega: ")
            endereco = buscar_cep(cep)
            
            if endereco:
                print(f"📍 Endereço localizado: {endereco['logradouro']}, {endereco['localidade']}/{endereco['uf']}")
            else:
                print("❌ CEP não encontrado.")
    except ValueError as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    principal()
