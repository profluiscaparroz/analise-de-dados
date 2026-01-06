# Análise de Regressão

## Visão Geral

Bem-vindo ao módulo de **Análise de Regressão**! Este diretório contém materiais completos e aprofundados sobre diferentes técnicas de regressão, cada uma em sua própria pasta com documentação detalhada, exemplos práticos e código Python.

A análise de regressão é uma das técnicas estatísticas mais fundamentais e amplamente utilizadas para modelar relações entre variáveis, fazer predições e entender padrões nos dados.

---

## 📚 Estrutura do Módulo

Este módulo está organizado seguindo o padrão BDD (Behavior-Driven Directory), onde cada tipo de regressão tem sua própria pasta contendo:

- **`docs/`** - Documentação teórica completa em Markdown e PDF
- **`src/`** - Notebooks Jupyter com exemplos práticos e código
- **`assets/`** - Imagens, gráficos e recursos adicionais (quando aplicável)

---

## 🎯 Tópicos de Regressão

### [01. Regressão Linear Simples](./01-regressao-linear-simples/)

**O que é:** Modelagem da relação entre uma variável dependente e UMA variável independente usando uma linha reta.

**Quando usar:**
- Relação linear entre duas variáveis
- Você quer entender como X afeta Y
- Predições simples e diretas

**Modelo matemático:**
```
Y = β₀ + β₁X + ε
```

**Exemplos práticos:**
- 🍦 Vendas de sorvete vs Temperatura
- 🏠 Preço de imóvel vs Área
- 📚 Nota vs Horas de estudo
- 🚗 Consumo de combustível vs Velocidade
- 💰 Salário vs Anos de experiência

**O que você vai aprender:**
- Método dos Mínimos Quadrados
- Interpretação de coeficientes
- Coeficiente de determinação (R²)
- Pressupostos do modelo
- Análise de resíduos
- Intervalos de confiança

**Navegação:**
- 📖 [Documentação Completa](./01-regressao-linear-simples/docs/README.md)
- 💻 [Notebook com Exemplos](./01-regressao-linear-simples/src/regressao_linear_simples_exemplos.ipynb)

---

### [02. Regressão Linear Múltipla](./02-regressao-linear-multipla/)

**O que é:** Extensão da regressão simples que permite modelar a relação entre uma variável dependente e MÚLTIPLAS variáveis independentes simultaneamente.

**Quando usar:**
- Fenômeno é influenciado por vários fatores
- Precisa controlar variáveis confundidoras
- Quer isolar o efeito de cada variável
- Análises mais realistas

**Modelo matemático:**
```
Y = β₀ + β₁X₁ + β₂X₂ + ... + βₚXₚ + ε
```

**Exemplos práticos:**
- 🏘️ Preço de imóveis (área, quartos, localização, idade, andar)
- 📊 Vendas (TV, rádio, internet, preço, concorrência)
- ⚡ Consumo de energia (temperatura, pessoas, área, aparelhos)
- 💵 Salário (experiência, educação, desempenho, cargo)
- 🌾 Rendimento agrícola (fertilizante, água, temperatura, pH)

**O que você vai aprender:**
- Interpretação de coeficientes parciais
- **Multicolinearidade** - Como detectar e tratar
- **VIF** (Variance Inflation Factor)
- Seleção de variáveis (Forward, Backward, Stepwise)
- R² Ajustado
- Critérios de informação (AIC, BIC)
- Análise de importância relativa

**Navegação:**
- 📖 [Documentação Completa](./02-regressao-linear-multipla/docs/README.md)

---

### [03. Regressão Polinomial](./03-regressao-polinomial/)

**O que é:** Extensão da regressão linear para modelar relações NÃO-LINEARES usando termos polinomiais (x, x², x³, etc.).

**Quando usar:**
- Relação entre X e Y tem curvatura
- Gráfico de dispersão mostra padrão curvo
- Resíduos da regressão linear mostram padrão
- Fenômenos com pontos de máximo/mínimo

**Modelo matemático:**
```
Grau 2: Y = β₀ + β₁X + β₂X² + ε
Grau 3: Y = β₀ + β₁X + β₂X² + β₃X³ + ε
```

