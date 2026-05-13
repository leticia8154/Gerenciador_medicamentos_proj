import os
import requests
from flask import Flask, render_template_string, request
from src.core import validar_medicamento

app = Flask(__name__)

# --- LÓGICA DE INTEGRAÇÃO COM API PÚBLICA (Requisito 1.2) ---
def buscar_endereco_por_cep(cep):
    """Consome a API ViaCEP para auxiliar idosos na localização de farmácias."""
    cep_limpo = "".join(filter(str.isdigit, cep))
    if len(cep_limpo) != 8:
        return None
    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep_limpo}/json/", timeout=5)
        dados = response.json()
        return dados if "erro" not in dados else None
    except Exception:
        return None

# --- INTERFACE WEB SIMPLES ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Gerenciador Melhor Idade</title>
    <style>
        body { font-family: sans-serif; background-color: #f0f2f5; display: flex; justify-content: center; padding: 50px; }
        .card { background: white; padding: 30px; border-radius: 12px; shadow: 0 4px 6px rgba(0,0,0,0.1); width: 400px; }
        h1 { color: #2c3e50; font-size: 20px; text-align: center; }
        .status { color: #27ae60; font-weight: bold; text-align: center; margin-bottom: 20px; }
        input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 6px; box-sizing: border-box; }
        button { width: 100%; padding: 10px; background: #3498db; color: white; border: none; border-radius: 6px; cursor: pointer; }
        .resultado { margin-top: 20px; padding: 10px; background: #e8f4fd; border-radius: 6px; color: #2980b9; font-size: 14px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>💊 Gerenciador Melhor Idade</h1>
        <p class="status">● Sistema Online</p>
        
        <form method="POST">
            <label>Validar Endereço de Entrega (CEP):</label>
            <input type="text" name="cep" placeholder="00000-000" required>
            <button type="submit">Consultar API</button>
        </form>

        {% if endereco %}
            <div class="resultado">
                <strong>📍 Localizado:</strong><br>
                {{ endereco }}
            </div>
        {% elif erro %}
            <div class="resultado" style="background: #fdeaea; color: #c0392b;">
                ⚠️ {{ erro }}
            </div>
        {% endif %}
        
        <hr style="margin-top: 30px; border: 0; border-top: 1px solid #eee;">
        <p style="font-size: 11px; color: #95a5a6; text-align: center;">Medisync © 2026 - Etapa Intermediária</p>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    endereco = None
    erro = None
    if request.method == 'POST':
        cep = request.form.get('cep')
        dados = buscar_endereco_por_cep(cep)
        if dados:
            endereco = f"{dados['logradouro']}, {dados['bairro']} - {dados['localidade']}/{dados['uf']}"
        else:
            erro = "CEP não encontrado ou inválido."
            
    return render_template_string(HTML_TEMPLATE, endereco=endereco, erro=erro)

# --- INICIALIZAÇÃO ---
if __name__ == "__main__":
    # O Render usa a variável de ambiente PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
