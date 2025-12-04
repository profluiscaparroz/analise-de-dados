# **Distribuição de Frequência: Organizando Dados para Iniciantes**

## **🎯 O que você vai aprender?**

Você vai descobrir como **organizar dados bagunçados** em tabelas organizadas que revelam padrões interessantes. É como arrumar sua gaveta de meias por cores e tamanhos - depois fica muito mais fácil encontrar o que você precisa!

**💡 Por que isso é útil?**
- **Identificar padrões** que não conseguimos ver nos dados "soltos"
- **Comparar categorias** de forma visual
- **Contar frequências** para tomar decisões
- **Criar gráficos** informativos

---

## **🤔 O que é Distribuição de Frequência?**

É uma **tabela organizadinha** que mostra:
- **Quantas vezes** cada valor (ou grupo de valores) aparece nos seus dados
- **Qual categoria** é mais comum
- **Como os dados se distribuem** pelo conjunto

**🏫 Exemplo Simples - Idades de uma Turma:**

Idades dos alunos (dados "bagunçados"):
```
18, 22, 19, 22, 18, 20, 21, 19, 20, 18, 23, 21, 20, 22, 19
```

**📋 Organizando em uma tabela:**

| Idade | Quantas Vezes Aparece | Porcentagem |
|-------|----------------------|-------------|
| 18    | 3 vezes             | 20%         |
| 19    | 3 vezes             | 20%         |
| 20    | 3 vezes             | 20%         |
| 21    | 2 vezes             | 13.3%       |
| 22    | 3 vezes             | 20%         |
| 23    | 1 vez               | 6.7%        |
| **Total** | **15 alunos**   | **100%**    |

**📊 O que descobrimos:**
- A maioria dos alunos tem entre **18-22 anos**
- **23 anos** é menos comum (apenas 1 aluno)
- As idades **18, 19, 20 e 22** são igualmente populares

---

## **📊 Tipos de Frequência (Explicação Simples)**

### **1. Frequência Absoluta - "Quantas Vezes"**
É simplesmente **quantas vezes** cada valor aparece.

**Exemplo:** Se temos as notas `7, 8, 7, 9, 7`, a nota 7 tem frequência absoluta de **3**.

### **2. Frequência Relativa - "Que Porcentagem"**
É a **porcentagem** que cada valor representa do total.

**🔢 Como calcular:**
```
Frequência Relativa = (Quantas vezes aparece ÷ Total de dados) × 100
```

**Exemplo:** Nota 7 aparece 3 vezes de 5 total = `(3 ÷ 5) × 100 = 60%`

### **3. Frequência Acumulada - "Até Aqui"**
Mostra **quantos dados** existem até determinado ponto.

**Exemplo com idades:**

| Idade | Freq. Absoluta | Freq. Acumulada |
|-------|---------------|-----------------|
| 18    | 3             | 3               |
| 19    | 3             | 6 (3+3)         |
| 20    | 3             | 9 (6+3)         |
| 21    | 2             | 11 (9+2)        |
| 22    | 3             | 14 (11+3)       |
| 23    | 1             | 15 (14+1)       |

**📊 Interpretação:**
- **9 alunos** têm 20 anos ou menos
- **14 alunos** têm 22 anos ou menos

---

## **🛠️ Como Criar uma Distribuição de Frequência (Passo a Passo)**

### **📝 Exemplo Prático: Notas de uma Prova**

Notas da turma (0-10):
```
6.5, 7.0, 8.5, 6.0, 9.0, 7.5, 8.0, 6.5, 9.5, 7.0, 8.0, 7.5, 6.0, 8.5, 9.0
```

### **Passo 1: Organize os Dados**
```
6.0, 6.0, 6.5, 6.5, 7.0, 7.0, 7.5, 7.5, 8.0, 8.0, 8.5, 8.5, 9.0, 9.0, 9.5
```

### **Passo 2: Conte as Frequências**

| Nota | Contagem | Freq. Absoluta |
|------|----------|----------------|
| 6.0  | ✓✓       | 2              |
| 6.5  | ✓✓       | 2              |
| 7.0  | ✓✓       | 2              |
| 7.5  | ✓✓       | 2              |
| 8.0  | ✓✓       | 2              |
| 8.5  | ✓✓       | 2              |
| 9.0  | ✓✓       | 2              |
| 9.5  | ✓        | 1              |

### **Passo 3: Calcule as Porcentagens**

