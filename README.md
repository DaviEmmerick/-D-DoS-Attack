# 🚀 DoS/DDoS - Simulação de Carga & Resiliência de API

🎯 Sobre o Projeto

Este repositório é um laboratório prático para demonstrar os conceitos de um ataque de Negação de Serviço, protocolos e a importância de testes de carga (Load Testing).

O objetivo é entender como uma API (FastAPI) reage ao ser submetida a um alto volume de requisições simultâneas disparadas por outra aplicação (Flask).

O projeto está dividido em duas partes principais:

API Alvo (FastAPI): Um servidor simples que representa o "alvo" do teste. Ele possui um endpoint que simula um pequeno tempo de processamento antes de responder.

Controlador/Atacante (Flask): Uma aplicação web com uma interface simples (um botão) que, ao ser acionada, dispara um "ataque" DoS, enviando milhares de requisições assíncronas para a API Alvo.

# ✨ Funcionalidades

1. Painel de Controle (Flask): Uma interface web minimalista para iniciar a simulação de carga com um único clique

2. Cliente de Teste Assíncrono: Utiliza httpx e asyncio para disparar um grande volume de requisições em paralelo, simulando de forma eficiente múltiplos usuários/fontes.

3. Execução em Thread: O processo de "ataque" é executado em uma thread separada para não bloquear a interface do Flask, permitindo que o servidor continue responsivo.

4.  Alvo (FastAPI): Um endpoint de exemplo que serve como "vítima" para o teste


# ✏️ Tecnologias/Libs Utilizadas

• Python

• Flask

• FastAPI

• HTTPX

• Asyncio

• Threading:

## 🚀 Como Rodar o Projeto

Você precisará de dois terminais abertos para rodar este projeto.

1️⃣ Crie e ative um ambiente virtual:
É altamente recomendado criar um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

2️⃣ Clone o repositório e acesse a pasta correta:

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_DIRETORIO>
```

3️⃣ Instalação:

```bash
pip install -r requirements.txt
```

4️⃣ Execução

No Terminal 1 (Inicie a API Alvo): Assumindo que seu arquivo FastAPI

```
uvicorn fastapi_target:app --port 8001
```

No Terminal 2 (Inicie o Controlador): Assumindo que seu arquivo Flask se chama flask_controller.py

```
flask --app flask_controller run --port 5000
```

# ✨ Implementações Futuras

-> Implementar Rate Limiting (limitação de taxa) no FastAPI como uma contramedida para mitigar o ataque.

-> Adicionar um dashboard simples ao Flask (talvez com WebSockets) para mostrar o status do ataque em tempo real.

-> Dockerizar as aplicações (Flask e FastAPI) usando docker-compose para facilitar a execução.

-> Inserir um template para deixar visual a requisição 
