# **Análise de Regressão: Fundamentos e Aplicações**

A **análise de regressão** é uma técnica estatística fundamental que investiga a relação entre variáveis, permitindo modelar e predizer o comportamento de uma variável dependente a partir de uma ou mais variáveis independentes.

## Sumário

1. [Conceitos Fundamentais](#conceitos-fundamentais)
2. [Regressão Linear Simples](#regressão-linear-simples)
3. [Regressão Linear Múltipla](#regressão-linear-múltipla)
4. [Pressupostos da Regressão](#pressupostos-da-regressão)
5. [Avaliação do Modelo](#avaliação-do-modelo)
6. [Diagnóstico e Validação](#diagnóstico-e-validação)
7. [Tipos Especiais de Regressão](#tipos-especiais-de-regressão)
8. [Exemplos Práticos](#exemplos-práticos)

---

## **Conceitos Fundamentais**

### **O que é Análise de Regressão?**

A análise de regressão é uma metodologia estatística que:
- **Modela relacionamentos** entre variáveis
- **Faz predições** sobre valores futuros
- **Quantifica influências** de variáveis explicativas
- **Identifica tendências** e padrões nos dados

### **Terminologia Básica**

- **Variável Dependente (Y)**: Variável que queremos explicar ou predizer
- **Variável Independente (X)**: Variável(is) que usamos para explicar Y
- **Intercepto (β₀)**: Valor de Y quando X = 0
- **Coeficiente Angular (β₁)**: Mudança em Y para cada unidade de mudança em X
- **Resíduos (ε)**: Diferença entre valores observados e preditos

### **Tipos de Regressão por Objetivo**

1. **Descritiva**: Descrever relações entre variáveis
2. **Preditiva**: Fazer previsões sobre novos dados
3. **Inferencial**: Testar hipóteses sobre relações

---

## **Regressão Linear Simples**

### **Modelo Matemático**

O modelo de regressão linear simples é expresso por:

$$Y = \beta_0 + \beta_1 X + \varepsilon$$

Onde:
- **Y**: Variável dependente
- **X**: Variável independente
- **β₀**: Intercepto (constante)
- **β₁**: Coeficiente angular (inclinação)
- **ε**: Termo de erro aleatório

### **Interpretação dos Coeficientes**

- **β₀**: Valor esperado de Y quando X = 0
- **β₁**: Mudança esperada em Y para cada aumento de 1 unidade em X

### **Exemplo Prático: Vendas vs Temperatura**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import seaborn as sns

# Dados simulados: Vendas de sorvete vs Temperatura
np.random.seed(42)
temperatura = np.random.normal(25, 5, 50)  # Temperatura média 25°C
vendas = 100 + 3 * temperatura + np.random.normal(0, 10, 50)  # Vendas com ruído

# Criar DataFrame
df = pd.DataFrame({
    'Temperatura': temperatura,
    'Vendas': vendas
})

print("Primeiras 5 observações:")
print(df.head())

# Visualização
plt.figure(figsize=(10, 6))
plt.scatter(df['Temperatura'], df['Vendas'], alpha=0.6)
plt.xlabel('Temperatura (°C)')
plt.ylabel('Vendas de Sorvete (R$)')
plt.title('Relação entre Temperatura e Vendas de Sorvete')
plt.grid(True, alpha=0.3)
plt.show()

# Ajustar modelo de regressão
X = df[['Temperatura']]
y = df['Vendas']

modelo = LinearRegression()
modelo.fit(X, y)

# Predições
y_pred = modelo.predict(X)

# Coeficientes
print(f"\nIntercepto (β₀): {modelo.intercept_:.2f}")
print(f"Coeficiente Angular (β₁): {modelo.coef_[0]:.2f}")
print(f"R²: {r2_score(y, y_pred):.3f}")

# Interpretação
print(f"\nInterpretação:")
print(f"Para cada 1°C de aumento na temperatura, as vendas aumentam em R$ {modelo.coef_[0]:.2f}")
print(f"Quando a temperatura é 0°C, as vendas esperadas são R$ {modelo.intercept_:.2f}")
```

### **Linha de Regressão**

```python
# Plotar linha de regressão
plt.figure(figsize=(10, 6))
plt.scatter(df['Temperatura'], df['Vendas'], alpha=0.6, label='Dados observados')
plt.plot(df['Temperatura'], y_pred, color='red', linewidth=2, label='Linha de regressão')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Vendas de Sorvete (R$)')
plt.title('Regressão Linear: Vendas vs Temperatura')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Equação da reta
print(f"Equação: Vendas = {modelo.intercept_:.2f} + {modelo.coef_[0]:.2f} × Temperatura")
```

---

## **Regressão Linear Múltipla**

### **Modelo Matemático**

$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_p X_p + \varepsilon$$

### **Exemplo: Preço de Imóveis**

```python
# Dados simulados de imóveis
np.random.seed(42)
n_amostras = 100

area = np.random.normal(100, 30, n_amostras)  # Área em m²
quartos = np.random.poisson(3, n_amostras)   # Número de quartos
idade = np.random.exponential(10, n_amostras)  # Idade do imóvel

# Preço baseado em múltiplas variáveis
preco = (2000 * area + 
         15000 * quartos - 
         1000 * idade + 
         np.random.normal(0, 20000, n_amostras))

# DataFrame
df_imoveis = pd.DataFrame({
    'Area': area,
    'Quartos': quartos,
    'Idade': idade,
    'Preco': preco
})

print("Estatísticas descritivas:")
print(df_imoveis.describe())

# Matriz de correlação
print("\nMatriz de correlação:")
correlation_matrix = df_imoveis.corr()
print(correlation_matrix)

# Visualizar correlações
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Matriz de Correlação - Variáveis do Imóvel')
plt.show()
```

### **Ajuste do Modelo Múltiplo**

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Variáveis independentes e dependente
X = df_imoveis[['Area', 'Quartos', 'Idade']]
y = df_imoveis['Preco']

# Divisão treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ajustar modelo
modelo_multiplo = LinearRegression()
modelo_multiplo.fit(X_train, y_train)

# Predições
y_train_pred = modelo_multiplo.predict(X_train)
y_test_pred = modelo_multiplo.predict(X_test)

# Coeficientes
print("Coeficientes do modelo:")
print(f"Intercepto: R$ {modelo_multiplo.intercept_:,.2f}")
for i, coef in enumerate(modelo_multiplo.coef_):
    print(f"{X.columns[i]}: R$ {coef:,.2f}")

# Métricas de avaliação
print(f"\nMétricas do modelo:")
print(f"R² (treino): {r2_score(y_train, y_train_pred):.3f}")
print(f"R² (teste): {r2_score(y_test, y_test_pred):.3f}")
print(f"RMSE (teste): R$ {np.sqrt(mean_squared_error(y_test, y_test_pred)):,.2f}")
print(f"MAE (teste): R$ {mean_absolute_error(y_test, y_test_pred):,.2f}")
```

---

## **Pressupostos da Regressão**

### **1. Linearidade**
A relação entre X e Y deve ser linear.

```python
# Verificar linearidade
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for i, col in enumerate(['Area', 'Quartos', 'Idade']):
    axes[i].scatter(df_imoveis[col], df_imoveis['Preco'], alpha=0.6)
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Preço')
    axes[i].set_title(f'Preço vs {col}')
    axes[i].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### **2. Independência dos Resíduos**
Os resíduos devem ser independentes entre si.

### **3. Homocedasticidade**
A variância dos resíduos deve ser constante.

```python
# Análise de resíduos
residuos = y_test - y_test_pred

# Gráfico de resíduos vs valores preditos
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(y_test_pred, residuos, alpha=0.6)
plt.xlabel('Valores Preditos')
plt.ylabel('Resíduos')
plt.title('Resíduos vs Valores Preditos')
plt.axhline(y=0, color='red', linestyle='--')
plt.grid(True, alpha=0.3)

# Histograma dos resíduos
plt.subplot(1, 2, 2)
plt.hist(residuos, bins=15, alpha=0.7, edgecolor='black')
plt.xlabel('Resíduos')
plt.ylabel('Frequência')
plt.title('Distribuição dos Resíduos')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### **4. Normalidade dos Resíduos**

```python
from scipy import stats

# Teste de normalidade
shapiro_stat, shapiro_p = stats.shapiro(residuos)
print(f"Teste de Shapiro-Wilk:")
print(f"Estatística: {shapiro_stat:.4f}")
print(f"Valor-p: {shapiro_p:.4f}")

if shapiro_p > 0.05:
    print("Os resíduos seguem distribuição normal (p > 0.05)")
else:
    print("Os resíduos não seguem distribuição normal (p ≤ 0.05)")

# Q-Q plot
from scipy.stats import probplot

plt.figure(figsize=(8, 6))
probplot(residuos, dist="norm", plot=plt)
plt.title('Q-Q Plot - Normalidade dos Resíduos')
plt.grid(True, alpha=0.3)
plt.show()
```

---

## **Avaliação do Modelo**

### **Métricas de Avaliação**

#### **1. Coeficiente de Determinação (R²)**
Proporção da variabilidade explicada pelo modelo.

$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}}$$

```python
def metricas_regressao(y_true, y_pred):
    """Calcular múltiplas métricas de regressão"""
    
    # R²
    r2 = r2_score(y_true, y_pred)
    
    # R² ajustado
    n = len(y_true)
    p = X_test.shape[1]  # número de variáveis
    r2_adj = 1 - (1 - r2) * (n - 1) / (n - p - 1)
    
    # RMSE (Root Mean Squared Error)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    
    # MAE (Mean Absolute Error)
    mae = mean_absolute_error(y_true, y_pred)
    
    # MAPE (Mean Absolute Percentage Error)
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    
    return {
        'R²': r2,
        'R² Ajustado': r2_adj,
        'RMSE': rmse,
        'MAE': mae,
        'MAPE': mape
    }

# Calcular métricas
metricas = metricas_regressao(y_test, y_test_pred)

print("Métricas de Avaliação:")
for metrica, valor in metricas.items():
    if metrica in ['RMSE', 'MAE']:
        print(f"{metrica}: R$ {valor:,.2f}")
    elif metrica == 'MAPE':
        print(f"{metrica}: {valor:.2f}%")
    else:
        print(f"{metrica}: {valor:.3f}")
```

### **2. Análise de Importância das Variáveis**

```python
# Importância das variáveis (coeficientes padronizados)
from sklearn.preprocessing import StandardScaler

# Padronizar variáveis
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Ajustar modelo com dados padronizados
modelo_padronizado = LinearRegression()
modelo_padronizado.fit(X_scaled, y)

# Importância relativa
importancia = pd.DataFrame({
    'Variavel': X.columns,
    'Coeficiente': modelo_multiplo.coef_,
    'Coef_Padronizado': modelo_padronizado.coef_,
    'Importancia_Abs': np.abs(modelo_padronizado.coef_)
}).sort_values('Importancia_Abs', ascending=False)

print("\nImportância das Variáveis:")
print(importancia)

# Visualizar importância
plt.figure(figsize=(10, 6))
plt.barh(importancia['Variavel'], importancia['Importancia_Abs'])
plt.xlabel('Importância Absoluta (Coeficiente Padronizado)')
plt.title('Importância das Variáveis no Modelo')
plt.grid(True, alpha=0.3)
plt.show()
```

---

## **Tipos Especiais de Regressão**

### **1. Regressão Polinomial**

```python
from sklearn.preprocessing import PolynomialFeatures

# Exemplo: Relação não-linear entre idade do carro e depreciação
np.random.seed(42)
idade_carro = np.random.uniform(0, 20, 100)
valor_carro = 50000 * np.exp(-0.15 * idade_carro) + np.random.normal(0, 2000, 100)

# Regressão linear simples
modelo_linear = LinearRegression()
modelo_linear.fit(idade_carro.reshape(-1, 1), valor_carro)

# Regressão polinomial (grau 2)
poly_features = PolynomialFeatures(degree=2)
idade_poly = poly_features.fit_transform(idade_carro.reshape(-1, 1))

modelo_poly = LinearRegression()
modelo_poly.fit(idade_poly, valor_carro)

# Comparar modelos
idade_teste = np.linspace(0, 20, 100).reshape(-1, 1)
pred_linear = modelo_linear.predict(idade_teste)
pred_poly = modelo_poly.predict(poly_features.transform(idade_teste))

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(idade_carro, valor_carro, alpha=0.6, label='Dados')
plt.plot(idade_teste, pred_linear, 'r-', label='Linear')
plt.xlabel('Idade do Carro (anos)')
plt.ylabel('Valor (R$)')
plt.title('Regressão Linear')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.scatter(idade_carro, valor_carro, alpha=0.6, label='Dados')
plt.plot(idade_teste, pred_poly, 'g-', label='Polinomial (grau 2)')
plt.xlabel('Idade do Carro (anos)')
plt.ylabel('Valor (R$)')
plt.title('Regressão Polinomial')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Comparar R²
r2_linear = r2_score(valor_carro, modelo_linear.predict(idade_carro.reshape(-1, 1)))
r2_poly = r2_score(valor_carro, modelo_poly.predict(idade_poly))

print(f"R² Linear: {r2_linear:.3f}")
print(f"R² Polinomial: {r2_poly:.3f}")
```

### **2. Regressão Ridge (L2)**

```python
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

# Regressão Ridge para lidar com multicolinearidade
alphas = [0.1, 1, 10, 100]
ridge_scores = []

for alpha in alphas:
    ridge = Ridge(alpha=alpha)
    scores = cross_val_score(ridge, X_train, y_train, cv=5, scoring='r2')
    ridge_scores.append(scores.mean())

# Melhor alpha
melhor_alpha = alphas[np.argmax(ridge_scores)]
print(f"Melhor alpha para Ridge: {melhor_alpha}")

# Modelo Ridge otimizado
ridge_modelo = Ridge(alpha=melhor_alpha)
ridge_modelo.fit(X_train, y_train)
ridge_pred = ridge_modelo.predict(X_test)

print(f"R² Ridge: {r2_score(y_test, ridge_pred):.3f}")
print(f"R² Linear: {r2_score(y_test, y_test_pred):.3f}")
```

### **3. Regressão Lasso (L1)**

```python
from sklearn.linear_model import Lasso

# Regressão Lasso para seleção de variáveis
lasso = Lasso(alpha=1000)
lasso.fit(X_train, y_train)
lasso_pred = lasso.predict(X_test)

print(f"\nCoeficientes Lasso:")
for i, coef in enumerate(lasso.coef_):
    print(f"{X.columns[i]}: {coef:.2f}")

print(f"\nR² Lasso: {r2_score(y_test, lasso_pred):.3f}")
```

---

## **Exemplo Prático Completo: Análise de Vendas**

```python
# Cenário: Empresa quer prever vendas baseado em investimento em marketing
np.random.seed(42)
n = 200

# Variáveis independentes
tv_ads = np.random.uniform(0, 300, n)          # Gastos com TV (milhares)
radio_ads = np.random.uniform(0, 50, n)       # Gastos com Rádio (milhares)
newspaper_ads = np.random.uniform(0, 100, n)  # Gastos com Jornal (milhares)
competitor_price = np.random.uniform(50, 150, n)  # Preço do concorrente

# Vendas (variável dependente)
vendas = (2.5 * tv_ads + 
          4.0 * radio_ads + 
          0.1 * newspaper_ads +
          -0.8 * competitor_price +
          np.random.normal(0, 20, n) + 100)

# DataFrame
df_vendas = pd.DataFrame({
    'TV_Ads': tv_ads,
    'Radio_Ads': radio_ads,
    'Newspaper_Ads': newspaper_ads,
    'Competitor_Price': competitor_price,
    'Sales': vendas
})

print("Dataset de Vendas - Primeiras 5 linhas:")
print(df_vendas.head())

# Análise exploratória
print("\nCorrelação com vendas:")
correlacoes = df_vendas.corr()['Sales'].sort_values(ascending=False)
print(correlacoes)

# Modelo final
X = df_vendas.drop('Sales', axis=1)
y = df_vendas['Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo_final = LinearRegression()
modelo_final.fit(X_train, y_train)
y_pred_final = modelo_final.predict(X_test)

# Resultados
print(f"\nResultados do Modelo de Vendas:")
print(f"R²: {r2_score(y_test, y_pred_final):.3f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred_final)):.2f}")

print(f"\nCoeficientes:")
print(f"Intercepto: {modelo_final.intercept_:.2f}")
for i, coef in enumerate(modelo_final.coef_):
    print(f"{X.columns[i]}: {coef:.2f}")

# Interpretação de negócio
print(f"\nInterpretação de Negócio:")
print(f"• Para cada R$ 1.000 investidos em TV, vendas aumentam em {modelo_final.coef_[0]:.1f} unidades")
print(f"• Para cada R$ 1.000 investidos em Rádio, vendas aumentam em {modelo_final.coef_[1]:.1f} unidades")
print(f"• Para cada R$ 1 de aumento no preço do concorrente, vendas aumentam em {modelo_final.coef_[3]:.1f} unidades")
```

---

## **Conclusão**

A análise de regressão é uma ferramenta poderosa para:

### **✅ Aplicações Práticas**
- **Previsão de vendas** baseada em investimento em marketing
- **Avaliação de imóveis** considerando características físicas
- **Análise de fatores** que influenciam performance
- **Modelagem de crescimento** de negócios

### **🎯 Pontos-Chave**
- Sempre verificar pressupostos antes da interpretação
- R² alto não garante modelo útil
- Avaliar significância prática além da estatística
- Considerar overfitting em modelos complexos

### **⚠️ Limitações**
- Assume relações lineares (exceto quando modificada)
- Sensível a outliers
- Pressupostos devem ser atendidos
- Correlação ≠ Causação

### **🚀 Próximos Passos**
- Explorar métodos de regularização (Ridge, Lasso)
- Aprender regressão logística para variáveis categóricas
- Estudar métodos não-lineares (Random Forest, Neural Networks)
- Implementar validação cruzada e seleção de modelos

---

## **Referências**

**JAMES, Gareth et al.** *An Introduction to Statistical Learning: with Applications in R*. 2. ed. New York: Springer, 2021.

**MONTGOMERY, Douglas C.; PECK, Elizabeth A.; VINING, G. Geoffrey.** *Introduction to Linear Regression Analysis*. 5. ed. Hoboken: Wiley, 2012.

**KUTNER, Michael H. et al.** *Applied Linear Statistical Models*. 5. ed. New York: McGraw-Hill, 2005.

**HASTIE, Trevor; TIBSHIRANI, Robert; FRIEDMAN, Jerome.** *The Elements of Statistical Learning*. 2. ed. New York: Springer, 2009.