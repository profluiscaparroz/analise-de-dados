# Regressão Ridge (L2 Regularization)

## Sumário

1. [Introdução](#introdução)
2. [O Problema da Regressão Linear](#o-problema-da-regressão-linear)
3. [Conceitos Fundamentais](#conceitos-fundamentais)
4. [Modelo Matemático](#modelo-matemático)
5. [Parâmetro de Regularização (λ ou α)](#parâmetro-de-regularização-λ-ou-α)
6. [Vantagens e Desvantagens](#vantagens-e-desvantagens)
7. [Ridge vs Regressão Linear](#ridge-vs-regressão-linear)
8. [Exemplos do Dia a Dia](#exemplos-do-dia-a-dia)
9. [Implementação em Python](#implementação-em-python)
10. [Escolha do Hiperparâmetro α](#escolha-do-hiperparâmetro-α)
11. [Casos Práticos](#casos-práticos)
12. [Limitações e Cuidados](#limitações-e-cuidados)
13. [Referências](#referências)

---

## Introdução

A **Regressão Ridge** (também conhecida como **Regularização L2** ou **Tikhonov Regularization**) é uma técnica que melhora a regressão linear adicionando uma **penalização** aos coeficientes grandes. É especialmente útil quando há **multicolinearidade** ou **muitas variáveis** no modelo.

### Por que Ridge é Necessário?

Na regressão linear padrão, quando temos:
- **Multicolinearidade**: Variáveis independentes correlacionadas entre si
- **Muitas variáveis**: Mais preditores que observações (p > n)
- **Overfitting**: Modelo se ajusta demais aos dados de treino

Esses problemas causam:
❌ Coeficientes instáveis (variam muito com pequenas mudanças nos dados)  
❌ Variâncias infladas  
❌ Predições ruins em novos dados  
❌ Interpretação difícil

Ridge resolve esses problemas **sacrificando um pouco de viés para reduzir muito a variância**.

### Aplicações Comuns

✅ **Genômica**: Milhares de genes, poucas amostras  
✅ **Processamento de Imagens**: Muitos pixels como features  
✅ **Econometria**: Variáveis macroeconômicas correlacionadas  
✅ **Marketing**: Múltiplos canais correlacionados  
✅ **Previsão de séries temporais**: Features defasadas correlacionadas

---

## O Problema da Regressão Linear

### Multicolinearidade

**O que é?**
Quando variáveis independentes estão fortemente correlacionadas.

**Exemplo:**
- Altura e Peso (correlação ~0.8)
- PIB e Consumo (correlação ~0.95)
- Gastos em TV e Gastos em Marketing Total (correlação ~0.9)

**Consequências:**
```
Problema 1: Coeficientes Instáveis
────────────────────────────────
Dataset 1: β₁ = 5.2,  β₂ = 3.1
Dataset 2: β₁ = 8.7,  β₂ = -0.4  ← Mudança drástica!

Problema 2: Variância Alta
────────────────────────────────
Erro padrão muito grande → Intervalos de confiança muito amplos

Problema 3: Sinais Incorretos
────────────────────────────────
Coeficientes podem ter sinais opostos ao esperado
```

### Problema p > n

Quando temos mais variáveis (p) que observações (n):
- Matriz X'X não é inversível
- Infinitas soluções possíveis
- Overfitting severo

**Exemplo:**
```
Estudo genético:
- 20.000 genes (variáveis)
- 100 pacientes (observações)
```

Ridge permite estimar o modelo mesmo nessa situação!

---

## Conceitos Fundamentais

### Regularização

**Regularização** é o processo de adicionar informação para resolver problemas mal-postos ou prevenir overfitting.

**Intuição:**
- Modelo muito complexo → Overfitting
- Regularização → Penaliza complexidade
- Resultado → Melhor generalização

### Trade-off Viés-Variância

**Regressão Linear:**
- Baixo viés, alta variância
- Pode sofrer overfitting

**Ridge:**
- Adiciona viés (os coeficientes são "encolhidos")
- Reduz variância (estimativas mais estáveis)
- Geralmente melhora predição

```
Erro Total = Viés² + Variância + Ruído Irredutível

Ridge: ↑ Viés pequeno, ↓↓ Variância grande = ↓ Erro Total
```

### Encolhimento de Coeficientes (Shrinkage)

Ridge "encolhe" coeficientes em direção a zero (mas nunca exatamente zero).

**Visualização:**
```
Coeficientes OLS:     β₁=10,  β₂=8,   β₃=15
Ridge (α=0.1):        β₁=9.2, β₂=7.5, β₃=14.1
Ridge (α=1):          β₁=7.5, β₂=6.2, β₃=11.8
Ridge (α=10):         β₁=3.2, β₂=2.8, β₃=5.1
Ridge (α→∞):          β₁≈0,   β₂≈0,   β₃≈0
```

---

## Modelo Matemático

### Função Objetivo da Regressão Linear (OLS)

Minimizar a soma dos quadrados dos resíduos:

$$\text{minimize} \quad RSS = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2 = \sum_{i=1}^{n}(y_i - \beta_0 - \sum_{j=1}^{p}\beta_j x_{ij})^2$$

### Função Objetivo da Regressão Ridge

Ridge adiciona uma **penalização L2** (soma dos quadrados dos coeficientes):

$$\text{minimize} \quad RSS + \lambda \sum_{j=1}^{p}\beta_j^2$$

Ou equivalentemente:

$$\hat{\beta}^{ridge} = \arg\min_{\beta} \left\{ \sum_{i=1}^{n}(y_i - \beta_0 - \sum_{j=1}^{p}\beta_j x_{ij})^2 + \lambda \sum_{j=1}^{p}\beta_j^2 \right\}$$

Onde:
- **λ** (lambda) = parâmetro de regularização (λ ≥ 0)
- **Σβⱼ²** = penalização L2 (norma L2 ao quadrado)
- **β₀** = intercepto (geralmente não penalizado)

### Notação Matricial

$$\hat{\beta}^{ridge} = \arg\min_{\beta} \left\{ ||\mathbf{y} - \mathbf{X}\beta||_2^2 + \lambda ||\beta||_2^2 \right\}$$

### Solução Analítica

A solução de Ridge tem forma fechada:

$$\hat{\beta}^{ridge} = (\mathbf{X}^T\mathbf{X} + \lambda \mathbf{I})^{-1}\mathbf{X}^T\mathbf{y}$$

Onde **I** é a matriz identidade.

**Comparação com OLS:**
$$\hat{\beta}^{OLS} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$$

**Diferença:** λI adicionado à matriz garante que sempre seja inversível!

### Interpretação Geométrica

Ridge pode ser visto como um problema de **otimização restrita**:

$$\text{minimize} \quad \sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$
$$\text{sujeito a} \quad \sum_{j=1}^{p}\beta_j^2 \leq t$$

Onde **t** é um limite para a soma dos quadrados dos coeficientes.

**Geometricamente:**
- Coeficientes devem estar dentro de uma **esfera** de raio √t
- Solução é onde elipses de RSS tocam a esfera

---

## Parâmetro de Regularização (λ ou α)

### Notação

- **λ** (lambda): Notação estatística comum
- **α** (alpha): Usado em scikit-learn

São equivalentes: α = λ

### Impacto de λ/α

**λ = 0 (α = 0):**
- Sem regularização
- Equivalente a OLS
- Coeficientes não encolhidos

**λ pequeno (α pequeno, ex: 0.01):**
- Regularização fraca
- Coeficientes próximos aos de OLS
- Pouca redução de variância

**λ moderado (α moderado, ex: 1-10):**
- Equilíbrio entre viés e variância
- Coeficientes encolhidos significativamente
- Geralmente melhor desempenho

**λ grande (α grande, ex: 100):**
- Regularização forte
- Coeficientes muito encolhidos (próximos de zero)
- Modelo sub-ajustado (underfitting)

**λ → ∞ (α → ∞):**
- Todos coeficientes → 0
- Modelo prediz apenas a média de Y

### Visualização do Efeito de λ

```
      β (coeficiente)
       |
  OLS  |●
       |  
       |   ●  (α=0.1)
       |
       |     ●  (α=1)
       |
       |       ●  (α=10)
       |
       |          ●  (α=100)
    0  |____________●__________ λ/α
                              (α→∞)
```

### Importância da Padronização

**⚠️ CRUCIAL:** Variáveis devem ser padronizadas antes de Ridge!

**Por quê?**
- Penalização L2 é sensível à escala
- Variáveis com escalas maiores são penalizadas mais

**Exemplo:**
```
Sem padronização:
X₁ = Renda (0-100.000)     → β₁ será pequeno → pouca penalização
X₂ = Idade (0-100)          → β₂ será grande → muita penalização

Com padronização:
X₁ = (Renda - μ)/σ  (-3 a 3) → Tratamento justo
X₂ = (Idade - μ)/σ  (-3 a 3) → Tratamento justo
```

**Prática:**
```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

---

## Vantagens e Desvantagens

### Vantagens ✅

**1. Resolve Multicolinearidade**
- Estabiliza coeficientes quando variáveis são correlacionadas
- Reduz variância das estimativas

**2. Funciona com p > n**
- Pode estimar modelos mesmo com mais variáveis que observações
- Matriz sempre inversível devido a λI

**3. Reduz Overfitting**
- Penaliza complexidade
- Melhora generalização para novos dados

**4. Solução Analítica**
- Tem fórmula fechada
- Computacionalmente eficiente

**5. Mantém Todas as Variáveis**
- Não remove variáveis (diferente de Lasso)
- Útil quando todas variáveis são importantes

**6. Estabilidade Numérica**
- λI na diagonal melhora condicionamento da matriz
- Menos problemas computacionais

### Desvantagens ❌

**1. Não Faz Seleção de Variáveis**
- Encolhe coeficientes, mas não os zera
- Todas variáveis permanecem no modelo
- Dificulta interpretação com muitas variáveis

**2. Requer Padronização**
- Variáveis precisam estar na mesma escala
- Passo adicional necessário

**3. Escolha de λ/α**
- Requer validação cruzada
- Não há valor "correto" universal

**4. Interpretação Mais Difícil**
- Coeficientes são "encolhidos"
- Magnitudes não refletem importância real
- Interpretação direta é comprometida

**5. Viés Adicionado**
- Coeficientes são enviesados (por design)
- Trade-off pode não valer a pena se não há overfitting

---

## Ridge vs Regressão Linear

| Aspecto | Regressão Linear (OLS) | Regressão Ridge |
|---------|------------------------|-----------------|
| **Função objetivo** | Minimiza RSS | Minimiza RSS + λΣβ² |
| **Coeficientes** | Não enviesados | Enviesados |
| **Variância** | Pode ser alta | Reduzida |
| **Multicolinearidade** | Problemática | Resolvida |
| **p > n** | Não funciona | Funciona |
| **Seleção de variáveis** | Não faz | Não faz |
| **Interpretação** | Direta | Mais complexa |
| **Hiperparâmetros** | Nenhum | λ/α |
| **Quando usar** | Sem multicolinearidade, p < n | Com multicolinearidade, p grande |

---

## Exemplos do Dia a Dia

### Exemplo 1: Preço de Imóveis com Muitas Características

**Contexto:** Imobiliária tem 50 características de apartamentos (área, quartos, andar, idade, distância de escolas, hospitais, metrô, parques, comércio, etc.) mas apenas 200 apartamentos.

**Problema:**
- Muitas variáveis correlacionadas (ex: área total ↔ número de quartos)
- Risco de overfitting
- Coeficientes OLS instáveis

**Solução com Ridge:**
```python
# α = 10 escolhido por validação cruzada
modelo_ridge = Ridge(alpha=10)
modelo_ridge.fit(X_scaled, y)
```

**Resultado:**
- Coeficientes estáveis
- Melhor predição em dados novos
- R² teste: 0.85 (vs 0.72 com OLS)

**Aplicação Prática:**
- Avaliação automática de imóveis
- Precificação mais confiável
- Menos erros em avaliações

### Exemplo 2: Análise de Vendas com Múltiplos Canais

**Contexto:** Empresa tem gastos em 15 canais de marketing (TV, rádio, jornais, revistas, outdoors, Google Ads, Facebook, Instagram, YouTube, email, SEO, etc.)

**Problema:**
- Canais são correlacionados
- Difícil isolar efeito individual
- OLS atribui valores absurdos a alguns canais

**Exemplo OLS (problemático):**
```
TV:       β = 15.2 (ok)
Facebook: β = -8.3 (negativo?! improvável)
Google:   β = 22.7 (muito alto)
```

**Com Ridge (α=5):**
```
TV:       β = 7.5  (mais razoável)
Facebook: β = 3.2  (positivo, faz sentido)
Google:   β = 9.1  (mais realista)
```

**Aplicação:**
- Otimização de orçamento
- Mix de marketing mais eficiente
- ROI mais preciso por canal

### Exemplo 3: Previsão de Doença com Dados Genômicos

**Contexto:** Pesquisa médica para prever risco de doença usando expressão de 10.000 genes, com apenas 150 pacientes.

**Problema:**
- p >> n (10.000 >> 150)
- OLS não pode ser aplicado
- Genes muito correlacionados

**Solução:**
```python
# Ridge permite estimar o modelo!
ridge_genoma = Ridge(alpha=100)
ridge_genoma.fit(X_genes_scaled, y_doenca)
```

**Resultado:**
- Modelo consegue identificar padrões
- Predições razoáveis
- Base para pesquisa adicional

### Exemplo 4: Previsão de Demanda com Features Temporais

**Contexto:** Varejista quer prever demanda usando vendas dos últimos 30 dias como features.

**Problema:**
- Vendas de dias consecutivos são correlacionadas
- 30 features altamente correlacionadas
- Overfitting em OLS

**Variáveis:**
```
Y = Demanda hoje
X₁ = Vendas ontem
X₂ = Vendas 2 dias atrás
...
X₃₀ = Vendas 30 dias atrás
```

**Ridge:**
- Encolhe coeficientes de forma suave
- Aproveita informação de todos os dias
- Predição mais estável

### Exemplo 5: Análise Econômica com Indicadores Macroeconômicos

**Contexto:** Economista quer prever PIB usando 25 indicadores (inflação, desemprego, consumo, investimento, exportações, importações, taxas de juros, etc.)

**Problema:**
- Indicadores macroeconômicos são correlacionados por natureza
- Multicolinearidade severa
- Interpretação de OLS não confiável

**Ridge:**
- Coeficientes mais estáveis
- Melhores previsões
- Análise de sensibilidade mais robusta

---

## Implementação em Python

### Exemplo Completo: Preço de Imóveis com Multicolinearidade

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import r2_score, mean_squared_error
import warnings
warnings.filterwarnings('ignore')

# Configurar visualizações
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# ==============================================
# 1. GERAR DADOS COM MULTICOLINEARIDADE
# ==============================================
np.random.seed(42)
n = 200

# Variáveis correlacionadas
area = np.random.normal(80, 20, n)
# Quartos correlacionado com área
quartos = np.round(area / 30 + np.random.normal(0, 0.5, n))
# Banheiros correlacionado com quartos
banheiros = np.round(quartos * 0.7 + np.random.normal(0, 0.3, n))

# Outras variáveis
idade = np.random.exponential(10, n)
distancia = np.random.uniform(1, 20, n)
andar = np.random.randint(1, 20, n)

# Preço
preco = (150000 + 
         2500 * area + 
         20000 * quartos +
         15000 * banheiros -
         800 * idade -
         2000 * distancia +
         1500 * andar +
         np.random.normal(0, 30000, n))

# DataFrame
df = pd.DataFrame({
    'Area': area,
    'Quartos': quartos,
    'Banheiros': banheiros,
    'Idade': idade,
    'Distancia': distancia,
    'Andar': andar,
    'Preco': preco
})

print("=" * 70)
print("EXEMPLO: RIDGE REGRESSION PARA IMÓVEIS")
print("=" * 70)
print(f"\nNúmero de imóveis: {len(df)}")

# Verificar multicolinearidade
print("\nMatriz de Correlação das Variáveis Independentes:")
X_vars = ['Area', 'Quartos', 'Banheiros', 'Idade', 'Distancia', 'Andar']
corr_matrix = df[X_vars].corr()
print(corr_matrix)

# Visualizar correlações
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
            fmt='.2f', square=True, linewidths=1)
plt.title('Correlação entre Variáveis (Multicolinearidade!)', 
          fontsize=13, fontweight='bold')
plt.tight_layout()
plt.show()

# Identificar correlações altas
print("\nPares com correlação alta (|r| > 0.7):")
for i in range(len(corr_matrix)):
    for j in range(i+1, len(corr_matrix)):
        if abs(corr_matrix.iloc[i, j]) > 0.7:
            print(f"  {corr_matrix.index[i]} ↔ {corr_matrix.columns[j]}: "
                  f"{corr_matrix.iloc[i, j]:.3f}")

# ==============================================
# 2. PREPARAR DADOS
# ==============================================

X = df[X_vars]
y = df['Preco']

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# PADRONIZAR (crucial para Ridge!)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\n" + "=" * 70)
print("DADOS PREPARADOS")
print("=" * 70)
print(f"Treino: {len(X_train)} observações")
print(f"Teste: {len(X_test)} observações")
print(f"Variáveis: {X.shape[1]}")

# ==============================================
# 3. COMPARAR OLS vs RIDGE
# ==============================================

print("\n" + "=" * 70)
print("COMPARAÇÃO: OLS vs RIDGE")
print("=" * 70)

# Modelo OLS (regressão linear padrão)
ols = LinearRegression()
ols.fit(X_train_scaled, y_train)
y_train_ols = ols.predict(X_train_scaled)
y_test_ols = ols.predict(X_test_scaled)

# Modelo Ridge (α = 10)
ridge = Ridge(alpha=10)
ridge.fit(X_train_scaled, y_train)
y_train_ridge = ridge.predict(X_train_scaled)
y_test_ridge = ridge.predict(X_test_scaled)

# Métricas
r2_train_ols = r2_score(y_train, y_train_ols)
r2_test_ols = r2_score(y_test, y_test_ols)
rmse_test_ols = np.sqrt(mean_squared_error(y_test, y_test_ols))

r2_train_ridge = r2_score(y_train, y_train_ridge)
r2_test_ridge = r2_score(y_test, y_test_ridge)
rmse_test_ridge = np.sqrt(mean_squared_error(y_test, y_test_ridge))

# Tabela de comparação
print("\n{:<15} {:>15} {:>15}".format("Métrica", "OLS", "Ridge (α=10)"))
print("-" * 50)
print("{:<15} {:>15.4f} {:>15.4f}".format("R² Treino", r2_train_ols, r2_train_ridge))
print("{:<15} {:>15.4f} {:>15.4f}".format("R² Teste", r2_test_ols, r2_test_ridge))
print("{:<15} {:>15,.2f} {:>15,.2f}".format("RMSE Teste", rmse_test_ols, rmse_test_ridge))

# Comparar coeficientes
print("\n" + "=" * 70)
print("COEFICIENTES: OLS vs RIDGE")
print("=" * 70)
print("\n{:<15} {:>15} {:>15}".format("Variável", "OLS", "Ridge (α=10)"))
print("-" * 50)
for i, var in enumerate(X_vars):
    print("{:<15} {:>15,.2f} {:>15,.2f}".format(
        var, ols.coef_[i], ridge.coef_[i]
    ))

# Visualizar coeficientes
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# OLS
axes[0].barh(X_vars, ols.coef_, color='steelblue', edgecolor='black')
axes[0].axvline(x=0, color='red', linestyle='--', linewidth=1)
axes[0].set_xlabel('Coeficiente', fontsize=12)
axes[0].set_title('Coeficientes OLS\n(Com Multicolinearidade)', 
                   fontsize=13, fontweight='bold')
axes[0].grid(True, alpha=0.3, axis='x')

# Ridge
axes[1].barh(X_vars, ridge.coef_, color='darkgreen', edgecolor='black')
axes[1].axvline(x=0, color='red', linestyle='--', linewidth=1)
axes[1].set_xlabel('Coeficiente', fontsize=12)
axes[1].set_title('Coeficientes Ridge (α=10)\n(Regularizados)', 
                   fontsize=13, fontweight='bold')
axes[1].grid(True, alpha=0.3, axis='x')

plt.tight_layout()
plt.show()

# ==============================================
# 4. ENCONTRAR MELHOR α POR VALIDAÇÃO CRUZADA
# ==============================================

print("\n" + "=" * 70)
print("BUSCA DO MELHOR α (VALIDAÇÃO CRUZADA)")
print("=" * 70)

# Testar diferentes valores de α
alphas = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
cv_scores = []

for alpha in alphas:
    ridge_cv = Ridge(alpha=alpha)
    scores = cross_val_score(ridge_cv, X_train_scaled, y_train,
                             cv=5, scoring='r2')
    cv_scores.append(scores.mean())
    print(f"α = {alpha:>7.3f}  →  R² médio (CV): {scores.mean():.4f} "
          f"(±{scores.std():.4f})")

# Melhor α
best_idx = np.argmax(cv_scores)
best_alpha = alphas[best_idx]
print(f"\nMelhor α: {best_alpha}")

# Visualizar
plt.figure(figsize=(10, 6))
plt.plot(alphas, cv_scores, 'o-', linewidth=2, markersize=8)
plt.axvline(x=best_alpha, color='red', linestyle='--', linewidth=2,
            label=f'Melhor α = {best_alpha}')
plt.xscale('log')
plt.xlabel('α (escala log)', fontsize=12)
plt.ylabel('R² médio (Validação Cruzada 5-fold)', fontsize=12)
plt.title('Escolha do Hiperparâmetro α', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ==============================================
# 5. MODELO FINAL COM MELHOR α
# ==============================================

ridge_final = Ridge(alpha=best_alpha)
ridge_final.fit(X_train_scaled, y_train)
y_test_final = ridge_final.predict(X_test_scaled)

r2_final = r2_score(y_test, y_test_final)
rmse_final = np.sqrt(mean_squared_error(y_test, y_test_final))

print("\n" + "=" * 70)
print(f"MODELO FINAL - RIDGE (α = {best_alpha})")
print("=" * 70)
print(f"\nR² no teste: {r2_final:.4f}")
print(f"RMSE no teste: R$ {rmse_final:,.2f}")

print("\nCoeficientes finais:")
for i, var in enumerate(X_vars):
    print(f"  {var:15s}: {ridge_final.coef_[i]:>10,.2f}")

# ==============================================
# 6. TRAJETÓRIA DOS COEFICIENTES (RIDGE PATH)
# ==============================================

print("\n" + "=" * 70)
print("TRAJETÓRIA DOS COEFICIENTES (Ridge Path)")
print("=" * 70)

alphas_path = np.logspace(-2, 4, 100)
coefs_path = []

for alpha in alphas_path:
    ridge_path = Ridge(alpha=alpha)
    ridge_path.fit(X_train_scaled, y_train)
    coefs_path.append(ridge_path.coef_)

coefs_path = np.array(coefs_path)

plt.figure(figsize=(12, 6))
for i, var in enumerate(X_vars):
    plt.plot(alphas_path, coefs_path[:, i], label=var, linewidth=2)

plt.axvline(x=best_alpha, color='red', linestyle='--', linewidth=2,
            alpha=0.7, label=f'α ótimo = {best_alpha}')
plt.xscale('log')
plt.xlabel('α (escala log)', fontsize=12)
plt.ylabel('Valor do Coeficiente', fontsize=12)
plt.title('Ridge Path: Evolução dos Coeficientes com α', 
          fontsize=14, fontweight='bold')
plt.legend(fontsize=10, loc='best')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\nObservações:")
print("• Com α pequeno: coeficientes próximos de OLS")
print("• Com α grande: coeficientes encolhem para zero")
print("• α ótimo: equilíbrio entre viés e variância")

# ==============================================
# 7. VISUALIZAR PREDIÇÕES
# ==============================================

plt.figure(figsize=(12, 6))
plt.scatter(y_test, y_test_final, alpha=0.6, s=100, edgecolors='black')
plt.plot([y_test.min(), y_test.max()], 
         [y_test.min(), y_test.max()],
         'r--', linewidth=2, label='Predição perfeita')
plt.xlabel('Preço Real (R$)', fontsize=12)
plt.ylabel('Preço Predito (R$)', fontsize=12)
plt.title(f'Ridge Regression: Real vs Predito\nR² = {r2_final:.4f}', 
          fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\n" + "=" * 70)
print("ANÁLISE COMPLETA FINALIZADA")
print("=" * 70)
```

---

## Escolha do Hiperparâmetro α

### Métodos para Escolher α

#### 1. Validação Cruzada (Recomendado)

```python
from sklearn.model_selection import RidgeCV

# RidgeCV faz validação cruzada automaticamente
alphas = np.logspace(-2, 4, 100)
ridge_cv = RidgeCV(alphas=alphas, cv=5)
ridge_cv.fit(X_train_scaled, y_train)

print(f"Melhor α: {ridge_cv.alpha_}")
```

#### 2. Grid Search

```python
from sklearn.model_selection import GridSearchCV

param_grid = {'alpha': np.logspace(-2, 4, 50)}
grid = GridSearchCV(Ridge(), param_grid, cv=5, scoring='r2')
grid.fit(X_train_scaled, y_train)

print(f"Melhor α: {grid.best_params_['alpha']}")
print(f"Melhor R²: {grid.best_score_:.4f}")
```

#### 3. Critério de Informação (AIC/BIC)

Calcular AIC ou BIC para diferentes valores de α e escolher o menor.

### Regras Práticas

✅ Começar com α em {0.01, 0.1, 1, 10, 100}  
✅ Usar escala logarítmica para busca  
✅ Sempre usar validação cruzada  
✅ Verificar Ridge Path para entender comportamento  
✅ Considerar trade-off entre R²_treino e R²_teste

---

## Casos Práticos

### Caso 1: Previsão de Vendas com 50 Variáveis

**Problema:** Empresa tem dados de 50 variáveis mas apenas 200 observações.

**Solução:**
```python
# OLS não funciona bem (p/n = 0.25)
# Ridge funciona perfeitamente
ridge = RidgeCV(alphas=np.logspace(-2, 3, 50), cv=5)
ridge.fit(X_scaled, y)
```

**Resultado:**
- R² OLS: 0.65 (overfitting)
- R² Ridge: 0.79 (melhor generalização)

### Caso 2: Análise de Expressão Gênica

**Problema:** 10.000 genes, 100 pacientes.

**Solução:**
```python
# p >> n (OLS impossível)
ridge = Ridge(alpha=1000)  # α alto devido a p muito grande
ridge.fit(X_genes_scaled, y_doenca)
```

---

## Limitações e Cuidados

### 1. Não Faz Seleção de Variáveis

Ridge mantém todas as variáveis. Para seleção, use Lasso.

### 2. Interpretação Comprometida

Coeficientes são enviesados. Foco em predição, não interpretação.

### 3. Requer Padronização

Sempre padronize! Ridge é sensível à escala.

### 4. Escolha de α Requer Cuidado

Use validação cruzada. Não há valor universal.

### 5. Trade-off Viés-Variância

Aceita viés para reduzir variância. Nem sempre vale a pena.

---

## Referências

### Livros

**HASTIE, Trevor; TIBSHIRANI, Robert; FRIEDMAN, Jerome.** *The Elements of Statistical Learning*. 2. ed. Springer, 2009.
- Capítulo 3.4: Shrinkage Methods

**JAMES, Gareth et al.** *An Introduction to Statistical Learning*. 2. ed. Springer, 2021.
- Seção 6.2: Ridge Regression

**HOERL, Arthur E.; KENNARD, Robert W.** "Ridge Regression: Biased Estimation for Nonorthogonal Problems." *Technometrics*, v. 12, n. 1, p. 55-67, 1970.
- Artigo original sobre Ridge

---

## Conclusão

Ridge Regression é essencial quando:

✅ **Há multicolinearidade** entre variáveis  
✅ **p é grande** (muitas variáveis)  
✅ **Overfitting** é problema  
✅ **Todas variáveis são importantes** (não quer remover nenhuma)  
✅ **Estabilidade** é mais importante que interpretação

**Lembre-se:**
- Sempre padronize variáveis
- Use validação cruzada para escolher α
- Compare com OLS e Lasso
- Foco em predição, não interpretação

**Próximos Passos:**
- Estude Lasso para seleção de variáveis
- Aprenda Elastic Net (combina Ridge e Lasso)
- Explore PCR (Principal Components Regression)

---

*Documento criado como parte do repositório de Análise de Dados*  
*Última atualização: 2026*
