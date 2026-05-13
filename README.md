# Gerenciador de Medicamentos - CicloMedi💊

> **Link Oficial do Deploy:** [https://gerenciador-medicamentos-proj.onrender.com/](https://gerenciador-medicamentos-proj.onrender.com/)

[![CI Pipeline](https://github.com/leticia8154/Instrucoes_medicamentos_proj/actions/workflows/ci.yml/badge.svg)](https://github.com/leticia8154/Instrucoes_medicamentos_proj/actions)

## 🌟 Problema Real
Muitos idosos têm dificuldade em gerenciar múltiplos medicamentos, resultando em doses esquecidas ou duplicadas. 

## 🚀 Solução (CicloMedi)
Uma aplicação web intuitiva para validar medicamentos e organizar a rotina de medicação, integrada com a **API ViaCEP** para logística de entrega e localização de endereços.

## 🛠️ Tecnologias e Ferramentas
- **Linguagem:** Python 3.11
- **Framework Web:** Flask
- **Servidor de Produção:** Gunicorn
- **Integração:** API Pública ViaCEP (Consumo de dados externos)
- **Qualidade de Código:** Ruff (Linter) e Pytest (Testes Unitários/Integração)
- **CI/CD:** GitHub Actions (Automação de testes e análise)
- **Hospedagem:** Render (Cloud PaaS)

## 📂 Estrutura de Diretórios
- `src/`: Código-fonte principal da aplicação (Flask + Lógica de Core).
- `testes/`: Scripts de testes automatizados e integração com API.
- `.github/workflows/`: Configurações do pipeline de CI/CD.
- `requirements.txt`: Lista de dependências do projeto.

## 🔧 Como Executar Localmente
1. Clone o repositório: `git clone https://github.com/leticia8154/Instrucoes_medicamentos_proj.git`
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute a aplicação: `python src/main.py`

## 📝 Autora
Letícia Araújo
