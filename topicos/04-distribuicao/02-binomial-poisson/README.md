# **Distribuições Binomial e Poisson: Guia Introdutório**

## **História do Usuário (BDD)**

**Como estudante de estatística**  
**Quero ter um guia introdutório sobre distribuições Binomial e Poisson**  
**Para que eu compreenda rapidamente os conceitos principais e suas aplicações práticas**

---

## Sumário

1. [Distribuição Binomial](#distribuição-binomial)
2. [Distribuição de Poisson](#distribuição-de-poisson)  
3. [Comparação entre as Distribuições](#comparação-entre-as-distribuições)
4. [Aplicações Práticas](#aplicações-práticas)
5. [Exemplos com Python](#exemplos-com-python)

---

# **Distribuição Binomial**

## **O que é?**

A distribuição binomial modela situações onde realizamos **n experimentos independentes**, cada um com apenas **dois resultados possíveis** (sucesso ou fracasso) e **probabilidade constante** de sucesso.

### **Condições Necessárias**
- **Independência**: o resultado de cada tentativa não influencia as outras
- **Probabilidade constante**: a chance de sucesso é sempre a mesma (p)
- **Número fixo de tentativas**: sempre n experimentos

### **Exemplos do Dia a Dia**
- 🪙 Lançar uma moeda 10 vezes e contar quantas "caras" saem
- 🔧 Testar 20 componentes eletrônicos e contar quantos funcionam
- 📊 Perguntar a 100 pessoas se aprovam um produto

### **Fórmula Básica**

$$P(X = k) = \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}$$

**Onde:**
- **n** = número total de tentativas
- **k** = número de sucessos desejados  
- **p** = probabilidade de sucesso em cada tentativa
- $\binom{n}{k}$ = combinação de n elementos tomados k a k

### **Propriedades Importantes**
- **Média**: μ = n × p
- **Variância**: σ² = n × p × (1-p)
- **Desvio Padrão**: σ = √[n × p × (1-p)]

### **Exemplo Simples**

**Problema**: Em uma prova de 5 questões de múltipla escolha (4 alternativas cada), qual a probabilidade de acertar exatamente 2 questões "no chute"?

**Solução**:
- n = 5 (5 questões)
- k = 2 (queremos 2 acertos)  
- p = 0.25 (chance de acertar = 1/4)

$$P(X = 2) = \binom{5}{2} \cdot (0.25)^2 \cdot (0.75)^3 = 10 \cdot 0.0625 \cdot 0.421875 = 0.2637$$

**Resposta**: 26,37% de chance

---

# **Distribuição de Poisson**

## **O que é?**

A distribuição de Poisson modela o **número de eventos que ocorrem em um intervalo fixo** (tempo ou espaço), quando esses eventos são **raros** e **independentes**, com uma **taxa média constante**.

### **Quando Usar?**
- Os eventos são **independentes** entre si
- A **taxa média** de ocorrências é **constante**  
- Os eventos são **raros** em relação ao período observado
- O período/espaço observado é **fixo**

### **Exemplos do Dia a Dia**
- 📧 Número de emails recebidos por hora
- 🚗 Acidentes de trânsito por dia em uma cidade
- 📞 Chamadas telefônicas por minuto em um call center
- ⭐ Estrelas cadentes vistas por noite

### **Fórmula Básica**

$$P(X = k) = \frac{\lambda^k \cdot e^{-\lambda}}{k!}$$

**Onde:**
- **k** = número de eventos que queremos calcular (0, 1, 2, 3...)
- **λ (lambda)** = taxa média de eventos por período
- **e** = número de Euler (≈ 2.71828)
- **k!** = fatorial de k

### **Propriedades Importantes**
- **Média**: μ = λ
- **Variância**: σ² = λ  
- **Desvio Padrão**: σ = √λ

### **Exemplo Simples**

**Problema**: Um call center recebe em média 4 chamadas por minuto. Qual a probabilidade de receber exatamente 6 chamadas em 1 minuto?

**Solução**:
- λ = 4 (média de 4 chamadas por minuto)
- k = 6 (queremos exatamente 6 chamadas)

$$P(X = 6) = \frac{4^6 \cdot e^{-4}}{6!} = \frac{4096 \cdot 0.0183}{720} = 0.1042$$

**Resposta**: 10,42% de chance

---

# **Comparação entre as Distribuições**

| Aspecto | Binomial | Poisson |
|---------|----------|---------|
| **Tipo de experimento** | n tentativas fixas | Eventos em intervalo contínuo |
| **Resultado** | Sucesso/Fracasso | Contagem de eventos raros |
| **Parâmetros** | n (tentativas) e p (probabilidade) | λ (taxa média) |
| **Média** | n × p | λ |
| **Variância** | n × p × (1-p) | λ |
| **Quando usar** | Experimentos com resultado binário | Contagem de eventos raros |

### **Relação Especial**
Quando **n é grande** e **p é pequeno** (n×p ≈ λ), a **Binomial se aproxima da Poisson**!

---

# **Aplicações Práticas**

## **Distribuição Binomial**
- 📊 **Controle de Qualidade**: Testar lotes de produtos e contar defeitos
- 📈 **Marketing**: Análise de conversão em campanhas (clica/não clica)
- 🏥 **Medicina**: Eficácia de tratamentos (melhora/não melhora)
- 🎯 **A/B Testing**: Comparar versões de sites ou aplicativos

## **Distribuição de Poisson**  
- 🚨 **Segurança**: Modelar acidentes, falhas de sistema, ataques cibernéticos
- 📞 **Telecomunicações**: Dimensionar centrais telefônicas e call centers
- 🛒 **Varejo**: Prever demanda e otimizar estoques
- 🚑 **Saúde Pública**: Monitorar surtos de doenças raras

---

# **Exemplos com Python**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson

# Configuração dos gráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# DISTRIBUIÇÃO BINOMIAL
# Exemplo: 10 lançamentos de moeda (p = 0.5)
n, p = 10, 0.5
x_binom = np.arange(0, n+1)
pmf_binom = binom.pmf(x_binom, n, p)

ax1.bar(x_binom, pmf_binom, alpha=0.7, color='blue')
ax1.set_title('Distribuição Binomial\n(n=10, p=0.5)')
ax1.set_xlabel('Número de sucessos (k)')
ax1.set_ylabel('Probabilidade')
ax1.grid(True, alpha=0.3)

# DISTRIBUIÇÃO POISSON
# Exemplo: 4 eventos por período em média
lam = 4
x_poisson = np.arange(0, 15)
pmf_poisson = poisson.pmf(x_poisson, lam)

ax2.bar(x_poisson, pmf_poisson, alpha=0.7, color='red')
ax2.set_title('Distribuição Poisson\n(λ=4)')
ax2.set_xlabel('Número de eventos (k)')
ax2.set_ylabel('Probabilidade')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Calculando probabilidades específicas
print("=== BINOMIAL ===")
print(f"P(X = 5) = {binom.pmf(5, n, p):.4f}")
print(f"Média: {binom.mean(n, p)}")
print(f"Variância: {binom.var(n, p)}")

print("\n=== POISSON ===")
print(f"P(X = 4) = {poisson.pmf(4, lam):.4f}")
print(f"Média: {poisson.mean(lam)}")
print(f"Variância: {poisson.var(lam)}")
```

### **Instalação das Dependências**

```bash
pip install numpy matplotlib scipy
```

---

## **🧠 Resumo Executivo**

### **Use Binomial quando:**
- ✅ Tem um número **fixo de tentativas** (n)
- ✅ Cada tentativa tem **dois resultados** possíveis
- ✅ Probabilidade é **constante** em todas as tentativas
- ✅ Tentativas são **independentes**

### **Use Poisson quando:**
- ✅ Quer contar **eventos raros** em um período
- ✅ Taxa média é **conhecida e constante**  
- ✅ Eventos são **independentes**
- ✅ O período observado é **fixo**

### **Fórmulas para Memorizar**

**Binomial**: $P(X = k) = \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}$

**Poisson**: $P(X = k) = \frac{\lambda^k \cdot e^{-\lambda}}{k!}$

---

*Esse guia apresenta os conceitos fundamentais de forma resumida. Para análises mais detalhadas e exemplos adicionais, consulte a literatura especializada em probabilidade e estatística.*