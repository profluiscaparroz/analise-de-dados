

# **Lista de Símbolos Matemáticos e Estatísticos**

## **Índice**

1. [Importância dos Símbolos na Estatística e Análise de Dados](#1-importância-dos-símbolos-na-estatística-e-análise-de-dados)
2. [Símbolos Fundamentais](#2-símbolos-fundamentais)
3. [Símbolos Estatísticos Complementares](#3-símbolos-estatísticos-complementares)
4. [Símbolos Avançados em Inferência e Aprendizado de Máquina](#4-símbolos-avançados-em-inferência-e-aprendizado-de-máquina)
5. [Aplicações Práticas dos Símbolos](#5-aplicações-práticas-dos-símbolos)
6. [Questões de Revisão](#6-questões-de-revisão)
7. [Referências](#7-referências)

---

## **1. Importância dos Símbolos na Estatística e Análise de Dados**

Os símbolos matemáticos e estatísticos constituem a linguagem universal da ciência quantitativa, sendo fundamentais para a compreensão, comunicação e desenvolvimento de conceitos em estatística e análise de dados. Como observa **Stigler (1986)** em *The History of Statistics*, a notação matemática padronizada permitiu que a estatística se desenvolvesse como ciência rigorosa, facilitando a comunicação entre pesquisadores de diferentes países e culturas.

A importância dos símbolos pode ser compreendida em várias dimensões:

### **1.1 Precisão e Clareza Comunicativa**

Os símbolos matemáticos eliminam ambiguidades inerentes à linguagem natural. Quando escrevemos $\mu$ para média populacional e $\bar{x}$ para média amostral, estabelecemos uma distinção clara que é universalmente reconhecida. **Tufte (2001)** em *The Visual Display of Quantitative Information* argumenta que a notação matemática bem estruturada é essencial para a comunicação eficaz de conceitos quantitativos complexos.

### **1.2 Eficiência Cognitiva**

A utilização de símbolos permite expressar conceitos complexos de forma concisa. A expressão $\mathbb{E}[X]$ comunica instantaneamente o conceito de valor esperado de uma variável aleatória $X$, evitando descrições verbais extensas. Segundo **Hadamard (1945)**, a economia cognitiva proporcionada pela notação matemática é crucial para o pensamento científico avançado.

### **1.3 Universalidade e Padronização**

Os símbolos matemáticos transcendem barreiras linguísticas e culturais. Um pesquisador brasileiro e um chinês podem compreender perfeitamente uma fórmula estatística utilizando a mesma notação, facilitando a colaboração internacional e a reprodutibilidade da pesquisa científica (**Box, Hunter & Hunter, 2005**).

### **1.4 Fundamentação para Análise de Dados Moderna**

Na era do **big data** e **machine learning**, a compreensão dos símbolos matemáticos torna-se ainda mais crítica. Algoritmos de aprendizado de máquina, desde regressão linear até redes neurais profundas, são fundamentados em conceitos expressos por meio de notação matemática. **Hastie, Tibshirani e Friedman (2009)** demonstram como o domínio da notação estatística é prerequisito para compreender métodos avançados de análise preditiva.

### **1.5 Construção do Pensamento Analítico**

O domínio dos símbolos matemáticos não é meramente técnico; ele estrutura a forma como pensamos sobre problemas quantitativos. **Lakoff e Núñez (2000)** em *Where Mathematics Comes From* argumentam que a notação matemática molda nossa capacidade de raciocínio abstrato e resolução de problemas complexos.

---

## **2. Símbolos Fundamentais**

Os símbolos apresentados a seguir constituem o vocabulário básico para qualquer pessoa que trabalhe com estatística e análise de dados. Estes símbolos aparecem constantemente em literatura acadêmica, relatórios técnicos e implementações computacionais.

### ✅ **Principais símbolos e suas interpretações em português:**

| Símbolo | Nome (leitura) | Significado / Interpretação | **Exemplo do Cotidiano** |
|--------|----------------|------------------------------|--------------------------|
| $\mathbb{E}[X]$ | **Esperança de X** | Valor médio teórico de uma variável aleatória $X$ | Ao lançar um dado justo, $\mathbb{E}[dado]$ = 3,5 (valor esperado médio) |
| $\hat{\theta}$ | **Theta chapéu** | Estimador de um parâmetro populacional $\theta$ | Se $\theta$ é a altura média de todos os brasileiros, $\hat{\theta}$ = 1,70m é nossa estimativa baseada numa amostra |
| $\bar{x}$ | **x barra** | Média amostral | Se você gastou R$100, R$150 e R$125, então $\bar{x}$ = R$125 (sua média de gastos) |
| $\mu$ | **mi** | Média populacional | $\mu$ = salário médio de **todos** os trabalhadores do Brasil (valor real, geralmente desconhecido) |
| $\sigma$ | **sigma** | Desvio padrão populacional | $\sigma$ = variação real de todas as alturas na população brasileira |
| $s$ | **s** | Desvio padrão amostral | $s$ = variação das alturas apenas nas 100 pessoas que você mediu |
| $\text{Var}(X)$ | **Variância de X** | Esperança do quadrado do desvio de $X$ da média | Mede o quanto os dados se espalham: vendas diárias com $\text{Var}$ = 10.000 variam mais que com $\text{Var}$ = 100 |
| $\sqrt{x}$ | **raiz quadrada** | Usada em cálculos de desvio padrão ou erro | $\sqrt{16}$ = 4; se variância = 16, então desvio padrão = 4 |
| $\sum$ | **soma** | Indica uma soma (ex: somatório dos elementos) | $\sum \text{vendas}$ = venda_jan + venda_fev + venda_mar = total vendido |
| $\int$ | **integral** | Usada em distribuições contínuas (ex: densidade de probabilidade) | Área sob a curva de probabilidade; integral da velocidade dá a distância percorrida |
| $P(A)$ | **probabilidade de A** | Chance de um evento A ocorrer | $P(\text{chover})$ = 0,30 significa 30% de chance de chuva |
| $f(x)$ | **função f de x** | Função densidade ou distribuição | $f(x) = 2x$ descreve como uma variável se comporta; em estatística, descreve probabilidades |
| $\Pr(X = x)$ | **Probabilidade de X igual a x** | Distribuições discretas | $\Pr(\text{tirar 6 no dado})$ = $\frac{1}{6}$ ≈ 16,67% |
| $Z \sim N(0,1)$ | **Z segue distribuição normal padrão** | Distribuição normal com média 0 e desvio 1 | Alturas padronizadas seguem $N(0,1)$; z-score de uma pessoa |
| $\Rightarrow$ | **implica** | Relação lógica (se... então...) | Se está chovendo $\Rightarrow$ o chão está molhado |
| $\propto$ | **proporcional a** | Algo é proporcional a outro valor | Salário $\propto$ horas trabalhadas (salário aumenta proporcionalmente às horas) |
| $\arg\min$, $\arg\max$ | **arg mínimo / máximo** | Valor de entrada que minimiza ou maximiza uma função | $\arg\min(\text{custo})$ = rota que minimiza tempo de viagem |

A tabela acima apresenta os símbolos mais fundamentais em estatística e análise de dados. Cada símbolo representa um conceito específico que aparece frequentemente na literatura. Por exemplo, a distinção entre $\mu$ (parâmetro populacional) e $\bar{x}$ (estatística amostral) é fundamental para compreender a diferença entre população e amostra, conceito central na inferência estatística (**Casella & Berger, 2002**).

---

## **3. Símbolos Estatísticos Complementares**

Esta seção apresenta símbolos mais especializados, comumente utilizados em inferência estatística, testes de hipóteses e modelagem estatística. O domínio destes símbolos é essencial para compreender literatura acadêmica avançada e implementar análises estatísticas rigorosas.

### 📘 **Tabela Complementar de Símbolos Estatísticos**

| Símbolo                         | Nome (leitura)                       | Significado / Interpretação | **Exemplo do Cotidiano** |
|--------------------------------|--------------------------------------|------------------------------|--------------------------|
| $\theta$                   | **theta**                            | Parâmetro populacional genérico | $\theta$ = proporção real de pessoas satisfeitas com um produto |
| $\epsilon$                 | **épsilon**                          | Erro aleatório ou termo de erro | Diferença entre preço previsto e real de uma casa: preço_real = preço_previsto + $\epsilon$ |
| $\delta$                   | **delta**                            | Diferença entre valores / parâmetro de decisão | $\delta$ = diferença na eficácia entre dois medicamentos |
| $\alpha$                   | **alfa**                             | Nível de significância (ex: 0.05) | $\alpha$ = 0,05 significa "aceito 5% de chance de erro" ao tomar uma decisão |
| $\beta$                    | **beta**                             | Coeficiente de regressão / Erro tipo II | Em "salário = 2000 + 500×anos_estudo", $\beta$ = 500 (cada ano de estudo aumenta salário em R$500) |
| $\gamma$                   | **gama**                             | Parâmetro auxiliar ou taxa | Taxa de crescimento populacional; parâmetro de forma em distribuições |
| $\lambda$                  | **lambda**                           | Taxa em Poisson / regularização | $\lambda$ = 3 ligações/hora no call center (taxa média de chegada) |
| $\rho$                     | **rô**                               | Correlação populacional | $\rho$ = 0,80 entre altura e peso em toda população (correlação verdadeira) |
| $r$                        | **r**                                | Correlação amostral de Pearson | $r$ = 0,75 entre notas de matemática e física nos 50 alunos pesquisados |
| $\chi^2$                   | **qui-quadrado**                     | Distribuição usada em testes de aderência | Testar se um dado é viciado; verificar se há relação entre fumar e ter câncer |
| $t$                        | **t**                                | Estatística t (distribuição t de Student) | Usado quando temos amostras pequenas (ex: apenas 15 pacientes) |
| $F$                        | **F**                                | Estatística de teste F (ANOVA) | Comparar médias de vendas em 3 lojas diferentes simultaneamente |
| $H_0$, $H_1$           | **hipóteses nula e alternativa**     | Hipóteses estatísticas em teste | $H_0$: "a vacina não funciona"; $H_1$: "a vacina funciona" |
| $\text{MSE}$               | **erro quadrático médio**            | $\mathbb{E}[(\hat{\theta} - \theta)^2]$ | Mede qualidade da previsão: MSE baixo = previsões mais precisas |
| $\text{RMSE}$              | **raiz do erro quadrático médio**    | $\sqrt{\text{MSE}}$ | Se RMSE = R$5.000, suas previsões de preço erram em média R$5.000 |
| $\text{Bias}$              | **viés**                             | $\mathbb{E}[\hat{\theta}] - \theta$ | Se você sempre prevê preços R$10.000 acima do real, o viés = R$10.000 |
| $\text{Var}(\hat{\theta})$ | **variância do estimador**           | Mede a dispersão do estimador | Previsões muito variáveis (ora R$100k, ora R$200k) têm alta variância |
| $\text{SE}$                | **erro padrão (standard error)**     | $\text{SE} = \frac{\sigma}{\sqrt{n}}$ | Com mais dados (n maior), o erro diminui: 100 pessoas dá SE menor que 10 pessoas |
| $\text{CI}$                | **intervalo de confiança**           | Intervalo estimado para o parâmetro populacional | IC 95%: [R$45.000, R$55.000] - 95% de confiança que o valor real está neste intervalo |

Os símbolos desta tabela são particularmente importantes para inferência estatística e análise de qualidade de estimadores. Por exemplo, o **erro quadrático médio (MSE)** e seu componente **viés** são fundamentais para avaliar a qualidade de estimadores, conforme discutido extensivamente por **Lehmann e Casella (1998)** em *Theory of Point Estimation*.

---

## **4. Símbolos Avançados em Inferência e Aprendizado de Máquina**

Os símbolos apresentados nesta seção são essenciais para compreender métodos avançados de inferência estatística, teoria da informação e aprendizado de máquina. Estes conceitos são amplamente utilizados em aplicações modernas de ciência de dados e inteligência artificial.

### 📗 **Tabela de Símbolos Estatísticos e Matemáticos — Avançada**

| Símbolo                         | Nome (Leitura)                        | Significado / Uso |
|----------------------------------|----------------------------------------|--------------------|
| $\delta$                    | **delta**                              | Função de decisão (estatística) ou erro absoluto pequeno |
| $\epsilon$                  | **épsilon**                            | Erro arbitrariamente pequeno (limites, convergência) |
| $\alpha$                    | **alfa**                               | Nível de significância (ex: 0,05) |
| $\beta$                     | **beta**                               | Potência de teste (1 − erro tipo II) ou coeficiente de regressão |
| $\gamma$                    | **gama**                               | Parâmetro de distribuição (ex: gama) ou taxa de aprendizado |
| $\theta$                    | **teta**                               | Parâmetro desconhecido (estimado por $\hat{\theta}$) |
| $\lambda$                  | **lambda**                             | Taxa de ocorrência (Poisson / exponencial), regularização |
| $\kappa$                    | **kapa**                                | Estatística de concordância (coeficiente Kappa) |
| $\rho$                      | **rô**                                  | Correlação populacional |
| $\tau$                      | **tau**                                 | Medida de concordância de Kendall |
| $\chi^2$                    | **qui-quadrado**                        | Distribuição usada em testes de aderência e independência |
| $\ell(\theta)$              | **log-verossimilhança**                | Função de log-verossimilhança |
| $\mathcal{L}$               | **Lê** (letra cursiva L)                | Função de verossimilhança |
| $\mathcal{D}$               | **dê**                                  | Conjunto de dados ou distribuição |
| $KL(P \| Q)$               | **Divergência KL**                      | Medida de diferença entre distribuições |
| $I(X; Y)$                   | **Informação mútua**                    | Dependência entre variáveis aleatórias |
| $H(X)$                      | **Entropia de X**                       | Quantidade de incerteza (teoria da informação) |
| $Cov(X, Y)$                 | **covariância entre X e Y**            | Dependência linear entre variáveis |
| $Corr(X, Y)$                | **correlação entre X e Y**             | Covariância padronizada |
| $\forall$                  | **para todo**                           | Quantificador universal (lógica) |
| $\exists$                  | **existe**                              | Quantificador existencial |
| $\not\in$                  | **não pertence a**                      | Excluído de um conjunto |
| $\infty$                   | **infinito**                            | Limite sem fim (séries, integrais) |

Esta tabela reúne símbolos utilizados em áreas mais especializadas como teoria da informação (entropia $H(X)$, informação mútua $I(X;Y)$), inferência bayesiana (função de verossimilhança $\mathcal{L}$), e aprendizado de máquina (regularização $\lambda$). O domínio destes símbolos é essencial para compreender literatura científica contemporânea em **machine learning** e **deep learning** (**Goodfellow, Bengio & Courville, 2016**).

---

## **5. Aplicações Práticas dos Símbolos**

### **5.1 Exemplos do Dia a Dia**

Para tornar os símbolos matemáticos mais acessíveis e compreensíveis, apresentamos exemplos práticos do cotidiano que ilustram o uso de cada símbolo em situações reais.

#### **📊 Cenário 1: Analisando Gastos Mensais**

**Situação:** Você quer entender seus gastos com alimentação nos últimos 6 meses.

- **Gastos registrados (R$):** 800, 950, 850, 900, 1100, 800

**Aplicação dos símbolos:**

- $\bar{x}$ = (800 + 950 + 850 + 900 + 1100 + 800) / 6 = **R$ 900,00** (média amostral dos seus gastos)
- $\sum x_i$ = 800 + 950 + 850 + 900 + 1100 + 800 = **R$ 5.400,00** (total gasto no período)
- $s$ ≈ **R$ 117,26** (desvio padrão amostral - mostra quanto seus gastos variam mês a mês)
- **Interpretação:** Você gasta em média R$ 900 por mês em alimentação, com uma variação típica de ±R$ 117

#### **📈 Cenário 2: Previsão do Tempo**

**Situação:** Aplicativo de clima mostra "probabilidade de chuva"

- $P(\text{chuva})$ = 0,70 ou 70%
- $P(\text{não chover})$ = 1 - 0,70 = 0,30 ou 30%
- **Probabilidade condicional:** $P(\text{chuva}|\text{nublado})$ = "probabilidade de chover **dado que** está nublado" = 85%

**Interpretação:** Em 10 dias similares, esperamos que chova em aproximadamente 7 deles.

#### **🎲 Cenário 3: Jogo de Dados**

**Situação:** Calculando o valor esperado ao lançar um dado honesto.

- Resultados possíveis: {1, 2, 3, 4, 5, 6}
- $P(X = k)$ = $\frac{1}{6}$ para cada resultado $k$
- $\mathbb{E}[X]$ = $\frac{1+2+3+4+5+6}{6}$ = **3,5**

**Interpretação:** Se você jogar o dado muitas vezes e calcular a média, o resultado tenderá a 3,5.

#### **🏥 Cenário 4: Eficácia de Tratamento Médico**

**Situação:** Estudo clínico avalia se um novo medicamento é eficaz.

- $H_0$: "O medicamento **não tem efeito**" (hipótese nula)
- $H_1$: "O medicamento **tem efeito**" (hipótese alternativa)
- $\alpha$ = 0,05 (nível de significância - aceitamos 5% de chance de erro)
- **Resultado:** p-valor = 0,02 < 0,05 ⟹ Rejeitamos $H_0$

**Interpretação:** Há evidências estatísticas de que o medicamento é eficaz, com menos de 5% de chance de estarmos errados.

#### **🏠 Cenário 5: Preço de Imóveis**

**Situação:** Imobiliária quer prever preço de apartamentos com base na área (m²).

**Modelo de regressão:** Preço = $\beta_0$ + $\beta_1 \times \text{Área}$ + $\epsilon$

- $\beta_0$ = **R$ 50.000** (intercepto - valor base)
- $\beta_1$ = **R$ 5.000/m²** (coeficiente - quanto aumenta o preço por m² adicional)
- $\epsilon$ ~ $N(0, \sigma^2)$ (erro aleatório)

**Exemplo prático:**
- Apartamento de 80 m²: Preço estimado = 50.000 + 5.000 × 80 = **R$ 450.000**

#### **📱 Cenário 6: Taxa de Cliques em Anúncios**

**Situação:** Empresa analisa cliques em campanha de marketing digital.

- Total de visualizações: $n$ = 10.000
- Total de cliques: $x$ = 250
- **Taxa de cliques:** $\hat{p}$ = $\frac{x}{n}$ = $\frac{250}{10.000}$ = **2,5%**
- **Erro padrão:** $SE = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$ ≈ **0,16%**
- **Intervalo de confiança 95%:** [2,18%, 2,82%]

**Interpretação:** Estamos 95% confiantes de que a verdadeira taxa de cliques está entre 2,18% e 2,82%.

#### **🚗 Cenário 7: Tempo de Viagem ao Trabalho**

**Situação:** Você quer entender sua rotina de deslocamento.

**Dados de 10 dias (minutos):** 25, 30, 28, 35, 40, 27, 29, 32, 26, 38

- $\bar{x}$ = **31 minutos** (tempo médio)
- $\text{Mediana}$ = **29,5 minutos** (valor central)
- $\text{Moda}$ = não há (nenhum valor se repete)
- **Quartis:**
  - $Q_1$ = 27 min (25% dos dias você leva até 27 min)
  - $Q_2$ = 29,5 min (mediana)
  - $Q_3$ = 35 min (75% dos dias você leva até 35 min)

**Interpretação:** Em metade dos dias você leva menos de 29,5 minutos, e em 75% dos dias chega em até 35 minutos.

#### **🎯 Cenário 8: Controle de Qualidade na Fábrica**

**Situação:** Fábrica produz parafusos que devem ter 10mm de comprimento.

- $\mu$ = 10,0 mm (média populacional esperada)
- $\sigma$ = 0,2 mm (desvio padrão populacional aceitável)
- **Distribuição:** $X \sim N(10, 0,2^2)$ (distribuição normal)
- **Parafuso de 10,5mm:** está a $\frac{10,5-10}{0,2}$ = **2,5 desvios padrão** da média

**Interpretação:** Usando a distribuição normal, menos de 1% dos parafusos deveriam ter 10,5mm ou mais. Este pode ser um defeito.

#### **💰 Cenário 9: Investimentos Financeiros**

**Situação:** Comparando retorno de dois investimentos ao longo de 5 anos.

**Investimento A - retornos anuais:** 5%, 8%, 6%, 7%, 9%
- **Média aritmética:** $\bar{x}_A$ = (5+8+6+7+9)/5 = **7%**

**Investimento B - crescimento composto:**
- **Média geométrica:** $\bar{x}_G = \sqrt[5]{(1,05)(1,08)(1,06)(1,07)(1,09)} - 1$ ≈ **6,98%**

**Interpretação:** Para retornos compostos (como investimentos), a média geométrica é mais apropriada que a aritmética.

#### **📊 Cenário 10: Correlação entre Estudo e Nota**

**Situação:** Analisando se há relação entre horas de estudo e nota na prova.

| Aluno | Horas ($X$) | Nota ($Y$) |
|-------|-------------|------------|
| 1 | 2 | 5,5 |
| 2 | 4 | 7,0 |
| 3 | 6 | 8,5 |
| 4 | 8 | 9,0 |
| 5 | 3 | 6,0 |

- **Correlação de Pearson:** $r$ ≈ **0,95** (correlação amostral)
- **Covariância:** $Cov(X,Y)$ > 0 (quando uma variável aumenta, a outra tende a aumentar)

**Interpretação:** Há uma forte correlação positiva - mais horas de estudo estão associadas a notas maiores.

---

### **5.2 Em Relatórios Científicos**

A utilização correta da notação matemática em relatórios científicos demonstra rigor metodológico e facilita a revisão por pares. Quando um pesquisador reporta que "$\bar{x} = 45.2$ com $s = 12.1$ e $n = 200$", comunica de forma precisa informações sobre média amostral, desvio padrão amostral e tamanho da amostra.

### **5.3 Em Análise de Dados Computacional**

Linguagens como R, Python e Julia implementam funções que correspondem diretamente aos símbolos matemáticos. Por exemplo, a função `np.mean()` em Python calcula $\bar{x}$, enquanto `scipy.stats.chi2.cdf()` trabalha com a distribuição $\chi^2$. Esta correspondência entre notação matemática e implementação computacional é crucial para traduzir teoria em prática (**McKinney, 2017**).

### **5.4 Em Comunicação com Stakeholders**

Embora stakeholders não-técnicos possam não conhecer todos os símbolos, a apresentação de resultados utilizando notação padronizada (como intervalos de confiança $\text{CI}$) demonstra rigor analítico e facilita a comunicação com outros profissionais técnicos envolvidos no projeto.

---

## **6. Questões de Revisão**

### **Questão 1**
Explique a diferença conceitual entre $\mu$ e $\bar{x}$, e discuta por que esta distinção é fundamental para a inferência estatística.

### **Questão 2**
Em que contextos utilizaríamos a distribuição $\chi^2$ (qui-quadrado) e como ela se relaciona com testes de hipóteses?

### **Questão 3**
Defina matematicamente o conceito de viés de um estimador utilizando a notação $\text{Bias}(\hat{\theta})$ apresentada nas tabelas.

### **Questão 4**
Explique como a função de log-verossimilhança $\ell(\theta)$ se relaciona com a estimação de máxima verossimilhança em estatística.

### **Questão 5**
Discuta a importância da entropia $H(X)$ na teoria da informação e como este conceito se aplica em aprendizado de máquina.

### **Questão 6**
Por que a distinção entre $\sigma$ e $s$ é crucial ao reportar resultados de uma análise estatística?

### **Questão 7**
Explique como os símbolos $\alpha$ e $\beta$ são utilizados no contexto de testes de hipóteses estatísticas.

### **Questão 8**
Defina matematicamente a correlação populacional $\rho$ e sua estimativa amostral $r$, explicando suas diferenças conceituais.

---

## **7. Referências**

- BOX, G. E. P.; HUNTER, W. G.; HUNTER, J. S. *Statistics for Experimenters: Design, Innovation, and Discovery*. 2ª ed. Hoboken: Wiley, 2005.

- CASELLA, G.; BERGER, R. L. *Statistical Inference*. 2ª ed. Pacific Grove: Duxbury, 2002.

- GOODFELLOW, I.; BENGIO, Y.; COURVILLE, A. *Deep Learning*. Cambridge: MIT Press, 2016.

- HADAMARD, J. *The Psychology of Invention in the Mathematical Field*. Princeton: Princeton University Press, 1945.

- HASTIE, T.; TIBSHIRANI, R.; FRIEDMAN, J. *The Elements of Statistical Learning: Data Mining, Inference, and Prediction*. 2ª ed. New York: Springer, 2009.

- LAKOFF, G.; NÚÑEZ, R. E. *Where Mathematics Comes From: How the Embodied Mind Brings Mathematics into Being*. New York: Basic Books, 2000.

- LEHMANN, E. L.; CASELLA, G. *Theory of Point Estimation*. 2ª ed. New York: Springer, 1998.

- MCKINNEY, W. *Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython*. 2ª ed. Sebastopol: O'Reilly Media, 2017.

- STIGLER, S. M. *The History of Statistics: The Measurement of Uncertainty before 1900*. Cambridge: Belknap Press, 1986.

- TUFTE, E. R. *The Visual Display of Quantitative Information*. 2ª ed. Cheshire: Graphics Press, 2001.
