# **Teste de Hipóteses: Fundamentos e Aplicações**

O **teste de hipóteses** é uma metodologia estatística fundamental para tomar decisões baseadas em dados. Permite avaliar se uma afirmação (hipótese) sobre uma população é suportada pela evidência disponível em uma amostra.

## Sumário

1. [Conceitos Fundamentais](#conceitos-fundamentais)
2. [Estrutura de um Teste de Hipóteses](#estrutura-de-um-teste-de-hipóteses)
3. [Fundamentos Matemáticos](#fundamentos-matemáticos)
4. [Tipos de Erro](#tipos-de-erro)
5. [Principais Testes Estatísticos](#principais-testes-estatísticos)
6. [Pressupostos dos Testes e Escolha Adequada](#pressupostos-dos-testes-e-escolha-adequada)
7. [Valor-p e Significância Estatística](#valor-p-e-significância-estatística)
8. [Tamanho do Efeito e Poder Estatístico](#tamanho-do-efeito-e-poder-estatístico)
9. [Exemplos Práticos](#exemplos-práticos)
10. [Conclusão](#conclusão)
11. [Referências Acadêmicas](#referências-acadêmicas)

---

## **Conceitos Fundamentais**

### **O que é um Teste de Hipóteses?**

Um teste de hipóteses é um procedimento estatístico formal que usa dados amostrais para avaliar a plausibilidade de uma afirmação (hipótese) sobre um parâmetro populacional. O objetivo é determinar se há evidência suficiente para rejeitar uma afirmação inicial (hipótese nula) em favor de uma alternativa.

**Definição Formal**: Um teste de hipóteses é um método inferencial que, baseado em uma amostra aleatória de tamanho *n* de uma população, permite tomar decisões sobre afirmações relativas aos parâmetros populacionais (μ, σ, p, etc.), controlando as probabilidades de erro.

### **Fundamentos Teóricos**

O teste de hipóteses tem suas raízes no trabalho de pioneiros como:
- **Ronald Fisher** (anos 1920): Desenvolveu o conceito de teste de significância e valor-p
- **Jerzy Neyman e Egon Pearson** (anos 1930): Formalizaram a teoria dos testes de hipóteses com α e β
- **Karl Pearson**: Contribuiu com o teste qui-quadrado e outras ferramentas fundamentais

**Paradigma Frequentista**: O teste de hipóteses clássico se baseia na abordagem frequentista, onde as probabilidades são interpretadas como frequências relativas de eventos em repetições infinitas de um experimento.

### **Por que Testar Hipóteses?**

- **Validar teorias**: Verificar se dados suportam teorias científicas
- **Tomar decisões**: Decidir entre diferentes cursos de ação com risco controlado
- **Controlar qualidade**: Verificar se processos atendem especificações técnicas
- **Avaliar tratamentos**: Determinar eficácia de medicamentos ou intervenções
- **Inferência científica**: Generalizar conclusões de amostras para populações

---

## **Estrutura de um Teste de Hipóteses**

### **1. Formulação das Hipóteses**

**Hipótese Nula (H₀)**:
- Afirmação que assume "não há efeito" ou "não há diferença"
- Representa o status quo ou crença atual
- É o que tentamos refutar

**Hipótese Alternativa (H₁ ou Hₐ)**:
- Afirmação que contradiz a hipótese nula
- É o que queremos demonstrar
- Pode ser unilateral ou bilateral

### **Tipos de Testes Quanto à Direcionalidade**

**Teste Bilateral (ou bicaudal)**:
- H₁: μ ≠ μ₀ (a média é diferente do valor hipotético)
- Usado quando não há expectativa prévia sobre a direção da diferença
- Região de rejeição em ambas as caudas da distribuição

**Teste Unilateral à Direita**:
- H₁: μ > μ₀ (a média é maior que o valor hipotético)
- Usado quando se espera um aumento
- Região de rejeição na cauda direita

**Teste Unilateral à Esquerda**:
- H₁: μ < μ₀ (a média é menor que o valor hipotético)
- Usado quando se espera uma diminuição
- Região de rejeição na cauda esquerda

### **Exemplos de Formulação**

**Exemplo 1: Teste de Média (Bilateral)**
- H₀: μ = 100 (a média populacional é 100)
- H₁: μ ≠ 100 (a média populacional é diferente de 100)

**Exemplo 2: Comparação de Grupos**
- H₀: μ₁ = μ₂ (as médias dos dois grupos são iguais)
- H₁: μ₁ ≠ μ₂ (as médias dos dois grupos são diferentes)

**Exemplo 3: Teste Unilateral**
- H₀: μ ≤ 10 (tempo médio é no máximo 10 minutos)
- H₁: μ > 10 (tempo médio é maior que 10 minutos)

### **2. Escolha do Nível de Significância (α)**

O nível de significância (alfa) é a probabilidade de rejeitar H₀ quando ela é verdadeira:
- **α = 0,05** (5%): Padrão mais comum
- **α = 0,01** (1%): Mais conservador
- **α = 0,10** (10%): Menos rigoroso

### **3. Seleção da Estatística de Teste**

Depende do tipo de dados e hipótese:
- **Teste t**: Para médias com variância desconhecida
- **Teste Z**: Para médias com variância conhecida
- **Teste χ²**: Para independência ou aderência
- **Teste F**: Para comparação de variâncias

### **4. Cálculo do Valor-p**

O valor-p é a probabilidade de obter um resultado tão extremo quanto o observado, assumindo que H₀ é verdadeira.

### **5. Decisão**

- Se p-valor ≤ α: **Rejeitamos H₀**
- Se p-valor > α: **Não rejeitamos H₀** (ver discussão detalhada na seção [Valor-p e Significância Estatística](#valor-p-e-significância-estatística))

---

## **Fundamentos Matemáticos**

### **Estatísticas de Teste e Suas Distribuições**

#### **Teste Z para Média (σ conhecido)**

Quando a variância populacional σ² é conhecida e n é grande (n > 30) ou os dados são normais:

**Estatística de teste:**
```
Z = (X̄ - μ₀) / (σ / √n)
```

Onde:
- X̄ = média amostral
- μ₀ = média hipotética (H₀)
- σ = desvio padrão populacional
- n = tamanho da amostra

Sob H₀, Z segue distribuição Normal(0, 1)

**Exemplo em Python:**
```python
import numpy as np
from scipy import stats

# Dados
dados = [23, 25, 28, 22, 24, 26, 27, 25, 23, 24, 26, 25]
media_hipotetica = 25
sigma_populacional = 2  # conhecido

# Cálculo manual
n = len(dados)
media_amostral = np.mean(dados)
z_stat = (media_amostral - media_hipotetica) / (sigma_populacional / np.sqrt(n))

# p-valor (teste bilateral)
p_valor = 2 * (1 - stats.norm.cdf(abs(z_stat)))

print(f"Média amostral: {media_amostral:.4f}")
print(f"Estatística Z: {z_stat:.4f}")
print(f"p-valor: {p_valor:.4f}")
```

#### **Teste t de Student (σ desconhecido)**

Quando a variância populacional é desconhecida (caso mais comum):

**Estatística de teste:**
```
t = (X̄ - μ₀) / (s / √n)
```

Onde:
- s = desvio padrão amostral
- Sob H₀, t segue distribuição t de Student com (n-1) graus de liberdade

**Para duas amostras independentes:**
```
t = (X̄₁ - X̄₂) / √(s²pooled × (1/n₁ + 1/n₂))

s²pooled = ((n₁-1)s₁² + (n₂-1)s₂²) / (n₁ + n₂ - 2)
```

**Exemplo em Python:**
```python
# Teste t para uma amostra (cálculo manual)
dados = [23, 25, 28, 22, 24, 26, 27, 25]
media_hipotetica = 25

n = len(dados)
media_amostral = np.mean(dados)
desvio_padrao = np.std(dados, ddof=1)  # ddof=1 para calcular desvio padrão amostral (divisão por n-1)

# Estatística t
t_stat = (media_amostral - media_hipotetica) / (desvio_padrao / np.sqrt(n))

# Graus de liberdade
df = n - 1

# p-valor (bilateral)
p_valor = 2 * (1 - stats.t.cdf(abs(t_stat), df))

print(f"Estatística t: {t_stat:.4f}")
print(f"Graus de liberdade: {df}")
print(f"p-valor: {p_valor:.4f}")

# Região crítica
alpha = 0.05
t_critico = stats.t.ppf(1 - alpha/2, df)
print(f"Valor crítico t (α={alpha}): ±{t_critico:.4f}")

if abs(t_stat) > t_critico:
    print("Decisão: Rejeitar H₀")
else:
    print("Decisão: Não rejeitar H₀")
```

#### **Teste Qui-Quadrado (χ²)**

**Para teste de independência:**
```
χ² = Σ ((Oᵢⱼ - Eᵢⱼ)² / Eᵢⱼ)
```

Onde:
- Oᵢⱼ = frequência observada na célula (i,j)
- Eᵢⱼ = frequência esperada = (total linha i × total coluna j) / total geral
- Graus de liberdade = (linhas - 1) × (colunas - 1)

**Exemplo em Python:**
```python
import pandas as pd
from scipy.stats import chi2_contingency

# Tabela de contingência
tabela = np.array([[30, 10],
                   [20, 40]])

chi2_stat, p_valor, df, expected = chi2_contingency(tabela)

print("Frequências Observadas:")
print(tabela)
print("\nFrequências Esperadas:")
print(expected)
print(f"\nEstatística χ²: {chi2_stat:.4f}")
print(f"Graus de liberdade: {df}")
print(f"p-valor: {p_valor:.4f}")

# Cálculo manual da estatística
chi2_manual = np.sum((tabela - expected)**2 / expected)
print(f"\nχ² (cálculo manual): {chi2_manual:.4f}")
```

#### **Teste F (ANOVA)**

**Para ANOVA de uma via:**
```
F = MSB / MSW

MSB = Σnᵢ(X̄ᵢ - X̄)² / (k - 1)  (Mean Square Between groups)
MSW = Σ(nᵢ - 1)sᵢ² / (N - k)    (Mean Square Within groups)
```

Onde:
- k = número de grupos
- N = total de observações
- nᵢ = tamanho do grupo i
- X̄ᵢ = média do grupo i
- X̄ = média geral

**Exemplo em Python:**
```python
# ANOVA de uma via (cálculo manual e usando scipy)
grupo1 = np.array([23, 25, 28, 22, 24])
grupo2 = np.array([26, 27, 29, 25, 28])
grupo3 = np.array([30, 32, 28, 31, 29])

# Cálculo manual
todos_dados = np.concatenate([grupo1, grupo2, grupo3])
media_geral = np.mean(todos_dados)

n1, n2, n3 = len(grupo1), len(grupo2), len(grupo3)
N = n1 + n2 + n3
k = 3

# Sum of Squares Between (SSB)
ssb = (n1 * (np.mean(grupo1) - media_geral)**2 +
       n2 * (np.mean(grupo2) - media_geral)**2 +
       n3 * (np.mean(grupo3) - media_geral)**2)

# Sum of Squares Within (SSW)
ssw = (np.sum((grupo1 - np.mean(grupo1))**2) +
       np.sum((grupo2 - np.mean(grupo2))**2) +
       np.sum((grupo3 - np.mean(grupo3))**2))

# Mean Squares
msb = ssb / (k - 1)
msw = ssw / (N - k)

# Estatística F
f_stat = msb / msw

# Graus de liberdade
df_between = k - 1
df_within = N - k

# p-valor
p_valor = 1 - stats.f.cdf(f_stat, df_between, df_within)

print("=== CÁLCULO MANUAL ===")
print(f"SSB (Between): {ssb:.4f}")
print(f"SSW (Within): {ssw:.4f}")
print(f"MSB: {msb:.4f}")
print(f"MSW: {msw:.4f}")
print(f"Estatística F: {f_stat:.4f}")
print(f"Graus de liberdade: ({df_between}, {df_within})")
print(f"p-valor: {p_valor:.4f}")

# Comparação com scipy
f_scipy, p_scipy = stats.f_oneway(grupo1, grupo2, grupo3)
print("\n=== SCIPY ===")
print(f"Estatística F: {f_scipy:.4f}")
print(f"p-valor: {p_scipy:.4f}")
```

### **Relação entre Teste de Hipóteses e Intervalo de Confiança**

Existe uma equivalência matemática entre testes de hipóteses e intervalos de confiança:

**Para teste bilateral com α = 0.05:**
- Rejeitar H₀: μ = μ₀ ⟺ μ₀ não está no IC 95%
- Não rejeitar H₀: μ = μ₀ ⟺ μ₀ está no IC 95%

**Exemplo demonstrando a equivalência:**
```python
# Dados
dados = [23, 25, 28, 22, 24, 26, 27, 25, 23, 24]
media_hipotetica = 25
alpha = 0.05

# Teste t
t_stat, p_valor = stats.ttest_1samp(dados, media_hipotetica)

# Intervalo de confiança
n = len(dados)
media = np.mean(dados)
se = stats.sem(dados)
df = n - 1
t_crit = stats.t.ppf(1 - alpha/2, df)
ic_inferior = media - t_crit * se
ic_superior = media + t_crit * se

print("=== TESTE DE HIPÓTESES ===")
print(f"H₀: μ = {media_hipotetica}")
print(f"p-valor: {p_valor:.4f}")
print(f"Decisão: {'Rejeitar H₀' if p_valor < alpha else 'Não rejeitar H₀'}")

print("\n=== INTERVALO DE CONFIANÇA 95% ===")
print(f"IC: [{ic_inferior:.4f}, {ic_superior:.4f}]")
print(f"{media_hipotetica} está no IC? {ic_inferior <= media_hipotetica <= ic_superior}")

print("\n=== EQUIVALÊNCIA ===")
no_ic = ic_inferior <= media_hipotetica <= ic_superior
nao_rejeita = p_valor >= alpha
print(f"μ₀ no IC: {no_ic}")
print(f"Não rejeita H₀: {nao_rejeita}")
print(f"Equivalência verificada: {no_ic == nao_rejeita}")
```

---

## **Tipos de Erro**

### **Erro Tipo I (α)**
- **Definição**: Rejeitar H₀ quando ela é verdadeira
- **Consequência**: "Falso positivo"
- **Probabilidade**: Nível de significância (α)

### **Erro Tipo II (β)**
- **Definição**: Não rejeitar H₀ quando ela é falsa
- **Consequência**: "Falso negativo"
- **Poder do teste**: 1 - β

### **Tabela de Decisões**

|                    | H₀ é Verdadeira | H₀ é Falsa      |
|--------------------|----------------|-----------------|
| **Rejeitamos H₀**  | Erro Tipo I (α) | Decisão Correta |
| **Não Rejeitamos H₀** | Decisão Correta | Erro Tipo II (β) |

### **⚖️ Balanceamento dos Erros**

- Reduzir α aumenta β
- Aumentar tamanho da amostra reduz ambos os erros
- A escolha depende das consequências de cada tipo de erro

---

## **Principais Testes Estatísticos**

### **Teste t de Student**

**Aplicação**: Testar médias quando σ é desconhecido

#### **Teste t para Uma Amostra**
```python
from scipy import stats
import numpy as np

# Dados de exemplo
dados = [23, 25, 28, 22, 24, 26, 27, 25, 23, 24]
media_testada = 25

# Teste t
t_stat, p_value = stats.ttest_1samp(dados, media_testada)

print(f"Estatística t: {t_stat:.4f}")
print(f"Valor-p: {p_value:.4f}")

# Interpretação
alpha = 0.05
if p_value < alpha:
    print("Rejeitamos H₀: há evidência de que a média é diferente de 25")
else:
    print("Não rejeitamos H₀: não há evidência suficiente")
```

#### **Teste t para Duas Amostras Independentes**
```python
# Duas amostras independentes
grupo1 = [23, 25, 28, 22, 24]
grupo2 = [26, 27, 29, 25, 28]

# Teste t
t_stat, p_value = stats.ttest_ind(grupo1, grupo2)

print(f"Estatística t: {t_stat:.4f}")
print(f"Valor-p: {p_value:.4f}")
```

### **Teste de Shapiro-Wilk (Normalidade)**

```python
# Testar normalidade dos dados
shapiro_stat, shapiro_p = stats.shapiro(dados)

print(f"Estatística de Shapiro-Wilk: {shapiro_stat:.4f}")
print(f"Valor-p: {shapiro_p:.4f}")

if shapiro_p > 0.05:
    print("Os dados seguem distribuição normal")
else:
    print("Os dados não seguem distribuição normal")
```

### **Teste Qui-Quadrado de Independência**

```python
import pandas as pd
from scipy.stats import chi2_contingency

# Exemplo: Relação entre gênero e preferência de produto
dados = pd.DataFrame({
    'Gênero': ['M', 'M', 'F', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
    'Produto': ['A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B', 'A']
})

# Tabela de contingência
tabela = pd.crosstab(dados['Gênero'], dados['Produto'])
print("Tabela de Contingência:")
print(tabela)

# Teste qui-quadrado
chi2, p_value, dof, expected = chi2_contingency(tabela)

print(f"\nEstatística Qui-quadrado: {chi2:.4f}")
print(f"Valor-p: {p_value:.4f}")
print(f"Graus de liberdade: {dof}")
```

### **Teste ANOVA (Análise de Variância)**

**Aplicação**: Comparar médias de três ou mais grupos independentes

**Pressupostos**:
- Normalidade dos dados em cada grupo
- Homogeneidade de variâncias (homocedasticidade)
- Independência das observações

```python
# Comparar médias de múltiplos grupos
grupo1 = [23, 25, 28, 22, 24]
grupo2 = [26, 27, 29, 25, 28]
grupo3 = [30, 32, 28, 31, 29]

# ANOVA de uma via
f_stat, p_value = stats.f_oneway(grupo1, grupo2, grupo3)

print(f"Estatística F: {f_stat:.4f}")
print(f"Valor-p: {p_value:.4f}")

if p_value < 0.05:
    print("Há diferença significativa entre os grupos")
else:
    print("Não há diferença significativa entre os grupos")
```

### **Testes Não-Paramétricos**

Testes não-paramétricos são alternativas robustas quando os pressupostos dos testes paramétricos não são satisfeitos. Eles não assumem distribuição específica dos dados.

#### **Teste de Mann-Whitney U (Wilcoxon Rank-Sum)**

**Aplicação**: Alternativa não-paramétrica ao teste t para duas amostras independentes

**Quando usar**:
- Dados não seguem distribuição normal
- Variáveis ordinais
- Presença de outliers extremos

```python
from scipy.stats import mannwhitneyu

# Duas amostras independentes
grupo1 = [23, 25, 28, 22, 24, 100]  # Contém outlier
grupo2 = [26, 27, 29, 25, 28]

# Teste de Mann-Whitney
u_stat, p_value = mannwhitneyu(grupo1, grupo2, alternative='two-sided')

print(f"Estatística U: {u_stat:.4f}")
print(f"Valor-p: {p_value:.4f}")

if p_value < 0.05:
    print("Há diferença significativa entre os grupos")
else:
    print("Não há diferença significativa entre os grupos")
```

#### **Teste de Wilcoxon Signed-Rank**

**Aplicação**: Alternativa não-paramétrica ao teste t pareado

**Quando usar**:
- Comparar medidas antes e depois em mesmos indivíduos
- Dados não normais ou ordinais

```python
from scipy.stats import wilcoxon

# Medidas antes e depois (mesmo indivíduo)
antes = [85, 90, 88, 92, 87, 89, 91, 86, 90, 88]
depois = [80, 85, 83, 88, 82, 84, 87, 81, 85, 83]

# Teste de Wilcoxon
w_stat, p_value = wilcoxon(antes, depois)

print(f"Estatística W: {w_stat:.4f}")
print(f"Valor-p: {p_value:.4f}")

if p_value < 0.05:
    print("Há diferença significativa entre antes e depois")
else:
    print("Não há diferença significativa entre antes e depois")
```

#### **Teste de Kruskal-Wallis**

**Aplicação**: Alternativa não-paramétrica à ANOVA de uma via

**Quando usar**:
- Comparar três ou mais grupos independentes
- Dados não seguem distribuição normal
- Presença de outliers

```python
from scipy.stats import kruskal

# Três ou mais grupos independentes
grupo1 = [23, 25, 28, 22, 24]
grupo2 = [26, 27, 29, 25, 28]
grupo3 = [30, 32, 28, 31, 29]

# Teste de Kruskal-Wallis
h_stat, p_value = kruskal(grupo1, grupo2, grupo3)

print(f"Estatística H: {h_stat:.4f}")
print(f"Valor-p: {p_value:.4f}")

if p_value < 0.05:
    print("Há diferença significativa entre os grupos")
else:
    print("Não há diferença significativa entre os grupos")
```

#### **Teste Exato de Fisher**

**Aplicação**: Testar independência em tabelas 2×2 com amostras pequenas

**Quando usar**:
- Tabelas de contingência 2×2
- Frequências esperadas < 5 (onde qui-quadrado não é confiável)

```python
from scipy.stats import fisher_exact

# Tabela de contingência 2x2
# Exemplo: Tratamento vs. Resultado
#              Sucesso  Fracasso
# Tratamento      8        2
# Controle        3        7

tabela = [[8, 2], [3, 7]]

# Teste exato de Fisher
odds_ratio, p_value = fisher_exact(tabela)

print(f"Odds Ratio: {odds_ratio:.4f}")
print(f"Valor-p: {p_value:.4f}")

if p_value < 0.05:
    print("Há associação significativa entre tratamento e resultado")
else:
    print("Não há associação significativa")
```

### **Teste de Levene (Homogeneidade de Variâncias)**

**Aplicação**: Verificar se dois ou mais grupos têm variâncias iguais

**Quando usar**:
- Antes de aplicar ANOVA ou teste t
- Verificar pressuposto de homocedasticidade

```python
from scipy.stats import levene

# Grupos para testar homogeneidade de variâncias
grupo1 = [23, 25, 28, 22, 24, 26, 27]
grupo2 = [26, 27, 29, 25, 28, 30, 31]
grupo3 = [15, 45, 10, 50, 20, 40, 25]  # Variância muito diferente

# Teste de Levene
w_stat, p_value = levene(grupo1, grupo2, grupo3)

print(f"Estatística W: {w_stat:.4f}")
print(f"Valor-p: {p_value:.4f}")

if p_value < 0.05:
    print("Variâncias são significativamente diferentes")
    print("Considere usar teste não-paramétrico ou correção de Welch")
else:
    print("Variâncias são homogêneas")
```

---

## **Pressupostos dos Testes e Escolha Adequada**

### **Fluxograma de Decisão para Escolha de Teste**

**Para comparar dois grupos independentes:**
1. Os dados são normais? (teste de Shapiro-Wilk)
   - **SIM**: Use teste t de Student
   - **NÃO**: Use teste de Mann-Whitney U

2. As variâncias são iguais? (teste de Levene)
   - **SIM**: Use teste t padrão
   - **NÃO**: Use teste t de Welch (correção para variâncias desiguais)

**Para comparar dois grupos pareados:**
1. As diferenças são normais?
   - **SIM**: Use teste t pareado
   - **NÃO**: Use teste de Wilcoxon signed-rank

**Para comparar três ou mais grupos independentes:**
1. Os dados são normais em todos os grupos?
   - **SIM**: Variâncias homogêneas? → ANOVA de uma via
   - **NÃO**: Use teste de Kruskal-Wallis

**Para testar associação entre variáveis categóricas:**
1. Tabela de contingência > 2×2 ou frequências esperadas ≥ 5?
   - **SIM**: Use teste qui-quadrado
   - **NÃO**: Use teste exato de Fisher

### **Verificação de Pressupostos - Exemplo Completo**

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Dados de exemplo
np.random.seed(42)
grupo1 = np.random.normal(25, 3, 30)
grupo2 = np.random.normal(28, 3, 30)

# 1. Verificar normalidade
shapiro1 = stats.shapiro(grupo1)
shapiro2 = stats.shapiro(grupo2)

print("=== VERIFICAÇÃO DE NORMALIDADE ===")
print(f"Grupo 1 - Shapiro-Wilk p-value: {shapiro1.pvalue:.4f}")
print(f"Grupo 2 - Shapiro-Wilk p-value: {shapiro2.pvalue:.4f}")

normalidade_ok = shapiro1.pvalue > 0.05 and shapiro2.pvalue > 0.05

if normalidade_ok:
    print("✓ Dados seguem distribuição normal\n")
    
    # 2. Verificar homogeneidade de variâncias
    levene_stat, levene_p = stats.levene(grupo1, grupo2)
    print("=== VERIFICAÇÃO DE HOMOGENEIDADE DE VARIÂNCIAS ===")
    print(f"Levene p-value: {levene_p:.4f}")
    
    if levene_p > 0.05:
        print("✓ Variâncias homogêneas\n")
        print("=== TESTE RECOMENDADO: t de Student ===")
        t_stat, p_value = stats.ttest_ind(grupo1, grupo2)
    else:
        print("✗ Variâncias heterogêneas\n")
        print("=== TESTE RECOMENDADO: t de Welch ===")
        t_stat, p_value = stats.ttest_ind(grupo1, grupo2, equal_var=False)
    
    print(f"Estatística t: {t_stat:.4f}")
    print(f"Valor-p: {p_value:.4f}")
    
else:
    print("✗ Dados não seguem distribuição normal\n")
    print("=== TESTE RECOMENDADO: Mann-Whitney U ===")
    u_stat, p_value = stats.mannwhitneyu(grupo1, grupo2)
    print(f"Estatística U: {u_stat:.4f}")
    print(f"Valor-p: {p_value:.4f}")

# Visualização
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Histogramas
axes[0].hist(grupo1, bins=10, alpha=0.7, label='Grupo 1')
axes[0].hist(grupo2, bins=10, alpha=0.7, label='Grupo 2')
axes[0].set_xlabel('Valor')
axes[0].set_ylabel('Frequência')
axes[0].set_title('Distribuição dos Dados')
axes[0].legend()

# Q-Q plots
stats.probplot(grupo1, dist="norm", plot=axes[1])
axes[1].set_title('Q-Q Plot - Grupo 1')

stats.probplot(grupo2, dist="norm", plot=axes[2])
axes[2].set_title('Q-Q Plot - Grupo 2')

plt.tight_layout()
# Nota: Ajuste o caminho conforme seu sistema operacional
# Windows: 'C:\\temp\\pressupostos_teste.png'
# Linux/Mac: '/tmp/pressupostos_teste.png'
plt.savefig('pressupostos_teste.png', dpi=150, bbox_inches='tight')
print("\n✓ Gráficos de diagnóstico salvos em pressupostos_teste.png")
```

---

## **Valor-p e Significância Estatística**

### **Interpretação do Valor-p**

O valor-p **NÃO** indica:
- A probabilidade de H₀ ser verdadeira
- O tamanho do efeito
- A importância prática do resultado

O valor-p **INDICA**:
- A força da evidência contra H₀
- A probabilidade de obter resultado tão extremo se H₀ fosse verdadeira

### **Interpretação Prática**

| Valor-p | Interpretação |
|---------|---------------|
| p < 0.001 | Evidência muito forte contra H₀ |
| 0.001 ≤ p < 0.01 | Evidência forte contra H₀ |
| 0.01 ≤ p < 0.05 | Evidência moderada contra H₀ |
| 0.05 ≤ p < 0.10 | Evidência fraca contra H₀ |
| p ≥ 0.10 | Pouca ou nenhuma evidência contra H₀ |

### **Correção para Múltiplos Testes**

Quando realizamos múltiplos testes estatísticos simultaneamente, a probabilidade de cometer pelo menos um erro tipo I aumenta. Isso é conhecido como o **problema de comparações múltiplas**.

#### **Problema de Comparações Múltiplas**

Se realizarmos *m* testes independentes, cada um com α = 0.05, a probabilidade de cometer pelo menos um erro tipo I é:

**P(pelo menos 1 erro tipo I) = 1 - (1 - α)^m**

Por exemplo, com 10 testes: 1 - (0.95)^10 = 1 - 0.5987 ≈ 0.40 (40% de chance!)

#### **Correção de Bonferroni**

Método conservador que divide o nível de significância pelo número de testes:

**α_ajustado = α / m**

```python
from scipy import stats
import numpy as np

# Múltiplos testes de hipóteses
np.random.seed(42)
grupos = [np.random.normal(25, 5, 30) for _ in range(5)]

# Comparações par a par
from itertools import combinations
p_values = []
comparacoes = []

for i, j in combinations(range(5), 2):
    t_stat, p_val = stats.ttest_ind(grupos[i], grupos[j])
    p_values.append(p_val)
    comparacoes.append(f"Grupo {i+1} vs Grupo {j+1}")

print("=== SEM CORREÇÃO ===")
alpha_original = 0.05
for comp, p_val in zip(comparacoes, p_values):
    sig = "SIGNIFICATIVO" if p_val < alpha_original else "Não significativo"
    print(f"{comp}: p = {p_val:.4f} - {sig}")

print(f"\n=== COM CORREÇÃO DE BONFERRONI ===")
m = len(p_values)  # Número de testes
alpha_bonferroni = alpha_original / m
print(f"α ajustado: {alpha_bonferroni:.4f}")

for comp, p_val in zip(comparacoes, p_values):
    sig = "SIGNIFICATIVO" if p_val < alpha_bonferroni else "Não significativo"
    print(f"{comp}: p = {p_val:.4f} - {sig}")
```

#### **Correção de False Discovery Rate (FDR) - Benjamini-Hochberg**

Método menos conservador que controla a proporção de falsos positivos entre as descobertas:

```python
from statsmodels.stats.multitest import multipletests

# p-values dos testes anteriores
p_values_array = np.array(p_values)

# Aplicar correção FDR
reject, p_adjusted, _, _ = multipletests(p_values_array, alpha=0.05, method='fdr_bh')

print("=== CORREÇÃO FDR (Benjamini-Hochberg) ===")
for comp, p_orig, p_adj, rej in zip(comparacoes, p_values, p_adjusted, reject):
    sig = "SIGNIFICATIVO" if rej else "Não significativo"
    print(f"{comp}")
    print(f"  p-value original: {p_orig:.4f}")
    print(f"  p-value ajustado: {p_adj:.4f}")
    print(f"  Decisão: {sig}\n")
```

#### **Comparação dos Métodos**

| Método | Conservadorismo | Quando usar |
|--------|----------------|-------------|
| **Sem correção** | Nenhum | Apenas 1 teste |
| **Bonferroni** | Muito conservador | Poucos testes (<10), controle rigoroso |
| **FDR** | Moderado | Muitos testes, pesquisa exploratória |
| **Holm-Bonferroni** | Moderado | Alternativa à Bonferroni |

---

## **Tamanho do Efeito e Poder Estatístico**

### **Tamanho do Efeito**

Medida da magnitude prática da diferença, independente do tamanho da amostra.

#### **d de Cohen (para diferença de médias)**
```python
def cohen_d(grupo1, grupo2):
    n1, n2 = len(grupo1), len(grupo2)
    s1, s2 = np.std(grupo1, ddof=1), np.std(grupo2, ddof=1)
    
    # Desvio padrão combinado
    s_pooled = np.sqrt(((n1-1)*s1**2 + (n2-1)*s2**2) / (n1+n2-2))
    
    # d de Cohen
    d = (np.mean(grupo1) - np.mean(grupo2)) / s_pooled
    return d

# Exemplo
grupo1 = [23, 25, 28, 22, 24]
grupo2 = [26, 27, 29, 25, 28]

d = cohen_d(grupo1, grupo2)
print(f"d de Cohen: {d:.3f}")

# Interpretação
if abs(d) < 0.2:
    print("Efeito pequeno")
elif abs(d) < 0.5:
    print("Efeito médio")
elif abs(d) < 0.8:
    print("Efeito grande")
else:
    print("Efeito muito grande")
```

### **Cálculo do Poder Estatístico**

```python
from statsmodels.stats import power

# Calcular poder para teste t
effect_size = 0.5  # d de Cohen
alpha = 0.05
sample_size = 30

poder = power.ttest_power(effect_size, sample_size, alpha)
print(f"Poder estatístico: {poder:.3f}")

# Calcular tamanho de amostra necessário
poder_desejado = 0.80
n_necessario = power.tt_solve_power(effect_size, poder_desejado, alpha)
print(f"Tamanho de amostra necessário: {n_necessario:.0f}")
```

---

## **Exemplos Práticos**

### **Exemplo 1: Teste A/B em E-commerce**

**Situação**: Uma loja online quer testar se um novo layout aumenta a taxa de conversão.

```python
import numpy as np
from scipy import stats

# Dados simulados
np.random.seed(42)

# Grupo controle (layout atual)
conversoes_controle = np.random.binomial(1, 0.12, 1000)  # 12% de conversão
taxa_controle = np.mean(conversoes_controle)

# Grupo teste (novo layout)
conversoes_teste = np.random.binomial(1, 0.14, 1000)     # 14% de conversão
taxa_teste = np.mean(conversoes_teste)

print(f"Taxa de conversão - Controle: {taxa_controle:.3f}")
print(f"Taxa de conversão - Teste: {taxa_teste:.3f}")

# Teste de proporções
from statsmodels.stats.proportion import proportions_ztest

# Contagens e totais
count = np.array([np.sum(conversoes_teste), np.sum(conversoes_controle)])
nobs = np.array([len(conversoes_teste), len(conversoes_controle)])

# Teste
z_stat, p_value = proportions_ztest(count, nobs)

print(f"\nEstatística Z: {z_stat:.4f}")
print(f"Valor-p: {p_value:.4f}")

if p_value < 0.05:
    print("O novo layout tem efeito significativo na conversão!")
else:
    print("Não há evidência de melhoria significativa.")
```

### **Exemplo 2: Controle de Qualidade**

**Situação**: Uma fábrica quer verificar se o peso médio de seus produtos está dentro da especificação.

```python
# Dados de peso (em gramas)
pesos = [498, 502, 501, 499, 503, 500, 497, 504, 501, 499, 
         502, 498, 500, 501, 503, 499, 498, 502, 500, 501]

peso_especificado = 500  # Peso alvo

# Estatísticas descritivas
print(f"Peso médio observado: {np.mean(pesos):.2f}g")
print(f"Desvio padrão: {np.std(pesos, ddof=1):.2f}g")

# Teste t para uma amostra
t_stat, p_value = stats.ttest_1samp(pesos, peso_especificado)

print(f"\nH₀: μ = {peso_especificado}g")
print(f"H₁: μ ≠ {peso_especificado}g")
print(f"Estatística t: {t_stat:.4f}")
print(f"Valor-p: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Rejeitamos H₀: o peso médio difere significativamente do especificado")
else:
    print("Não rejeitamos H₀: o peso médio está conforme especificação")

# Intervalo de confiança
from scipy.stats import t
n = len(pesos)
se = stats.sem(pesos)  # Erro padrão
t_crit = t.ppf(1 - alpha/2, df=n-1)
ic_inferior = np.mean(pesos) - t_crit * se
ic_superior = np.mean(pesos) + t_crit * se

print(f"\nIntervalo de confiança 95%: [{ic_inferior:.2f}, {ic_superior:.2f}]g")

# Interpretação do IC
if peso_especificado >= ic_inferior and peso_especificado <= ic_superior:
    print(f"O valor {peso_especificado}g está dentro do IC 95%")
else:
    print(f"O valor {peso_especificado}g está FORA do IC 95%")
```

### **Exemplo 3: Teste de Normalidade e Transformações**

**Situação**: Antes de aplicar um teste t, precisamos verificar se os dados seguem distribuição normal.

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Dados com distribuição assimétrica
np.random.seed(42)
dados_assimetricos = np.random.exponential(scale=2, size=100)

# 1. Visualização
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Histograma
axes[0, 0].hist(dados_assimetricos, bins=20, edgecolor='black', alpha=0.7)
axes[0, 0].set_title('Histograma - Dados Originais')
axes[0, 0].set_xlabel('Valor')
axes[0, 0].set_ylabel('Frequência')

# Q-Q plot
stats.probplot(dados_assimetricos, dist="norm", plot=axes[0, 1])
axes[0, 1].set_title('Q-Q Plot - Dados Originais')

# 2. Teste de normalidade
shapiro_stat, shapiro_p = stats.shapiro(dados_assimetricos)
print("=== DADOS ORIGINAIS ===")
print(f"Teste de Shapiro-Wilk:")
print(f"  Estatística: {shapiro_stat:.4f}")
print(f"  p-value: {shapiro_p:.4f}")

if shapiro_p < 0.05:
    print("  Conclusão: Dados NÃO seguem distribuição normal\n")
    
    # 3. Aplicar transformação logarítmica
    dados_transformados = np.log(dados_assimetricos)
    
    # Visualização dos dados transformados
    axes[1, 0].hist(dados_transformados, bins=20, edgecolor='black', alpha=0.7)
    axes[1, 0].set_title('Histograma - Dados Transformados (log)')
    axes[1, 0].set_xlabel('log(Valor)')
    axes[1, 0].set_ylabel('Frequência')
    
    stats.probplot(dados_transformados, dist="norm", plot=axes[1, 1])
    axes[1, 1].set_title('Q-Q Plot - Dados Transformados (log)')
    
    # Teste de normalidade nos dados transformados
    shapiro_stat2, shapiro_p2 = stats.shapiro(dados_transformados)
    print("=== DADOS TRANSFORMADOS (logaritmo) ===")
    print(f"Teste de Shapiro-Wilk:")
    print(f"  Estatística: {shapiro_stat2:.4f}")
    print(f"  p-value: {shapiro_p2:.4f}")
    
    if shapiro_p2 > 0.05:
        print("  Conclusão: Dados transformados seguem distribuição normal")
        print("  Recomendação: Use teste t nos dados transformados")
    else:
        print("  Conclusão: Mesmo transformados, dados não são normais")
        print("  Recomendação: Use teste não-paramétrico")
else:
    print("  Conclusão: Dados seguem distribuição normal")

plt.tight_layout()
plt.savefig('teste_normalidade.png', dpi=150, bbox_inches='tight')
print("\n✓ Gráfico salvo em teste_normalidade.png")
```

### **Exemplo 4: ANOVA com Testes Post-Hoc**

**Situação**: Comparar eficácia de três diferentes tratamentos médicos.

```python
import numpy as np
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd

# Dados simulados: três tratamentos
np.random.seed(42)
tratamento_a = np.random.normal(75, 10, 30)
tratamento_b = np.random.normal(80, 10, 30)
tratamento_c = np.random.normal(85, 10, 30)

# Combinar dados
dados = np.concatenate([tratamento_a, tratamento_b, tratamento_c])
grupos = ['A']*30 + ['B']*30 + ['C']*30

# 1. ANOVA
print("=== ANÁLISE DE VARIÂNCIA (ANOVA) ===")
f_stat, p_value = stats.f_oneway(tratamento_a, tratamento_b, tratamento_c)
print(f"Estatística F: {f_stat:.4f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("\nConclusão: Há diferença significativa entre os grupos")
    print("Procedendo com testes post-hoc...\n")
    
    # 2. Teste de Tukey HSD (Honest Significant Difference)
    print("=== TESTE POST-HOC: Tukey HSD ===")
    tukey_result = pairwise_tukeyhsd(dados, grupos, alpha=0.05)
    print(tukey_result)
    
    # 3. Estatísticas descritivas por grupo
    print("\n=== ESTATÍSTICAS DESCRITIVAS ===")
    df = pd.DataFrame({
        'Tratamento': grupos,
        'Eficacia': dados
    })
    
    print(df.groupby('Tratamento')['Eficacia'].describe())
    
    # 4. Visualização
    import matplotlib.pyplot as plt
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Boxplot
    df.boxplot(column='Eficacia', by='Tratamento', ax=axes[0])
    axes[0].set_title('Distribuição da Eficácia por Tratamento')
    axes[0].set_xlabel('Tratamento')
    axes[0].set_ylabel('Eficácia')
    plt.sca(axes[0])
    plt.xticks([1, 2, 3], ['A', 'B', 'C'])
    
    # Gráfico de médias com IC
    medias = df.groupby('Tratamento')['Eficacia'].mean()
    erros = df.groupby('Tratamento')['Eficacia'].sem() * 1.96  # IC 95%
    
    axes[1].bar(medias.index, medias.values, yerr=erros, capsize=10, 
                alpha=0.7, edgecolor='black')
    axes[1].set_title('Médias com Intervalos de Confiança 95%')
    axes[1].set_xlabel('Tratamento')
    axes[1].set_ylabel('Eficácia Média')
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('anova_posthoc.png', dpi=150, bbox_inches='tight')
    print("\n✓ Gráficos salvos em anova_posthoc.png")
else:
    print("\nConclusão: Não há diferença significativa entre os grupos")
```

### **Exemplo 5: Teste Qui-Quadrado com Análise de Resíduos**

**Situação**: Analisar a associação entre método de ensino e aprovação.

```python
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

# Dados: Método de ensino vs. Resultado
dados = {
    'Método': ['Tradicional']*100 + ['Ativo']*100 + ['Híbrido']*100,
    'Resultado': (['Aprovado']*60 + ['Reprovado']*40 + 
                  ['Aprovado']*75 + ['Reprovado']*25 +
                  ['Aprovado']*80 + ['Reprovado']*20)
}

df = pd.DataFrame(dados)

# Tabela de contingência
tabela = pd.crosstab(df['Método'], df['Resultado'], margins=True)
print("=== TABELA DE CONTINGÊNCIA ===")
print(tabela)
print()

# Tabela sem margens para o teste
tabela_teste = pd.crosstab(df['Método'], df['Resultado'])

# Teste qui-quadrado
chi2, p_value, dof, expected = chi2_contingency(tabela_teste)

print("=== TESTE QUI-QUADRADO ===")
print(f"Estatística χ²: {chi2:.4f}")
print(f"Graus de liberdade: {dof}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("\nConclusão: Há associação significativa entre método e resultado\n")
    
    # Análise de resíduos padronizados
    print("=== FREQUÊNCIAS ESPERADAS ===")
    expected_df = pd.DataFrame(expected, 
                              index=tabela_teste.index,
                              columns=tabela_teste.columns)
    print(expected_df)
    print()
    
    # Resíduos padronizados
    residuos = (tabela_teste - expected) / np.sqrt(expected)
    print("=== RESÍDUOS PADRONIZADOS ===")
    print("(Valores > |2| indicam contribuição significativa para χ²)")
    print(residuos)
    print()
    
    # Interpretação
    print("=== INTERPRETAÇÃO ===")
    for metodo in residuos.index:
        for resultado in residuos.columns:
            res = residuos.loc[metodo, resultado]
            if abs(res) > 2:
                direcao = "mais" if res > 0 else "menos"
                print(f"• {metodo} tem {direcao} {resultado}s do que o esperado (resíduo: {res:.2f})")
else:
    print("\nConclusão: Não há associação significativa entre método e resultado")

# Visualização
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Gráfico de barras agrupadas
tabela_teste.plot(kind='bar', ax=axes[0], edgecolor='black')
axes[0].set_title('Frequências Observadas')
axes[0].set_xlabel('Método de Ensino')
axes[0].set_ylabel('Frequência')
axes[0].legend(title='Resultado')
axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=45)

# Heatmap de resíduos
im = axes[1].imshow(residuos, cmap='RdBu_r', aspect='auto', vmin=-3, vmax=3)
axes[1].set_xticks(range(len(residuos.columns)))
axes[1].set_yticks(range(len(residuos.index)))
axes[1].set_xticklabels(residuos.columns)
axes[1].set_yticklabels(residuos.index)
axes[1].set_title('Resíduos Padronizados')
axes[1].set_xlabel('Resultado')
axes[1].set_ylabel('Método')

# Adicionar valores nos quadrados
for i in range(len(residuos.index)):
    for j in range(len(residuos.columns)):
        text = axes[1].text(j, i, f'{residuos.iloc[i, j]:.2f}',
                          ha="center", va="center", color="black")

plt.colorbar(im, ax=axes[1])
plt.tight_layout()
plt.savefig('qui_quadrado.png', dpi=150, bbox_inches='tight')
print("\n✓ Gráficos salvos em qui_quadrado.png")
```

---

## **Conclusão**

O teste de hipóteses é uma ferramenta poderosa e fundamental para a inferência estatística e tomada de decisões baseada em dados. Esta metodologia, desenvolvida ao longo do século XX por estatísticos pioneiros, permite quantificar a incerteza e controlar as probabilidades de erro nas decisões científicas e práticas.

### **Conceitos-Chave Revisados**

1. **Dualidade de Hipóteses**: O teste sempre envolve H₀ (hipótese nula) e H₁ (hipótese alternativa)
2. **Controle de Erros**: Balanceamento entre erro tipo I (α) e erro tipo II (β)
3. **Valor-p**: Medida de evidência contra H₀, não a probabilidade de H₀ ser verdadeira
4. **Pressupostos**: Cada teste tem pressupostos que devem ser verificados
5. **Alternativas Robustas**: Testes não-paramétricos quando pressupostos violados
6. **Múltiplos Testes**: Necessidade de correção quando fazemos muitas comparações

### **✅ Boas Práticas**

**Planejamento**:
- Formule hipóteses **antes** de ver os dados (evitar HARKing - Formulação de Hipóteses Após Conhecer os Resultados, do inglês "Hypothesizing After Results are Known")
- Defina α priori baseado nas consequências dos erros
- Calcule o tamanho amostral necessário para poder adequado (1-β ≥ 0.80)

**Verificação**:
- Sempre verifique pressupostos dos testes (normalidade, homogeneidade de variâncias)
- Use gráficos diagnósticos (Q-Q plots, histogramas, boxplots)
- Considere testes não-paramétricos quando pressupostos violados

**Interpretação**:
- Reporte sempre o tamanho do efeito (d de Cohen, η², r)
- Use intervalos de confiança complementando testes
- Considere significância prática, não apenas estatística
- Seja transparente sobre múltiplos testes e correções aplicadas

**Comunicação**:
- Reporte estatísticas de teste, p-valores e intervalos de confiança
- Descreva os pressupostos verificados
- Explique o significado prático dos resultados
- Reconheça limitações do estudo

### **⚠️ Cuidados e Limitações**

**Erros Comuns**:
- Valor-p **não** indica probabilidade da hipótese ser verdadeira
- Significância estatística **≠** importância prática
- "Não rejeitar H₀" **≠** "aceitar H₀" (ausência de evidência ≠ evidência de ausência)
- Amostras grandes podem detectar diferenças triviais como "significativas"

**Problemas de Interpretação**:
- p = 0.049 e p = 0.051 não são qualitativamente diferentes
- α = 0.05 é convenção, não lei da natureza
- Um único estudo raramente é conclusivo

**Questões Metodológicas**:
- Múltiplos testes aumentam probabilidade de erro tipo I
- P-hacking e cherry-picking comprometem validade
- Poder estatístico baixo leva a estudos inconclusivos
- Violação de pressupostos pode invalidar resultados

### **🎯 Recomendações Avançadas**

**Abordagens Complementares**:
- Combine testes de hipóteses com análise exploratória de dados (EDA)
- Use métodos de reamostragem (bootstrap, permutação) para validação
- Considere métodos Bayesianos para inferência mais intuitiva
- Aplique meta-análise para sintetizar múltiplos estudos

**Melhores Práticas Modernas**:
- Pré-registro de estudos para evitar viés de publicação
- Reporte de todos os testes realizados, não apenas significativos
- Compartilhamento de dados e código para reprodutibilidade
- Estimação de incerteza com intervalos de confiança

**Alternativas e Extensões**:
- **Inferência Bayesiana**: Incorpora conhecimento prévio, mais intuitiva
- **Equivalence Testing**: Testa se diferença é negligenciável
- **Permutation Tests**: Não assume distribuição paramétrica
- **Bootstrap**: Estimação de IC quando teoria assintótica não se aplica

### **📊 Comparação: Frequentista vs. Bayesiano**

| Aspecto | Frequentista | Bayesiano |
|---------|--------------|-----------|
| **Parâmetros** | Fixos e desconhecidos | Variáveis aleatórias |
| **Probabilidade** | Frequência de longo prazo | Grau de crença |
| **Inferência** | p-valor, IC | Distribuição posterior |
| **Conhecimento prévio** | Não incorpora | Incorpora via prior |
| **Interpretação** | Menos intuitiva | Mais intuitiva |
| **Computação** | Geralmente mais simples | Pode ser intensiva |

### **🔬 Contexto Científico Atual**

A comunidade científica tem debatido intensamente o uso e abuso dos testes de hipóteses. A American Statistical Association (ASA) publicou em 2016 uma declaração sobre p-valores, destacando:

1. P-valores podem indicar incompatibilidade entre dados e modelo, mas não medem o tamanho do efeito
2. P-valores não medem a probabilidade da hipótese ser verdadeira
3. Conclusões científicas não devem se basear apenas em cruzar um limiar de significância
4. Inferência apropriada requer relatório completo e transparência

**Movimento pela Ciência Aberta**:
- Pré-registro de hipóteses e análises
- Compartilhamento de dados brutos
- Código aberto para reprodutibilidade
- Relatório de todos os resultados (não apenas significativos)

### **💡 Direções Futuras**

O campo continua evoluindo com:
- **Machine Learning**: Integração com métodos de aprendizado de máquina
- **Big Data**: Adaptação para grandes volumes de dados
- **Computação**: Métodos computacionalmente intensivos (MCMC, bootstrap)
- **Causalidade**: Foco em inferência causal, não apenas associação

---

## **Referências Acadêmicas**

### **Livros Fundamentais**

**MONTGOMERY, Douglas C.; RUNGER, George C.** *Applied Statistics and Probability for Engineers*. 7. ed. Hoboken: Wiley, 2018.
- Abordagem aplicada com foco em engenharia e ciências aplicadas

**FIELD, Andy.** *Discovering Statistics Using IBM SPSS Statistics*. 5. ed. London: SAGE Publications, 2018.
- Excelente introdução com humor e exemplos práticos

**COHEN, Jacob.** *Statistical Power Analysis for the Behavioral Sciences*. 2. ed. Hillsdale: Lawrence Erlbaum Associates, 1988.
- Referência clássica sobre poder estatístico e tamanho do efeito

**CASELLA, George; BERGER, Roger L.** *Statistical Inference*. 2. ed. Pacific Grove: Duxbury, 2002.
- Tratamento matemático rigoroso da inferência estatística

**LEHMANN, Erich L.; ROMANO, Joseph P.** *Testing Statistical Hypotheses*. 3. ed. New York: Springer, 2005.
- Teoria completa e avançada de testes de hipóteses

### **Artigos Importantes**

**WASSERSTEIN, Ronald L.; LAZAR, Nicole A.** The ASA Statement on p-Values: Context, Process, and Purpose. *The American Statistician*, v. 70, n. 2, p. 129-133, 2016.
- Declaração oficial da ASA sobre uso correto de p-valores

**IOANNIDIS, John P. A.** Why Most Published Research Findings Are False. *PLOS Medicine*, v. 2, n. 8, e124, 2005.
- Análise crítica sobre vieses em pesquisa científica

**COHEN, Jacob.** The Earth is Round (p < .05). *American Psychologist*, v. 49, n. 12, p. 997-1003, 1994.
- Crítica ao uso mecânico de testes de significância

**GIGERENZER, Gerd.** Mindless Statistics. *Journal of Socio-Economics*, v. 33, n. 5, p. 587-606, 2004.
- Discussão sobre interpretação errônea de estatísticas

**BENJAMIN, Daniel J. et al.** Redefine Statistical Significance. *Nature Human Behaviour*, v. 2, n. 1, p. 6-10, 2018.
- Proposta controversa de redefinir limiar de significância para α = 0.005 (não amplamente adotada)

### **Recursos Online**

**STERNE, Jonathan A. C.; SMITH, George D.** Sifting the evidence—what's wrong with significance tests? *BMJ*, v. 322, p. 226-231, 2001.
- Disponível em: https://www.bmj.com/content/322/7280/226

**GOODMAN, Steven N.** Toward Evidence-Based Medical Statistics. 1: The P Value Fallacy. *Annals of Internal Medicine*, v. 130, n. 12, p. 995-1004, 1999.
- Discussão sobre falácias na interpretação de p-valores

**NUZZO, Regina.** Statistical Errors. *Nature*, v. 506, p. 150-152, 2014.
- Artigo acessível sobre erros comuns em estatística

### **Documentação de Software**

**SciPy Statistical Functions**: https://docs.scipy.org/doc/scipy/reference/stats.html
- Documentação oficial da biblioteca scipy.stats do Python

**Statsmodels**: https://www.statsmodels.org/stable/index.html
- Biblioteca Python para modelos estatísticos e testes

**Pingouin**: https://pingouin-stats.org/
- Biblioteca Python moderna para estatística