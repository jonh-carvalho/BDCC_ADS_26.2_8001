# Como se organiza e se classifica modelos de dados quanto a arquitetura

## Modelos de Dados por Arquitetura

### 1. Arquitetura Centralizada
- **Descrição**: Todos os dados são armazenados em um único local central
- **Características**:
  - Facilidade de manutenção
  - Controle unificado de acesso
  - Risco único de falha

### 2. Arquitetura Distribuída
- **Descrição**: Dados distribuídos across múltiplos locais
- **Características**:
  - Alta disponibilidade
  - Redundância de dados
  - Complexidade de gerenciamento

### 3. Arquitetura Híbrida
- **Descrição**: Combinação de abordagens centralizada e distribuída
- **Características**:
  - Flexibilidade de implementação
  - Otimização de recursos
  - Compromisso entre custo e desempenho

## Classificação dos Modelos

### Por Nível de Abstração
1. **Modelo Conceitual**
   - Representa entidades e relacionamentos
   - Independente de implementação

2. **Modelo Lógico**
   - Estrutura dados em tabelas
   - Define relacionamentos e restrições

3. **Modelo Físico**
   - Implementação específica do banco de dados
   - Considera otimizações de performance

---

### Por Tipo de Dados
- **Dados Transacionais**
  - Registros de operações em tempo real
  - Estruturados para processamento rápido
  - Exemplos: vendas, transações financeiras

- **Dados Analíticos**
  - Dados históricos para análise e relatórios
  - Estruturados para consultas complexas
  - Exemplos: métricas de desempenho, tendências

- **Dados de Referência**
  - Informações estáticas usadas como base
  - Dados de dimensão em modelos analíticos
  - Exemplos: catálogos, códigos de erro, parâmetros do sistema

- **Dados Operacionais**
  - Dados utilizados no dia a dia das operações
  - Atualizados com frequência
  - Exemplos: registros de usuários, estoque, processos

- **Dados Históricos**
  - Registros de eventos passados
  - Armazenados para análise de tendências
  - Exemplos: logs, relatórios mensais, histórico de mudanças
  - Registros de operações
  - Atualizados em tempo real

- **Dados Analíticos**
  - Históricos para análise
  - Processamento em lote

---