**Exemplos práticos:**
- 🚗 Depreciação de veículos (perda rápida inicial, depois estabiliza)
- 👷 Produtividade vs Horas de trabalho (aumenta até certo ponto, depois cai)
- 📈 Crescimento de vendas de produto novo (curva S)
- 🌱 Rendimento vs Fertilizante (aumenta até ótimo, depois prejudica)
- 🌡️ Vendas de sorvete vs Temperatura (pico em temp. moderada-alta)

**O que você vai aprender:**
- Escolha do grau do polinômio
- Validação cruzada para seleção de grau
- **Overfitting vs Underfitting**
- Fenômeno de Runge
- Identificação de pontos críticos (máximos/mínimos)
- Comparação entre diferentes graus

**Navegação:**
- 📖 [Documentação Completa](./03-regressao-polinomial/docs/README.md)

---

### [04. Regressão Ridge (L2 Regularization)](./04-regressao-ridge/)

**O que é:** Técnica de regularização que adiciona penalização L2 (soma dos quadrados) aos coeficientes para resolver multicolinearidade e prevenir overfitting.

**Quando usar:**
- **Multicolinearidade severa** entre variáveis
- Muitas variáveis (p grande)
- p > n (mais variáveis que observações)
- Coeficientes OLS são instáveis
- Todas variáveis devem permanecer no modelo

**Modelo matemático:**
```
minimize: RSS + λΣβⱼ²
```

**Exemplos práticos:**
- 🏠 Preço de imóveis com 50+ características correlacionadas
- 📱 Marketing com 15 canais correlacionados
- 🧬 Previsão de doença com 10.000 genes (p >> n)
- 📉 Previsão de demanda com 30 lags correlacionados
- 💹 Análise econômica com indicadores macro correlacionados

**O que você vai aprender:**
- **Trade-off Viés-Variância**
- Como Ridge estabiliza coeficientes
- Encolhimento de coeficientes (shrinkage)
- Escolha de λ/α por validação cruzada
- **Ridge Path** - Evolução dos coeficientes
- Padronização de variáveis (crucial!)
- Comparação com OLS

**Diferencial:**
- ✅ Estabiliza coeficientes
- ✅ Funciona com p > n
- ✅ Reduz overfitting
- ❌ Não remove variáveis (mantém todas)

**Navegação:**
- 📖 [Documentação Completa](./04-regressao-ridge/docs/README.md)

---

### [05. Regressão Lasso (L1 Regularization)](./05-regressao-lasso/)

**O que é:** Técnica de regularização que adiciona penalização L1 (soma dos valores absolutos) e **zera coeficientes**, fazendo **seleção automática de variáveis**.

**Quando usar:**
- Muitas variáveis, poucas importantes
- **Precisa identificar** quais variáveis importam
- Quer modelo **simples e interpretável**
- Seleção de variáveis é objetivo principal
- Modelo esparso é desejável

**Modelo matemático:**
```
minimize: RSS + λΣ|βⱼ|
```

**Exemplos práticos:**
- 🧬 Identificar genes relevantes entre 10.000 (pesquisa médica)
- 📝 Selecionar palavras importantes entre 5.000 (text mining)
- 📢 Identificar 4 canais efetivos entre 20 (marketing)
- 🏘️ Selecionar 18 features importantes entre 100+ (preços de imóveis)
- 📊 Identificar lags relevantes entre 50 (séries temporais)

**O que você vai aprender:**
- **Seleção automática de variáveis** - Principal diferencial!
- **Esparsidade** e seus benefícios
- **Lasso Path** - Como variáveis são removidas
- Ordem de importância das variáveis
- Comparação com Ridge e OLS
- **Elastic Net** - Combinação de L1 e L2
- Instabilidade da seleção e como lidar

**Diferencial:**
- ✅ **Seleciona variáveis** automaticamente
- ✅ Modelo esparso e interpretável
- ✅ Identifica fatores importantes
- ✅ Reduz custos (menos variáveis)
- ❌ Pode remover variáveis correlacionadas importantes

**Navegação:**
- 📖 [Documentação Completa](./05-regressao-lasso/docs/README.md)

---

## 🗺️ Guia de Escolha Rápida

### Diagrama de Decisão

