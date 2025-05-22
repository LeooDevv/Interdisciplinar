# N2 Interdisciplinar

## 📌 Objetivo do Projeto
Desenvolver uma aplicação em **Python** que simule o comportamento de **filas com múltiplos servidores (_modelo M/M/c_)**, utilizando dados reais ou simulados (_CSV_). O projeto envolve análise estatística dos dados e aplicação de metodologias ágeis de desenvolvimento com base no **Scrum**.

## 🏥 Contexto do Projeto
**Restaurante universitário**
**Central de suporte técnico**

---

## 🔢 Pesquisa Operacional
### 🖥️ Implementação
1. Ler um arquivo CSV com dados de **tempo entre chegadas** e **tempo de atendimento**
2. Simular o funcionamento de um sistema de **filas M/M/c**
3. Calcular as seguintes métricas:
   - **P₀**: Probabilidade do sistema estar vazio
   - **Pₑₛₚₑᵣₐ**: Probabilidade de espera
   - **Lₓ, Wₓ, W, L**: Indicadores de tempo e ocupação

### 📊 Visualizações
Gráficos de:
- Tempo de espera por cliente
- Tamanho da fila ao longo do tempo
- Tempo de ocupação dos servidores

### 📂 Entregáveis
- Código-fonte (_simulacao.py_)
- Arquivo **resultados.csv** gerado pela simulação
- Relatório técnico (**relatorio_operacional.pdf**), contendo:
  - Resultados das métricas calculadas
  - Gráficos da simulação
  - Respostas às perguntas:
    - Vale a pena adicionar mais um servidor?
    - Qual seria o impacto de um atendente mais rápido (_μ maior_)?

---

## 📊 Estatística
### 📌 Análise dos Dados
1. Estatísticas descritivas dos tempos de atendimento e espera:
   - Média, Mediana, Moda, Variância, Desvio padrão
2. Visualizações gráficas:
   - Histogramas dos tempos de atendimento e espera
   - **Boxplot** comparando tempos de atendimento e espera
3. Inferência estatística:
   - Intervalo de confiança para:
     - Média do tempo de atendimento
     - Média do tempo de espera

### 📂 Entregáveis
- Código-fonte (_analise_estatistica.py / .ipynb_)
- Relatório estatístico (**relatorio_estatistico.pdf**) com:
  - Resultados das análises estatísticas
  - Interpretação dos gráficos
  - Sugestões de melhorias no atendimento

---

## 🏗️ Engenharia de Software
### 📜 Metodologia Scrum
1. **Papéis Scrum**:
   - **Product Owner**: responsável pelo backlog
   - **Scrum Master**: guia os ritos Scrum
   - **Time de Desenvolvimento**: implementa o projeto

2. **Backlog do Produto** (exemplo de itens):
   - **PB1**: Ler o CSV com Pandas - _Sprint 1_
   - **PB2**: Simular fila com múltiplos servidores - _Sprint 1_
   - **PB3**: Calcular métricas da fila - _Sprint 1_
   - **PB4**: Gerar gráficos da simulação - _Sprint 2_

3. **Planejamento por Sprint**:
   - Sprint 1: implementação da base funcional
   - Sprint 2: análises estatísticas e gráficos
   - Sprint 3: finalização e interface

4. **Quadro Kanban** (_Trello, Planner_) para organização das tarefas.

5. **Cerimônias Scrum**:
   - Sprint Planning (definição de tarefas)
   - Daily Scrum (registro semanal de progresso)
   - Sprint Review (entregas)
   - Retrospective (aprendizados)

### 📂 Entregáveis
- Relatório Scrum (**relatorio_scrum.pdf**) contendo:
  - Backlog do produto
  - Prints das cerimônias Scrum
  - Prints do quadro Kanban

---

## 📝 Versionamento (_Git/GitHub_)
### 📜 Boas práticas
- **Repositório Git** com histórico organizado
- **Commits** separados por tarefa e com mensagens claras
- **Branches** para cada componente (_simulacao, estatistica, interface_)

---

## 🏁 Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/Interdisciplinar/Interdisciplinar.git

