#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Geração de visualizações para a Distribuição de Bernoulli
Este script cria gráficos educativos para demonstrar o comportamento da distribuição de Bernoulli
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import bernoulli
import matplotlib.patches as mpatches

# Configuração para texto em português
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['axes.labelsize'] = 11

def criar_grafico_bernoulli():
    """
    Cria um gráfico comparativo mostrando diferentes valores de p para a distribuição de Bernoulli
    """
    # Definir diferentes valores de p para comparação
    valores_p = [0.2, 0.5, 0.8]
    cores = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Distribuição de Bernoulli - Diferentes valores de p', fontsize=16, fontweight='bold')
    
    for i, (p, cor) in enumerate(zip(valores_p, cores)):
        ax = axes[i]
        
        # Valores possíveis (0 e 1)
        x = np.array([0, 1])
        
        # Probabilidades
        prob_0 = 1 - p  # P(X = 0)
        prob_1 = p      # P(X = 1)
        probabilidades = np.array([prob_0, prob_1])
        
        # Criar gráfico de barras
        barras = ax.bar(x, probabilidades, color=cor, alpha=0.8, edgecolor='black', linewidth=1.5)
        
        # Adicionar valores nas barras
        for j, (valor, prob) in enumerate(zip(x, probabilidades)):
            ax.text(valor, prob + 0.02, f'{prob:.1f}', 
                   ha='center', va='bottom', fontweight='bold', fontsize=12)
        
        # Configurações do eixo
        ax.set_xlabel('Resultado (X)', fontweight='bold')
        ax.set_ylabel('Probabilidade P(X)', fontweight='bold')
        ax.set_title(f'p = {p}', fontsize=14, fontweight='bold')
        ax.set_xticks([0, 1])
        ax.set_xticklabels(['0\n(Fracasso)', '1\n(Sucesso)'])
        ax.set_ylim(0, 1.1)
        ax.grid(True, alpha=0.3, axis='y')
        
        # Adicionar anotações
        ax.text(0.5, 0.95, f'E[X] = {p}', transform=ax.transAxes, 
               ha='center', va='top', fontsize=10,
               bbox=dict(boxstyle='round,pad=0.3', facecolor=cor, alpha=0.3))
        ax.text(0.5, 0.85, f'Var(X) = {p*(1-p):.2f}', transform=ax.transAxes, 
               ha='center', va='top', fontsize=10,
               bbox=dict(boxstyle='round,pad=0.3', facecolor=cor, alpha=0.3))
    
    plt.tight_layout()
    plt.savefig('distribuicao_bernoulli.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return fig

def criar_exemplo_moeda():
    """
    Cria um gráfico específico para o exemplo da moeda viciada (p=0.7)
    """
    p = 0.7
    
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    
    # Valores e probabilidades
    x = np.array([0, 1])
    probabilidades = np.array([1-p, p])
    
    # Criar gráfico de barras
    cores = ['#FF7F7F', '#90EE90']  # Vermelho claro para fracasso, verde claro para sucesso
    barras = ax.bar(x, probabilidades, color=cores, alpha=0.8, edgecolor='black', linewidth=2)
    
    # Adicionar valores nas barras
    for i, (valor, prob) in enumerate(zip(x, probabilidades)):
        ax.text(valor, prob + 0.03, f'{prob:.1f}\n({prob*100:.0f}%)', 
               ha='center', va='bottom', fontweight='bold', fontsize=14)
    
    # Configurações
    ax.set_xlabel('Resultado do Lançamento', fontweight='bold', fontsize=12)
    ax.set_ylabel('Probabilidade', fontweight='bold', fontsize=12)
    ax.set_title('Exemplo: Moeda Viciada (p = 0.7)', fontsize=16, fontweight='bold')
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['0\n(Coroa)', '1\n(Cara)'])
    ax.set_ylim(0, 1)
    ax.grid(True, alpha=0.3, axis='y')
    
    # Adicionar estatísticas
    ax.text(0.02, 0.98, f'Valor Esperado: E[X] = {p}', transform=ax.transAxes, 
           fontsize=12, va='top', ha='left',
           bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.8))
    ax.text(0.02, 0.88, f'Variância: Var(X) = {p*(1-p):.2f}', transform=ax.transAxes, 
           fontsize=12, va='top', ha='left',
           bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('exemplo_moeda_bernoulli.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return fig

def main():
    """
    Função principal que gera todas as visualizações da distribuição de Bernoulli
    """
    print("Gerando visualizações para a Distribuição de Bernoulli...")
    
    # Criar gráfico comparativo
    print("1. Criando gráfico comparativo com diferentes valores de p...")
    criar_grafico_bernoulli()
    
    # Criar exemplo da moeda
    print("2. Criando exemplo específico da moeda viciada...")
    criar_exemplo_moeda()
    
    print("✅ Visualizações geradas com sucesso!")
    print("Arquivos criados:")
    print("  - distribuicao_bernoulli.png")
    print("  - exemplo_moeda_bernoulli.png")

if __name__ == "__main__":
    main()