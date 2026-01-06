# Regressão Linear Simples

## Sumário

1. [Introdução](#introdução)
2. [Conceitos Fundamentais](#conceitos-fundamentais)
3. [Modelo Matemático](#modelo-matemático)
4. [Método dos Mínimos Quadrados](#método-dos-mínimos-quadrados)
5. [Interpretação dos Coeficientes](#interpretação-dos-coeficientes)
6. [Pressupostos do Modelo](#pressupostos-do-modelo)
7. [Métricas de Avaliação](#métricas-de-avaliação)
8. [Exemplos do Dia a Dia](#exemplos-do-dia-a-dia)
9. [Implementação em Python](#implementação-em-python)
10. [Limitações e Cuidados](#limitações-e-cuidados)
11. [Exercícios Práticos](#exercícios-práticos)
12. [Referências](#referências)

---

## Introdução

A **Regressão Linear Simples** é uma das técnicas estatísticas mais fundamentais e amplamente utilizadas para modelar a relação entre duas variáveis quantitativas. Ela estabelece uma relação linear entre uma variável dependente (resposta) e uma única variável independente (explicativa).

### Objetivos da Regressão Linear Simples

- **Descrever** a relação entre duas variáveis
- **Quantificar** a força e direção dessa relação
- **Predizer** valores futuros da variável dependente
- **Identificar** tendências e padrões nos dados

### Quando Usar?

A regressão linear simples é apropriada quando:
- Você tem uma variável dependente contínua
- Você tem uma variável independente contínua
- A relação entre as variáveis é aproximadamente linear
- Você quer entender como mudanças em X afetam Y

---

## Conceitos Fundamentais

### Variável Dependente (Y)

É a variável que queremos explicar ou predizer. Também chamada de:
- Variável resposta
- Variável de saída
- Variável explicada

**Exemplos:**
- Vendas de um produto
- Preço de um imóvel
- Peso de uma pessoa
- Consumo de energia

### Variável Independente (X)

É a variável que usamos para explicar ou predizer Y. Também chamada de:
- Variável explicativa
- Variável preditora
- Variável de entrada
- Regressor

**Exemplos:**
- Investimento em publicidade (para prever vendas)
- Área em m² (para prever preço de imóvel)
- Altura (para prever peso)
- Temperatura (para prever consumo de energia)

### Relação Linear

Uma relação é considerada linear quando os pontos em um gráfico de dispersão tendem a formar uma linha reta. Isso significa que mudanças proporcionais em X resultam em mudanças proporcionais em Y.

---

## Modelo Matemático

### Equação da Regressão Linear Simples

O modelo de regressão linear simples é expresso matematicamente como:

$$Y = \beta_0 + \beta_1 X + \varepsilon$$

Onde:
- **Y**: Variável dependente (variável resposta)
- **X**: Variável independente (variável explicativa)
- **β₀**: Intercepto (constante) - valor de Y quando X = 0
- **β₁**: Coeficiente angular (inclinação) - mudança em Y para cada unidade de mudança em X
- **ε**: Termo de erro aleatório (resíduo)

### Equação da Linha de Regressão Ajustada

Na prática, trabalhamos com valores estimados:

$$\hat{Y} = \hat{\beta}_0 + \hat{\beta}_1 X$$

Onde:
- **Ŷ**: Valor predito de Y
- **β̂₀**: Estimativa do intercepto
- **β̂₁**: Estimativa do coeficiente angular

### Resíduos

Os resíduos representam a diferença entre os valores observados e preditos:

$$e_i = Y_i - \hat{Y}_i$$

O objetivo da regressão é minimizar esses resíduos.

---

## Método dos Mínimos Quadrados

O Método dos Mínimos Quadrados Ordinários (MQO) é a técnica mais comum para estimar os parâmetros β₀ e β₁. O método busca minimizar a soma dos quadrados dos resíduos.

### Função Objetivo

Minimizar:

$$SQR = \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2 = \sum_{i=1}^{n} (Y_i - \hat{\beta}_0 - \hat{\beta}_1 X_i)^2$$

### Fórmulas dos Estimadores

As fórmulas para os estimadores de mínimos quadrados são:

**Coeficiente Angular:**

$$\hat{\beta}_1 = \frac{\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}{\sum_{i=1}^{n} (X_i - \bar{X})^2} = \frac{Cov(X,Y)}{Var(X)}$$

**Intercepto:**

$$\hat{\beta}_0 = \bar{Y} - \hat{\beta}_1 \bar{X}$$

Onde:
- **X̄**: Média de X
- **Ȳ**: Média de Y
- **Cov(X,Y)**: Covariância entre X e Y
- **Var(X)**: Variância de X

### Propriedades da Linha de Regressão

1. A linha de regressão sempre passa pelo ponto (X̄, Ȳ)
2. A soma dos resíduos é sempre zero: Σeᵢ = 0
3. Os resíduos são ortogonais aos valores preditos

---

## Interpretação dos Coeficientes

### Interpretação do Intercepto (β₀)

O intercepto representa o valor esperado de Y quando X = 0.

**Exemplo:**
- Se β₀ = 50 em um modelo que prevê vendas baseado em gastos com publicidade
- Interpretação: Quando não há gastos com publicidade (X=0), espera-se ter 50 unidades de vendas

⚠️ **Cuidado:** A interpretação só faz sentido se X = 0 estiver dentro do intervalo dos dados observados.

### Interpretação do Coeficiente Angular (β₁)

O coeficiente angular representa a mudança esperada em Y para cada aumento de uma unidade em X.

**Exemplo:**
- Se β₁ = 3.5 em um modelo que prevê vendas (em milhares) baseado em gastos com publicidade (em milhares de reais)
- Interpretação: Para cada R$ 1.000 adicionais investidos em publicidade, espera-se um aumento de 3.500 unidades nas vendas

### Sinal do Coeficiente Angular

- **β₁ > 0**: Relação positiva (aumento em X resulta em aumento em Y)
- **β₁ < 0**: Relação negativa (aumento em X resulta em diminuição em Y)
- **β₁ = 0**: Não há relação linear entre X e Y

---

## Pressupostos do Modelo

Para que a regressão linear simples forneça resultados válidos e confiáveis, alguns pressupostos devem ser atendidos:

### 1. Linearidade

**Descrição:** A relação entre X e Y deve ser linear.

**Como verificar:** 
- Gráfico de dispersão entre X e Y
- Gráfico de resíduos vs valores preditos

**O que fazer se violado:**
- Transformar variáveis (log, raiz quadrada, etc.)
- Considerar regressão polinomial
- Usar modelos não-lineares

### 2. Independência dos Resíduos

**Descrição:** Os resíduos devem ser independentes entre si. Não deve haver correlação entre os erros.

**Como verificar:**
- Teste de Durbin-Watson
- Gráfico de resíduos em sequência temporal

**Quando é violado:**
- Dados de séries temporais
- Observações agrupadas ou aninhadas
- Autocorrelação espacial

### 3. Homocedasticidade

**Descrição:** A variância dos resíduos deve ser constante para todos os valores de X.

**Como verificar:**
- Gráfico de resíduos vs valores preditos (buscar padrão de cone)
- Teste de Breusch-Pagan
- Teste de White

**O que fazer se violado:**
- Transformar a variável dependente
- Usar regressão ponderada
- Corrigir erros padrão (erros robustos)

### 4. Normalidade dos Resíduos

**Descrição:** Os resíduos devem seguir uma distribuição normal.

**Como verificar:**
- Histograma dos resíduos
- Q-Q plot
- Teste de Shapiro-Wilk
- Teste de Kolmogorov-Smirnov

**Importância:**
- Menos crítico para amostras grandes (Teorema do Limite Central)
- Importante para inferência estatística (intervalos de confiança e testes de hipótese)

### 5. Ausência de Outliers Influentes

**Descrição:** Outliers não devem ter influência desproporcional nos coeficientes estimados.

**Como verificar:**
- Distância de Cook
- Leverage (alavancagem)
- DFBETAS e DFFITS

---

## Métricas de Avaliação

### 1. Coeficiente de Determinação (R²)

O R² mede a proporção da variabilidade em Y que é explicada pelo modelo.

$$R^2 = 1 - \frac{SQR}{SQT} = 1 - \frac{\sum(Y_i - \hat{Y}_i)^2}{\sum(Y_i - \bar{Y})^2}$$

**Interpretação:**
- **R² = 0**: O modelo não explica nada da variabilidade em Y
- **R² = 1**: O modelo explica 100% da variabilidade em Y
- **R² = 0.7**: O modelo explica 70% da variabilidade em Y

**Limitações:**
- Não indica se o modelo é adequado
- Pode ser artificialmente alto com dados limitados
- Não penaliza complexidade do modelo

### 2. Coeficiente de Correlação (r)

A correlação de Pearson mede a força e direção da relação linear entre X e Y.

$$r = \frac{Cov(X,Y)}{\sigma_X \sigma_Y}$$

**Propriedades:**
- Varia entre -1 e 1
- r = ±√R² na regressão simples
- |r| próximo de 1 indica forte relação linear
- r próximo de 0 indica fraca relação linear

### 3. Erro Quadrático Médio (MSE)

$$MSE = \frac{1}{n} \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2$$

Representa o erro médio ao quadrado. Valores menores indicam melhor ajuste.

### 4. Raiz do Erro Quadrático Médio (RMSE)

$$RMSE = \sqrt{MSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2}$$

Tem a mesma unidade da variável Y, facilitando a interpretação.

### 5. Erro Absoluto Médio (MAE)

$$MAE = \frac{1}{n} \sum_{i=1}^{n} |Y_i - \hat{Y}_i|$$

Menos sensível a outliers que o MSE/RMSE.

### 6. Erro Percentual Absoluto Médio (MAPE)

$$MAPE = \frac{100\%}{n} \sum_{i=1}^{n} \left|\frac{Y_i - \hat{Y}_i}{Y_i}\right|$$

Expressa o erro como percentual do valor real.

---

## Exemplos do Dia a Dia

### Exemplo 1: Vendas de Sorvete vs Temperatura

**Contexto:** Uma sorveteria quer entender como a temperatura afeta suas vendas diárias.

**Variáveis:**
- Y = Vendas diárias (em reais)
- X = Temperatura máxima do dia (em °C)

**Hipótese:** Dias mais quentes resultam em maiores vendas de sorvete.

**Modelo Esperado:** Y = β₀ + β₁X, onde β₁ > 0

**Utilidade Prática:**
- Previsão de vendas baseada na previsão do tempo
- Planejamento de estoque
- Alocação de funcionários
- Decisões sobre promoções

### Exemplo 2: Preço de Imóvel vs Área

**Contexto:** Uma imobiliária quer estabelecer o preço de venda de apartamentos baseado na área.

**Variáveis:**
- Y = Preço do apartamento (em milhares de reais)
- X = Área do apartamento (em m²)

**Hipótese:** Apartamentos maiores têm preços mais altos.

**Modelo Esperado:** Y = β₀ + β₁X, onde β₁ > 0

**Utilidade Prática:**
- Precificação de novos imóveis
- Avaliação de ofertas
- Negociação com compradores
- Análise de mercado

### Exemplo 3: Consumo de Combustível vs Velocidade

**Contexto:** Um motorista quer saber como a velocidade média afeta o consumo de combustível.

**Variáveis:**
- Y = Consumo de combustível (litros/100km)
- X = Velocidade média (km/h)

**Modelo Esperado:** Pode ser linear em certos intervalos de velocidade

**Utilidade Prática:**
- Otimização de rotas
- Economia de combustível
- Planejamento de viagens
- Análise de custo-benefício

### Exemplo 4: Nota Final vs Horas de Estudo

**Contexto:** Um estudante quer avaliar o impacto das horas de estudo na nota final.

**Variáveis:**
- Y = Nota final (0-10)
- X = Horas de estudo por semana

**Hipótese:** Mais horas de estudo resultam em notas mais altas.

**Utilidade Prática:**
- Planejamento de estudos
- Definição de metas realistas
- Otimização de tempo
- Avaliação de efetividade

### Exemplo 5: Custo de Produção vs Quantidade

**Contexto:** Uma fábrica quer entender a relação entre quantidade produzida e custo total.

**Variáveis:**
- Y = Custo total de produção (em milhares de reais)
- X = Quantidade produzida (unidades)

**Modelo Esperado:** Y = β₀ + β₁X

**Utilidade Prática:**
- Orçamento de produção
- Análise de viabilidade
- Precificação de produtos
- Decisões sobre escala de produção

---

## Implementação em Python

### Exemplo Completo: Vendas de Sorvete vs Temperatura

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from scipy import stats

# Configurar estilo de gráficos
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# ==============================
# 1. GERAR DADOS SIMULADOS
# ==============================
np.random.seed(42)
n_amostras = 50

# Temperatura em graus Celsius
temperatura = np.random.normal(25, 5, n_amostras)

# Vendas com relação linear + ruído
vendas = 100 + 3 * temperatura + np.random.normal(0, 10, n_amostras)

# Criar DataFrame
df = pd.DataFrame({
    'Temperatura': temperatura,
    'Vendas': vendas
})

print("=" * 60)
print("DADOS DO EXEMPLO: VENDAS DE SORVETE")
print("=" * 60)
print(f"\nNúmero de observações: {len(df)}")
print("\nPrimeiras 5 observações:")
print(df.head())
print("\nEstatísticas descritivas:")
print(df.describe())

# ==============================
# 2. ANÁLISE EXPLORATÓRIA
# ==============================

# Gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(df['Temperatura'], df['Vendas'], alpha=0.6, s=100, edgecolors='black')
plt.xlabel('Temperatura (°C)', fontsize=12)
plt.ylabel('Vendas de Sorvete (R$)', fontsize=12)
plt.title('Relação entre Temperatura e Vendas de Sorvete', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('01_dispersao.png', dpi=300, bbox_inches='tight')
plt.show()

# Correlação
correlacao = df['Temperatura'].corr(df['Vendas'])
print(f"\nCorrelação de Pearson: {correlacao:.4f}")

# ==============================
# 3. AJUSTAR MODELO DE REGRESSÃO
# ==============================

# Preparar dados
X = df[['Temperatura']]  # Variável independente (formato matriz)
y = df['Vendas']          # Variável dependente

# Criar e ajustar o modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Fazer predições
y_pred = modelo.predict(X)

# Extrair coeficientes
intercepto = modelo.intercept_
coef_angular = modelo.coef_[0]

print("\n" + "=" * 60)
print("RESULTADOS DO MODELO DE REGRESSÃO")
print("=" * 60)
print(f"\nIntercepto (β₀): {intercepto:.2f}")
print(f"Coeficiente Angular (β₁): {coef_angular:.2f}")
print(f"\nEquação da reta: Vendas = {intercepto:.2f} + {coef_angular:.2f} × Temperatura")

# ==============================
# 4. INTERPRETAÇÃO DOS COEFICIENTES
# ==============================

print("\n" + "=" * 60)
print("INTERPRETAÇÃO")
print("=" * 60)
print(f"\n• Intercepto: Quando a temperatura é 0°C, as vendas esperadas são R$ {intercepto:.2f}")
print(f"• Coeficiente Angular: Para cada 1°C de aumento na temperatura,")
print(f"  as vendas aumentam em R$ {coef_angular:.2f}")
print(f"\nExemplo prático:")
temp_exemplo = 30
venda_prevista = intercepto + coef_angular * temp_exemplo
print(f"• Com temperatura de {temp_exemplo}°C, espera-se vendas de R$ {venda_prevista:.2f}")

# ==============================
# 5. VISUALIZAR LINHA DE REGRESSÃO
# ==============================

plt.figure(figsize=(10, 6))
plt.scatter(df['Temperatura'], df['Vendas'], alpha=0.6, s=100, 
            edgecolors='black', label='Dados observados')
plt.plot(df['Temperatura'], y_pred, color='red', linewidth=2, 
         label=f'Linha de regressão: Y = {intercepto:.1f} + {coef_angular:.1f}X')
plt.xlabel('Temperatura (°C)', fontsize=12)
plt.ylabel('Vendas de Sorvete (R$)', fontsize=12)
plt.title('Regressão Linear: Vendas vs Temperatura', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('02_regressao.png', dpi=300, bbox_inches='tight')
plt.show()

# ==============================
# 6. MÉTRICAS DE AVALIAÇÃO
# ==============================

# Calcular métricas
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))
mae = mean_absolute_error(y, y_pred)
mape = np.mean(np.abs((y - y_pred) / y)) * 100

print("\n" + "=" * 60)
print("MÉTRICAS DE AVALIAÇÃO DO MODELO")
print("=" * 60)
print(f"\nR² (Coeficiente de Determinação): {r2:.4f}")
print(f"  → O modelo explica {r2*100:.2f}% da variabilidade nas vendas")
print(f"\nRMSE (Raiz do Erro Quadrático Médio): R$ {rmse:.2f}")
print(f"  → Erro médio das previsões")
print(f"\nMAE (Erro Absoluto Médio): R$ {mae:.2f}")
print(f"  → Erro médio absoluto das previsões")
print(f"\nMAPE (Erro Percentual Absoluto Médio): {mape:.2f}%")
print(f"  → Erro médio em percentual")

# ==============================
# 7. ANÁLISE DOS RESÍDUOS
# ==============================

# Calcular resíduos
residuos = y - y_pred

# Criar figura com múltiplos subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Subplot 1: Resíduos vs Valores Preditos
axes[0, 0].scatter(y_pred, residuos, alpha=0.6, s=100, edgecolors='black')
axes[0, 0].axhline(y=0, color='red', linestyle='--', linewidth=2)
axes[0, 0].set_xlabel('Valores Preditos', fontsize=11)
axes[0, 0].set_ylabel('Resíduos', fontsize=11)
axes[0, 0].set_title('Resíduos vs Valores Preditos', fontsize=12, fontweight='bold')
axes[0, 0].grid(True, alpha=0.3)

# Subplot 2: Histograma dos Resíduos
axes[0, 1].hist(residuos, bins=15, alpha=0.7, edgecolor='black', color='skyblue')
axes[0, 1].axvline(x=0, color='red', linestyle='--', linewidth=2)
axes[0, 1].set_xlabel('Resíduos', fontsize=11)
axes[0, 1].set_ylabel('Frequência', fontsize=11)
axes[0, 1].set_title('Distribuição dos Resíduos', fontsize=12, fontweight='bold')
axes[0, 1].grid(True, alpha=0.3)

# Subplot 3: Q-Q Plot
stats.probplot(residuos, dist="norm", plot=axes[1, 0])
axes[1, 0].set_title('Q-Q Plot (Normalidade)', fontsize=12, fontweight='bold')
axes[1, 0].grid(True, alpha=0.3)

# Subplot 4: Resíduos vs Ordem
axes[1, 1].scatter(range(len(residuos)), residuos, alpha=0.6, s=100, edgecolors='black')
axes[1, 1].axhline(y=0, color='red', linestyle='--', linewidth=2)
axes[1, 1].set_xlabel('Ordem das Observações', fontsize=11)
axes[1, 1].set_ylabel('Resíduos', fontsize=11)
axes[1, 1].set_title('Resíduos vs Ordem', fontsize=12, fontweight='bold')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('03_analise_residuos.png', dpi=300, bbox_inches='tight')
plt.show()

# ==============================
# 8. TESTES DE PRESSUPOSTOS
# ==============================

print("\n" + "=" * 60)
print("VERIFICAÇÃO DOS PRESSUPOSTOS")
print("=" * 60)

# Teste de Normalidade (Shapiro-Wilk)
shapiro_stat, shapiro_p = stats.shapiro(residuos)
print(f"\n1. NORMALIDADE DOS RESÍDUOS")
print(f"   Teste de Shapiro-Wilk:")
print(f"   Estatística: {shapiro_stat:.4f}")
print(f"   Valor-p: {shapiro_p:.4f}")
if shapiro_p > 0.05:
    print(f"   ✓ Os resíduos seguem distribuição normal (p > 0.05)")
else:
    print(f"   ✗ Os resíduos NÃO seguem distribuição normal (p ≤ 0.05)")

# Teste de Homocedasticidade Visual
print(f"\n2. HOMOCEDASTICIDADE")
print(f"   Verificar visualmente no gráfico 'Resíduos vs Valores Preditos'")
print(f"   • Sem padrão de cone: homocedasticidade ✓")
print(f"   • Padrão de cone: heterocedasticidade ✗")

# Independência
print(f"\n3. INDEPENDÊNCIA")
print(f"   Verificar visualmente no gráfico 'Resíduos vs Ordem'")
print(f"   • Sem padrão: independência ✓")
print(f"   • Padrão temporal: autocorrelação ✗")

# ==============================
# 9. FAZER PREDIÇÕES
# ==============================

print("\n" + "=" * 60)
print("FAZENDO PREDIÇÕES")
print("=" * 60)

# Temperaturas para prever
temperaturas_novas = np.array([20, 25, 30, 35]).reshape(-1, 1)
vendas_previstas = modelo.predict(temperaturas_novas)

print("\nPrevisões para diferentes temperaturas:")
for temp, venda in zip(temperaturas_novas.flatten(), vendas_previstas):
    print(f"  Temperatura: {temp}°C → Vendas previstas: R$ {venda:.2f}")

# ==============================
# 10. INTERVALO DE CONFIANÇA
# ==============================

# Calcular erro padrão dos resíduos
n = len(y)
s_res = np.sqrt(np.sum(residuos**2) / (n - 2))

# Erro padrão da predição para uma nova observação
X_mean = X.values.mean()
X_std = X.values.std()
se_pred = s_res * np.sqrt(1 + 1/n + ((temperaturas_novas - X_mean)**2) / (n * X_std**2))

# Intervalo de confiança 95%
t_value = stats.t.ppf(0.975, n - 2)
ic_lower = vendas_previstas - t_value * se_pred.flatten()
ic_upper = vendas_previstas + t_value * se_pred.flatten()

print("\nIntervalos de confiança de 95% para as predições:")
for temp, venda, lower, upper in zip(temperaturas_novas.flatten(), 
                                      vendas_previstas, ic_lower, ic_upper):
    print(f"  {temp}°C: R$ {venda:.2f} [IC 95%: R$ {lower:.2f} - R$ {upper:.2f}]")

print("\n" + "=" * 60)
print("ANÁLISE COMPLETA FINALIZADA")
print("=" * 60)
```

### Visualizando Diferentes Cenários

```python
# Exemplo com diferentes tipos de relação
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

np.random.seed(42)
x = np.random.uniform(0, 10, 100)

# 1. Correlação positiva forte (r ≈ 0.9)
y1 = 2 * x + np.random.normal(0, 1, 100)
axes[0, 0].scatter(x, y1, alpha=0.6)
axes[0, 0].plot(x, np.poly1d(np.polyfit(x, y1, 1))(x), 'r-', linewidth=2)
axes[0, 0].set_title(f'Correlação Positiva Forte\nr = {np.corrcoef(x, y1)[0,1]:.2f}')
axes[0, 0].grid(True, alpha=0.3)

# 2. Correlação positiva moderada (r ≈ 0.6)
y2 = 2 * x + np.random.normal(0, 3, 100)
axes[0, 1].scatter(x, y2, alpha=0.6)
axes[0, 1].plot(x, np.poly1d(np.polyfit(x, y2, 1))(x), 'r-', linewidth=2)
axes[0, 1].set_title(f'Correlação Positiva Moderada\nr = {np.corrcoef(x, y2)[0,1]:.2f}')
axes[0, 1].grid(True, alpha=0.3)

# 3. Correlação fraca (r ≈ 0.3)
y3 = 2 * x + np.random.normal(0, 8, 100)
axes[0, 2].scatter(x, y3, alpha=0.6)
axes[0, 2].plot(x, np.poly1d(np.polyfit(x, y3, 1))(x), 'r-', linewidth=2)
axes[0, 2].set_title(f'Correlação Fraca\nr = {np.corrcoef(x, y3)[0,1]:.2f}')
axes[0, 2].grid(True, alpha=0.3)

# 4. Correlação negativa forte (r ≈ -0.9)
y4 = -2 * x + 20 + np.random.normal(0, 1, 100)
axes[1, 0].scatter(x, y4, alpha=0.6)
axes[1, 0].plot(x, np.poly1d(np.polyfit(x, y4, 1))(x), 'r-', linewidth=2)
axes[1, 0].set_title(f'Correlação Negativa Forte\nr = {np.corrcoef(x, y4)[0,1]:.2f}')
axes[1, 0].grid(True, alpha=0.3)

# 5. Sem correlação (r ≈ 0)
y5 = np.random.normal(10, 3, 100)
axes[1, 1].scatter(x, y5, alpha=0.6)
axes[1, 1].plot(x, np.poly1d(np.polyfit(x, y5, 1))(x), 'r-', linewidth=2)
axes[1, 1].set_title(f'Sem Correlação\nr = {np.corrcoef(x, y5)[0,1]:.2f}')
axes[1, 1].grid(True, alpha=0.3)

# 6. Relação não-linear
y6 = x**2 + np.random.normal(0, 3, 100)
axes[1, 2].scatter(x, y6, alpha=0.6)
axes[1, 2].plot(x, np.poly1d(np.polyfit(x, y6, 1))(x), 'r-', linewidth=2)
axes[1, 2].set_title(f'Relação Não-Linear\nr = {np.corrcoef(x, y6)[0,1]:.2f}\n(Inadequado para regressão linear)')
axes[1, 2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('04_tipos_correlacao.png', dpi=300, bbox_inches='tight')
plt.show()
```

---

## Limitações e Cuidados

### 1. Extrapolação

**Problema:** Fazer previsões fora do intervalo dos dados observados pode levar a resultados não confiáveis.

**Exemplo:** Se seus dados de temperatura vão de 15°C a 35°C, fazer previsões para 50°C é arriscado.

**Cuidado:** 
- Sempre verifique se o valor de X está dentro do intervalo observado
- Previsões fora do intervalo têm maior incerteza

### 2. Correlação ≠ Causação

**Problema:** Uma forte correlação não implica que X causa Y.

**Exemplo Clássico:** Vendas de sorvete e afogamentos estão correlacionadas, mas o sorvete não causa afogamentos. Ambos são causados por um terceiro fator: temperatura.

**Cuidado:**
- Sempre considere variáveis confundidoras
- Use conhecimento do domínio para interpretação
- Teste de causalidade requer experimentos controlados

### 3. Outliers

**Problema:** Valores extremos podem distorcer a linha de regressão.

**Cuidado:**
- Identifique e investigue outliers
- Considere se são erros de medição ou valores legítimos
- Use técnicas robustas se necessário

### 4. Multicolinearidade (não aplicável em regressão simples)

**Nota:** Este problema só ocorre na regressão múltipla, mas é importante estar ciente para futuras análises.

### 5. Não-Linearidade

**Problema:** Se a relação real não é linear, o modelo será inadequado.

**Cuidado:**
- Sempre faça gráfico de dispersão antes de ajustar o modelo
- Verifique gráficos de resíduos
- Considere transformações ou modelos não-lineares

### 6. Variabilidade não Constante (Heterocedasticidade)

**Problema:** Se a variabilidade dos resíduos aumenta com X, as inferências estatísticas são comprometidas.

**Cuidado:**
- Verifique gráfico de resíduos
- Considere transformação da variável Y (log, raiz quadrada)
- Use regressão ponderada ou erros robustos

---

## Exercícios Práticos

### Exercício 1: Análise de Dados Reais

Use os dados abaixo para construir um modelo de regressão:

```python
# Dados: Horas de estudo vs Nota
horas_estudo = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
notas = [55, 60, 65, 70, 75, 80, 85, 88, 92, 95]

# Tarefas:
# 1. Criar gráfico de dispersão
# 2. Calcular correlação
# 3. Ajustar modelo de regressão
# 4. Interpretar coeficientes
# 5. Calcular R²
# 6. Fazer previsão para 11 horas de estudo
# 7. Analisar resíduos
```

### Exercício 2: Validação de Pressupostos

Dado um conjunto de dados, verifique todos os pressupostos da regressão linear:
1. Linearidade
2. Independência
3. Homocedasticidade
4. Normalidade dos resíduos
5. Ausência de outliers influentes

### Exercício 3: Comparação de Modelos

Compare o desempenho de diferentes modelos usando as mesmas variáveis mas com diferentes transformações:
1. Y vs X (modelo original)
2. log(Y) vs X
3. Y vs log(X)
4. log(Y) vs log(X)

Qual modelo tem melhor ajuste?

### Exercício 4: Caso de Negócio

Você é analista de uma empresa e precisa:
1. Identificar a relação entre gastos com marketing e vendas
2. Quantificar o retorno sobre investimento (ROI)
3. Fazer recomendações sobre o orçamento de marketing
4. Calcular intervalos de confiança para as predições

---

## Referências

### Livros Fundamentais

**JAMES, Gareth et al.** *An Introduction to Statistical Learning: with Applications in R*. 2. ed. New York: Springer, 2021.
- Capítulo 3: Linear Regression
- Abordagem prática e acessível
- Excelente para iniciantes

**MONTGOMERY, Douglas C.; PECK, Elizabeth A.; VINING, G. Geoffrey.** *Introduction to Linear Regression Analysis*. 5. ed. Hoboken: Wiley, 2012.
- Texto clássico e completo
- Foco em fundamentos teóricos e aplicações

**KUTNER, Michael H. et al.** *Applied Linear Statistical Models*. 5. ed. New York: McGraw-Hill, 2005.
- Abordagem aplicada
- Muitos exemplos práticos

**FOX, John.** *Applied Regression Analysis and Generalized Linear Models*. 3. ed. Thousand Oaks: Sage, 2015.
- Excelente para diagnósticos
- Foco em regressão aplicada

### Recursos Online

- **Scikit-learn Documentation**: Documentação oficial do sklearn.linear_model
- **Towards Data Science**: Artigos práticos sobre regressão linear
- **StatQuest**: Vídeos educativos sobre conceitos estatísticos
- **Khan Academy**: Curso gratuito de estatística

### Artigos Científicos

**FREEDMAN, David A.** "Statistical Models and Shoe Leather." *Sociological Methodology*, v. 21, p. 291-313, 1991.
- Discussão sobre causalidade vs correlação

**ANSCOMBE, Francis J.** "Graphs in Statistical Analysis." *The American Statistician*, v. 27, n. 1, p. 17-21, 1973.
- O famoso Quarteto de Anscombe
- Importância da visualização de dados

### Pacotes Python Recomendados

- **scikit-learn**: Modelagem de machine learning
- **statsmodels**: Análise estatística detalhada
- **scipy**: Testes estatísticos
- **matplotlib/seaborn**: Visualização
- **pandas**: Manipulação de dados

---

## Conclusão

A regressão linear simples é uma ferramenta fundamental em análise de dados que:

✅ **Permite modelar** relações lineares entre variáveis  
✅ **Facilita previsões** de valores futuros  
✅ **Quantifica relacionamentos** de forma clara e interpretável  
✅ **Serve de base** para técnicas mais avançadas  

**Lembre-se:**
- Sempre visualize seus dados primeiro
- Verifique os pressupostos do modelo
- Interprete os resultados com conhecimento do domínio
- Use com cautela e sempre considere as limitações
- Correlação não implica causação

**Próximos Passos:**
- Estude Regressão Linear Múltipla
- Aprenda sobre Regressão Polinomial
- Explore técnicas de regularização (Ridge, Lasso)
- Aprofunde-se em diagnósticos de regressão

---

*Documento criado como parte do repositório de Análise de Dados*  
*Última atualização: 2026*
