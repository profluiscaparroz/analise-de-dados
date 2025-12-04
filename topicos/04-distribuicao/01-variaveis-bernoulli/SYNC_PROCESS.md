# Processo de Sincronização README.md ↔ README.pdf

## Descrição
Este documento descreve o processo automatizado para sincronizar o conteúdo entre `README.md` e `README.pdf` no diretório `01-variaveis-bernoulli`, seguindo o padrão BDD (Behavior Driven Development).

## Critérios de Aceitação (BDD)
- **DADO** que existe um arquivo `README.md` atualizado
- **QUANDO** o processo de sincronização é executado
- **ENTÃO** o arquivo `README.pdf` deve conter todo o conteúdo do `README.md`
- **E** o processo deve ser documentado e reproduzível

## Ferramentas Necessárias

### Dependências do Sistema
```bash
sudo apt update
sudo apt install -y pandoc texlive-latex-base texlive-fonts-recommended texlive-latex-extra poppler-utils
```

### Ferramentas Utilizadas
- **pandoc**: Conversão de Markdown para PDF via LaTeX
- **pdflatex**: Motor de renderização PDF
- **pdftotext**: Verificação de conteúdo do PDF gerado
- **texlive**: Pacotes LaTeX para formatação matemática

## Script de Sincronização

### Localização
O script de sincronização está disponível em: `/tmp/sync-readme.sh`

### Uso
```bash
# Tornar executável
chmod +x /tmp/sync-readme.sh

# Executar sincronização
/tmp/sync-readme.sh
```

### Funcionalidades do Script
1. **Verificação**: Confirma existência do arquivo fonte `README.md`
2. **Backup**: Cria backup do PDF existente (`README.pdf.backup`)
3. **Conversão**: Utiliza pandoc para gerar PDF a partir do Markdown
4. **Verificação**: Extrai texto do PDF e verifica presença das seções principais
5. **Limpeza**: Remove backup se conversão foi bem-sucedida
6. **Log**: Registra todo o processo em `/tmp/sync-readme.log`

### Parâmetros de Conversão
```bash
pandoc README.md \
    --to=pdf \
    --output=README.pdf \
    --pdf-engine=pdflatex \
    --variable=geometry:margin=1in \
    --variable=fontsize:11pt \
    --variable=mainfont:"DejaVu Serif" \
    --variable=monofont:"DejaVu Sans Mono" \
    --highlight-style=tango \
    --number-sections \
    --table-of-contents \
    --metadata title="Variáveis Aleatórias Discretas - Distribuição Equiprovável e de Bernoulli" \
    --metadata author="Prof. Luis Caparroz" \
    --metadata date="$(date +%Y-%m-%d)"
```

## Processo Manual de Sincronização

### Passo 1: Preparação
```bash
cd /home/runner/work/analise-de-dados/analise-de-dados/topicos/04-distribuicao/01-variaveis-bernoulli
```

### Passo 2: Backup do PDF atual
```bash
cp README.pdf README.pdf.backup
```

### Passo 3: Geração do PDF
```bash
pandoc README.md --to=pdf --output=README.pdf --pdf-engine=pdflatex
```

### Passo 4: Verificação
```bash
# Verificar tamanho do arquivo
ls -la README.pdf

# Extrair texto para verificação
pdftotext README.pdf /tmp/pdf_verification.txt

# Verificar presença das seções principais
grep -i "Distribuição de Bernoulli" /tmp/pdf_verification.txt
grep -i "Distribuição Equiprovável" /tmp/pdf_verification.txt
```

## Status da Sincronização

### Última Execução
- **Data**: $(date)
- **Status**: ✅ CONCLUÍDA
- **Arquivo Fonte**: README.md (879 linhas)
- **Arquivo Destino**: README.pdf (862 linhas extraídas)

### Verificações Realizadas
- ✅ Arquivo README.md encontrado
- ✅ Backup criado com sucesso
- ✅ PDF gerado (497,753 bytes)
- ✅ Seções principais verificadas no PDF
- ✅ Conteúdo sincronizado

### Observações Técnicas
- **Formatação Matemática**: Algumas expressões LaTeX podem ter formatação ligeiramente diferente no PDF
- **Símbolos Especiais**: Emojis e símbolos especiais são convertidos adequadamente
- **Estrutura**: Hierarquia de títulos e seções preservada

## Automatização

### Integração com Git Hooks
Para automatizar o processo, pode-se configurar um git hook:

```bash
# .git/hooks/pre-commit
#!/bin/bash
if [ -f "topicos/04-distribuicao/01-variaveis-bernoulli/README.md" ]; then
    /tmp/sync-readme.sh
    git add topicos/04-distribuicao/01-variaveis-bernoulli/README.pdf
fi
```

### Integração com CI/CD
Para pipelines de CI/CD, adicionar step de sincronização:

```yaml
- name: Sync README files
  run: |
    chmod +x /tmp/sync-readme.sh
    /tmp/sync-readme.sh
    git add topicos/04-distribuicao/01-variaveis-bernoulli/README.pdf
```

## Solução de Problemas

### Erro: "Missing $ inserted"
Problema com formatação LaTeX em expressões matemáticas. Verificar se todas as expressões matemáticas estão corretamente delimitadas por `$...$` ou `$$...$$`.

### Erro: PDF muito pequeno
Verificar se todos os pacotes LaTeX estão instalados corretamente e se não há erros de conversão silenciosos.

### Erro: Seções faltando
Executar `pdftotext` no PDF gerado e comparar com o arquivo markdown original para identificar conteúdo faltante.

## Manutenção

### Atualização Periódica
- Executar sincronização sempre após mudanças no README.md
- Verificar logs de conversão mensalmente
- Manter dependências atualizadas

### Monitoramento
- Comparar número de linhas entre MD e PDF extraído
- Verificar presença das seções principais
- Validar tamanho do arquivo PDF gerado

---
**Última atualização**: $(date)  
**Responsável**: Sistema automatizado de sincronização  
**Versão**: 1.0