```
┌─────────────────────────────────────────┐
│  Que tipo de relação você tem?          │
└─────────────────┬───────────────────────┘
                  │
        ┌─────────┴──────────┐
        │                    │
     LINEAR              NÃO-LINEAR
        │                    │
        │              ┌─────┴─────┐
        │              │           │
        │         CURVATURA    COMPLEXO
        │              │           │
        │         POLINOMIAL   ML Methods
        │
        │
┌───────┴────────┐
│ Quantas vars?  │
└───────┬────────┘
        │
    ┌───┴───┐
    │       │
  UMA    MÚLTIPLAS
    │       │
 SIMPLES    │
            │
    ┌───────┴────────┐
    │ Problemas?     │
    └───────┬────────┘
            │
    ┌───────┴────────┬────────────┬──────────┐
    │                │            │          │
   NENHUM    MULTICOLIN.    MUITAS    SELEÇÃO
    │                │            │          │
MÚLTIPLA        RIDGE      RIDGE    LASSO
                                  (ou Elastic Net)
```

### Tabela Comparativa Rápida

| Método | Variáveis | Multicolinearidade | Seleção | Interpretação | Quando Usar |
|--------|-----------|-------------------|---------|---------------|-------------|
| **Linear Simples** | 1 | N/A | Não | ⭐⭐⭐⭐⭐ | Relação linear entre 2 variáveis |
| **Múltipla** | Múltiplas | Problemática | Manual | ⭐⭐⭐⭐ | Vários fatores, sem multicol. |
| **Polinomial** | 1+ | Moderada | Manual | ⭐⭐⭐ | Relações não-lineares com curvatura |
| **Ridge** | Muitas | Resolve | Não | ⭐⭐ | Multicol., p>n, manter todas vars |
| **Lasso** | Muitas | Parcial | **Sim** | ⭐⭐⭐⭐ | Seleção de vars, modelo esparso |

---

## 📖 Como Usar Este Módulo

### 1. **Para Iniciantes - Trilha Recomendada**

```
Semana 1-2: Regressão Linear Simples
├─ Entenda conceitos básicos
├─ Domine interpretação de coeficientes
├─ Aprenda análise de resíduos
└─ Pratique com exemplos reais

Semana 3-4: Regressão Linear Múltipla
├─ Expanda para múltiplas variáveis
├─ Aprenda multicolinearidade
├─ Domine seleção de variáveis
└─ Pratique casos complexos

Semana 5: Regressão Polinomial
├─ Entenda relações não-lineares
├─ Aprenda escolha de grau
├─ Pratique overfitting/underfitting
└─ Compare com linear

Semana 6-7: Ridge e Lasso
├─ Entenda regularização
├─ Aprenda quando usar cada um
├─ Domine validação cruzada
└─ Pratique seleção automática (Lasso)
```

### 2. **Para Profissionais - Referência Rápida**

Vá direto ao tipo de regressão que precisa:
- **Predição simples**: Linear Simples
- **Análise multivariada**: Múltipla
- **Curvatura nos dados**: Polinomial
- **Multicolinearidade**: Ridge
- **Seleção de variáveis**: Lasso

### 3. **Para Pesquisadores**

Cada documento contém:
- ✅ Fundamentação teórica completa
- ✅ Referências bibliográficas
- ✅ Fórmulas matemáticas detalhadas
- ✅ Discussão de pressupostos
- ✅ Limitações e cuidados

---

## 🔧 Tecnologias e Ferramentas

### Python - Bibliotecas Principais

```python
# Manipulação de dados
import numpy as np
import pandas as pd

# Visualização
import matplotlib.pyplot as plt
import seaborn as sns

# Machine Learning
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import r2_score, mean_squared_error

# Estatística
from scipy import stats
import statsmodels.api as sm
```

### Ambiente Recomendado

```bash
# Criar ambiente virtual
python -m venv venv_regressao
source venv_regressao/bin/activate  # Linux/Mac
# ou
venv_regressao\Scripts\activate  # Windows

# Instalar dependências
pip install numpy pandas matplotlib seaborn scikit-learn scipy statsmodels jupyter
```

---

## 📊 Conceitos Transversais

### Pressupostos da Regressão Linear

