# Padrão de Estrutura de Diretórios - Análise de Dados

## Visão Geral

Este documento define o padrão de estrutura de diretórios para todos os tópicos de distribuição no repositório `analise-de-dados`. O objetivo é padronizar a organização dos arquivos para facilitar a navegação, manutenção e colaboração.

## Padrão BDD (Behavior-Driven Directory)

Todos os tópicos de distribuição devem seguir a seguinte estrutura:

```
nome-do-topico/
├── docs/                    # Documentação
│   ├── README.md           # Documentação principal em Markdown
│   └── README.pdf          # Documentação em PDF (opcional)
├── src/                    # Código fonte e exemplos práticos
│   ├── *.py               # Scripts Python (se aplicável)
│   ├── *.ipynb            # Jupyter Notebooks
│   └── exemplos/          # Exemplos práticos (se necessário)
├── assets/                 # Recursos adicionais (opcional)
│   ├── images/            # Imagens e gráficos
│   └── data/              # Arquivos de dados (se aplicável)
└── tests/                  # Testes (opcional)
    └── *.py               # Scripts de teste
```

## Descrição dos Diretórios

### `/docs`
- **Obrigatório**
- Contém toda a documentação teórica do tópico
- Arquivo `README.md` é obrigatório
- Arquivo `README.pdf` é opcional mas recomendado

### `/src`
- **Obrigatório**
- Contém implementações práticas, exemplos de código, Jupyter Notebooks
- Organizado de forma lógica conforme a complexidade do tópico

### `/assets` 
- **Opcional**
- Para recursos adicionais como imagens, gráficos, datasets específicos

### `/tests`
- **Opcional**
- Para scripts de teste e validação de código

## Benefícios da Padronização

1. **Navegação Facilitada**: Estrutura consistente em todos os tópicos
2. **Manutenção Simplificada**: Fácil localização de arquivos específicos
3. **Colaboração Melhorada**: Novos colaboradores podem encontrar arquivos rapidamente
4. **Separação Clara**: Documentação separada de código prático
5. **Escalabilidade**: Estrutura permite crescimento organizado do conteúdo

## Implementação

Este padrão deve ser aplicado a todos os tópicos de distribuição, começando por:
- `04-distribuicao/01-variaveis-bernoulli/`
- `04-distribuicao/02-binomial-poisson/`

## Exemplo de Referência

O tópico `distribuicao-weibull/` já implementa este padrão e pode servir como referência.

---

**Documento criado como parte da padronização da estrutura de diretórios do repositório.**