| Nota | Freq. Absoluta | Freq. Relativa | Porcentagem |
|------|---------------|---------------|-------------|
| 6.0  | 2             | 2/15 = 0.133  | 13.3%       |
| 6.5  | 2             | 2/15 = 0.133  | 13.3%       |
| 7.0  | 2             | 2/15 = 0.133  | 13.3%       |
| 7.5  | 2             | 2/15 = 0.133  | 13.3%       |
| 8.0  | 2             | 2/15 = 0.133  | 13.3%       |
| 8.5  | 2             | 2/15 = 0.133  | 13.3%       |
| 9.0  | 2             | 2/15 = 0.133  | 13.3%       |
| 9.5  | 1             | 1/15 = 0.067  | 6.7%        |
| **Total** | **15**    | **1.000**     | **100%**    |

### **Passo 4: Interprete os Resultados**

**📊 O que descobrimos:**
- As notas estão **bem distribuídas** (quase todas têm a mesma frequência)
- Apenas **6.7%** tiraram a nota máxima (9.5)
- **Não há padrão claro** - turma heterogênea

---

## **🏢 Exemplo com Intervalos - Salários de uma Empresa**

Quando temos **muitos valores diferentes**, é melhor agrupá-los em **intervalos**.

### **Salários (em R$):**
```
2.500, 2.800, 3.200, 3.500, 3.800, 4.200, 4.500, 5.000, 5.500, 
6.000, 6.800, 7.200, 8.000, 9.500, 12.000
```

### **Organizando em Intervalos:**

| Faixa Salarial | Freq. Absoluta | Freq. Relativa | Porcentagem |
|----------------|---------------|---------------|-------------|
| R$ 2.000-4.000 | 5             | 5/15 = 0.33   | 33.3%       |
| R$ 4.000-6.000 | 4             | 4/15 = 0.27   | 26.7%       |
| R$ 6.000-8.000 | 3             | 3/15 = 0.20   | 20.0%       |
| R$ 8.000-12.000| 3             | 3/15 = 0.20   | 20.0%       |
| **Total**      | **15**        | **1.00**      | **100%**    |

### **📊 Insights para o RH:**
- **1/3 dos funcionários** ganha até R$ 4.000
- **60% dos funcionários** ganha até R$ 6.000  
- **20% dos funcionários** ganha mais de R$ 8.000
- Pode indicar necessidade de **reajustes** na faixa baixa

---

## **🎨 Transformando em Gráficos**

### **📊 Gráfico de Barras - Preferência de Cores**

Cores preferidas em uma pesquisa:
```
Azul, Verde, Azul, Vermelho, Azul, Verde, Amarelo, Azul, Verde, Vermelho
```

**Tabela:**
| Cor      | Frequência | Porcentagem |
|----------|------------|-------------|
| Azul     | 4          | 40%         |
| Verde    | 3          | 30%         |
| Vermelho | 2          | 20%         |
| Amarelo  | 1          | 10%         |

**📈 No gráfico de barras:**
- **Azul** teria a barra mais alta (40%)
- **Amarelo** teria a barra mais baixa (10%)
- **Fácil visualizar** qual cor é mais popular!

---

## **💡 Dicas Práticas**

### **✅ Do's (Faça):**
- **Organize os dados** antes de contar
- **Use intervalos** quando há muitos valores diferentes
- **Calcule porcentagens** para facilitar comparações
- **Dê títulos descritivos** às suas tabelas

### **❌ Don'ts (Não faça):**
- **Não misture** diferentes tipos de dados
- **Não esqueça** de incluir todos os dados
- **Não crie intervalos** muito pequenos ou muito grandes
- **Não se esqueça** de verificar se as porcentagens somam 100%

### **🌟 Quando Usar Distribuição de Frequência:**
- **Pesquisas de opinião** (qual produto prefere?)
- **Análise de vendas** (quais produtos vendem mais?)
- **Estudos demográficos** (distribuição de idades)
- **Controle de qualidade** (quantos defeitos por categoria?)
- **Análise acadêmica** (distribuição de notas)

---

**🎉 Parabéns! Agora você sabe organizar dados de forma profissional!**

Com essa habilidade você pode:
✅ **Identificar padrões** nos seus dados  
✅ **Criar relatórios** organizados  
✅ **Tomar decisões** baseadas em frequências  
✅ **Preparar dados** para gráficos  
✅ **Apresentar informações** de forma clara
