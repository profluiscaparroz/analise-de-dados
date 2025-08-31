# **Qualidade de Dados: Fundamentos e Metodologias de Validação**

A **qualidade de dados** é um aspecto fundamental na análise de dados que determina a confiabilidade, precisão e utilidade dos insights extraídos. Dados de baixa qualidade podem levar a conclusões incorretas e decisões prejudiciais para organizações e projetos.

## Sumário

1. [O que é Qualidade de Dados](#o-que-é-qualidade-de-dados)
2. [Dimensões da Qualidade de Dados](#dimensões-da-qualidade-de-dados)
3. [Problemas Comuns de Qualidade](#problemas-comuns-de-qualidade)
4. [Técnicas de Validação de Dados](#técnicas-de-validação-de-dados)
5. [Processo de Limpeza de Dados](#processo-de-limpeza-de-dados)
6. [Ferramentas e Metodologias](#ferramentas-e-metodologias)
7. [Exemplos Práticos](#exemplos-práticos)

---

## **O que é Qualidade de Dados**

Qualidade de dados refere-se ao grau em que os dados atendem aos requisitos para seu uso pretendido. Dados de alta qualidade são:

- **Precisos**: Refletem corretamente a realidade
- **Completos**: Contêm todas as informações necessárias
- **Consistentes**: Não contêm contradições
- **Confiáveis**: Podem ser utilizados com segurança para tomada de decisões
- **Atualizados**: Representam o estado atual das informações

### 📊 **Impacto da Qualidade dos Dados**

Segundo estudos da IBM, dados de baixa qualidade custam à economia americana aproximadamente **3,1 trilhões de dólares por ano**. Os impactos incluem:

- Decisões incorretas baseadas em informações imprecisas
- Perda de confiança do cliente
- Ineficiências operacionais
- Custos adicionais de correção
- Riscos de conformidade regulatória

---

## **Dimensões da Qualidade de Dados**

### **1. Precisão (Accuracy)**
Os dados representam corretamente o objeto ou evento real.

**Exemplo**: Um cliente cadastrado com idade de 150 anos indica problema de precisão.

### **2. Completude (Completeness)**
Todos os dados necessários estão presentes.

**Exemplo**: Tabela de vendas onde 30% dos registros não têm informação de região.

### **3. Consistência (Consistency)**
Os dados não contêm contradições internas ou com outras fontes.

**Exemplo**: Cliente com data de nascimento posterior à data de primeiro pedido.

### **4. Integridade (Integrity)**
Os dados seguem regras de negócio e restrições definidas.

**Exemplo**: Código de produto que não existe na tabela de produtos.

### **5. Validade (Validity)**
Os dados seguem formatos e regras sintáticas definidas.

**Exemplo**: Campo de email com valor "abc123" ao invés de um email válido.

### **6. Atualidade (Timeliness)**
Os dados são atuais e relevantes para o momento de uso.

**Exemplo**: Preços de produtos que não foram atualizados há meses.

### **7. Unicidade (Uniqueness)**
Não há duplicação desnecessária de dados.

**Exemplo**: Mesmo cliente cadastrado múltiplas vezes com grafias ligeiramente diferentes.

---

## **Problemas Comuns de Qualidade**

### **🔴 Dados Ausentes (Missing Data)**

**Tipos de dados ausentes**:
- **MCAR** (Missing Completely at Random): Ausência aleatória
- **MAR** (Missing at Random): Ausência relacionada a outras variáveis observadas
- **NMAR** (Not Missing at Random): Ausência relacionada ao próprio valor não observado

**Estratégias de tratamento**:
- Remoção de registros incompletos
- Imputação com média/mediana/moda
- Imputação múltipla
- Algoritmos específicos para dados ausentes

### **🔴 Outliers e Valores Anômalos**

**Identificação**:
- Análise visual (box plots, histogramas)
- Regra do IQR (Intervalo Interquartil)
- Z-score (valores > 3 desvios padrão)
- Métodos estatísticos avançados

**Tratamento**:
- Remoção (se confirmadamente erro)
- Transformação (log, raiz quadrada)
- Winsorização (substituição por percentis)
- Manutenção (se representam fenômenos reais)

### **🔴 Inconsistências e Duplicatas**

**Exemplos comuns**:
- Variações na grafia de nomes
- Diferentes formatos de data/hora
- Unidades de medida inconsistentes
- Registros duplicados com pequenas variações

---

## **Técnicas de Validação de Dados**

### **1. Validação Sintática**
Verifica se os dados seguem formatos esperados.

```python
import re

def validar_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = re.sub(r'[^0-9]', '', cpf)
    return len(cpf) == 11 and not cpf == cpf[0] * 11
```

### **2. Validação Semântica**
Verifica se os dados fazem sentido no contexto.

```python
from datetime import datetime, date

def validar_idade(data_nascimento):
    hoje = date.today()
    idade = hoje.year - data_nascimento.year
    return 0 <= idade <= 120

def validar_salario(salario, cargo):
    # Faixas salariais por cargo
    faixas = {
        'estagiario': (800, 2000),
        'junior': (2000, 5000),
        'senior': (5000, 15000),
        'gerente': (8000, 25000)
    }
    
    if cargo.lower() in faixas:
        min_sal, max_sal = faixas[cargo.lower()]
        return min_sal <= salario <= max_sal
    return True  # Se cargo não conhecido, aceita
```

### **3. Validação de Referências**
Verifica integridade referencial entre tabelas.

```python
def validar_integridade_referencial(df_vendas, df_produtos):
    # Verifica se todos os produtos em vendas existem na tabela de produtos
    produtos_invalidos = df_vendas[
        ~df_vendas['produto_id'].isin(df_produtos['id'])
    ]
    return len(produtos_invalidos) == 0, produtos_invalidos
```

---

## **Processo de Limpeza de Dados**

### **Etapa 1: Profiling dos Dados**
Análise inicial para entender a estrutura e qualidade.

```python
import pandas as pd
import numpy as np

def profile_dataframe(df):
    print("=== PROFILING DE DADOS ===")
    print(f"Dimensões: {df.shape}")
    print(f"\nTipos de dados:")
    print(df.dtypes)
    print(f"\nValores ausentes:")
    print(df.isnull().sum())
    print(f"\nValores únicos por coluna:")
    print(df.nunique())
    print(f"\nEstatísticas descritivas:")
    print(df.describe())
```

### **Etapa 2: Identificação de Problemas**

```python
def identificar_problemas(df):
    problemas = []
    
    # Verificar dados ausentes
    colunas_com_nulos = df.columns[df.isnull().any()].tolist()
    if colunas_com_nulos:
        problemas.append(f"Colunas com valores ausentes: {colunas_com_nulos}")
    
    # Verificar duplicatas
    duplicatas = df.duplicated().sum()
    if duplicatas > 0:
        problemas.append(f"Registros duplicados: {duplicatas}")
    
    # Verificar outliers (para colunas numéricas)
    for col in df.select_dtypes(include=[np.number]).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)][col].count()
        if outliers > 0:
            problemas.append(f"Outliers em {col}: {outliers}")
    
    return problemas
```

### **Etapa 3: Correção e Limpeza**

```python
def limpar_dados(df):
    df_limpo = df.copy()
    
    # Remover duplicatas
    df_limpo = df_limpo.drop_duplicates()
    
    # Padronizar texto
    for col in df_limpo.select_dtypes(include=['object']).columns:
        df_limpo[col] = df_limpo[col].astype(str).str.strip().str.lower()
    
    # Tratar valores ausentes
    for col in df_limpo.columns:
        if df_limpo[col].dtype in ['int64', 'float64']:
            # Para numéricos: preencher com mediana
            df_limpo[col].fillna(df_limpo[col].median(), inplace=True)
        else:
            # Para categóricos: preencher com moda
            df_limpo[col].fillna(df_limpo[col].mode()[0] if not df_limpo[col].mode().empty else 'N/A', inplace=True)
    
    return df_limpo
```

---

## **Ferramentas e Metodologias**

### **Ferramentas Open Source**
- **pandas (Python)**: Manipulação e limpeza de dados
- **Great Expectations (Python)**: Framework para validação de dados
- **Deequ (Scala/Python)**: Biblioteca da Amazon para qualidade de dados
- **OpenRefine**: Ferramenta visual para limpeza de dados

### **Ferramentas Comerciais**
- **Talend Data Quality**: Plataforma completa de qualidade de dados
- **IBM InfoSphere QualityStage**: Solução enterprise
- **Microsoft Data Quality Services**: Integrado ao SQL Server
- **Dataiku**: Plataforma de ciência de dados com foco em qualidade

### **Metodologias**
- **TDQM** (Total Data Quality Management): Abordagem holística
- **DAMA-DMBOK**: Framework de gestão de dados
- **ISO 8000**: Padrão internacional para qualidade de dados

---

## **Exemplos Práticos**

### **Exemplo 1: Validação de Dataset de Vendas**

```python
import pandas as pd
from datetime import datetime

# Carregar dados
df_vendas = pd.read_csv('vendas.csv')

# Funções de validação
def validar_vendas(df):
    erros = []
    
    # Validar se valor_venda é positivo
    if (df['valor_venda'] <= 0).any():
        erros.append("Encontrados valores de venda negativos ou zero")
    
    # Validar se data_venda não é futura
    df['data_venda'] = pd.to_datetime(df['data_venda'])
    if (df['data_venda'] > datetime.now()).any():
        erros.append("Encontradas datas de venda futuras")
    
    # Validar se quantidade é inteira e positiva
    if (df['quantidade'] <= 0).any() or (df['quantidade'] != df['quantidade'].astype(int)).any():
        erros.append("Quantidades inválidas encontradas")
    
    return erros

# Executar validação
erros_encontrados = validar_vendas(df_vendas)
for erro in erros_encontrados:
    print(f"❌ {erro}")
```

### **Exemplo 2: Detecção de Duplicatas Inteligente**

```python
from fuzzywuzzy import fuzz

def detectar_duplicatas_fuzzy(df, coluna_nome, threshold=85):
    """Detecta duplicatas usando similaridade de strings"""
    duplicatas_potenciais = []
    
    for i, nome1 in enumerate(df[coluna_nome]):
        for j, nome2 in enumerate(df[coluna_nome]):
            if i < j:  # Evitar comparar o mesmo registro
                similaridade = fuzz.ratio(str(nome1).lower(), str(nome2).lower())
                if similaridade >= threshold:
                    duplicatas_potenciais.append({
                        'index1': i,
                        'index2': j,
                        'nome1': nome1,
                        'nome2': nome2,
                        'similaridade': similaridade
                    })
    
    return duplicatas_potenciais

# Exemplo de uso
df_clientes = pd.DataFrame({
    'nome': ['João Silva', 'Joao Silva', 'Maria Santos', 'Pedro Oliveira']
})

duplicatas = detectar_duplicatas_fuzzy(df_clientes, 'nome')
for dup in duplicatas:
    print(f"Possível duplicata: '{dup['nome1']}' vs '{dup['nome2']}' (Similaridade: {dup['similaridade']}%)")
```

---

## **Conclusão**

A qualidade de dados é fundamental para o sucesso de qualquer projeto de análise de dados. Um processo bem estruturado de validação e limpeza de dados deve incluir:

1. **Avaliação inicial** dos dados (profiling)
2. **Identificação** de problemas de qualidade
3. **Implementação** de regras de validação
4. **Correção** de problemas identificados
5. **Monitoramento** contínuo da qualidade

**Princípios importantes**:
- **Prevenção é melhor que correção**: Implemente validações na entrada de dados
- **Documente tudo**: Mantenha registro das regras de limpeza aplicadas
- **Mantenha dados originais**: Sempre preserve uma cópia dos dados brutos
- **Monitore continuamente**: A qualidade de dados é um processo, não um evento único

Investir em qualidade de dados é investir na confiabilidade e valor dos insights gerados pela análise de dados.

---

## **Referências**

**REDMAN, Thomas C.** *Data Driven: Creating a Data Culture*. Boston: Harvard Business Review Press, 2020.

**LOSHIN, David.** *Master Data Management*. Burlington: Morgan Kaufmann, 2009.

**SEBASTIAN-COLEMAN, Laura.** *Measuring Data Quality for Ongoing Improvement*. Burlington: Morgan Kaufmann, 2012.

**WANG, Richard Y.; STRONG, Diane M.** Beyond Accuracy: What Data Quality Means to Data Consumers. *Journal of Management Information Systems*, v. 12, n. 4, p. 5-33, 1996.