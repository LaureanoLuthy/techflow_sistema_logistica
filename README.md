# TechFlow Solutions - Sistema de Gerenciamento de Logística

## 📌 Sobre o Projeto
Este projeto consiste no desenvolvimento de um sistema de gerenciamento de tarefas focado em uma startup de logística. O objetivo é permitir o acompanhamento de fluxos de trabalho em tempo real e a priorização de demandas críticas.

## 🎯 Escopo do Projeto
* **Gestão de Tarefas (CRUD):** Criação e listagem de entregas/tarefas.
* **Priorização:** Sistema de marcação de tarefas críticas (Alta, Normal, Baixa).
* **Integração Contínua:** Testes automatizados rodando a cada atualização.

## 🛠️ Metodologia Adotada
Utilizamos a metodologia ágil **Kanban**, focada em:
* **Visualização:** Uso do GitHub Projects para gerenciar o fluxo de trabalho.
* **Ciclos de Entrega:** Commits frequentes e organizados (Conventional Commits).
* **Qualidade:** CI via GitHub Actions para garantir que o código esteja sempre funcional.

## 📋 Levantamento de Requisitos (Simulação de Entrevista)
Para alinhar as expectativas com a Startup de Logística, realizamos uma entrevista técnica. Abaixo, os principais pontos levantados:
1. **Problema Principal:** Falta de visibilidade em tempo real.
2. **Usuários:** Gestores de frota e operadores.
3. **Priorização:** Etiquetas "Alta", "Normal" e "Baixa".
4. **Qualidade:** Necessidade de testes automatizados e controle de versão.

## 🔄 Mudança de Escopo (Item 6 - Faculdade)
Durante o desenvolvimento, identificamos uma nova necessidade do stakeholder para agilizar a triagem visual.
* **Card Relacionado:** #10 (Simulação de mudança de escopo).
* **Alteração:** O sistema agora prefixa o destino com a tag "⚠️ URGENTE" automaticamente para cargas de prioridade "Alta".

### ✅ Funcionalidades Implementadas
- [x] Estrutura de pastas profissional (`/src`, `/tests`, `/docs`).
- [x] Criação de tarefas com ID e Destino.
- [x] Sistema de priorização automática.
- [x] Armazenamento temporário em lista (CRUD básico).
- [x] Pipeline de CI (GitHub Actions) configurado e passando.

## 🚀 Como rodar o projeto
1. Instale o Python.
2. Instale o Pytest: `pip install pytest`.
3. Para rodar os testes: `pytest tests/`.