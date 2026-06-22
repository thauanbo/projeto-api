<img src="https://raw.githubusercontent.com/thauanbo/thauanbo/refs/heads/main/img/banner-project.png" alt="Banner" width="100%">

# Infraestrutura de API: Backend, Frontend e Proxy Reverso

Este projeto tem como objetivo demonstrar uma infraestrutura moderna de aplicações utilizando containers Docker, banco de dados relacional (MySQL), proxy reverso (Nginx) e análise de tráfego de rede (Wireshark).

## 📂 Estrutura do Projeto

projeto-api/
├── backend/          # API REST desenvolvida em Python (FastAPI)
├── frontend/         # Interface web estática
├── nginx/            # Configuração do Proxy Reverso
└── docker-compose.yml # Orquestração de todos os serviços

## 🚀 Tecnologias Utilizadas
Backend: Python (FastAPI)
Banco de Dados: MySQL 8.0
Proxy Reverso: Nginx
Orquestração: Docker Compose
Análise de Rede: Wireshark


## ⚙️ Como Executar o Projeto
Certifique-se de ter o Docker Desktop instalado em sua máquina.
Clone o repositório:
Bash
git clone [https://github.com/thauanbo/projeto-api.git](https://github.com/thauanbo/projeto-api.git)
cd projeto-api
Suba todo o ambiente:
Bash
docker-compose up --build
Acesse a aplicação:
Abra o navegador e acesse: http://localhost:8080

## 🛠️ Detalhes dos Serviços
Backend (API): Desenvolvido em FastAPI, expõe as rotas GET /usuarios e POST /usuarios.
Nginx: Atua como gateway. Redireciona requisições iniciadas em /api/ para a porta 8000 do container da API e serve o conteúdo estático do frontend na raiz.
Banco de Dados: MySQL configurado via Docker para persistência, com script de inicialização (init.sql) automático.

## 🔍 Análise de Tráfego (Wireshark)
Este projeto foi validado utilizando o Wireshark para capturar o fluxo de dados entre os serviços.
Protocolo: HTTP/JSON.
Ponto de Captura: Interface de rede Docker Bridge.
Análise: O tráfego POST e GET foi monitorado para confirmar a integridade das requisições entre o cliente e o banco de dados.
