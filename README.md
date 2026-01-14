# TechFlow Solutions - Sistema de Gerenciamento de Logística

## 📌 Sobre o Projeto
Este projeto consiste no desenvolvimento de um sistema de gerenciamento de tarefas focado em uma startup de logística. O objetivo é permitir o acompanhamento de fluxos de trabalho em tempo real e a priorização de demandas críticas.


## 🎯 Escopo do Projeto
* **Módulo de Autenticação:** Login seguro para gestores e operadores.
* **Gestão de Tarefas (CRUD):** Criação, leitura, atualização e exclusão de entregas/tarefas.
* **Painel de Controle:** Visualização de status das operações.
* **Priorização:** Sistema de marcação de tarefas críticas.

## 🛠️ Metodologia Adotada
Utilizamos a metodologia ágil **Kanban**, focada em:
* **Visualização:** Uso do GitHub Projects para gerenciar o fluxo de trabalho.
* **Ciclos de Entrega:** Commits frequentes e organizados.
* **Qualidade:** Integração Contínua (CI) via GitHub Actions com testes automatizados.

## ⚠️ Gestão de Mudanças (Log de Alterações)


## 📋 Levantamento de Requisitos (Simulação de Entrevista)

Para alinhar as expectativas com a Startup de Logística, realizamos uma entrevista técnica. Abaixo, os principais pontos levantados:

**1. Qual o principal problema que o sistema deve resolver?** R: A falta de visibilidade em tempo real sobre em qual etapa da entrega cada motorista se encontra.

**2. Quem serão os usuários principais?** R: Gestores de frota (back-office) e operadores de galpão.

**3. O sistema deve permitir a criação de tarefas de entrega?** R: Sim, com descrição, destino e prioridade.

**4. Como as tarefas devem ser priorizadas?** R: Através de etiquetas: "Normal", "Urgente" e "Crítica".

**5. É necessário controle de login?** R: Sim, apenas usuários autorizados podem alterar o status de uma entrega.

**6. O que define uma tarefa como "Concluída"?** R: O registro da confirmação de entrega no destino final.

**7. O sistema precisa gerar relatórios de desempenho?** R: No MVP (mínimo produto viável), apenas o quadro Kanban para monitoramento visual é suficiente.

**8. Como será a gestão de mudanças durante o desenvolvimento?** R: Usaremos o GitHub Projects para adaptar o escopo conforme novas necessidades surjam.

**9. Existe alguma restrição tecnológica?** R: O código deve ser versionado no GitHub e possuir testes automatizados para garantir a qualidade.

**10. Qual a frequência de atualização do status das tarefas?** R: As atualizações devem ser imediatas assim que o status da operação mudar.

### 🛠️ Funcionalidades Implementadas
- [x] Criação de tarefas com ID e Destino.
- [x] Sistema de priorização (Alta, Normal, Baixa).
- [x] Armazenamento temporário em lista (CRUD básico).

## 🔄 Mudança de Escopo card 10#
Durante o desenvolvimento, identificamos a necessidade de destacar visualmente as cargas de prioridade "Alta". 
**Alteração:** O sistema agora prefixa o destino com "⚠️ URGENTE" automaticamente para essas tarefas, conforme nova solicitação do stakeholder.