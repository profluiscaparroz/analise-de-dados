# Distribuições - Estrutura Padronizada

Este diretório contém os tópicos relacionados às distribuições estatísticas, organizados seguindo o **Padrão BDD (Behavior-Driven Directory)** para facilitar navegação e manutenção.

## Estrutura Padronizada

Todos os tópicos de distribuição seguem a seguinte estrutura:

```
nome-do-topico/
├── docs/                    # Documentação
│   ├── README.md           # Documentação principal em Markdown
│   └── README.pdf          # Documentação em PDF
└── src/                    # Código fonte e exemplos práticos
    └── *.ipynb            # Jupyter Notebooks com exemplos
```

## Tópicos Disponíveis

### 📊 01-variaveis-bernoulli
- **Documentação**: [docs/README.md](./01-variaveis-bernoulli/docs/README.md)
- **Exemplos práticos**: [src/exemplos_bernoulli.ipynb](./01-variaveis-bernoulli/src/exemplos_bernoulli.ipynb)
- **Conteúdo**: Variáveis aleatórias discretas, distribuição uniforme discreta, distribuição de Bernoulli

### 📈 02-binomial-poisson  
- **Documentação**: [docs/README.md](./02-binomial-poisson/docs/README.md)
- **Exemplos práticos**: [src/exemplos_binomial_poisson.ipynb](./02-binomial-poisson/src/exemplos_binomial_poisson.ipynb)
- **Conteúdo**: Distribuições Binomial e Poisson, comparações e aproximações

## Benefícios da Padronização

✅ **Navegação consistente** em todos os tópicos  
✅ **Separação clara** entre teoria (docs) e prática (src)  
✅ **Manutenção facilitada** com estrutura previsível  
✅ **Colaboração simplificada** para novos contribuidores  

## Referência

Esta estrutura está documentada em detalhes no arquivo [DIRECTORY_STRUCTURE_STANDARD.md](../../DIRECTORY_STRUCTURE_STANDARD.md) na raiz do repositório.

---
*Estrutura padronizada implementada em conformidade com os critérios de aceitação para organização e manutenção do material de distribuições.*