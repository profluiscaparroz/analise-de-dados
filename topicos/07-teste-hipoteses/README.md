# **Teste de Hipóteses: Fundamentos e Aplicações**

O **teste de hipóteses** é uma metodologia estatística fundamental para tomar decisões baseadas em dados. Permite avaliar se uma afirmação (hipótese) sobre uma população é suportada pela evidência disponível em uma amostra.

## Sumário

1. [Conceitos Fundamentais](#conceitos-fundamentais)
2. [Estrutura de um Teste de Hipóteses](#estrutura-de-um-teste-de-hipóteses)
3. [Tipos de Erro](#tipos-de-erro)
4. [Principais Testes Estatísticos](#principais-testes-estatísticos)
5. [Valor-p e Significância Estatística](#valor-p-e-significância-estatística)
6. [Tamanho do Efeito e Poder Estatístico](#tamanho-do-efeito-e-poder-estatístico)
7. [Exemplos Práticos](#exemplos-práticos)

---

## **Conceitos Fundamentais**

### **O que é um Teste de Hipóteses?**

Um teste de hipóteses é um procedimento que usa dados amostrais para avaliar a plausibilidade de uma hipótese sobre um parâmetro populacional. O objetivo é determinar se há evidência suficiente para rejeitar uma afirmação inicial (hipótese nula) em favor de uma alternativa.

### **Por que Testar Hipóteses?**

- **Validar teorias**: Verificar se dados suportam teorias científicas
- **Tomar decisões**: Decidir entre diferentes cursos de ação
- **Controlar qualidade**: Verificar se processos atendem especificações
- **Avaliar tratamentos**: Determinar eficácia de medicamentos ou intervenções

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

### **Exemplos de Formulação**

**Exemplo 1: Teste de Média**
- H₀: μ = 100 (a média populacional é 100)
- H₁: μ ≠ 100 (a média populacional é diferente de 100)

**Exemplo 2: Comparação de Grupos**
- H₀: μ₁ = μ₂ (as médias dos dois grupos são iguais)
- H₁: μ₁ ≠ μ₂ (as médias dos dois grupos são diferentes)

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
- Se p-valor > α: **Não rejeitamos H₀**

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
```

---

## **Conclusão**

O teste de hipóteses é uma ferramenta poderosa para tomada de decisões baseada em dados. Pontos importantes:

### **✅ Boas Práticas**
- Formule hipóteses antes de ver os dados
- Verifique pressupostos dos testes
- Reporte sempre o tamanho do efeito
- Considere significância prática, não apenas estatística
- Use intervalos de confiança complementando testes

### **⚠️ Cuidados**
- Valor-p não indica probabilidade da hipótese ser verdadeira
- Significância estatística ≠ importância prática
- Múltiplos testes aumentam probabilidade de erro tipo I
- Amostras grandes podem detectar diferenças triviais

### **🎯 Recomendações**
- Combine testes de hipóteses com análise exploratória
- Considere métodos Bayesianos para problemas complexos
- Sempre avalie poder estatístico e tamanho da amostra
- Documente e justifique escolhas metodológicas

---

## **Referências**

**MONTGOMERY, Douglas C.; RUNGER, George C.** *Applied Statistics and Probability for Engineers*. 7. ed. Hoboken: Wiley, 2018.

**FIELD, Andy.** *Discovering Statistics Using IBM SPSS Statistics*. 5. ed. London: SAGE Publications, 2018.

**WASSERSTEIN, Ronald L.; LAZAR, Nicole A.** The ASA Statement on p-Values: Context, Process, and Purpose. *The American Statistician*, v. 70, n. 2, p. 129-133, 2016.

**COHEN, Jacob.** Statistical Power Analysis for the Behavioral Sciences. 2. ed. Hillsdale: Lawrence Erlbaum Associates, 1988.