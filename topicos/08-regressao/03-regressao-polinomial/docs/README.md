# Regressão Polinomial

## Sumário

1. [Introdução](#introdução)
2. [Conceitos Fundamentais](#conceitos-fundamentais)
3. [Modelo Matemático](#modelo-matemático)
4. [Escolha do Grau do Polinômio](#escolha-do-grau-do-polinômio)
5. [Vantagens e Desvantagens](#vantagens-e-desvantagens)
6. [Exemplos do Dia a Dia](#exemplos-do-dia-a-dia)
7. [Implementação em Python](#implementação-em-python)
8. [Comparação com Regressão Linear](#comparação-com-regressão-linear)
9. [Overfitting e Underfitting](#overfitting-e-underfitting)
10. [Casos Práticos](#casos-práticos)
11. [Limitações e Cuidados](#limitações-e-cuidados)
12. [Referências](#referências)

---

## Introdução

A **Regressão Polinomial** é uma extensão da regressão linear que permite modelar relações **não-lineares** entre variáveis. Embora seja chamada de "polinomial", tecnicamente ainda é um modelo de regressão linear (nos parâmetros), mas com termos polinomiais das variáveis independentes.

### Quando Usar Regressão Polinomial?

Use regressão polinomial quando:
- A relação entre X e Y não é linear
- Há curvatura nos dados
- Gráfico de dispersão mostra padrão curvo
- Resíduos da regressão linear mostram padrão sistemático
- Conhecimento do domínio indica relação não-linear

### Por que é Importante?

No mundo real, muitas relações são não-lineares:
- **Depreciação de veículos** - Perde valor rapidamente no início, depois estabiliza
- **Produtividade vs Horas de trabalho** - Aumenta até certo ponto, depois diminui
- **Crescimento de plantas** - Curva sigmoidal
- **Resposta a doses de medicamentos** - Eficácia aumenta até platô

---

## Conceitos Fundamentais

### O que é um Polinômio?

Um polinômio é uma expressão matemática envolvendo potências de uma variável:

$$P(x) = a_0 + a_1x + a_2x^2 + a_3x^3 + ... + a_nx^n$$

Onde:
- **n** = grau do polinômio
- **aᵢ** = coeficientes
- **x** = variável independente

### Tipos de Polinômios por Grau

**Grau 1 (Linear):**
$$y = \beta_0 + \beta_1x$$
- Forma uma linha reta
- Sem curvatura

**Grau 2 (Quadrático):**
$$y = \beta_0 + \beta_1x + \beta_2x^2$$
- Forma uma parábola
- Uma curvatura (côncava ou convexa)
- Um ponto de máximo ou mínimo

**Grau 3 (Cúbico):**
$$y = \beta_0 + \beta_1x + \beta_2x^2 + \beta_3x^3$$
- Forma curva em S
- Até dois pontos de inflexão
- Pode ter ponto de máximo e mínimo

**Grau n:**
- Até n-1 mudanças de direção
- Maior flexibilidade
- Maior risco de overfitting

### Características Visuais

```
Grau 1: ────────────  (linha reta)
Grau 2: ╭────────╮   (parábola)
Grau 3: ╭──╮          (curva S)
        │  ╰────╯
Grau 4+: mais ondulações
```

---

## Modelo Matemático

### Regressão Polinomial de Grau 2

$$Y = \beta_0 + \beta_1 X + \beta_2 X^2 + \varepsilon$$

### Regressão Polinomial de Grau n

$$Y = \beta_0 + \beta_1 X + \beta_2 X^2 + ... + \beta_n X^n + \varepsilon$$

### Forma Matricial

Embora os termos sejam não-lineares em X, o modelo é **linear nos parâmetros** β:

$$\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$$

Onde X inclui as potências de x:

$$\mathbf{X} = \begin{bmatrix}
1 & x_1 & x_1^2 & ... & x_1^n \\
1 & x_2 & x_2^2 & ... & x_2^n \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_m & x_m^2 & ... & x_m^n
\end{bmatrix}$$

### Estimação dos Coeficientes

Mesmo método dos mínimos quadrados da regressão linear:

$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$$

---

## Escolha do Grau do Polinômio

Escolher o grau correto é crucial para o desempenho do modelo.

### Métodos para Escolher o Grau

#### 1. Análise Visual

Plotar dados com diferentes graus e observar ajuste.

**Critérios:**
- Captura a tendência geral?
- Não tem ondulações excessivas?
- Faz sentido teoricamente?

#### 2. Validação Cruzada

Usar k-fold cross-validation para comparar desempenho.

**Procedimento:**
1. Treinar modelos com graus 1, 2, 3, ..., n
2. Calcular erro médio de validação para cada
3. Escolher grau com menor erro

#### 3. Critérios de Informação

**AIC (Akaike Information Criterion):**
$$AIC = n \ln(SSE/n) + 2k$$

**BIC (Bayesian Information Criterion):**
$$BIC = n \ln(SSE/n) + k \ln(n)$$

Onde k = número de parâmetros (grau + 1)

**Regra:** Menor valor é melhor

#### 4. R² Ajustado

$$R_{adj}^2 = 1 - \frac{(1-R^2)(n-1)}{n-p-1}$$

**Vantagem:** Penaliza complexidade
**Regra:** Maior valor, mas com parcimônia

#### 5. Teste do Erro de Teste

**Procedimento:**
1. Dividir dados em treino/teste
2. Ajustar modelos de diferentes graus no treino
3. Avaliar erro no teste
4. Escolher grau com menor erro de teste

### Regras Práticas

✅ **Comece simples** - Teste grau 2 antes de 3  
✅ **Máximo grau 4** - Raramente necessita mais  
✅ **Prefira parcimônia** - Entre modelos similares, escolha o mais simples  
✅ **Considere teoria** - O grau faz sentido no contexto?  
✅ **Evite extrapolação** - Polinômios se comportam mal fora do intervalo dos dados

---

## Vantagens e Desvantagens

### Vantagens ✅

**1. Simplicidade Conceitual**
- Fácil de entender e explicar
- Extensão natural da regressão linear

**2. Flexibilidade**
- Pode aproximar muitas funções não-lineares
- Adequado para diversos tipos de curvatura

**3. Implementação Simples**
- Usa mesmas ferramentas da regressão linear
- Disponível em qualquer software estatístico

**4. Interpretação de Tendências**
- Fácil identificar pontos de máximo/mínimo
- Útil para otimização

**5. Ainda é Linear nos Parâmetros**
- Mantém propriedades estatísticas da regressão linear
- Inferência estatística é direta

### Desvantagens ❌

**1. Extrapolação Perigosa**
- Comportamento imprevisível fora do intervalo dos dados
- Pode divergir rapidamente

**2. Multicolinearidade**
- Termos polinomiais são correlacionados (x, x², x³)
- Pode causar instabilidade nos coeficientes

**3. Escolha do Grau**
- Não há regra única
- Requer tentativa e erro

**4. Overfitting**
- Graus altos podem memorizar ruído
- Péssima generalização

**5. Interpretação Limitada**
- Difícil interpretar coeficientes individualmente
- Foco em tendência geral, não coeficientes específicos

**6. Oscilações Indesejadas**
- Graus altos podem criar ondulações artificiais
- Fenômeno de Runge

---

## Exemplos do Dia a Dia

### Exemplo 1: Depreciação de Veículos

**Contexto:** Um carro perde valor com o tempo, mas não de forma linear.

**Variáveis:**
- **Y** = Valor do carro (R$)
- **X** = Idade do carro (anos)

**Modelo Esperado:** Quadrático (grau 2)
$$\text{Valor} = \beta_0 + \beta_1 \times \text{Idade} + \beta_2 \times \text{Idade}^2$$

**Comportamento:**
- Perda rápida nos primeiros anos (coeficiente negativo para X²)
- Desaceleração da perda após alguns anos
- Curva côncava para baixo

**Interpretação Prática:**
- Comprar carro usado de 3-5 anos pode ser ótimo negócio
- Perda maior ocorre no primeiro ano
- Após 10 anos, a depreciação é mais lenta

**Aplicações:**
- Precificação de seminovos
- Decisões de troca
- Seguro de veículos

### Exemplo 2: Produtividade vs Horas de Trabalho

**Contexto:** Relação entre horas trabalhadas e produtividade não é linear.

**Variáveis:**
- **Y** = Produtividade (tarefas completadas)
- **X** = Horas trabalhadas por dia

**Modelo Esperado:** Quadrático (grau 2)
$$\text{Produtividade} = \beta_0 + \beta_1 \times \text{Horas} + \beta_2 \times \text{Horas}^2$$

**Comportamento:**
- Produtividade aumenta com horas até certo ponto
- Depois começa a diminuir (fadiga, stress)
- Parábola com ponto de máximo

**Insights:**
- Identificar número ótimo de horas (ponto de máximo)
- Trabalhar demais reduz produtividade
- Jornadas muito longas são contraproducentes

**Aplicações:**
- Gestão de jornadas
- Políticas de trabalho
- Bem-estar dos funcionários

### Exemplo 3: Crescimento de Vendas de Produto

**Contexto:** Vendas de um novo produto seguem curva de crescimento.

**Variáveis:**
- **Y** = Vendas mensais
- **X** = Meses desde lançamento

**Modelo Esperado:** Cúbico (grau 3) ou logístico
$$\text{Vendas} = \beta_0 + \beta_1 X + \beta_2 X^2 + \beta_3 X^3$$

**Fases:**
1. **Introdução** - Crescimento lento inicial
2. **Crescimento** - Aceleração rápida
3. **Maturidade** - Desaceleração
4. **Declínio** - Possível queda

**Aplicações:**
- Previsão de demanda
- Gestão de estoque
- Planejamento de marketing

### Exemplo 4: Rendimento Agrícola vs Fertilizante

**Contexto:** Excesso de fertilizante pode prejudicar plantação.

**Variáveis:**
- **Y** = Rendimento (ton/hectare)
- **X** = Quantidade de fertilizante (kg/hectare)

**Modelo Esperado:** Quadrático
$$\text{Rendimento} = \beta_0 + \beta_1 \times \text{Fert} + \beta_2 \times \text{Fert}^2$$

**Comportamento:**
- Rendimento aumenta com fertilizante
- Atinge ponto ótimo
- Depois diminui (toxicidade, custo excessivo)

**Insights:**
- Identificar dose ótima de fertilizante
- Maximizar lucro (rendimento - custo)
- Evitar desperdício e danos ambientais

### Exemplo 5: Temperatura e Consumo de Sorvete

**Contexto:** Relação não-linear entre temperatura e vendas de sorvete.

**Variáveis:**
- **Y** = Vendas de sorvete
- **X** = Temperatura (°C)

**Modelo Esperado:** Quadrático
$$\text{Vendas} = \beta_0 + \beta_1 \times \text{Temp} + \beta_2 \times \text{Temp}^2$$

**Comportamento:**
- Vendas baixas em temperaturas muito baixas e muito altas
- Pico em temperatura moderada-alta (25-35°C)
- Pode cair em temperaturas extremas (>40°C - pessoas ficam em casa)

---

## Implementação em Python

### Exemplo Completo: Depreciação de Veículos

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

# Configurar visualizações
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# ==============================================
# 1. GERAR DADOS SIMULADOS
# ==============================================
np.random.seed(42)
n = 100

# Idade do carro (0 a 20 anos)
idade = np.random.uniform(0, 20, n)

# Valor do carro com relação não-linear (depreciação)
# Modelo real: Valor inicial de 50.000, deprecia exponencialmente
valor_real = 50000 * np.exp(-0.15 * idade)
valor = valor_real + np.random.normal(0, 3000, n)  # Adicionar ruído

# Criar DataFrame
df = pd.DataFrame({
    'Idade': idade,
    'Valor': valor
})

print("=" * 70)
print("EXEMPLO: DEPRECIAÇÃO DE VEÍCULOS")
print("=" * 70)
print(f"\nNúmero de veículos: {len(df)}")
print("\nPrimeiras observações:")
print(df.head(10))
print("\nEstatísticas:")
print(df.describe())

# ==============================================
# 2. VISUALIZAÇÃO DOS DADOS
# ==============================================

plt.figure(figsize=(10, 6))
plt.scatter(df['Idade'], df['Valor'], alpha=0.6, s=100, edgecolors='black')
plt.xlabel('Idade do Carro (anos)', fontsize=12)
plt.ylabel('Valor do Carro (R$)', fontsize=12)
plt.title('Depreciação de Veículos', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ==============================================
# 3. COMPARAR MODELOS DE DIFERENTES GRAUS
# ==============================================

# Preparar dados
X = df[['Idade']]
y = df['Valor']

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Testar graus 1, 2, 3, 4
graus = [1, 2, 3, 4]
resultados = []

print("\n" + "=" * 70)
print("COMPARAÇÃO DE MODELOS POLINOMIAIS")
print("=" * 70)

plt.figure(figsize=(16, 10))

for idx, grau in enumerate(graus, 1):
    # Criar características polinomiais
    poly = PolynomialFeatures(degree=grau, include_bias=False)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    
    # Ajustar modelo
    modelo = LinearRegression()
    modelo.fit(X_train_poly, y_train)
    
    # Predições
    y_train_pred = modelo.predict(X_train_poly)
    y_test_pred = modelo.predict(X_test_poly)
    
    # Métricas
    r2_train = r2_score(y_train, y_train_pred)
    r2_test = r2_score(y_test, y_test_pred)
    rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
    
    # Armazenar resultados
    resultados.append({
        'Grau': grau,
        'R²_Treino': r2_train,
        'R²_Teste': r2_test,
        'RMSE_Teste': rmse_test,
        'Num_Parametros': grau + 1
    })
    
    # Visualizar
    plt.subplot(2, 2, idx)
    
    # Pontos de treino
    plt.scatter(X_train, y_train, alpha=0.5, s=50, 
                edgecolors='black', label='Treino')
    
    # Pontos de teste
    plt.scatter(X_test, y_test, alpha=0.5, s=50, 
                edgecolors='black', color='red', label='Teste')
    
    # Curva do modelo
    X_range = np.linspace(X.min(), X.max(), 200).reshape(-1, 1)
    X_range_poly = poly.transform(X_range)
    y_range_pred = modelo.predict(X_range_poly)
    plt.plot(X_range, y_range_pred, 'g-', linewidth=2, 
             label=f'Modelo (grau {grau})')
    
    plt.xlabel('Idade (anos)', fontsize=11)
    plt.ylabel('Valor (R$)', fontsize=11)
    plt.title(f'Grau {grau}: R²_teste = {r2_test:.3f}', 
              fontsize=12, fontweight='bold')
    plt.legend(fontsize=9)
    plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Tabela de resultados
df_resultados = pd.DataFrame(resultados)
print("\nResultados dos Modelos:\n")
print(df_resultados.to_string(index=False))

# Identificar melhor modelo
melhor_idx = df_resultados['R²_Teste'].idxmax()
print(f"\nMelhor modelo: Grau {df_resultados.loc[melhor_idx, 'Grau']}")
print(f"R² no teste: {df_resultados.loc[melhor_idx, 'R²_Teste']:.4f}")

# ==============================================
# 4. ANÁLISE DETALHADA DO MELHOR MODELO
# ==============================================

grau_otimo = df_resultados.loc[melhor_idx, 'Grau']

print(f"\n" + "=" * 70)
print(f"ANÁLISE DETALHADA - MODELO DE GRAU {grau_otimo}")
print("=" * 70)

# Ajustar modelo final
poly_final = PolynomialFeatures(degree=grau_otimo, include_bias=False)
X_poly_final = poly_final.fit_transform(X)

modelo_final = LinearRegression()
modelo_final.fit(X_poly_final, y)

# Mostrar equação
print(f"\nCoeficientes:")
print(f"  Intercepto: {modelo_final.intercept_:,.2f}")
for i, coef in enumerate(modelo_final.coef_, 1):
    print(f"  Idade^{i}: {coef:,.4f}")

# Equação
eq = f"Valor = {modelo_final.intercept_:,.0f}"
for i, coef in enumerate(modelo_final.coef_, 1):
    sign = "+" if coef >= 0 else "-"
    eq += f" {sign} {abs(coef):,.2f}×Idade^{i}"
print(f"\nEquação do modelo:\n{eq}")

# ==============================================
# 5. ENCONTRAR PONTO DE MÍNIMO (se grau >= 2)
# ==============================================

if grau_otimo >= 2:
    print("\n" + "=" * 70)
    print("ANÁLISE DE PONTO CRÍTICO")
    print("=" * 70)
    
    # Para quadrático, ponto de mínimo é: x = -b/(2a)
    if grau_otimo == 2:
        a = modelo_final.coef_[1]  # coeficiente de x²
        b = modelo_final.coef_[0]  # coeficiente de x
        
        if a != 0:
            x_critico = -b / (2 * a)
            
            # Verificar se está no intervalo dos dados
            if X.min().values[0] <= x_critico <= X.max().values[0]:
                y_critico = modelo_final.predict(
                    poly_final.transform([[x_critico]])
                )[0]
                
                tipo = "mínimo" if a > 0 else "máximo"
                print(f"\nPonto de {tipo}:")
                print(f"  Idade: {x_critico:.2f} anos")
                print(f"  Valor: R$ {y_critico:,.2f}")
                
                if tipo == "mínimo":
                    print("\nInterpretação:")
                    print(f"  O valor do carro atinge o mínimo aos {x_critico:.1f} anos")
                    print("  Após isso, o modelo prevê aumento (improvável na prática)")

# ==============================================
# 6. FAZER PREDIÇÕES
# ==============================================

print("\n" + "=" * 70)
print("PREDIÇÕES PARA DIFERENTES IDADES")
print("=" * 70)

idades_exemplo = np.array([0, 3, 5, 10, 15, 20]).reshape(-1, 1)
idades_poly = poly_final.transform(idades_exemplo)
valores_pred = modelo_final.predict(idades_poly)

print("\nValores estimados:")
for idade, valor in zip(idades_exemplo.flatten(), valores_pred):
    print(f"  {idade:2.0f} anos: R$ {valor:>10,.2f}")

# ==============================================
# 7. VISUALIZAÇÃO FINAL
# ==============================================

plt.figure(figsize=(12, 6))

# Dados reais
plt.scatter(X, y, alpha=0.6, s=100, edgecolors='black', 
            label='Dados observados', zorder=3)

# Modelo polinomial
X_range = np.linspace(X.min(), X.max(), 300).reshape(-1, 1)
X_range_poly = poly_final.transform(X_range)
y_range_pred = modelo_final.predict(X_range_poly)
plt.plot(X_range, y_range_pred, 'r-', linewidth=3, 
         label=f'Modelo Polinomial (grau {grau_otimo})', zorder=2)

# Modelo linear para comparação
modelo_linear = LinearRegression()
modelo_linear.fit(X, y)
y_linear = modelo_linear.predict(X_range)
plt.plot(X_range, y_linear, 'b--', linewidth=2, 
         label='Modelo Linear (comparação)', alpha=0.7, zorder=1)

plt.xlabel('Idade do Carro (anos)', fontsize=13)
plt.ylabel('Valor do Carro (R$)', fontsize=13)
plt.title(f'Modelo Final de Depreciação - Grau {grau_otimo}', 
          fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ==============================================
# 8. ANÁLISE DE RESÍDUOS
# ==============================================

y_pred_final = modelo_final.predict(X_poly_final)
residuos = y - y_pred_final

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Resíduos vs Valores Preditos
axes[0].scatter(y_pred_final, residuos, alpha=0.6, edgecolors='black')
axes[0].axhline(y=0, color='red', linestyle='--', linewidth=2)
axes[0].set_xlabel('Valores Preditos', fontsize=11)
axes[0].set_ylabel('Resíduos', fontsize=11)
axes[0].set_title('Resíduos vs Valores Preditos', fontsize=12, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# Histograma dos Resíduos
axes[1].hist(residuos, bins=20, alpha=0.7, edgecolor='black', color='skyblue')
axes[1].axvline(x=0, color='red', linestyle='--', linewidth=2)
axes[1].set_xlabel('Resíduos', fontsize=11)
axes[1].set_ylabel('Frequência', fontsize=11)
axes[1].set_title('Distribuição dos Resíduos', fontsize=12, fontweight='bold')
axes[1].grid(True, alpha=0.3)

# Q-Q Plot
from scipy import stats as sp_stats
sp_stats.probplot(residuos, dist="norm", plot=axes[2])
axes[2].set_title('Q-Q Plot', fontsize=12, fontweight='bold')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n" + "=" * 70)
print("ANÁLISE COMPLETA FINALIZADA")
print("=" * 70)
```

### Comparando Modelos com Validação Cruzada

```python
from sklearn.model_selection import cross_val_score

print("\nVALIDAÇÃO CRUZADA (5-Fold)")
print("=" * 50)

for grau in range(1, 6):
    poly = PolynomialFeatures(degree=grau, include_bias=False)
    X_poly = poly.fit_transform(X)
    
    modelo = LinearRegression()
    
    # Validação cruzada com R² negativo (erro)
    scores = cross_val_score(modelo, X_poly, y, cv=5, 
                             scoring='neg_mean_squared_error')
    rmse_scores = np.sqrt(-scores)
    
    print(f"\nGrau {grau}:")
    print(f"  RMSE médio: {rmse_scores.mean():,.2f}")
    print(f"  Desvio padrão: {rmse_scores.std():,.2f}")
```

---

## Comparação com Regressão Linear

| Aspecto | Regressão Linear | Regressão Polinomial |
|---------|------------------|---------------------|
| **Forma da relação** | Linha reta | Curva |
| **Flexibilidade** | Baixa | Alta |
| **Número de parâmetros** | 2 (β₀, β₁) | n+1 (β₀, β₁, ..., βₙ) |
| **Risco de overfitting** | Baixo | Alto (graus elevados) |
| **Interpretação** | Direta | Mais complexa |
| **Extrapolação** | Razoável | Perigosa |
| **Multicolinearidade** | Não é problema | Pode ser problema |
| **Quando usar** | Relação linear | Relação não-linear com curvatura |

### Quando Preferir Linear?

✅ Relação é aproximadamente linear  
✅ Simplicidade é importante  
✅ Extrapolação é necessária  
✅ Interpretação dos coeficientes é crucial

### Quando Preferir Polinomial?

✅ Dados mostram curvatura clara  
✅ Gráfico de dispersão não é linear  
✅ Resíduos do modelo linear mostram padrão  
✅ Conhecimento do domínio indica não-linearidade

---

## Overfitting e Underfitting

### Underfitting (Subajuste)

**Sintomas:**
- R² baixo em treino E teste
- Modelo muito simples
- Não captura padrão nos dados

**Exemplo:** Usar modelo linear quando dados são claramente curvos

**Solução:** Aumentar complexidade (grau do polinômio)

### Overfitting (Sobreajuste)

**Sintomas:**
- R² alto em treino, baixo em teste
- Modelo muito complexo
- "Memoriza" ruído dos dados
- Muitas ondulações na curva

**Exemplo:** Usar grau 10 quando grau 2 seria suficiente

**Solução:** Reduzir complexidade, regularização, mais dados

### Encontrar Equilíbrio

```
Underfitting ←──────── Complexidade Ideal ────────→ Overfitting
(grau muito baixo)      (grau adequado)         (grau muito alto)

R²_treino: Baixo        Médio-Alto              Muito Alto
R²_teste:  Baixo        Alto                    Baixo
Curva:     Muito lisa   Suave com curvatura     Muitas oscilações
```

**Objetivo:** Maximizar R²_teste, não R²_treino!

---

## Casos Práticos

### Caso 1: Otimização de Dose de Fertilizante

**Problema:** Agricultor quer maximizar rendimento.

**Análise:**
1. Coletar dados de rendimento vs quantidade de fertilizante
2. Ajustar modelo quadrático
3. Encontrar ponto de máximo (derivada = 0)
4. Calcular dose ótima

**Resultado:**
- Dose ótima identificada
- Aumento de 15% no rendimento
- Redução de 20% no custo (evita excesso)

### Caso 2: Precificação Dinâmica de Passagens Aéreas

**Problema:** Companhia aérea quer otimizar preços.

**Análise:**
- Variável: Demanda vs Dias até o voo
- Modelo: Polinomial grau 3
- Comportamento: U invertido com ajustes

**Resultado:**
- Preços mais altos perto do voo
- Promoções em períodos de baixa demanda
- Aumento de 8% na receita

---

## Limitações e Cuidados

### 1. Extrapolação é Perigosa

⚠️ **NUNCA** extrapole muito além dos dados!

**Por quê?**
- Polinômios podem divergir rapidamente
- Comportamento imprevisível

**Exemplo:**
```
Dados: idades 0-20 anos
Predição para 25 anos: arriscada
Predição para 50 anos: absurda
```

### 2. Fenômeno de Runge

Com graus muito altos, oscilações aparecem nas bordas.

**Solução:** Usar splines ou métodos mais sofisticados

### 3. Multicolinearidade

x, x², x³ são altamente correlacionados.

**Solução:** 
- Centralizar dados
- Usar polinômios ortogonais
- Regularização

### 4. Interpretação Limitada

Coeficientes individuais têm pouca interpretação prática.

**Foco:** Tendência geral e pontos críticos

### 5. Não Captura Todos os Padrões

Algumas relações não-lineares não são bem aproximadas por polinômios.

**Alternativas:**
- Transformações (log, exp)
- Splines
- GAM (Generalized Additive Models)
- Machine Learning (Random Forest, etc.)

---

## Referências

### Livros

**HASTIE, Trevor; TIBSHIRANI, Robert; FRIEDMAN, Jerome.** *The Elements of Statistical Learning*. 2. ed. Springer, 2009.
- Capítulo 5: Basis Expansions and Regularization

**JAMES, Gareth et al.** *An Introduction to Statistical Learning*. 2. ed. Springer, 2021.
- Seção 7.1: Polynomial Regression

**KUTNER, Michael H. et al.** *Applied Linear Statistical Models*. 5. ed. McGraw-Hill, 2005.
- Capítulo 8: Polynomial Regression

### Recursos Online

- **Scikit-learn Documentation**: `PolynomialFeatures`
- **Towards Data Science**: Artigos sobre regressão polinomial
- **StatQuest**: Vídeos educativos

---

## Conclusão

A Regressão Polinomial é uma ferramenta poderosa para:

✅ **Modelar relações não-lineares** de forma simples  
✅ **Identificar pontos ótimos** (máximos/mínimos)  
✅ **Capturar curvaturas** nos dados  
✅ **Aproximar funções complexas** com flexibilidade  

**Lembre-se:**
- Comece com graus baixos (2 ou 3)
- Use validação cruzada para escolher o grau
- Visualize sempre os resultados
- Cuidado com extrapolação
- Prefira simplicidade quando possível

**Próximos Passos:**
- Estude Regressão Ridge e Lasso para regularização
- Explore Splines para maior flexibilidade
- Aprenda GAM para relações não-lineares complexas
- Considere métodos de Machine Learning

---

*Documento criado como parte do repositório de Análise de Dados*  
*Última atualização: 2026*
