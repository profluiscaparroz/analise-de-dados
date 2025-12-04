# Tendências de Medidas Estatísticas: Conceitos e Aplicações

## Sumário

- [Média aritmética](#1-média-aritmética)
- [Média Geométrica](#2-média-geométrica-definição-propriedades-e-aplicações)
- [Média harmônica](#3-média-harmônica)
- [Mediana](#4-mediana)
- [Moda](#5-moda)

A estatística desempenha um papel fundamental na análise e interpretação de dados, sendo amplamente utilizada em diversas áreas do conhecimento. Dentre as principais ferramentas estatísticas, destacam-se as medidas de tendência central, que permitem resumir um conjunto de dados em um único valor representativo. Essas medidas incluem a **média aritmética**, a **mediana** e a **moda**, cada uma com suas características e aplicações específicas.

## 1. Média Aritmética

A média aritmética é uma das medidas de tendência central mais utilizadas na estatística e desempenha um papel fundamental na análise de dados. Seu cálculo é simples e permite resumir um conjunto de valores em um único número representativo. No entanto, sua interpretação correta requer compreensão de suas propriedades, limitações e aplicações práticas em diferentes contextos.

A média aritmética de um conjunto de $n$ valores é calculada somando-se todos os valores e dividindo pelo número total de observações. A fórmula matemática é dada por:

$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$

onde:
- $\bar{x}$ representa a média aritmética;
- $x_i$ são os valores individuais do conjunto de dados;
- $n$ é o número total de observações.

A média é amplamente utilizada devido à sua simplicidade e facilidade de cálculo. Ela fornece um valor representativo do conjunto de dados, sendo especialmente útil em distribuições simétricas.

### Propriedades da Média Aritmética

A média aritmética possui diversas propriedades que a tornam uma ferramenta poderosa na estatística:

- **Linearidade**: Se dois conjuntos de dados possuem médias $\bar{x}$ e $\bar{y}$, então a média da soma dos conjuntos é a soma das médias.
- **Sensibilidade a Outliers**: Valores extremos podem influenciar significativamente a média, tornando-a pouco representativa em distribuições assimétricas.
- **Utilização em Distribuições Simétricas**: Quando os dados estão uniformemente distribuídos, a média fornece uma boa medida central.
- **Dependência da Escala**: Se todos os valores forem multiplicados por um fator constante, a média também será multiplicada pelo mesmo fator.

### Aplicações Práticas da Média Aritmética

A média aritmética é amplamente utilizada em diversas áreas do conhecimento. Algumas aplicações práticas incluem:

#### Economia e Finanças

Na análise econômica, a média aritmética é frequentemente utilizada para calcular indicadores como a renda per capita, o crescimento médio do PIB e taxas médias de juros. Por exemplo, se um investidor deseja calcular o retorno médio de um ativo financeiro ao longo de um período, pode utilizar a média aritmética para obter uma visão geral do desempenho do investimento.

#### Educação

Na área educacional, a média aritmética é usada para calcular notas finais de estudantes. Ao combinar diferentes avaliações, a média fornece uma estimativa do desempenho acadêmico do aluno. No entanto, em alguns casos, pesos diferentes são atribuídos a avaliações específicas, resultando na **média ponderada**, uma variação da média aritmética convencional.

#### Saúde e Epidemiologia

Em epidemiologia, a média aritmética é utilizada para calcular indicadores como a idade média dos pacientes em um estudo clínico ou a concentração média de uma substância em amostras biológicas. Esses cálculos ajudam os pesquisadores a compreender padrões de doenças e avaliar a eficácia de tratamentos médicos.

#### Engenharia e Qualidade

Na engenharia, a média aritmética é empregada no controle de qualidade e monitoramento de processos. Em indústrias manufatureiras, por exemplo, a média é usada para avaliar variações na produção e garantir que os produtos atendam a padrões pré-estabelecidos.

### Limitações da Média Aritmética

Embora a média aritmética seja uma medida estatística útil, ela apresenta algumas limitações importantes:

- **Influência de Outliers**: Pequenos conjuntos de dados podem ser significativamente afetados por valores extremos.
- **Não Representativa em Distribuições Assimétricas**: Em distribuições assimétricas, a média pode não representar adequadamente a tendência central, sendo preferível o uso da mediana.
- **Perda de Informações**: A média resume um conjunto de dados em um único valor, o que pode ocultar detalhes importantes sobre a variabilidade dos dados.

### Alternativas e Complementos à Média Aritmética

Para lidar com algumas das limitações da média aritmética, outras medidas podem ser utilizadas:

- **Mediana**: Melhor para distribuições assimétricas, pois não é afetada por valores extremos.
- **Moda**: Útil para identificar valores mais frequentes em conjuntos de dados categóricos.
- **Média Geométrica**: Aplicada em casos onde há crescimento exponencial, como taxas de crescimento econômico e retornos financeiros.

### Conclusão

A média aritmética é uma ferramenta estatística fundamental, sendo amplamente utilizada em diversas áreas do conhecimento. No entanto, sua correta interpretação exige atenção às características do conjunto de dados e às possíveis influências de valores extremos. Em muitos casos, a combinação da média com outras medidas estatísticas, como a mediana e o desvio padrão, proporciona uma análise mais completa e precisa.

### Referências

- MONTGOMERY, D. C.; RUNGER, G. C. *Applied Statistics and Probability for Engineers*. John Wiley & Sons, 2018.
- TRIOLA, M. F. *Elementary Statistics*. Pearson, 2021.
- MOORE, D. S.; MCCABE, G. P. *Introduction to the Practice of Statistics*. W. H. Freeman, 2017.

## 2. Média Geométrica: Definição, Propriedades e Aplicações

A média geométrica é uma medida de tendência central utilizada principalmente para calcular a taxa média de crescimento em processos multiplicativos. Diferente da média aritmética, que soma os valores e divide pelo total, a média geométrica multiplica os valores e extrai a raiz correspondente. Seu uso é comum em finanças, economia, ciências da computação e estatística aplicada.

### 1. Definição Matemática

A média geométrica de um conjunto de $n$ valores positivos $x_1, x_2, \dots, x_n$ é dada por:

$G = \sqrt[n]{x_1 \cdot x_2 \cdot \dots \cdot x_n}$

ou, de forma equivalente,

$G = \left( \prod_{i=1}^{n} x_i \right)^{\frac{1}{n}}$

Esta fórmula garante que a média geométrica sempre resultará em um valor menor ou igual à média aritmética, conforme demonstrado pela desigualdade de Minkowski.

### Propriedades da Média Geométrica

A média geométrica possui algumas propriedades fundamentais:

- **Invariância a Escalas Proporcionais**: Se todos os elementos forem multiplicados por uma constante, a média geométrica também é multiplicada por essa constante.
- **Sempre Menor ou Igual à Média Aritmética**: A desigualdade entre média geométrica e aritmética indica que a média geométrica é uma estimativa conservadora em relação à aritmética.
- **Adequada para Crescimento Composto**: Em processos onde os valores são multiplicativos, a média geométrica é mais apropriada que a média aritmética.

### Aplicações da Média Geométrica

A média geométrica é amplamente empregada em diversas áreas, incluindo:

#### Finanças e Economia

Em análise financeira, a média geométrica é usada para calcular a taxa média de retorno sobre investimentos ao longo do tempo, considerando o crescimento composto.

Exemplo:

Se um investimento tem taxas de retorno anuais de 10%, 5% e 15%, a média geométrica é:

$G = \sqrt[3]{(1.10) \times (1.05) \times (1.15)} - 1 \approx 9.9\%$

#### Ciências Biológicas e Epidemiologia

A média geométrica é utilizada para calcular a taxa de crescimento populacional e de propagação de doenças.

#### Estatística e Análise de Dados

A média geométrica é empregada em análises estatísticas que envolvem variáveis multiplicativas, como na construção de índices estatísticos e modelos matemáticos.

### Limitações da Média Geométrica

Apesar de suas vantagens, a média geométrica também possui limitações:

- **Necessidade de Valores Positivos**: Não pode ser aplicada quando há valores negativos ou nulos no conjunto de dados.
- **Maior Complexidade Computacional**: Exige operações de multiplicação e extração de raiz, podendo ser menos intuitiva que a média aritmética.
- **Sensibilidade a Pequenas Variações**: Em conjuntos com valores muito próximos, pode não representar grandes diferenças na distribuição dos dados.

### Conclusão

A média geométrica é uma ferramenta essencial na estatística e em diversas áreas do conhecimento, sendo particularmente útil em análises que envolvem crescimento composto e proporções multiplicativas. Seu uso adequado depende do contexto dos dados e da natureza das variáveis analisadas. No entanto, sua aplicação deve ser feita com cautela, considerando suas limitações e comparando-a com outras medidas de tendência central.

## Referências

- MOOD, A. M.; GRAYBILL, F. A.; BOES, D. C. *Introduction to the Theory of Statistics*. McGraw-Hill, 1974.
- MONTGOMERY, D. C. *Applied Statistics and Probability for Engineers*. John Wiley & Sons, 2019.
- BLAND, J. M.; ALTMAN, D. G. *Statistical Methods for Assessing Agreement Between Two Methods of Clinical Measurement*. The Lancet, 1986.

## 3. Média harmônica

A média harmônica é uma medida de tendência central que é particularmente útil para conjuntos de dados em que as quantidades são expressas em taxas ou razões. Diferente da média aritmética e da média geométrica, a média harmônica enfatiza os valores menores da distribuição, sendo amplamente utilizada em áreas como economia, física e estatística aplicada.

### Definição da Média Harmônica

A média harmônica de um conjunto de $ n $ números positivos $ x_1, x_2, ..., x_n $ é definida como o recíproco da média aritmética dos recíprocos dos valores individuais:

$H = \frac{n}{\sum_{i=1}^{n} \frac{1}{x_i}}$

Essa expressão mostra que a média harmônica dá mais peso aos valores menores, o que a torna particularmente útil em situações onde a influência dos valores pequenos é mais relevante.

### Propriedades da Média Harmônica

A média harmônica apresenta propriedades importantes:

- **Sempre menor ou igual à média aritmética e à média geométrica**: Para quaisquer valores positivos, temos que:
  $H \leq G \leq A$
  onde $H$ é a média harmônica, $G$ é a média geométrica e $A$ é a média aritmética.

- **Maior sensibilidade a valores pequenos**: Pequenos valores exercem maior influência na média harmônica do que na aritmética ou geométrica.

- **Utilização em cálculos de taxas**: A média harmônica é a abordagem correta para calcular a média de grandezas como velocidade média e taxa de juros harmônica.

### Aplicabilidades da Média Harmônica

#### Economia e Finanças
A média harmônica é usada na cálculo do índice de retorno médio de investimentos quando os retornos são expressos como razões. Isso evita superestimações que poderiam ocorrer ao se utilizar a média aritmética.

#### Física e Engenharia
Em problemas que envolvem velocidades médias, a média harmônica é a forma correta de calcular a velocidade média quando a distância percorrida é constante. Por exemplo, se um carro percorre uma determinada distância a 60 km/h em um trecho e a 40 km/h em outro, a velocidade média correta é obtida pela média harmônica, e não pela aritmética.

#### Estatística e Ciência de Dados
A média harmônica é útil na análise de dados, especialmente em métricas de avaliação de modelos de aprendizado de máquina. Um exemplo é o cálculo da média F1-score, que utiliza a média harmônica para combinar precisão e revocação de classificação.

### Exemplos de Cálculo

#### Exemplo 1: Velocidade Média
Se um carro percorre 100 km a uma velocidade de 60 km/h e depois outros 100 km a 40 km/h, a velocidade média $ V_m $ é dada por:

$V_m = \frac{2}{\frac{1}{60} + \frac{1}{40}} = 48 \text{ km/h}$

#### Exemplo 2: Média de Taxas de Crescimento
Se uma empresa cresce 20% no primeiro ano e 30% no segundo ano, a taxa média de crescimento não é simplesmente a média aritmética de 25%, mas sim a média harmônica:

$H = \frac{2}{\frac{1}{1.2} + \frac{1}{1.3}} = 24,39\%$

### Limitações da Média Harmônica

Apesar de sua utilidade, a média harmônica possui algumas limitações:
- Não pode ser aplicada quando existem valores nulos ou negativos no conjunto de dados.
- Em algumas situações, a média geométrica ou a aritmética pode ser mais apropriada.

### Conclusão

A média harmônica é uma ferramenta estatística essencial para calcular a média de taxas e razões, sendo amplamente utilizada em diversas áreas do conhecimento. Sua capacidade de enfatizar valores menores a torna especialmente útil em situações onde pequenos valores impactam significativamente o resultado final. No entanto, seu uso deve ser considerado com atenção, pois pode não ser adequada para todos os tipos de dados.

## Referências

- MOOD, A. M.; GRAYBILL, F. A.; BOES, D. C. *Introduction to the Theory of Statistics*. McGraw-Hill, 1974.
- MONTGOMERY, D. C. *Applied Statistics and Probability for Engineers*. John Wiley & Sons, 2019.
- WASSERMAN, L. *All of Statistics: A Concise Course in Statistical Inference*. Springer, 2004.


## 4. Mediana

A mediana é uma medida de tendência central amplamente utilizada na estatística para representar o valor central de um conjunto de dados. Em muitas situações, a mediana é preferida à média aritmética, especialmente quando há a presença de outliers ou distribuições assimétricas. Sua utilização está presente em diversas áreas do conhecimento, como economia, saúde, ciências sociais e engenharia.

### Histórico e Origem da Mediana

O conceito de mediana remonta ao século XIX, tendo sido formalmente introduzido por Francis Galton em 1881. Galton, um estatístico e eugenista britânico, usou a mediana como uma alternativa mais robusta à média para representar distribuições assimétricas de dados. No entanto, já no século XVIII, Pierre-Simon Laplace mencionou a ideia da mediana como uma estimativa central em distribuições estatísticas. Desde então, a mediana tem sido amplamente utilizada em diversas áreas da ciência e da engenharia.

### Definição da Mediana

A mediana de um conjunto de $ n $ valores ordenados é o valor que ocupa a posição central. Se $n$ for ímpar, a mediana é o elemento exatamente no meio da distribuição. Se $n$ for par, a mediana é a média aritmética dos dois valores centrais. A fórmula matemática para a mediana pode ser expressa como:

- Para um número ímpar de observações:

  $\tilde{x} = x_{(\frac{n+1}{2})}$

- Para um número par de observações:

  $\tilde{x} = \frac{x_{(\frac{n}{2})} + x_{(\frac{n}{2}+1)}}{2}$

onde $x_{(i)}$ representa o $i$-ésimo valor ordenado do conjunto de dados.

### Exemplo

Considere um conjunto de dados representando a idade de 7 pessoas: {23, 29, 31, 34, 35, 40, 42}. Como o número de elementos é ímpar (7), a mediana será o quarto valor ordenado:

$\tilde{x} = 34$

Agora, considere um conjunto de dados com 6 valores: {23, 29, 31, 34, 35, 40}. Como o número de elementos é par, a mediana será a média dos dois valores centrais:

$\tilde{x} = \frac{31 + 34}{2} = 32.5$

### Propriedades da Mediana

A mediana possui diversas propriedades que a tornam uma ferramenta estatística robusta e confiável:

- **Robustez contra Outliers**: Diferente da média aritmética, a mediana não é influenciada por valores extremos, tornando-a ideal para distribuições assimétricas ou conjuntos de dados com outliers.
- **Simplicidade de Cálculo**: Embora requeira a ordenação dos dados, seu cálculo é intuitivo e direto, sendo útil para análise exploratória.
- **Resistência a Assimetria**: Em distribuições enviesadas, a mediana fornece um valor central mais representativo do que a média.
- **Invariante a Transformações Monotônicas**: A mediana preserva sua posição relativa quando aplicadas transformações monotônicas estritas nos dados.

### Aplicações da Mediana

A mediana é utilizada em diversos campos do conhecimento devido às suas propriedades vantajosas. Algumas aplicações incluem:

#### Economia e Finanças

A mediana é amplamente empregada em análises econômicas, especialmente para medir a renda ou o patrimônio de uma população. Como a distribuição de renda geralmente apresenta assimetria positiva, a mediana reflete melhor o poder aquisitivo da maioria da população do que a média aritmética, que pode ser distorcida por indivíduos extremamente ricos (Piketty, 2014).

#### Exemplo

Seis famílias possuem as seguintes rendas mensais (em R$ mil): {2, 2.5, 3, 4, 10, 50}. A média aritmética seria:

$\bar{x} = \frac{2 + 2.5 + 3 + 4 + 10 + 50}{6} = 11.58$

Entretanto, a mediana seria:

$\tilde{x} = \frac{3 + 4}{2} = 3.5$

Indicando que a maior parte da população tem renda muito menor do que a média sugere.

### Saúde e Epidemiologia

Em estudos epidemiológicos, a mediana é frequentemente usada para expressar medidas como tempo de sobrevivência em análises de Kaplan-Meier (Bland, 2015). Ela fornece um indicador robusto para a análise da longevidade em tratamentos médicos e experimentos clínicos.

#### Exemplo

Um estudo clínico registrou os tempos de recuperação (em dias) de 9 pacientes após um tratamento: {5, 6, 7, 7, 8, 10, 12, 15, 20}. A mediana será:

$\tilde{x} = 8$

#### Engenharia e Controle de Qualidade

Na engenharia, a mediana é utilizada para avaliar dados experimentais quando há variações inesperadas nos processos produtivos. Em controle de qualidade, ela auxilia na detecção de falhas e na análise de resistência de materiais (Montgomery, 2019).

### Comparação entre Mediana e Média Aritmética

A escolha entre a média aritmética e a mediana depende da distribuição dos dados. Em distribuições simétricas, ambas as medidas são semelhantes. No entanto, quando os dados apresentam assimetria, a mediana pode fornecer uma melhor representação da tendência central. A tabela a seguir resume as diferenças entre essas medidas:

| Característica        | Média Aritmética | Mediana |
|----------------------|----------------|--------|
| Sensibilidade a outliers | Alta | Baixa |
| Relevância em dados assimétricos | Baixa | Alta |
| Facilidade de cálculo | Alta | Média |
| Aplicabilidade em distribuições normais | Alta | Média |

### Limitações da Mediana

Apesar de suas vantagens, a mediana também apresenta algumas limitações:

- **Perda de Informação**: Ao focar no valor central, a mediana ignora variações nos dados, não refletindo sua dispersão.
- **Necessidade de Ordenação dos Dados**: O cálculo da mediana requer que os dados sejam ordenados, o que pode ser computacionalmente caro em grandes conjuntos de dados.
- **Menor Sensibilidade a Mudanças Pequenas**: Pequenas variações nos valores não afetam a mediana, tornando-a menos responsiva a mudanças sutis nos dados.

### Conclusão

A mediana é uma medida de tendência central robusta e amplamente utilizada, sendo uma alternativa eficaz à média aritmética em distribuições assimétricas ou com outliers. Seu uso é comum em diversas áreas, desde economia e finanças até epidemiologia e ciências sociais. No entanto, como qualquer medida estatística, sua interpretação deve ser realizada em conjunto com outras estatísticas descritivas para obter uma visão mais completa dos dados.

## Referências

- BLAND, M. *An Introduction to Medical Statistics*. Oxford University Press, 2015.
- FIELD, A. *Discovering Statistics Using SPSS*. SAGE Publications, 2020.
- MONTGOMERY, D. C. *Applied Statistics and Probability for Engineers*. John Wiley & Sons, 2019.
- PIKETTY, T. *Capital in the Twenty-First Century*. Harvard University Press, 2014.


## 5. Moda

A moda é uma medida de tendência central amplamente utilizada na estatística para descrever a frequência de ocorrência de valores em um conjunto de dados. Ao contrário da média e da mediana, que estão relacionadas à posição central dos dados, a moda identifica os valores mais comuns dentro de uma distribuição.

### Definição da Moda

A moda de um conjunto de dados é o valor ou os valores que ocorrem com maior frequência. Dependendo da distribuição dos dados, podemos classificar a moda de diferentes formas:

- **Unimodal**: Quando existe apenas um valor modal (um único valor mais frequente).
- **Bimodal**: Quando existem dois valores modais com a mesma frequência máxima.
- **Multimodal**: Quando existem três ou mais valores modais.
- **Amodal**: Quando nenhum valor se destaca por ocorrer com maior frequência.

Matematicamente, se tivermos um conjunto de dados $X = \{x_1, x_2, \dots, x_n\}$, a moda $Mo$ é definida como:

$Mo = \arg\max_{x_i} f(x_i)$

onde $f(x_i)$ representa a frequência de ocorrência de cada valor $x_i$.

### Propriedades da Moda

A moda possui diversas propriedades que a tornam uma ferramenta valiosa na estatística:

- **Simplicidade de Interpretação**: Como se baseia na frequência, a moda é intuitiva e facilmente compreendida.
- **Aplicabilidade a Dados Categóricos**: Ao contrário da média e da mediana, a moda pode ser usada para variáveis qualitativas.
- **Resistência a Outliers**: A moda não é influenciada por valores extremos na distribuição dos dados.

### Aplicações da Moda

A moda é amplamente utilizada em diversas áreas do conhecimento devido à sua capacidade de representar a tendência central em diferentes contextos.

#### Pesquisa de Mercado

Na análise de preferências do consumidor, a moda é usada para determinar o produto, serviço ou característica mais popular. Por exemplo, em uma pesquisa de satisfação, a moda pode indicar a resposta mais escolhida pelos clientes (Kotler & Keller, 2016).

#### Educação e Avaliação de Desempenho

No contexto educacional, a moda pode ser utilizada para identificar a nota mais frequente entre os alunos de uma turma, auxiliando professores e gestores a compreenderem padrões de desempenho (Brookhart, 2013).

#### Ciências Sociais

Pesquisas sociais frequentemente utilizam a moda para analisar opiniões majoritárias em enquetes e censos. Por exemplo, a moda pode ser usada para identificar a profissão mais comum dentro de um grupo populacional (Field, 2020).

#### Medicina e Epidemiologia

Na saúde pública, a moda é utilizada para identificar sintomas mais comuns em doenças, contribuindo para diagnósticos e medidas preventivas (Bland, 2015).

### Comparando Moda, Média e Mediana

A escolha entre moda, média e mediana depende do tipo de dado analisado e da distribuição dos valores. A tabela abaixo resume as diferenças entre essas medidas:

| Característica        | Moda | Média Aritmética | Mediana |
|----------------------|------|----------------|--------|
| Tipo de dado | Qualitativo e quantitativo | Apenas quantitativo | Apenas quantitativo |
| Sensibilidade a outliers | Baixa | Alta | Baixa |
| Facilidade de interpretação | Alta | Média | Média |
| Representatividade em dados assimétricos | Alta | Baixa | Alta |

### Exemplos de Cálculo da Moda

#### Exemplo 1: Moda em Dados Quantitativos Discretos

Considere o seguinte conjunto de notas de alunos:

$\{7, 8, 9, 8, 10, 8, 7, 6, 9, 8\}$

A moda é **8**, pois é o valor que ocorre com maior frequência.

#### Exemplo 2: Moda em Dados Categóricos

Suponha que uma pesquisa perguntou a 10 pessoas qual sua cor favorita, e as respostas foram:

$\{"Azul", "Vermelho", "Azul", "Verde", "Azul", "Amarelo", "Verde", "Azul", "Vermelho", "Verde"\}$

A moda é **"Azul"**, pois aparece mais vezes do que as outras cores.

#### Exemplo 3: Moda em Distribuição Bimodal

Se tivermos o conjunto:

$\{5, 6, 6, 7, 8, 8, 9\}$

As modas são **6** e **8**, tornando essa uma distribuição bimodal.

### Limitações da Moda

Apesar de suas vantagens, a moda também apresenta algumas limitações:

- **Nem sempre é única**: Conjuntos multimodais podem dificultar a interpretação.
- **Pode ser inexistente**: Em algumas distribuições, nenhum valor se repete com mais frequência do que os outros.
- **Menos informativa para distribuições contínuas**: Para dados contínuos, a moda pode ser pouco útil, pois a frequência de cada valor pode ser baixa.

### Conclusão

A moda é uma medida fundamental da estatística descritiva, sendo essencial para dados categóricos e quantitativos discretos. Sua aplicabilidade em diversas áreas a torna uma ferramenta poderosa para análise de dados. Entretanto, seu uso deve ser complementado com outras medidas estatísticas para uma representação mais completa da tendência central.

### Referências

- BLAND, M. *An Introduction to Medical Statistics*. Oxford University Press, 2015.
- BROOKHART, S. M. *How to Use Grading to Improve Learning*. ASCD, 2013.
- FIELD, A. *Discovering Statistics Using SPSS*. SAGE Publications, 2020.
- KOTLER, P.; KELLER, K. L. *Marketing Management*. Pearson, 2016.

## 4. Comparação e Aplicações das Medidas de Tendência Central

Cada medida de tendência central tem suas vantagens e desvantagens dependendo do contexto:

| Medida  | Vantagens | Desvantagens |
|---------|----------|-------------|
| **Média** | Fácil de calcular e interpretar; útil para distribuições simétricas. | Sensível a outliers e distribuições assimétricas. |
| **Mediana** | Resistente a valores extremos; útil para dados assimétricos. | Pode ser menos representativa em distribuições simétricas. |
| **Moda** | Útil para dados categóricos e distribuições multimodais. | Pode não existir ou ser pouco informativa em alguns conjuntos de dados. |

Dessa forma, a escolha da medida estatística mais apropriada depende da distribuição dos dados e do objetivo da análise. Em cenários onde há muitos valores discrepantes, a mediana é geralmente preferida. Em contrapartida, quando se busca uma medida que leve em consideração todos os valores observados, a média pode ser a melhor opção.

## 5. Conclusão

As medidas de tendência central são essenciais para a análise de dados e a tomada de decisões em diversas áreas do conhecimento. A escolha entre média, mediana e moda deve ser guiada pelas características dos dados analisados e pelo propósito do estudo. O entendimento dessas tendências estatísticas é crucial para evitar interpretações equivocadas e garantir análises mais precisas e confiáveis.

## Referências

- FREEDMAN, D.; PISANI, R.; PURVES, R. *Statistics*. W. W. Norton & Company, 2017.
- MONTGOMERY, D. C.; RUNGER, G. C. *Applied Statistics and Probability for Engineers*. John Wiley & Sons, 2018.
- TRIOLA, M. F. *Elementary Statistics*. Pearson, 2021.