Todos os métodos de regressão linear (Simples, Múltipla, Polinomial, Ridge, Lasso) compartilham pressupostos básicos:

1. **Linearidade** - Relação linear entre X e Y (nos parâmetros)
2. **Independência** - Observações independentes
3. **Homocedasticidade** - Variância constante dos resíduos
4. **Normalidade** - Resíduos seguem distribuição normal
5. **Ausência de multicolinearidade** (para múltipla)

### Métricas Comuns

**R² (Coeficiente de Determinação)**
```
R² = 1 - (SSR/SST)
Interpretação: Proporção da variabilidade explicada
```

**RMSE (Root Mean Squared Error)**
```
RMSE = √(Σ(yᵢ - ŷᵢ)²/n)
Interpretação: Erro médio na mesma unidade de Y
```

**MAE (Mean Absolute Error)**
```
MAE = Σ|yᵢ - ŷᵢ|/n
Interpretação: Erro médio absoluto
```

### Workflow Típico de Regressão

```
1. Análise Exploratória
   ├─ Gráficos de dispersão
   ├─ Matriz de correlação
   └─ Estatísticas descritivas

2. Preparação dos Dados
   ├─ Tratamento de missing values
   ├─ Remoção de outliers (se necessário)
   ├─ Padronização (Ridge/Lasso)
   └─ Divisão treino/teste

3. Modelagem
   ├─ Escolha do tipo de regressão
   ├─ Ajuste do modelo
   └─ Otimização de hiperparâmetros

4. Validação
   ├─ Métricas de avaliação
   ├─ Análise de resíduos
   └─ Verificação de pressupostos

5. Interpretação e Comunicação
   ├─ Coeficientes
   ├─ Visualizações
   └─ Insights de negócio
```

---

## 🎓 Recursos Adicionais

### Livros Recomendados

1. **JAMES, Gareth et al.** *An Introduction to Statistical Learning*. 2. ed. Springer, 2021.
   - Excelente para iniciantes
   - Foco em aplicações práticas
   - Exemplos em R (conceitos aplicáveis a Python)

2. **HASTIE, Trevor; TIBSHIRANI, Robert; FRIEDMAN, Jerome.** *The Elements of Statistical Learning*. 2. ed. Springer, 2009.
   - Mais avançado
   - Fundamentação teórica profunda
   - Referência definitiva

3. **KUTNER, Michael H. et al.** *Applied Linear Statistical Models*. 5. ed. McGraw-Hill, 2005.
   - Foco em regressão aplicada
   - Muitos exemplos práticos

4. **MONTGOMERY, Douglas C.; PECK, Elizabeth A.; VINING, G. Geoffrey.** *Introduction to Linear Regression Analysis*. 5. ed. Wiley, 2012.
   - Tratamento completo de regressão
   - Diagnósticos detalhados

### Cursos Online

- **Coursera**: "Machine Learning" por Andrew Ng
- **edX**: "Data Science: Linear Regression" por Harvard
- **Kaggle Learn**: "Intro to Machine Learning"
- **Khan Academy**: Estatística e Probabilidade

### Datasets para Prática

- **Scikit-learn built-in**: california_housing, diabetes, fetch_openml('house_prices')
- **Kaggle**: House Prices (Ames), California Housing, Bike Sharing, etc.
- **UCI ML Repository**: Vários datasets de regressão
- **Statsmodels**: Datasets clássicos de estatística
- **Seaborn built-in**: tips, mpg, diamonds (para exemplos)

---

## 🤝 Contribuindo

Este material é parte do repositório de **Análise de Dados** e está em constante evolução.

### Como Contribuir

1. Relate erros ou sugestões via Issues
2. Proponha melhorias via Pull Requests
3. Adicione exemplos práticos
4. Melhore a documentação
5. Traduza para outros idiomas

### Padrão de Qualidade

Ao contribuir, mantenha:
- ✅ Explicações claras e didáticas
- ✅ Exemplos práticos do dia a dia
- ✅ Código comentado e executável
- ✅ Referências bibliográficas
- ✅ Formatação consistente

---

## 📜 Licença

Este material é disponibilizado sob licença MIT. Veja o arquivo LICENSE no repositório principal para mais detalhes.

