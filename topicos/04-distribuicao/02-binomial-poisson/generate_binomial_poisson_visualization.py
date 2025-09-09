#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Geração de visualizações para as Distribuições Binomial e Poisson
Este script cria gráficos educativos para demonstrar o comportamento das distribuições Binomial e Poisson
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, poisson
import matplotlib.patches as mpatches

# Configuração para texto em português
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.labelsize'] = 10

def criar_grafico_binomial():
    """
    Cria gráficos da distribuição binomial com diferentes parâmetros
    """
    # Parâmetros para comparação
    parametros = [
        (10, 0.3),   # n=10, p=0.3
        (10, 0.5),   # n=10, p=0.5  
        (20, 0.3),   # n=20, p=0.3
        (30, 0.1)    # n=30, p=0.1
    ]
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Distribuição Binomial - Diferentes Parâmetros (n, p)', fontsize=16, fontweight='bold')
    
    cores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    
    for i, ((n, p), cor) in enumerate(zip(parametros, cores)):
        row, col = i // 2, i % 2
        ax = axes[row, col]
        
        # Valores de k possíveis
        k_values = np.arange(0, n + 1)
        
        # Calcular probabilidades
        probabilidades = binom.pmf(k_values, n, p)
        
        # Criar gráfico de barras
        barras = ax.bar(k_values, probabilidades, color=cor, alpha=0.7, edgecolor='black', linewidth=0.8)
        
        # Destacar o valor mais provável (moda)
        moda = int(np.round((n + 1) * p)) if (n + 1) * p != int((n + 1) * p) else int((n + 1) * p) - 1
        if moda < len(barras):
            barras[moda].set_color('#FF4444')
            barras[moda].set_alpha(1.0)
        
        # Configurações
        ax.set_xlabel('Número de Sucessos (k)', fontweight='bold')
        ax.set_ylabel('Probabilidade P(X = k)', fontweight='bold')
        ax.set_title(f'n = {n}, p = {p}', fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Calcular e exibir estatísticas
        media = n * p
        variancia = n * p * (1 - p)
        
        # Adicionar caixa de estatísticas
        stats_text = f'E[X] = {media:.1f}\nVar(X) = {variancia:.1f}\nModa ≈ {moda}'
        ax.text(0.98, 0.95, stats_text, transform=ax.transAxes, 
               fontsize=9, va='top', ha='right',
               bbox=dict(boxstyle='round,pad=0.4', facecolor=cor, alpha=0.3))
    
    plt.tight_layout()
    plt.savefig('distribuicao_binomial.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return fig

def criar_exemplo_binomial():
    """
    Cria um exemplo específico da distribuição binomial (prova de múltipla escolha)
    """
    n, p = 5, 0.5  # 5 questões, probabilidade 0.5 de acerto
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Valores de k
    k_values = np.arange(0, n + 1)
    probabilidades = binom.pmf(k_values, n, p)
    
    # Criar gráfico
    cores = plt.cm.viridis(np.linspace(0, 1, len(k_values)))
    barras = ax.bar(k_values, probabilidades, color=cores, alpha=0.8, edgecolor='black', linewidth=1.2)
    
    # Adicionar valores nas barras
    for k, prob, barra in zip(k_values, probabilidades, barras):
        ax.text(k, prob + 0.01, f'{prob:.3f}', ha='center', va='bottom', 
               fontweight='bold', fontsize=10)
    
    # Configurações
    ax.set_xlabel('Número de Acertos (k)', fontweight='bold', fontsize=12)
    ax.set_ylabel('Probabilidade P(X = k)', fontweight='bold', fontsize=12)
    ax.set_title('Exemplo: Prova de Múltipla Escolha\n(n = 5 questões, p = 0.5)', 
                fontsize=14, fontweight='bold')
    ax.set_xticks(k_values)
    ax.grid(True, alpha=0.3, axis='y')
    
    # Destacar k=2 (do exemplo no README)
    barras[2].set_color('#FF4444')
    barras[2].set_alpha(1.0)
    ax.annotate(f'P(X=2) = {probabilidades[2]:.4f}', 
                xy=(2, probabilidades[2]), xytext=(3.5, probabilidades[2] + 0.1),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=12, fontweight='bold', color='red')
    
    # Estatísticas
    media = n * p
    variancia = n * p * (1 - p)
    ax.text(0.02, 0.98, f'Valor Esperado: E[X] = {media:.1f}', transform=ax.transAxes, 
           fontsize=11, va='top', ha='left',
           bbox=dict(boxstyle='round,pad=0.4', facecolor='lightblue', alpha=0.8))
    ax.text(0.02, 0.88, f'Variância: Var(X) = {variancia:.2f}', transform=ax.transAxes, 
           fontsize=11, va='top', ha='left',
           bbox=dict(boxstyle='round,pad=0.4', facecolor='lightblue', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('exemplo_prova_binomial.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return fig

def criar_grafico_poisson():
    """
    Cria gráficos da distribuição Poisson com diferentes valores de λ
    """
    # Diferentes valores de lambda
    lambdas = [1, 3, 5, 10]
    cores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Distribuição de Poisson - Diferentes valores de λ', fontsize=16, fontweight='bold')
    
    for i, (lam, cor) in enumerate(zip(lambdas, cores)):
        row, col = i // 2, i % 2
        ax = axes[row, col]
        
        # Valores de k (ajustar range baseado em lambda)
        k_max = max(20, int(lam + 4 * np.sqrt(lam)))
        k_values = np.arange(0, k_max + 1)
        
        # Calcular probabilidades
        probabilidades = poisson.pmf(k_values, lam)
        
        # Filtrar apenas valores significativos (probabilidade > 0.001)
        mask = probabilidades > 0.001
        k_values = k_values[mask]
        probabilidades = probabilidades[mask]
        
        # Criar gráfico de barras (stem plot para Poisson fica mais claro)
        markerline, stemlines, baseline = ax.stem(k_values, probabilidades, 
                                                  basefmt=' ', linefmt=cor, markerfmt='o')
        markerline.set_markerfacecolor(cor)
        markerline.set_markeredgecolor('black')
        markerline.set_markersize(6)
        stemlines.set_linewidth(2)
        
        # Configurações
        ax.set_xlabel('Número de Eventos (k)', fontweight='bold')
        ax.set_ylabel('Probabilidade P(X = k)', fontweight='bold')
        ax.set_title(f'λ = {lam}', fontsize=13, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Adicionar estatísticas (para Poisson: E[X] = Var(X) = λ)
        stats_text = f'E[X] = {lam}\nVar(X) = {lam}'
        ax.text(0.98, 0.95, stats_text, transform=ax.transAxes, 
               fontsize=10, va='top', ha='right',
               bbox=dict(boxstyle='round,pad=0.4', facecolor=cor, alpha=0.3))
    
    plt.tight_layout()
    plt.savefig('distribuicao_poisson.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return fig

def criar_exemplo_poisson():
    """
    Cria um exemplo específico da distribuição Poisson (central de atendimento)
    """
    lam = 4  # média de 4 ligações por minuto
    
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    
    # Valores de k
    k_values = np.arange(0, 15)  # 0 a 14 ligações
    probabilidades = poisson.pmf(k_values, lam)
    
    # Criar gráfico de barras
    cores = plt.cm.plasma(probabilidades / probabilidades.max())
    barras = ax.bar(k_values, probabilidades, color=cores, alpha=0.8, edgecolor='black', linewidth=1)
    
    # Destacar k=2 (do exemplo no README)
    barras[2].set_color('#FF4444')
    barras[2].set_alpha(1.0)
    ax.annotate(f'P(X=2) = {probabilidades[2]:.4f}', 
                xy=(2, probabilidades[2]), xytext=(5, probabilidades[2] + 0.05),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=12, fontweight='bold', color='red')
    
    # Adicionar valores nas barras principais
    for k, prob in zip(k_values[:8], probabilidades[:8]):  # Mostrar só os primeiros 8
        if prob > 0.02:  # Só mostrar se probabilidade for significativa
            ax.text(k, prob + 0.005, f'{prob:.3f}', ha='center', va='bottom', 
                   fontsize=9, fontweight='bold')
    
    # Configurações
    ax.set_xlabel('Número de Ligações por Minuto (k)', fontweight='bold', fontsize=12)
    ax.set_ylabel('Probabilidade P(X = k)', fontweight='bold', fontsize=12)
    ax.set_title('Exemplo: Central de Atendimento\n(λ = 4 ligações por minuto)', 
                fontsize=14, fontweight='bold')
    ax.set_xticks(k_values)
    ax.grid(True, alpha=0.3, axis='y')
    
    # Estatísticas
    ax.text(0.98, 0.98, f'Valor Esperado: E[X] = {lam}', transform=ax.transAxes, 
           fontsize=11, va='top', ha='right',
           bbox=dict(boxstyle='round,pad=0.4', facecolor='lightgreen', alpha=0.8))
    ax.text(0.98, 0.88, f'Variância: Var(X) = {lam}', transform=ax.transAxes, 
           fontsize=11, va='top', ha='right',
           bbox=dict(boxstyle='round,pad=0.4', facecolor='lightgreen', alpha=0.8))
    ax.text(0.98, 0.78, f'Desvio Padrão: σ = {np.sqrt(lam):.2f}', transform=ax.transAxes, 
           fontsize=11, va='top', ha='right',
           bbox=dict(boxstyle='round,pad=0.4', facecolor='lightgreen', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('exemplo_central_poisson.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return fig

def main():
    """
    Função principal que gera todas as visualizações das distribuições Binomial e Poisson
    """
    print("Gerando visualizações para as Distribuições Binomial e Poisson...")
    
    # Distribuição Binomial
    print("1. Criando gráficos comparativos da Distribuição Binomial...")
    criar_grafico_binomial()
    
    print("2. Criando exemplo da prova de múltipla escolha (Binomial)...")
    criar_exemplo_binomial()
    
    # Distribuição Poisson
    print("3. Criando gráficos comparativos da Distribuição Poisson...")
    criar_grafico_poisson()
    
    print("4. Criando exemplo da central de atendimento (Poisson)...")
    criar_exemplo_poisson()
    
    print("✅ Visualizações geradas com sucesso!")
    print("Arquivos criados:")
    print("  - distribuicao_binomial.png")
    print("  - exemplo_prova_binomial.png")
    print("  - distribuicao_poisson.png")
    print("  - exemplo_central_poisson.png")

if __name__ == "__main__":
    main()