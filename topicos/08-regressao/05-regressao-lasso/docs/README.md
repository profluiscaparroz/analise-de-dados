# Regressão Lasso (L1 Regularization)

## Sumário

1. [Introdução](#introdução)
2. [O Que é Lasso?](#o-que-é-lasso)
3. [Conceitos Fundamentais](#conceitos-fundamentais)
4. [Modelo Matemático](#modelo-matemático)
5. [Seleção Automática de Variáveis](#seleção-automática-de-variáveis)
6. [Parâmetro de Regularização (λ ou α)](#parâmetro-de-regularização-λ-ou-α)
7. [Vantagens e Desvantagens](#vantagens-e-desvantagens)
8. [Lasso vs Ridge vs OLS](#lasso-vs-ridge-vs-ols)
9. [Exemplos do Dia a Dia](#exemplos-do-dia-a-dia)
10. [Implementação em Python](#implementação-em-python)
11. [Elastic Net](#elastic-net)
12. [Casos Práticos](#casos-práticos)
13. [Limitações e Cuidados](#limitações-e-cuidados)
14. [Referências](#referências)

---

## Introdução

A **Regressão Lasso** (*Least Absolute Shrinkage and Selection Operator*) é uma técnica de regularização que, além de encolher coeficientes como o Ridge, pode **zerá-los completamente**, realizando **seleção automática de variáveis**.

### Por que Lasso é Importante?

Em muitos problemas do mundo real:
- Temos **centenas ou milhares** de variáveis potenciais
- Apenas **algumas são realmente importantes**
- Precisamos **identificar** quais variáveis usar
- Queremos um modelo **simples e interpretável**

Lasso resolve todos esses problemas!

### Diferença Chave: Ridge vs Lasso

```
Ridge (L2):
• Encolhe coeficientes → próximos de zero
• NUNCA zera coeficientes
• Mantém todas as variáveis

Lasso (L1):
• Encolhe coeficientes → próximos de zero
• PODE zerar coeficientes ✓
• Remove variáveis não importantes
```

### Aplicações Principais

✅ **Genômica**: Identificar genes relevantes entre milhares  
✅ **Text Mining**: Selecionar palavras importantes  
✅ **Finance**: Escolher indicadores econômicos  
✅ **Marketing**: Identificar canais efetivos  
✅ **Medicina**: Descobrir fatores de risco principais

---

## O Que é Lasso?

### LASSO = Least Absolute Shrinkage and Selection Operator

**Proposto por:** Robert Tibshirani (1996)

**Objetivo Duplo:**
1. **Shrinkage** (Encolhimento) - Regularização como Ridge
2. **Selection** (Seleção) - Zera coeficientes de variáveis não importantes

### Intuição Geométrica

**Ridge (penalização L2):**
- Restringe coeficientes a uma **esfera**
- Coeficientes raramente são exatamente zero
- Todos permanecem no modelo

**Lasso (penalização L1):**
- Restringe coeficientes a um **diamante** (ou losango)
- Coeficientes frequentemente tocam os **vértices** (onde alguns são zero)
- Variáveis são removidas automaticamente

### Visualização 2D

```
Ridge (círculo):              Lasso (diamante):
      |                             /\
   ●  |  ●                         /  \
  ────●────  ← sempre interior   ● ── ● ← toca vértices!
   ●  |  ●                         \  /
      |                             \/
      
Solução OLS: ●                Vértice = 1 coef. é ZERO
```

---

## Conceitos Fundamentais

### Regularização L1

**Definição:** Penalização pela **soma dos valores absolutos** dos coeficientes.

$$\text{Penalização L1} = \lambda \sum_{j=1}^{p}|\beta_j|$$

**Características:**
- Não diferenciável em β = 0
- Promove **esparsidade** (muitos coeficientes zero)
- Efetua seleção de variáveis

### Esparsidade (Sparsity)

**Esparsidade** = Muitos coeficientes são exatamente zero

**Exemplo:**
```
Modelo com 100 variáveis:
OLS:    100 coeficientes não-zero
Ridge:  100 coeficientes pequenos (mas não-zero)
Lasso:  15 coeficientes não-zero, 85 zeros ← ESPARSO
```

**Benefícios:**
✅ Modelo mais simples  
✅ Mais interpretável  
✅ Menos overfitting  
✅ Reduz custos (menos variáveis para coletar)

### Seleção de Variáveis

Lasso faz seleção **automaticamente** como parte da otimização:
- **Não requer** métodos stepwise
- **Não requer** decisões ad-hoc
- **Não requer** múltiplos ajustes de modelos

**Exemplo:**
```python
# Lasso com α=0.1
modelo = Lasso(alpha=0.1)
modelo.fit(X, y)

# Variáveis selecionadas automaticamente
vars_selecionadas = X.columns[modelo.coef_ != 0]
print(f"Selecionadas: {list(vars_selecionadas)}")
# Output: ['Area', 'Quartos', 'Localizacao']
# Idade, Distancia, Andar foram REMOVIDAS (coef = 0)
```

---

## Modelo Matemático

### Função Objetivo

Lasso minimiza:

$$\hat{\beta}^{lasso} = \arg\min_{\beta} \left\{ \sum_{i=1}^{n}(y_i - \beta_0 - \sum_{j=1}^{p}\beta_j x_{ij})^2 + \lambda \sum_{j=1}^{p}|\beta_j| \right\}$$

Ou em notação compacta:

$$\hat{\beta}^{lasso} = \arg\min_{\beta} \left\{ ||\mathbf{y} - \mathbf{X}\beta||_2^2 + \lambda ||\beta||_1 \right\}$$

Onde:
- **||y - Xβ||₂²** = Soma dos quadrados dos resíduos (RSS)
- **||β||₁** = Norma L1 = Σ|βⱼ| (soma dos valores absolutos)
- **λ** = Parâmetro de regularização (λ ≥ 0)

### Forma de Otimização Restrita

Equivalentemente, Lasso pode ser expresso como:

$$\text{minimize} \quad \sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$
$$\text{sujeito a} \quad \sum_{j=1}^{p}|\beta_j| \leq t$$

Onde **t** controla o nível de regularização.

### Diferença nas Penalizações

| Método | Penalização | Forma Geométrica | Esparsidade |
|--------|-------------|------------------|-------------|
| **OLS** | Nenhuma | - | Não |
| **Ridge** | Σβⱼ² (L2) | Esfera | Não |
| **Lasso** | Σ\|βⱼ\| (L1) | Diamante | **Sim** |

### Por que L1 Gera Esparsidade?

**Geometricamente:**
- Região restrita de Lasso tem **vértices**
- Elipses de RSS frequentemente tocam os **vértices**
- Nos vértices, pelo menos um coeficiente é zero

**Algebricamente:**
- Derivada de |β| não existe em β=0
- Algoritmo de otimização "empurra" coeficientes pequenos para exatamente zero

### Não Há Solução Fechada

Diferente de Ridge, Lasso **não tem solução analítica**.

**Algoritmos usados:**
- **Coordinate Descent** (mais comum)
- **LARS** (Least Angle Regression)
- **Proximal Gradient Descent**

---

## Seleção Automática de Variáveis

### Como Lasso Seleciona?

À medida que λ aumenta:

```
λ = 0:    Todos coeficientes ≠ 0 (igual OLS)
λ pequeno: Alguns coeficientes → 0
λ médio:   Muitos coeficientes = 0
λ grande:  Quase todos = 0
λ → ∞:    Todos coeficientes = 0
```

### Ordem de Remoção

Variáveis são removidas em **ordem de importância**:
1. Primeiro: variáveis menos correlacionadas com Y
2. Último: variáveis mais importantes

### Lasso Path

Visualização de como coeficientes evoluem com λ:

```python
from sklearn.linear_model import lasso_path

alphas, coefs, _ = lasso_path(X, y, alphas=alphas_range)

plt.plot(alphas, coefs.T)
plt.xscale('log')
plt.xlabel('α')
plt.ylabel('Coeficientes')
plt.title('Lasso Path')
```

**Interpretação:**
- Cada linha = uma variável
- Linhas que tocam zero = variáveis removidas
- Ordem de chegada ao zero = ordem de importância (inversa)

### Vantagens da Seleção Automática

✅ **Objetiva** - Baseada em dados, não em julgamento subjetivo  
✅ **Eficiente** - Um único ajuste do modelo  
✅ **Reproduzível** - Sempre mesmo resultado  
✅ **Integrada** - Regularização e seleção juntas

### Limitações da Seleção Lasso

⚠️ **Variáveis correlacionadas**: Pode remover variáveis importantes se correlacionadas  
⚠️ **Instabilidade**: Pequenas mudanças nos dados podem mudar seleção  
⚠️ **p > n**: Seleciona no máximo n variáveis (mesmo que mais sejam relevantes)  
⚠️ **Agrupamentos**: Não trata bem grupos de variáveis correlacionadas

---

## Parâmetro de Regularização (λ ou α)

### Notação

- **λ** (lambda): Notação estatística
- **α** (alpha): scikit-learn

São equivalentes: α = λ

### Impacto de λ/α

**α = 0:**
```
• Sem regularização
• Equivalente a OLS
• Todas variáveis no modelo
```

**α pequeno (ex: 0.001):**
```
• Regularização fraca
• Poucas variáveis removidas
• Coeficientes próximos de OLS
```

**α ótimo (ex: 0.1-1):**
```
• Equilíbrio viés-variância
• Seleção razoável de variáveis
• Melhor generalização
```

**α grande (ex: 100):**
```
• Regularização forte
• Quase todas variáveis removidas
• Underfitting
```

**α → ∞:**
```
• Todas variáveis removidas
• Modelo apenas com intercepto
• Prediz média de Y
```

### Escolha de α

#### 1. Validação Cruzada (Recomendado)

```python
from sklearn.linear_model import LassoCV

lasso_cv = LassoCV(cv=5, alphas=np.logspace(-4, 1, 100))
lasso_cv.fit(X, y)

print(f"Melhor α: {lasso_cv.alpha_}")
print(f"Variáveis selecionadas: {np.sum(lasso_cv.coef_ != 0)}")
```

#### 2. Critério de Informação

AIC, BIC ou critérios personalizados.

#### 3. Análise Visual

Plotar Lasso Path e escolher α que dá conjunto razoável de variáveis.

---

## Vantagens e Desvantagens

### Vantagens ✅

**1. Seleção Automática de Variáveis**
- Remove variáveis não importantes
- Modelo mais simples e interpretável
- Único grande diferencial sobre Ridge!

**2. Reduz Overfitting**
- Menos variáveis = menos complexidade
- Melhor generalização

**3. Interpretabilidade**
- Modelo esparso é mais fácil de explicar
- Identifica fatores realmente importantes

**4. Reduz Custo**
- Menos variáveis para coletar
- Menos processamento
- Mais eficiente em produção

**5. Funciona com p > n**
- Como Ridge, funciona mesmo com mais variáveis que observações

**6. Robustez**
- Remove variáveis ruidosas automaticamente

### Desvantagens ❌

**1. Limitação com Variáveis Correlacionadas**
- Tende a selecionar apenas uma de um grupo correlacionado
- Pode remover variável importante se correlacionada

**Exemplo:**
```
Altura e Peso são correlacionados
Lasso pode:
  - Manter Altura, remover Peso, OU
  - Manter Peso, remover Altura
Ambos igualmente importantes, mas Lasso escolhe um arbitrariamente
```

**2. Instabilidade na Seleção**
- Pequenas mudanças nos dados podem mudar seleção
- Menos estável que Ridge

**3. Limitação p > n**
- Seleciona no máximo n variáveis
- Mesmo que mais sejam relevantes

**4. Não Diferenciável**
- Otimização mais complexa que Ridge
- Algoritmos mais lentos

**5. Pode Ser Muito Agressivo**
- Pode remover variáveis úteis
- α errado pode prejudicar muito

**6. Coeficientes Enviesados**
- Como Ridge, adiciona viés
- Trade-off viés-variância

---

## Lasso vs Ridge vs OLS

### Tabela Comparativa

| Aspecto | OLS | Ridge (L2) | Lasso (L1) |
|---------|-----|------------|------------|
| **Penalização** | Nenhuma | Σβⱼ² | Σ\|βⱼ\| |
| **Esparsidade** | Não | Não | **Sim** |
| **Seleção de variáveis** | Não | Não | **Sim** |
| **Multicolinearidade** | Problemática | Resolve | Parcial |
| **Interpretabilidade** | Alta | Baixa | **Alta** |
| **Estabilidade** | Baixa | Alta | **Moderada** |
| **p > n** | Não funciona | Funciona | Funciona |
| **Solução** | Analítica | Analítica | **Numérica** |
| **Velocidade** | Rápida | Rápida | **Moderada** |
| **Quando usar** | p < n, sem multicolinearidade | Multicolinearidade, todas vars importantes | **Seleção de variáveis importante** |

### Quando Usar Cada Um?

**Use OLS quando:**
- p << n (poucas variáveis, muitas observações)
- Sem multicolinearidade
- Todas variáveis são teoricamente importantes

**Use Ridge quando:**
- Multicolinearidade severa
- Todas variáveis devem permanecer no modelo
- p > n
- Estabilidade é crucial

**Use Lasso quando:**
- Muitas variáveis, poucas importantes
- Quer identificar quais variáveis importam
- Interpretabilidade é crucial
- Modelo esparso é desejável

**Use Elastic Net quando:**
- Variáveis correlacionadas E quer seleção
- Melhor dos dois mundos
- Combina L1 e L2

### Regra Prática

```
Decisão rápida:
├─ Precisa selecionar variáveis? 
│  ├─ Sim → Lasso ou Elastic Net
│  └─ Não → Ridge
└─ Poucas variáveis, sem multicolinearidade?
   └─ Sim → OLS
```

---

## Exemplos do Dia a Dia

### Exemplo 1: Previsão de Doença com Dados Genéticos

**Contexto:** Pesquisa com 10.000 genes, mas apenas ~100 realmente relacionados à doença.

**Problema com OLS/Ridge:**
- OLS: Impossível (p >> n)
- Ridge: Funciona, mas mantém 10.000 genes

**Solução com Lasso:**
```python
lasso = LassoCV(cv=5)
lasso.fit(X_genes, y_doenca)

# Lasso seleciona apenas 127 genes
genes_selecionados = genes[lasso.coef_ != 0]
print(f"Genes selecionados: {len(genes_selecionados)}")
# Output: 127 (de 10.000!)
```

**Vantagens:**
- Modelo simples (127 vs 10.000)
- Identificou genes relevantes
- Interpretável para médicos
- Base para pesquisa adicional

### Exemplo 2: Text Mining - Classificação de Sentimentos

**Contexto:** Classificar reviews como positivos/negativos. 5.000 palavras únicas, mas poucas são discriminativas.

**Problema:**
- A maioria das palavras não importa
- "a", "o", "de" não ajudam
- Apenas palavras como "excelente", "péssimo", "adorei" importam

**Lasso:**
```python
# Vetorização TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
X_words = vectorizer.fit_transform(reviews)

# Lasso
lasso = Lasso(alpha=0.01)
lasso.fit(X_words, sentiment)

# Palavras importantes
palavras = vectorizer.get_feature_names_out()
importantes = palavras[lasso.coef_ != 0]
print(f"Palavras selecionadas: {len(importantes)} de 5000")
print(importantes[:10])
# Output: ['excelente', 'ótimo', 'péssimo', 'horrível', ...]
```

### Exemplo 3: Marketing Mix - Identificar Canais Efetivos

**Contexto:** Empresa investe em 20 canais de marketing, mas nem todos são efetivos.

**Variáveis:**
- TV (5 tipos), Rádio (3 tipos), Outdoor, Online (Google, Facebook, Instagram, YouTube, LinkedIn, Twitter), Email, SMS, etc.

**Lasso:**
```python
lasso = LassoCV(cv=5)
lasso.fit(X_canais, vendas)

# Canais efetivos
canais_efetivos = canais[lasso.coef_ != 0]
print(f"Canais efetivos: {list(canais_efetivos)}")
# Output: ['TV_Prime', 'Google_Ads', 'Facebook', 'Email']

# Realocar orçamento
# Parar de gastar em canais com coef = 0
# Focar em canais selecionados
```

**Resultado:**
- Identificou 4 canais principais
- Cortou 16 canais ineficazes
- Realocou orçamento
- Aumento de 25% no ROI

### Exemplo 4: Previsão de Preço de Imóveis com Muitas Features

**Contexto:** Sistema automático com 100+ características potenciais.

**Features:**
- Área, quartos, banheiros, idade, andar
- Distância a: 20 tipos de POIs (escolas, hospitais, metrô, parques, shopping, etc.)
- Características do bairro: 30 variáveis demográficas
- Características da região: 25 variáveis

**Lasso:**
```python
lasso_cv = LassoCV(cv=10)
lasso_cv.fit(X_todas, preco)

# Lasso seleciona 18 de 100+ features
features_importantes = features[lasso_cv.coef_ != 0]

print("Features mais importantes:")
for feat in features_importantes:
    print(f"  {feat}: {lasso_cv.coef_[features.get_loc(feat)]:.2f}")
    
# Output:
#   Area: 2500.32
#   Quartos: 18000.15
#   Dist_Metro: -3200.45
#   Dist_Shopping: -1500.22
#   ...
```

**Aplicação Prática:**
- Sistema só coleta 18 features (não 100+)
- Avaliação mais rápida
- Menor custo
- Mesma precisão

### Exemplo 5: Previsão de Séries Temporais com Features Defasadas

**Contexto:** Prever vendas usando 50 lags (vendas dos últimos 50 dias).

**Problema:**
- Lags consecutivos são correlacionados
- Nem todos os lags são importantes
- Alguns períodos (7, 14, 30 dias) mais relevantes

**Lasso:**
```python
# Criar features defasadas
for i in range(1, 51):
    df[f'lag_{i}'] = df['vendas'].shift(i)

X_lags = df[[f'lag_{i}' for i in range(1, 51)]]

lasso = LassoCV(cv=5)
lasso.fit(X_lags, y)

# Lags selecionados
lags_importantes = [i for i in range(1, 51) 
                    if lasso.coef_[i-1] != 0]
print(f"Lags selecionados: {lags_importantes}")
# Output: [1, 2, 7, 14, 30] (exemplo)
```

**Insights:**
- Vendas de ontem e anteontem importam
- Efeito semanal (lag 7)
- Efeito quinzenal (lag 14)
- Efeito mensal (lag 30)

---

## Implementação em Python

### Exemplo Completo: Seleção de Variáveis em Dados de Imóveis

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import Lasso, LassoCV, lasso_path
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import warnings
warnings.filterwarnings('ignore')

# Configurar visualizações
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# ==============================================
# 1. GERAR DADOS COM MUITAS VARIÁVEIS
# ==============================================
np.random.seed(42)
n = 300  # observações

# Variáveis IMPORTANTES (realmente afetam o preço)
area = np.random.normal(80, 20, n)
quartos = np.random.poisson(3, n)
localizacao = np.random.choice([0, 1, 2], n, p=[0.3, 0.5, 0.2])

# Variáveis MENOS IMPORTANTES
idade = np.random.exponential(10, n)
andar = np.random.randint(1, 20, n)

# Variáveis IRRELEVANTES (ruído)
# Distâncias a 10 POIs diferentes
pois = []
for i in range(10):
    pois.append(np.random.uniform(0, 20, n))

# Preço baseado principalmente em Area, Quartos, Localizacao
preco = (150000 + 
         2800 * area +              # IMPORTANTE
         25000 * quartos +           # IMPORTANTE
         50000 * localizacao +       # IMPORTANTE
         -500 * idade +              # MENOS IMPORTANTE
         800 * andar +               # MENOS IMPORTANTE
         np.random.normal(0, 25000, n))

# Criar DataFrame
df = pd.DataFrame({
    'Preco': preco,
    'Area': area,
    'Quartos': quartos,
    'Localizacao': localizacao,
    'Idade': idade,
    'Andar': andar
})

# Adicionar POIs (variáveis irrelevantes)
for i, poi in enumerate(pois, 1):
    df[f'Dist_POI_{i}'] = poi

print("=" * 70)
print("LASSO: SELEÇÃO AUTOMÁTICA DE VARIÁVEIS")
print("=" * 70)
print(f"\nNúmero de observações: {n}")
print(f"Número de variáveis: {df.shape[1] - 1}")
print(f"\nVariáveis realmente importantes: Area, Quartos, Localizacao")
print(f"Variáveis menos importantes: Idade, Andar")
print(f"Variáveis irrelevantes: Dist_POI_1 a Dist_POI_10")

# ==============================================
# 2. PREPARAR DADOS
# ==============================================

X = df.drop('Preco', axis=1)
y = df['Preco']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Padronizar
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==============================================
# 3. COMPARAR OLS, RIDGE, LASSO
# ==============================================

print("\n" + "=" * 70)
print("COMPARAÇÃO: OLS vs RIDGE vs LASSO")
print("=" * 70)

# OLS
ols = LinearRegression()
ols.fit(X_train_scaled, y_train)
y_pred_ols = ols.predict(X_test_scaled)
r2_ols = r2_score(y_test, y_pred_ols)
vars_ols = np.sum(ols.coef_ != 0)

# Ridge
ridge = Ridge(alpha=10)
ridge.fit(X_train_scaled, y_train)
y_pred_ridge = ridge.predict(X_test_scaled)
r2_ridge = r2_score(y_test, y_pred_ridge)
vars_ridge = np.sum(np.abs(ridge.coef_) > 0.01)  # Aproximação

# Lasso
lasso = Lasso(alpha=1000)
lasso.fit(X_train_scaled, y_train)
y_pred_lasso = lasso.predict(X_test_scaled)
r2_lasso = r2_score(y_test, y_pred_lasso)
vars_lasso = np.sum(lasso.coef_ != 0)

# Tabela de comparação
print("\n{:<20} {:>10} {:>10} {:>10}".format(
    "Métrica", "OLS", "Ridge", "Lasso"
))
print("-" * 55)
print("{:<20} {:>10.4f} {:>10.4f} {:>10.4f}".format(
    "R² Teste", r2_ols, r2_ridge, r2_lasso
))
print("{:<20} {:>10} {:>10} {:>10}".format(
    "Vars no modelo", vars_ols, vars_ridge, vars_lasso
))

print(f"\n🎯 Lasso selecionou apenas {vars_lasso} de {X.shape[1]} variáveis!")

# ==============================================
# 4. IDENTIFICAR VARIÁVEIS SELECIONADAS
# ==============================================

print("\n" + "=" * 70)
print("VARIÁVEIS SELECIONADAS PELO LASSO")
print("=" * 70)

vars_selecionadas = X.columns[lasso.coef_ != 0]
vars_removidas = X.columns[lasso.coef_ == 0]

print(f"\n✓ SELECIONADAS ({len(vars_selecionadas)}):")
for var in vars_selecionadas:
    coef = lasso.coef_[X.columns.get_loc(var)]
    print(f"  {var:20s}: {coef:>12,.2f}")

print(f"\n✗ REMOVIDAS ({len(vars_removidas)}):")
for var in vars_removidas:
    print(f"  {var}")

# ==============================================
# 5. ENCONTRAR α ÓTIMO COM VALIDAÇÃO CRUZADA
# ==============================================

print("\n" + "=" * 70)
print("BUSCA DO MELHOR α (VALIDAÇÃO CRUZADA)")
print("=" * 70)

lasso_cv = LassoCV(cv=5, alphas=np.logspace(-1, 4, 100), max_iter=10000)
lasso_cv.fit(X_train_scaled, y_train)

print(f"\nMelhor α: {lasso_cv.alpha_:.2f}")

y_pred_cv = lasso_cv.predict(X_test_scaled)
r2_cv = r2_score(y_test, y_pred_cv)
vars_cv = np.sum(lasso_cv.coef_ != 0)

print(f"R² no teste: {r2_cv:.4f}")
print(f"Variáveis selecionadas: {vars_cv}")

print("\nVariáveis selecionadas pelo modelo ótimo:")
vars_sel_cv = X.columns[lasso_cv.coef_ != 0]
for var in vars_sel_cv:
    coef = lasso_cv.coef_[X.columns.get_loc(var)]
    print(f"  {var:20s}: {coef:>12,.2f}")

# ==============================================
# 6. LASSO PATH (trajetória dos coeficientes)
# ==============================================

print("\n" + "=" * 70)
print("LASSO PATH: Evolução dos Coeficientes")
print("=" * 70)

alphas_path = np.logspace(-1, 4, 100)
coefs_lasso, _, _ = lasso_path(X_train_scaled, y_train, 
                                alphas=alphas_path, max_iter=10000)

plt.figure(figsize=(12, 6))
for i, var in enumerate(X.columns):
    # Destacar variáveis importantes
    if var in ['Area', 'Quartos', 'Localizacao']:
        plt.plot(alphas_path, coefs_lasso[i, :], 
                linewidth=2.5, label=var)
    else:
        plt.plot(alphas_path, coefs_lasso[i, :], 
                linewidth=0.8, alpha=0.5, color='gray')

plt.axvline(x=lasso_cv.alpha_, color='red', linestyle='--', 
            linewidth=2, label=f'α ótimo = {lasso_cv.alpha_:.1f}')
plt.xscale('log')
plt.xlabel('α (escala log)', fontsize=12)
plt.ylabel('Coeficientes', fontsize=12)
plt.title('Lasso Path: Como Variáveis São Removidas', 
          fontsize=14, fontweight='bold')
plt.legend(loc='best', fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\nObservações:")
print("• Linhas grossas: variáveis importantes (Area, Quartos, Localizacao)")
print("• Linhas finas: variáveis menos importantes ou irrelevantes")
print("• Quanto maior α, mais variáveis vão para zero")
print(f"• No α ótimo ({lasso_cv.alpha_:.1f}), {vars_cv} variáveis permanecem")

# ==============================================
# 7. COMPARAR COEFICIENTES
# ==============================================

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# OLS
axes[0].barh(range(len(X.columns)), ols.coef_, color='steelblue', edgecolor='black')
axes[0].set_yticks(range(len(X.columns)))
axes[0].set_yticklabels(X.columns, fontsize=9)
axes[0].axvline(x=0, color='red', linestyle='--', linewidth=1)
axes[0].set_xlabel('Coeficiente', fontsize=11)
axes[0].set_title(f'OLS\n({vars_ols} variáveis)', fontsize=12, fontweight='bold')
axes[0].grid(True, alpha=0.3, axis='x')

# Ridge
axes[1].barh(range(len(X.columns)), ridge.coef_, color='darkgreen', edgecolor='black')
axes[1].set_yticks(range(len(X.columns)))
axes[1].set_yticklabels(X.columns, fontsize=9)
axes[1].axvline(x=0, color='red', linestyle='--', linewidth=1)
axes[1].set_xlabel('Coeficiente', fontsize=11)
axes[1].set_title(f'Ridge (α=10)\n(~{vars_ridge} variáveis)', 
                   fontsize=12, fontweight='bold')
axes[1].grid(True, alpha=0.3, axis='x')

# Lasso
axes[2].barh(range(len(X.columns)), lasso_cv.coef_, color='darkred', edgecolor='black')
axes[2].set_yticks(range(len(X.columns)))
axes[2].set_yticklabels(X.columns, fontsize=9)
axes[2].axvline(x=0, color='red', linestyle='--', linewidth=1)
axes[2].set_xlabel('Coeficiente', fontsize=11)
axes[2].set_title(f'Lasso (α={lasso_cv.alpha_:.1f})\n({vars_cv} variáveis)', 
                   fontsize=12, fontweight='bold')
axes[2].grid(True, alpha=0.3, axis='x')

plt.tight_layout()
plt.show()

# ==============================================
# 8. ANÁLISE DE IMPORTÂNCIA
# ==============================================

print("\n" + "=" * 70)
print("ANÁLISE DE IMPORTÂNCIA")
print("=" * 70)

importancia = pd.DataFrame({
    'Variavel': X.columns,
    'Coef_Lasso': lasso_cv.coef_,
    'Abs_Coef': np.abs(lasso_cv.coef_)
}).sort_values('Abs_Coef', ascending=False)

print("\nRanking de Importância (Lasso):")
print(importancia[importancia['Coef_Lasso'] != 0].to_string(index=False))

# Visualizar top 10
top_10 = importancia.head(10)
plt.figure(figsize=(10, 6))
colors = ['darkred' if c != 0 else 'lightgray' for c in top_10['Coef_Lasso']]
plt.barh(top_10['Variavel'], top_10['Abs_Coef'], color=colors, edgecolor='black')
plt.xlabel('Importância Absoluta |Coeficiente|', fontsize=12)
plt.title('Top 10 Variáveis por Importância (Lasso)', 
          fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.show()

print("\n" + "=" * 70)
print("ANÁLISE COMPLETA FINALIZADA")
print("=" * 70)

# Conclusão
print("\n📊 RESUMO:")
print(f"  • Dataset tinha {X.shape[1]} variáveis")
print(f"  • Lasso selecionou {vars_cv} variáveis")
print(f"  • Removeu {X.shape[1] - vars_cv} variáveis irrelevantes")
print(f"  • R² mantido em {r2_cv:.4f}")
print(f"  • Modelo mais simples e interpretável!")
```

---

## Elastic Net

### O Que é Elastic Net?

**Elastic Net** combina as penalizações L1 (Lasso) e L2 (Ridge):

$$\text{minimize} \quad RSS + \lambda_1 \sum_{j}|\beta_j| + \lambda_2 \sum_{j}\beta_j^2$$

Ou:

$$\text{minimize} \quad RSS + \lambda \left( \alpha ||\beta||_1 + \frac{1-\alpha}{2} ||\beta||_2^2 \right)$$

Onde **α ∈ [0, 1]** controla o mix:
- **α = 1**: Lasso puro
- **α = 0**: Ridge puro
- **α = 0.5**: Meio a meio

### Vantagens do Elastic Net

✅ **Melhor que Lasso** quando variáveis são correlacionadas  
✅ **Seleção de grupos** - Seleciona/remove grupos de variáveis correlacionadas juntas  
✅ **Mais estável** que Lasso  
✅ **Funciona com p > n** como Lasso e Ridge

### Quando Usar Elastic Net?

Use quando:
- Variáveis são correlacionadas E quer seleção
- Lasso é instável nos seus dados
- Quer o "melhor dos dois mundos"

### Implementação

```python
from sklearn.linear_model import ElasticNetCV

elastic = ElasticNetCV(l1_ratio=[0.1, 0.5, 0.7, 0.9, 0.95, 0.99], cv=5)
elastic.fit(X_scaled, y)

print(f"α ótimo: {elastic.alpha_}")
print(f"l1_ratio ótimo: {elastic.l1_ratio_}")
print(f"Variáveis selecionadas: {np.sum(elastic.coef_ != 0)}")
```

---

## Casos Práticos

### Caso 1: Identificação de Genes em Pesquisa Médica

**Resultado:** De 20.000 genes, Lasso identificou 85 como relevantes para a doença.

### Caso 2: Otimização de Campanhas de Marketing

**Resultado:** De 30 canais, Lasso identificou 7 canais realmente efetivos. Empresa realocou orçamento e aumentou ROI em 30%.

---

## Limitações e Cuidados

### 1. Variáveis Correlacionadas

Lasso pode remover variáveis importantes se correlacionadas.

**Solução:** Use Elastic Net.

### 2. Instabilidade

Pequenas mudanças nos dados podem mudar seleção drasticamente.

**Solução:** 
- Use Elastic Net
- Bootstrap/cross-validation repetidos
- Análise de estabilidade da seleção

### 3. Limitação p > n

Lasso seleciona no máximo n variáveis.

**Solução:** Se espera mais variáveis importantes, considere outros métodos.

### 4. Viés nos Coeficientes

Coeficientes selecionados são enviesados (shrunken).

**Solução:** Após seleção, reajustar OLS apenas com variáveis selecionadas.

### 5. Hiperparâmetro α

Escolha errada de α pode prejudicar muito.

**Solução:** Sempre use validação cruzada.

---

## Referências

### Artigo Original

**TIBSHIRANI, Robert.** "Regression Shrinkage and Selection via the Lasso." *Journal of the Royal Statistical Society. Series B*, v. 58, n. 1, p. 267-288, 1996.
- Artigo que introduziu Lasso

### Livros

**HASTIE, Trevor; TIBSHIRANI, Robert; FRIEDMAN, Jerome.** *The Elements of Statistical Learning*. 2. ed. Springer, 2009.
- Capítulo 3.4: Lasso e Elastic Net

**JAMES, Gareth et al.** *An Introduction to Statistical Learning*. 2. ed. Springer, 2021.
- Seção 6.2: The Lasso

---

## Conclusão

Lasso é a escolha ideal quando:

✅ **Precisa selecionar variáveis** importantes  
✅ **Tem muitas variáveis** potenciais  
✅ **Quer modelo simples** e interpretável  
✅ **Custo de coleta** de variáveis é importante  
✅ **Esparsidade** é desejável

**Lembre-se:**
- Sempre padronize variáveis
- Use validação cruzada para α
- Compare com Ridge e Elastic Net
- Considere Elastic Net se variáveis correlacionadas
- Análise de estabilidade da seleção é importante

**Próximos Passos:**
- Aprenda Elastic Net
- Explore métodos ensemble para seleção de variáveis
- Estude Stability Selection
- Considere Algoritmos Genéticos para seleção

---

*Documento criado como parte do repositório de Análise de Dados*  
*Última atualização: 2026*