---

## 📧 Contato e Suporte

Para dúvidas, sugestões ou discussões:
- **Issues**: Use o sistema de Issues do GitHub
- **Discussões**: Use GitHub Discussions
- **Email**: Via perfil do GitHub

---

## 🎯 Próximos Passos Recomendados

Após dominar regressão linear, explore:

### Modelos Relacionados
- **Regressão Logística** - Para variáveis categóricas
- **GLM** (Generalized Linear Models) - Extensão para distribuições não-normais
- **GAM** (Generalized Additive Models) - Relações não-lineares mais flexíveis
- **Modelos de Séries Temporais** - ARIMA, SARIMA, etc.

### Machine Learning
- **Árvores de Decisão e Random Forests**
- **Gradient Boosting** (XGBoost, LightGBM, CatBoost)
- **Redes Neurais** para regressão
- **Support Vector Regression (SVR)**

### Estatística Avançada
- **Regressão Não-Paramétrica**
- **Modelos Hierárquicos/Multinível**
- **Regressão Quantílica**
- **Modelos Bayesianos**

---

## 📚 Glossário Rápido

| Termo | Significado |
|-------|-------------|
| **Variável Dependente (Y)** | Variável que queremos prever/explicar |
| **Variável Independente (X)** | Variável(is) que usamos para prever Y |
| **Coeficiente (β)** | Parâmetro que quantifica relação entre X e Y |
| **Intercepto (β₀)** | Valor de Y quando X=0 |
| **Resíduo** | Diferença entre valor real e predito |
| **R²** | Proporção da variabilidade explicada (0-1) |
| **RMSE** | Raiz do erro quadrático médio |
| **Multicolinearidade** | Correlação entre variáveis independentes |
| **Overfitting** | Modelo muito complexo, memoriza treino |
| **Regularização** | Técnica para reduzir overfitting |
| **Esparsidade** | Muitos coeficientes são zero (Lasso) |
| **Validação Cruzada** | Técnica para avaliar generalização |

---

## ✅ Checklist de Aprendizado

Use este checklist para acompanhar seu progresso:

### Regressão Linear Simples
- [ ] Entendo o conceito de relação linear
- [ ] Sei interpretar coeficientes (β₀, β₁)
- [ ] Sei calcular e interpretar R²
- [ ] Sei fazer análise de resíduos
- [ ] Entendo pressupostos do modelo
- [ ] Consigo implementar em Python

### Regressão Linear Múltipla
- [ ] Entendo conceito de coeficientes parciais
- [ ] Sei detectar multicolinearidade (VIF)
- [ ] Conheço métodos de seleção de variáveis
- [ ] Sei usar R² ajustado
- [ ] Consigo interpretar modelo com múltiplas variáveis

### Regressão Polinomial
- [ ] Entendo quando usar polinomial vs linear
- [ ] Sei escolher grau do polinômio
- [ ] Entendo overfitting vs underfitting
- [ ] Sei identificar pontos críticos

### Ridge Regression
- [ ] Entendo conceito de regularização L2
- [ ] Sei quando usar Ridge
- [ ] Entendo trade-off viés-variância
- [ ] Sei escolher α por validação cruzada
- [ ] Lembro de padronizar variáveis

### Lasso Regression
- [ ] Entendo conceito de regularização L1
- [ ] Entendo seleção automática de variáveis
- [ ] Sei interpretar Lasso Path
- [ ] Sei quando usar Lasso vs Ridge
- [ ] Conheço Elastic Net

---

## 🎉 Conclusão

Este módulo oferece uma cobertura completa de técnicas de regressão, desde os fundamentos até métodos avançados de regularização. Cada tópico foi desenvolvido com:

✨ **Teoria sólida** - Fundamentação matemática e estatística  
✨ **Exemplos práticos** - Casos reais do dia a dia  
✨ **Código funcional** - Implementações completas em Python  
✨ **Visualizações** - Gráficos para melhor compreensão  
✨ **Boas práticas** - Workflow profissional

**Boa jornada de aprendizado! 📈🚀**

---

*Última atualização: Janeiro de 2026*  
*Repositório: Análise de Dados - Prof. Luis Caparroz*
