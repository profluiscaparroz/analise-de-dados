# Regressão Linear Múltipla

## Sumário

1. [Introdução](#introdução)
2. [Conceitos Fundamentais](#conceitos-fundamentais)
3. [Modelo Matemático](#modelo-matemático)
4. [Interpretação dos Coeficientes](#interpretação-dos-coeficientes)
5. [Pressupostos do Modelo](#pressupostos-do-modelo)
6. [Multicolinearidade](#multicolinearidade)
7. [Seleção de Variáveis](#seleção-de-variáveis)
8. [Métricas de Avaliação](#métricas-de-avaliação)
9. [Exemplos do Dia a Dia](#exemplos-do-dia-a-dia)
10. [Implementação em Python](#implementação-em-python)
11. [Casos Práticos Completos](#casos-práticos-completos)
12. [Limitações e Cuidados](#limitações-e-cuidados)
13. [Exercícios Práticos](#exercícios-práticos)
14. [Referências](#referências)

---

## Introdução

A **Regressão Linear Múltipla** é uma extensão natural da regressão linear simples que permite modelar a relação entre uma variável dependente e **múltiplas variáveis independentes** simultaneamente. Esta técnica é fundamental para análises mais realistas, onde o fenômeno de interesse geralmente é influenciado por vários fatores.

### Por que usar Regressão Múltipla?

Na prática, é raro que um resultado seja influenciado por apenas um fator. Por exemplo:
- **Preço de um imóvel** não depende apenas da área, mas também da localização, número de quartos, idade, etc.
- **Vendas de um produto** são afetadas por preço, publicidade, sazonalidade, concorrência, etc.
- **Desempenho acadêmico** é influenciado por horas de estudo, qualidade do sono, participação em aulas, etc.

### Vantagens da Regressão Múltipla

✅ **Modelagem mais realista** - Considera múltiplos fatores simultaneamente  
✅ **Controle de confundidores** - Isola o efeito de cada variável  
✅ **Maior poder preditivo** - Geralmente resulta em melhores previsões  
✅ **Análise de importância relativa** - Identifica quais variáveis são mais importantes  
✅ **Interações entre variáveis** - Pode modelar efeitos combinados

---

## Conceitos Fundamentais

### Variáveis no Modelo

**Variável Dependente (Y)**
- Variável que queremos explicar ou predizer
- Também chamada de variável resposta ou variável de saída
- Deve ser contínua

**Variáveis Independentes (X₁, X₂, ..., Xₚ)**
- Variáveis usadas para explicar Y
- Também chamadas de preditores, regressores ou variáveis explicativas
- Podem ser contínuas ou categóricas (após codificação)

### Exemplo Ilustrativo

**Predizer o Preço de um Carro Usado**

- **Y** = Preço do carro (variável dependente)
- **X₁** = Ano de fabricação
- **X₂** = Quilometragem
- **X₃** = Número de proprietários anteriores
- **X₄** = Tamanho do motor (litros)
- **X₅** = Condição (variável categórica)

### Diferença entre Regressão Simples e Múltipla

| Aspecto | Regressão Simples | Regressão Múltipla |
|---------|-------------------|-------------------|
| Número de variáveis independentes | 1 | 2 ou mais |
| Visualização | Linha em 2D | Hiperplano em múltiplas dimensões |
| Complexidade | Baixa | Moderada a alta |
| Interpretação | Direta | Requer cuidado com confundidores |
| Poder preditivo | Limitado | Geralmente superior |

---

## Modelo Matemático

### Equação Geral

O modelo de regressão linear múltipla é expresso como:

$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_p X_p + \varepsilon$$

Onde:
- **Y**: Variável dependente
- **X₁, X₂, ..., Xₚ**: p variáveis independentes
- **β₀**: Intercepto (constante)
- **β₁, β₂, ..., βₚ**: Coeficientes parciais de regressão
- **ε**: Termo de erro aleatório

### Forma Matricial

Para facilitar os cálculos com múltiplas variáveis, usamos notação matricial:

$$\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$$

Onde:
- **Y**: Vetor de respostas (n × 1)
- **X**: Matriz de design (n × (p+1))
- **β**: Vetor de coeficientes ((p+1) × 1)
- **ε**: Vetor de erros (n × 1)

### Estimação dos Coeficientes

Os coeficientes são estimados pelo método dos mínimos quadrados:

$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$$

### Valores Preditos

$$\hat{Y} = \hat{\beta}_0 + \hat{\beta}_1 X_1 + \hat{\beta}_2 X_2 + ... + \hat{\beta}_p X_p$$

### Resíduos

$$e_i = Y_i - \hat{Y}_i$$

---

## Interpretação dos Coeficientes

### Coeficientes Parciais

Na regressão múltipla, cada coeficiente βⱼ representa o **efeito parcial** de Xⱼ sobre Y, **mantendo todas as outras variáveis constantes**.

### Interpretação do Intercepto (β₀)

**Definição:** Valor esperado de Y quando todas as variáveis independentes são iguais a zero.

**Exemplo:**
```
Modelo: Preço = 50000 + 2000×Área + 15000×Quartos - 500×Idade

Intercepto = 50000
```

**Interpretação:** Um imóvel com 0 m², 0 quartos e 0 anos teria preço esperado de R$ 50.000 (não faz sentido prático - extrapolação).

⚠️ **Cuidado:** O intercepto nem sempre tem interpretação prática se X=0 não fizer sentido no contexto.

### Interpretação dos Coeficientes Angulares (βⱼ)

**Definição:** Mudança esperada em Y quando Xⱼ aumenta em uma unidade, **mantendo todas as outras variáveis constantes** (ceteris paribus).

**Exemplo:**
```
Modelo: Preço = 50000 + 2000×Área + 15000×Quartos - 500×Idade

Coeficiente da Área = 2000
```

**Interpretação:** Cada m² adicional aumenta o preço em R$ 2.000, **mantendo o número de quartos e a idade do imóvel constantes**.

### Importância do "Ceteris Paribus"

A condição "mantendo as outras variáveis constantes" é crucial porque:

1. **Isola o efeito** de uma variável específica
2. **Controla confundidores** - variáveis que poderiam distorcer a relação
3. **Permite comparação justa** entre diferentes preditores

### Coeficientes Padronizados

Para comparar a importância relativa de variáveis com diferentes escalas, usamos coeficientes padronizados (betas):

$$\beta_j^* = \beta_j \times \frac{\sigma_{X_j}}{\sigma_Y}$$

**Interpretação:** Mudança em Y (em desvios padrão) quando Xⱼ aumenta em um desvio padrão.

### Exemplo Comparativo

**Modelo Original:**
```
Salário = 2000 + 300×AnosExperiencia + 50×HorasTreinamento
```

Não podemos comparar diretamente 300 com 50, pois as unidades são diferentes.

**Modelo Padronizado:**
```
Salário_padronizado = 0.65×AnosExperiencia_padronizado + 0.25×HorasTreinamento_padronizado
```

**Interpretação:** Anos de experiência tem impacto maior (0.65 > 0.25) no salário.

---

## Pressupostos do Modelo

A regressão linear múltipla exige os mesmos pressupostos da regressão simples, com atenção especial à multicolinearidade.

### 1. Linearidade

**Descrição:** A relação entre Y e cada Xⱼ deve ser linear.

**Como verificar:**
- Gráficos de dispersão parcial (partial plots)
- Gráficos de resíduos parciais
- RESET test de Ramsey

**O que fazer se violado:**
- Transformar variáveis (log, raiz quadrada, etc.)
- Adicionar termos polinomiais
- Usar modelos não-lineares

### 2. Independência dos Resíduos

**Descrição:** Observações devem ser independentes entre si.

**Como verificar:**
- Teste de Durbin-Watson
- Gráfico de autocorrelação (ACF)

**Violações comuns:**
- Dados de séries temporais
- Observações agrupadas (clusters)
- Amostragem hierárquica

### 3. Homocedasticidade

**Descrição:** Variância dos resíduos deve ser constante.

**Como verificar:**
- Gráfico de resíduos vs valores preditos
- Teste de Breusch-Pagan
- Teste de White

**O que fazer se violado:**
- Transformar Y (log, Box-Cox)
- Usar erros padrão robustos (HC)
- Regressão ponderada (WLS)

### 4. Normalidade dos Resíduos

**Descrição:** Resíduos devem seguir distribuição normal.

**Como verificar:**
- Q-Q plot
- Teste de Shapiro-Wilk
- Teste de Jarque-Bera

**Importância:**
- Crítico para amostras pequenas
- Menos importante para grandes amostras (Teorema do Limite Central)

### 5. Ausência de Multicolinearidade

**Descrição:** Variáveis independentes não devem estar altamente correlacionadas entre si.

⚠️ **Este é um pressuposto adicional específico da regressão múltipla!**

Veja seção dedicada abaixo.

---

## Multicolinearidade

### O que é Multicolinearidade?

Multicolinearidade ocorre quando duas ou mais variáveis independentes estão **fortemente correlacionadas** entre si.

### Tipos de Multicolinearidade

**1. Perfeita (Colinearidade Exata)**
- Uma variável é combinação linear exata de outras
- Exemplo: X₃ = 2×X₁ + 3×X₂
- Torna a matriz X'X singular (não inversível)
- O modelo não pode ser estimado

**2. Imperfeita (Multicolinearidade)**
- Correlação alta, mas não perfeita
- Exemplo: Peso e altura de pessoas (r ≈ 0.8)
- O modelo pode ser estimado, mas com problemas

### Problemas Causados

❌ **Coeficientes instáveis** - Pequenas mudanças nos dados causam grandes mudanças nos coeficientes  
❌ **Erros padrão inflados** - Reduz a precisão das estimativas  
❌ **Testes de significância não confiáveis** - Variáveis importantes podem parecer não significativas  
❌ **Interpretação difícil** - Dificulta isolar o efeito de cada variável  
❌ **Sinais incorretos** - Coeficientes podem ter sinais opostos ao esperado

### Como Detectar

#### 1. Matriz de Correlação

Calcular correlações entre todas as variáveis independentes.

**Regra prática:**
- |r| > 0.8: Multicolinearidade preocupante
- |r| > 0.9: Multicolinearidade severa

#### 2. VIF (Variance Inflation Factor)

O VIF mede quanto a variância de um coeficiente é inflada devido à multicolinearidade.

$$VIF_j = \frac{1}{1 - R_j^2}$$

Onde R²ⱼ é o R² da regressão de Xⱼ contra todas as outras variáveis.

**Interpretação:**
- VIF = 1: Sem multicolinearidade
- VIF < 5: Multicolinearidade aceitável
- 5 ≤ VIF < 10: Multicolinearidade moderada
- VIF ≥ 10: Multicolinearidade severa (ação necessária)

#### 3. Tolerância

$$Tolerance_j = \frac{1}{VIF_j} = 1 - R_j^2$$

**Interpretação:**
- Tolerance > 0.2: Aceitável
- Tolerance < 0.1: Problemático

#### 4. Número de Condição

Baseado nos autovalores da matriz X'X.

**Interpretação:**
- κ < 10: Sem problema
- 10 ≤ κ < 30: Multicolinearidade moderada
- κ ≥ 30: Multicolinearidade severa

### Como Lidar com Multicolinearidade

#### 1. Remover Variáveis

Identifique e remova uma das variáveis altamente correlacionadas.

**Critérios para escolha:**
- Menor relevância teórica
- Menor correlação com Y
- Menor qualidade dos dados

#### 2. Combinar Variáveis

Crie um índice ou variável composta.

**Exemplo:** Ao invés de usar "Renda" e "Patrimônio" separadamente, criar "Situação Financeira" = média ponderada.

#### 3. Análise de Componentes Principais (PCA)

Transforme variáveis correlacionadas em componentes não-correlacionados.

**Vantagens:**
- Elimina multicolinearidade
- Reduz dimensionalidade

**Desvantagens:**
- Perda de interpretabilidade
- Componentes são combinações abstratas

#### 4. Regressão Ridge

Use regularização L2 para lidar com multicolinearidade.

**Como funciona:**
- Adiciona penalização aos coeficientes grandes
- Estabiliza as estimativas

#### 5. Aumentar Tamanho Amostral

Mais dados podem reduzir o impacto da multicolinearidade.

#### 6. Não Fazer Nada

Se o objetivo é apenas **predição** (não interpretação), multicolinearidade pode não ser problema sério.

---

## Seleção de Variáveis

Escolher quais variáveis incluir no modelo é crucial para obter bons resultados.

### Por que Selecionar Variáveis?

✅ **Simplicidade** - Modelos mais simples são mais fáceis de interpretar  
✅ **Generalização** - Evita overfitting  
✅ **Eficiência** - Menos variáveis = menos dados necessários  
✅ **Custo** - Coletar menos variáveis reduz custos

### Critérios de Seleção

#### 1. Relevância Teórica

**Sempre comece com conhecimento do domínio!**

Perguntas a fazer:
- Faz sentido teoricamente que X influencie Y?
- Há estudos prévios que suportam essa relação?
- A variável é mensurável de forma confiável?

#### 2. Significância Estatística

Teste se o coeficiente é estatisticamente diferente de zero.

**Teste t:**
- H₀: βⱼ = 0
- H₁: βⱼ ≠ 0

**Regra:** Se p-valor < 0.05, rejeita H₀ (variável é significativa).

⚠️ **Cuidado:** Não usar significância como único critério!

#### 3. Impacto Prático

**Significância estatística ≠ Importância prática**

Perguntas:
- O tamanho do efeito é relevante no contexto?
- A mudança em Y é grande o suficiente para importar?

### Métodos de Seleção

#### 1. Seleção Manual

**Abordagem:** Analista escolhe variáveis baseado em teoria e análise exploratória.

**Vantagens:**
- Considera conhecimento do domínio
- Flexibilidade

**Desvantagens:**
- Subjetivo
- Pode ignorar relações não óbvias

#### 2. Forward Selection (Seleção Progressiva)

**Passo a passo:**
1. Começar sem variáveis (apenas intercepto)
2. Adicionar a variável que melhora mais o modelo
3. Repetir até nenhuma variável melhorar significativamente

**Critério de entrada:** p-valor < α (ex: 0.05) ou AIC menor

#### 3. Backward Elimination (Eliminação Regressiva)

**Passo a passo:**
1. Começar com todas as variáveis
2. Remover a variável menos significativa
3. Repetir até todas serem significativas

**Critério de remoção:** p-valor > α (ex: 0.10) ou AIC maior

#### 4. Stepwise Selection (Seleção Passo a Passo)

**Combinação de Forward e Backward:**
- Adiciona variáveis como Forward
- Verifica e remove variáveis que se tornaram não significativas

#### 5. Critérios de Informação

**AIC (Akaike Information Criterion):**

$$AIC = n \ln(SSE/n) + 2(p+1)$$

**BIC (Bayesian Information Criterion):**

$$BIC = n \ln(SSE/n) + \ln(n)(p+1)$$

**Interpretação:**
- Menores valores são melhores
- Balanceia ajuste vs complexidade
- BIC penaliza mais a complexidade que AIC

#### 6. Validação Cruzada

Divide dados em treino e teste, avalia desempenho em dados não vistos.

**K-fold CV:**
1. Dividir dados em k partes
2. Treinar em k-1 partes, testar em 1
3. Repetir k vezes
4. Calcular erro médio

### R² Ajustado

O R² sempre aumenta ao adicionar variáveis. O R² ajustado penaliza a adição de variáveis:

$$R_{adj}^2 = 1 - \frac{(1-R^2)(n-1)}{n-p-1}$$

**Vantagens:**
- Só aumenta se nova variável melhora o modelo significativamente
- Permite comparar modelos com diferentes números de variáveis

---

## Métricas de Avaliação

### Métricas de Ajuste

#### 1. R² (Coeficiente de Determinação)

$$R^2 = 1 - \frac{SSE}{SST} = 1 - \frac{\sum(Y_i - \hat{Y}_i)^2}{\sum(Y_i - \bar{Y})^2}$$

**Interpretação:** Proporção da variabilidade em Y explicada pelo modelo.

**Limitação:** Sempre aumenta com mais variáveis.

#### 2. R² Ajustado

$$R_{adj}^2 = 1 - \frac{(1-R^2)(n-1)}{n-p-1}$$

**Vantagem:** Penaliza modelos complexos.

#### 3. RMSE (Root Mean Squared Error)

$$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(Y_i - \hat{Y}_i)^2}$$

**Interpretação:** Erro médio na mesma unidade de Y.

#### 4. MAE (Mean Absolute Error)

$$MAE = \frac{1}{n}\sum_{i=1}^{n}|Y_i - \hat{Y}_i|$$

**Vantagem:** Menos sensível a outliers que RMSE.

#### 5. MAPE (Mean Absolute Percentage Error)

$$MAPE = \frac{100\%}{n}\sum_{i=1}^{n}\left|\frac{Y_i - \hat{Y}_i}{Y_i}\right|$$

**Interpretação:** Erro médio em percentual.

### Testes de Significância

#### Teste F Global

Testa se **pelo menos uma** variável independente é significativa.

**Hipóteses:**
- H₀: β₁ = β₂ = ... = βₚ = 0 (modelo não é útil)
- H₁: Pelo menos um βⱼ ≠ 0

**Estatística:**

$$F = \frac{(SST - SSE)/p}{SSE/(n-p-1)}$$

#### Teste t Individual

Testa se um coeficiente específico é diferente de zero.

**Hipóteses:**
- H₀: βⱼ = 0
- H₁: βⱼ ≠ 0

**Estatística:**

$$t = \frac{\hat{\beta}_j}{SE(\hat{\beta}_j)}$$

---

## Exemplos do Dia a Dia

### Exemplo 1: Preço de Imóveis

**Contexto:** Imobiliária quer precificar apartamentos considerando múltiplas características.

**Variáveis:**
- **Y** = Preço do apartamento (R$)
- **X₁** = Área (m²)
- **X₂** = Número de quartos
- **X₃** = Número de banheiros
- **X₄** = Idade do imóvel (anos)
- **X₅** = Distância ao centro (km)
- **X₆** = Andar

**Modelo Esperado:**
```
Preço = β₀ + β₁×Área + β₂×Quartos + β₃×Banheiros - β₄×Idade - β₅×Distância + β₆×Andar
```

**Interpretações Esperadas:**
- β₁ > 0: Maior área → maior preço
- β₄ < 0: Mais antigo → menor preço
- β₅ < 0: Mais longe do centro → menor preço

**Aplicações Práticas:**
- Avaliação de imóveis para venda
- Decisões de compra
- Análise de mercado imobiliário
- Identificação de bons negócios

### Exemplo 2: Desempenho de Vendas

**Contexto:** Empresa quer entender o que impacta vendas regionais.

**Variáveis:**
- **Y** = Vendas mensais (unidades)
- **X₁** = Gastos com TV (mil R$)
- **X₂** = Gastos com internet (mil R$)
- **X₃** = Gastos com rádio (mil R$)
- **X₄** = Número de vendedores
- **X₅** = Preço médio do produto (R$)
- **X₆** = Concorrentes na região

**Objetivos:**
- Identificar canais de marketing mais efetivos
- Otimizar orçamento publicitário
- Entender impacto de preço e concorrência
- Planejar contratação de vendedores

### Exemplo 3: Consumo de Energia Elétrica

**Contexto:** Residência quer entender e prever consumo de energia.

**Variáveis:**
- **Y** = Consumo mensal (kWh)
- **X₁** = Temperatura média (°C)
- **X₂** = Número de pessoas na casa
- **X₃** = Área construída (m²)
- **X₄** = Número de eletrodomésticos
- **X₅** = Uso de ar-condicionado (horas/dia)

**Aplicações:**
- Previsão de contas
- Identificação de desperdícios
- Planejamento de melhorias
- Comparação com vizinhos

### Exemplo 4: Salário de Funcionários

**Contexto:** Empresa quer estabelecer política salarial justa.

**Variáveis:**
- **Y** = Salário mensal (R$)
- **X₁** = Anos de experiência
- **X₂** = Anos de educação
- **X₃** = Avaliação de desempenho (1-10)
- **X₄** = Número de certificações
- **X₅** = Cargo (variável categórica)
- **X₆** = Departamento (variável categórica)

**Objetivos:**
- Estabelecer faixas salariais
- Identificar disparidades
- Planejar aumentos e promoções
- Garantir equidade

### Exemplo 5: Rendimento Agrícola

**Contexto:** Fazenda quer maximizar produção de soja.

**Variáveis:**
- **Y** = Produtividade (toneladas/hectare)
- **X₁** = Quantidade de fertilizante (kg/ha)
- **X₂** = Quantidade de água (mm)
- **X₃** = Densidade de plantio (plantas/m²)
- **X₄** = Temperatura média (°C)
- **X₅** = pH do solo
- **X₆** = Controle de pragas (índice)

**Aplicações:**
- Otimização de insumos
- Redução de custos
- Aumento de produtividade
- Sustentabilidade

---

## Implementação em Python

### Exemplo Completo: Preço de Imóveis

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler
from scipy import stats
from statsmodels.stats.outliers_influence import variance_inflation_factor
import warnings
warnings.filterwarnings('ignore')

# Configurar visualizações
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# ==============================================
# 1. GERAR DADOS SIMULADOS DE IMÓVEIS
# ==============================================
np.random.seed(42)
n = 200

# Variáveis independentes
area = np.random.normal(80, 25, n)                    # Área em m²
quartos = np.random.poisson(3, n)                     # Número de quartos
banheiros = np.random.poisson(2, n)                   # Número de banheiros
idade = np.random.exponential(10, n)                  # Idade em anos
distancia_centro = np.random.uniform(1, 20, n)       # Distância em km
andar = np.random.randint(1, 15, n)                   # Andar

# Variável dependente com relação múltipla
preco = (150000 + 
         2500 * area + 
         20000 * quartos +
         15000 * banheiros -
         800 * idade -
         2000 * distancia_centro +
         1500 * andar +
         np.random.normal(0, 30000, n))

# Criar DataFrame
df = pd.DataFrame({
    'Preco': preco,
    'Area': area,
    'Quartos': quartos,
    'Banheiros': banheiros,
    'Idade': idade,
    'Distancia_Centro': distancia_centro,
    'Andar': andar
})

print("=" * 70)
print("DATASET: PREÇOS DE IMÓVEIS")
print("=" * 70)
print(f"\nNúmero de observações: {len(df)}")
print("\nPrimeiras 10 observações:")
print(df.head(10))
print("\nEstatísticas descritivas:")
print(df.describe())

# ==============================================
# 2. ANÁLISE EXPLORATÓRIA
# ==============================================

# Matriz de correlação
print("\n" + "=" * 70)
print("MATRIZ DE CORRELAÇÃO")
print("=" * 70)
correlation_matrix = df.corr()
print("\nCorrelação com Preço:")
print(correlation_matrix['Preco'].sort_values(ascending=False))

# Visualizar matriz de correlação
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
            fmt='.2f', square=True, linewidths=1)
plt.title('Matriz de Correlação - Variáveis dos Imóveis', 
          fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# ==============================================
# 3. VERIFICAR MULTICOLINEARIDADE (VIF)
# ==============================================

print("\n" + "=" * 70)
print("ANÁLISE DE MULTICOLINEARIDADE (VIF)")
print("=" * 70)

X_temp = df.drop('Preco', axis=1)
vif_data = pd.DataFrame()
vif_data["Variável"] = X_temp.columns
vif_data["VIF"] = [variance_inflation_factor(X_temp.values, i) 
                   for i in range(len(X_temp.columns))]
vif_data = vif_data.sort_values('VIF', ascending=False)

print("\n", vif_data)
print("\nInterpretação:")
print("  VIF < 5: Multicolinearidade aceitável ✓")
print("  5 ≤ VIF < 10: Multicolinearidade moderada ⚠")
print("  VIF ≥ 10: Multicolinearidade severa ✗")

# ==============================================
# 4. DIVIDIR DADOS EM TREINO E TESTE
# ==============================================

X = df.drop('Preco', axis=1)
y = df['Preco']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nDados de treino: {len(X_train)} observações")
print(f"Dados de teste: {len(X_test)} observações")

# ==============================================
# 5. AJUSTAR MODELO DE REGRESSÃO MÚLTIPLA
# ==============================================

modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Fazer predições
y_train_pred = modelo.predict(X_train)
y_test_pred = modelo.predict(X_test)

# Extrair coeficientes
print("\n" + "=" * 70)
print("COEFICIENTES DO MODELO")
print("=" * 70)
print(f"\nIntercepto: R$ {modelo.intercept_:,.2f}")
print("\nCoeficientes:")
for i, col in enumerate(X.columns):
    print(f"  {col:20s}: R$ {modelo.coef_[i]:>10,.2f}")

# Equação do modelo
print("\nEquação do modelo:")
equation = f"Preço = {modelo.intercept_:,.0f}"
for i, col in enumerate(X.columns):
    sign = "+" if modelo.coef_[i] >= 0 else "-"
    equation += f" {sign} {abs(modelo.coef_[i]):,.0f}×{col}"
print(equation)

# ==============================================
# 6. INTERPRETAÇÃO DOS COEFICIENTES
# ==============================================

print("\n" + "=" * 70)
print("INTERPRETAÇÃO DOS COEFICIENTES")
print("=" * 70)

interpretacoes = {
    'Area': f"Cada m² adicional aumenta o preço em R$ {modelo.coef_[0]:,.2f}",
    'Quartos': f"Cada quarto adicional aumenta o preço em R$ {modelo.coef_[1]:,.2f}",
    'Banheiros': f"Cada banheiro adicional aumenta o preço em R$ {modelo.coef_[2]:,.2f}",
    'Idade': f"Cada ano de idade {'aumenta' if modelo.coef_[3] > 0 else 'diminui'} o preço em R$ {abs(modelo.coef_[3]):,.2f}",
    'Distancia_Centro': f"Cada km adicional do centro {'aumenta' if modelo.coef_[4] > 0 else 'diminui'} o preço em R$ {abs(modelo.coef_[4]):,.2f}",
    'Andar': f"Cada andar adicional aumenta o preço em R$ {modelo.coef_[5]:,.2f}"
}

for var, interp in interpretacoes.items():
    print(f"\n• {var}:")
    print(f"  {interp}")

# ==============================================
# 7. MÉTRICAS DE AVALIAÇÃO
# ==============================================

# Calcular métricas
r2_train = r2_score(y_train, y_train_pred)
r2_test = r2_score(y_test, y_test_pred)
rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
mae_test = mean_absolute_error(y_test, y_test_pred)
mape_test = np.mean(np.abs((y_test - y_test_pred) / y_test)) * 100

# R² ajustado
n = len(X_train)
p = X_train.shape[1]
r2_adj_train = 1 - (1 - r2_train) * (n - 1) / (n - p - 1)

print("\n" + "=" * 70)
print("MÉTRICAS DE AVALIAÇÃO DO MODELO")
print("=" * 70)
print(f"\nConjunto de Treino:")
print(f"  R²: {r2_train:.4f}")
print(f"  R² Ajustado: {r2_adj_train:.4f}")
print(f"  RMSE: R$ {rmse_train:,.2f}")

print(f"\nConjunto de Teste:")
print(f"  R²: {r2_test:.4f}")
print(f"  → O modelo explica {r2_test*100:.2f}% da variabilidade nos preços")
print(f"  RMSE: R$ {rmse_test:,.2f}")
print(f"  MAE: R$ {mae_test:,.2f}")
print(f"  MAPE: {mape_test:.2f}%")

# ==============================================
# 8. VISUALIZAÇÕES
# ==============================================

# Valores reais vs preditos
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Conjunto de treino
axes[0].scatter(y_train, y_train_pred, alpha=0.6, edgecolors='black')
axes[0].plot([y_train.min(), y_train.max()], 
             [y_train.min(), y_train.max()], 
             'r--', linewidth=2, label='Predição perfeita')
axes[0].set_xlabel('Preço Real (R$)', fontsize=12)
axes[0].set_ylabel('Preço Predito (R$)', fontsize=12)
axes[0].set_title(f'Conjunto de Treino\nR² = {r2_train:.4f}', 
                  fontsize=13, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Conjunto de teste
axes[1].scatter(y_test, y_test_pred, alpha=0.6, edgecolors='black', color='green')
axes[1].plot([y_test.min(), y_test.max()], 
             [y_test.min(), y_test.max()], 
             'r--', linewidth=2, label='Predição perfeita')
axes[1].set_xlabel('Preço Real (R$)', fontsize=12)
axes[1].set_ylabel('Preço Predito (R$)', fontsize=12)
axes[1].set_title(f'Conjunto de Teste\nR² = {r2_test:.4f}', 
                  fontsize=13, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ==============================================
# 9. ANÁLISE DE RESÍDUOS
# ==============================================

residuos = y_test - y_test_pred

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Resíduos vs Valores Preditos
axes[0, 0].scatter(y_test_pred, residuos, alpha=0.6, edgecolors='black')
axes[0, 0].axhline(y=0, color='red', linestyle='--', linewidth=2)
axes[0, 0].set_xlabel('Valores Preditos (R$)', fontsize=11)
axes[0, 0].set_ylabel('Resíduos (R$)', fontsize=11)
axes[0, 0].set_title('Resíduos vs Valores Preditos', fontsize=12, fontweight='bold')
axes[0, 0].grid(True, alpha=0.3)

# Histograma dos Resíduos
axes[0, 1].hist(residuos, bins=20, alpha=0.7, edgecolor='black', color='skyblue')
axes[0, 1].axvline(x=0, color='red', linestyle='--', linewidth=2)
axes[0, 1].set_xlabel('Resíduos (R$)', fontsize=11)
axes[0, 1].set_ylabel('Frequência', fontsize=11)
axes[0, 1].set_title('Distribuição dos Resíduos', fontsize=12, fontweight='bold')
axes[0, 1].grid(True, alpha=0.3)

# Q-Q Plot
stats.probplot(residuos, dist="norm", plot=axes[1, 0])
axes[1, 0].set_title('Q-Q Plot (Normalidade)', fontsize=12, fontweight='bold')
axes[1, 0].grid(True, alpha=0.3)

# Resíduos Padronizados
residuos_pad = (residuos - residuos.mean()) / residuos.std()
axes[1, 1].scatter(y_test_pred, residuos_pad, alpha=0.6, edgecolors='black')
axes[1, 1].axhline(y=0, color='red', linestyle='--', linewidth=2)
axes[1, 1].axhline(y=2, color='orange', linestyle=':', linewidth=1.5, label='±2 σ')
axes[1, 1].axhline(y=-2, color='orange', linestyle=':', linewidth=1.5)
axes[1, 1].set_xlabel('Valores Preditos (R$)', fontsize=11)
axes[1, 1].set_ylabel('Resíduos Padronizados', fontsize=11)
axes[1, 1].set_title('Resíduos Padronizados', fontsize=12, fontweight='bold')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ==============================================
# 10. ANÁLISE DE IMPORTÂNCIA DAS VARIÁVEIS
# ==============================================

# Padronizar dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Modelo com dados padronizados
modelo_pad = LinearRegression()
modelo_pad.fit(X_scaled, y)

# Importância das variáveis
importancia = pd.DataFrame({
    'Variavel': X.columns,
    'Coeficiente_Original': modelo.coef_,
    'Coeficiente_Padronizado': modelo_pad.coef_,
    'Importancia_Absoluta': np.abs(modelo_pad.coef_)
}).sort_values('Importancia_Absoluta', ascending=False)

print("\n" + "=" * 70)
print("IMPORTÂNCIA RELATIVA DAS VARIÁVEIS")
print("=" * 70)
print("\n", importancia.to_string(index=False))

# Visualizar importância
plt.figure(figsize=(10, 6))
plt.barh(importancia['Variavel'], importancia['Importancia_Absoluta'], 
         color='steelblue', edgecolor='black')
plt.xlabel('Importância Absoluta (Coeficiente Padronizado)', fontsize=12)
plt.title('Importância Relativa das Variáveis no Modelo', 
          fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.show()

# ==============================================
# 11. FAZER PREDIÇÕES PARA NOVOS IMÓVEIS
# ==============================================

print("\n" + "=" * 70)
print("EXEMPLOS DE PREDIÇÃO")
print("=" * 70)

# Criar exemplos de imóveis
imoveis_exemplo = pd.DataFrame({
    'Area': [60, 80, 100, 120],
    'Quartos': [2, 3, 3, 4],
    'Banheiros': [1, 2, 2, 3],
    'Idade': [5, 10, 2, 0],
    'Distancia_Centro': [10, 8, 5, 3],
    'Andar': [5, 8, 10, 12]
})

# Fazer predições
precos_previstos = modelo.predict(imoveis_exemplo)

print("\nCaracterísticas dos imóveis e preços previstos:\n")
for idx in range(len(imoveis_exemplo)):
    print(f"Imóvel {idx+1}:")
    for col in imoveis_exemplo.columns:
        print(f"  {col}: {imoveis_exemplo.iloc[idx][col]}")
    print(f"  Preço Previsto: R$ {precos_previstos[idx]:,.2f}\n")

print("=" * 70)
print("ANÁLISE COMPLETA FINALIZADA")
print("=" * 70)
```

---

## Casos Práticos Completos

### Caso 1: Otimização de Campanha de Marketing

**Problema:** Uma empresa quer otimizar investimento em diferentes canais de marketing.

**Dados:**
- Vendas mensais por região
- Gastos em TV, rádio, internet
- Tamanho da equipe de vendas
- Preço médio

**Análise:**
1. Identificar quais canais têm maior ROI
2. Alocar orçamento otimamente
3. Prever vendas para diferentes cenários

**Insights Esperados:**
- Internet pode ter coeficiente maior que TV
- Interação entre canais (ex: TV + internet)
- Efeito de saturação (retornos decrescentes)

### Caso 2: Previsão de Demanda Energética

**Problema:** Concessionária quer prever demanda para planejamento.

**Variáveis:**
- Temperatura
- Dia da semana
- Feriados
- Atividade industrial
- População

**Aplicações:**
- Programação de geração
- Compra/venda de energia
- Investimento em infraestrutura

---

## Limitações e Cuidados

### 1. Extrapolação

**Problema:** Prever fora do intervalo dos dados é arriscado.

**Exemplo:** Treinar modelo com apartamentos de 40-150m² e prever para 300m².

### 2. Variáveis Omitidas

**Problema:** Não incluir variável importante distorce outros coeficientes.

**Exemplo:** Modelo de salário que não inclui educação pode superestimar experiência.

### 3. Causalidade vs Correlação

**Lembre-se:** Regressão mostra associação, não causação.

**Para estabelecer causalidade:**
- Experimentos controlados (RCT)
- Variáveis instrumentais
- Descontinuidade de regressão
- Diferenças em diferenças

### 4. Overfitting

**Problema:** Modelo muito complexo "memoriza" dados de treino.

**Sintomas:**
- R² alto em treino, baixo em teste
- Muitas variáveis sem justificativa
- Coeficientes instáveis

**Soluções:**
- Validação cruzada
- Regularização (Ridge, Lasso)
- Seleção cuidadosa de variáveis

### 5. Dados Influentes e Outliers

**Cuidado:** Um outlier pode distorcer todo o modelo.

**Identificar:**
- Distância de Cook > 1
- DFBETAS > 2/√n
- Leverage > 2(p+1)/n

### 6. Relações Não-Lineares

**Problema:** Assumir linearidade quando relação é não-linear.

**Soluções:**
- Transformações (log, raiz, quadrado)
- Regressão polinomial
- Splines
- Modelos não-lineares (GAM, Random Forest)

---

## Exercícios Práticos

### Exercício 1: Análise de Salários

Dados de 100 funcionários com: salário, experiência, educação, avaliação.

**Tarefas:**
1. Ajustar modelo de regressão múltipla
2. Interpretar coeficientes
3. Calcular VIF
4. Identificar variável mais importante
5. Fazer predições

### Exercício 2: Comparação de Modelos

Compare:
- Modelo com todas as variáveis
- Modelo após seleção stepwise
- Modelo baseado em teoria

Qual é melhor? Por quê?

### Exercício 3: Diagnóstico Completo

Dado um modelo ajustado:
1. Verificar todos os pressupostos
2. Identificar problemas
3. Propor soluções
4. Re-ajustar modelo corrigido

---

## Referências

### Livros Fundamentais

**JAMES, Gareth et al.** *An Introduction to Statistical Learning*. 2. ed. Springer, 2021.
- Capítulo 3: Linear Regression

**KUTNER, Michael H. et al.** *Applied Linear Statistical Models*. 5. ed. McGraw-Hill, 2005.
- Referência completa em regressão aplicada

**MONTGOMERY, Douglas C.; PECK, Elizabeth A.; VINING, G. Geoffrey.** *Introduction to Linear Regression Analysis*. 5. ed. Wiley, 2012.
- Tratamento detalhado de diagnósticos

**FOX, John.** *Applied Regression Analysis and Generalized Linear Models*. 3. ed. Sage, 2015.
- Excelente para diagnósticos avançados

### Recursos Python

- **scikit-learn**: `LinearRegression`, métricas
- **statsmodels**: Análise estatística detalhada, testes
- **scipy**: Testes estatísticos
- **seaborn**: Visualizações
- **pandas**: Manipulação de dados

### Artigos Importantes

**FARRAR, Donald E.; GLAUBER, Robert R.** "Multicollinearity in Regression Analysis: The Problem Revisited." *The Review of Economics and Statistics*, v. 49, n. 1, p. 92-107, 1967.

**BELSLEY, David A.; KUH, Edwin; WELSCH, Roy E.** *Regression Diagnostics*. Wiley, 1980.
- Referência clássica em diagnósticos

---

## Conclusão

A Regressão Linear Múltipla é uma ferramenta essencial que permite:

✅ **Modelar fenômenos complexos** com múltiplos fatores  
✅ **Controlar confundidores** e isolar efeitos  
✅ **Fazer previsões robustas** considerando várias informações  
✅ **Identificar fatores importantes** e suas magnitudes relativas  
✅ **Tomar decisões embasadas** em análises quantitativas  

**Lembre-se:**
- Sempre comece com análise exploratória
- Verifique pressupostos sistematicamente
- Cuidado com multicolinearidade
- Interprete com conhecimento do domínio
- Valide o modelo em dados novos

**Próximos Passos:**
- Regressão Polinomial para relações não-lineares
- Regularização (Ridge, Lasso) para muitas variáveis
- Regressão Logística para variáveis categóricas
- Modelos aditivos generalizados (GAM)

---

*Documento criado como parte do repositório de Análise de Dados*  
*Última atualização: 2026*
