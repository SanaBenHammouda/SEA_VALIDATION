"""
Générateur de Visualisations pour Monte Carlo Threading Demo

Ce module crée tous les graphiques pour la présentation:
- Comparaison des temps d'exécution (barres)
- Scalabilité (ligne)
- Visualisation de la méthode Monte Carlo
- Facteur d'accélération (speedup)
"""

import os
import sys
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from typing import Dict
import numpy as np

# Ajouter le dossier parent au path pour les imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.performance_analyzer import BenchmarkResults


def ensure_output_directory():
    """
    Crée le dossier results/ s'il n'existe pas.
    """
    os.makedirs("results", exist_ok=True)


def plot_execution_times(results: Dict[str, BenchmarkResults], output_path: str = "results/execution_times.png"):
    """
    Crée un graphique en barres comparant les temps d'exécution.
    
    Ce graphique montre visuellement la différence de temps entre:
    - Mono-thread (référence)
    - Multi-thread avec 2, 4, 8 threads
    
    Args:
        results: Dictionnaire des résultats du benchmark
        output_path: Chemin où sauvegarder le graphique
    """
    ensure_output_directory()
    
    # Préparer les données
    configurations = []
    times = []
    errors = []  # Écart-type pour les barres d'erreur
    colors = []
    
    color_map = {
        'mono': '#e74c3c',      # Rouge pour mono-thread
        'multi_2': '#3498db',   # Bleu pour multi-thread
        'multi_4': '#2ecc71',   # Vert
        'multi_8': '#9b59b6'    # Violet
    }
    
    for key in ['mono', 'multi_2', 'multi_4', 'multi_8']:
        if key in results:
            r = results[key]
            configurations.append(r.configuration)
            times.append(r.avg_time)
            errors.append(r.std_time)
            colors.append(color_map[key])
    
    # Créer le graphique
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Créer les barres avec barres d'erreur
    bars = ax.bar(configurations, times, yerr=errors, capsize=5, 
                   color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    
    # Ajouter les valeurs sur les barres
    for bar, time in zip(bars, times):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{time:.3f}s',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # Configuration du graphique
    ax.set_xlabel('Configuration', fontsize=13, fontweight='bold')
    ax.set_ylabel('Temps d\'exécution (secondes)', fontsize=13, fontweight='bold')
    ax.set_title('Comparaison des Temps d\'Exécution\nMono-thread vs Multi-thread', 
                 fontsize=15, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Rotation des labels pour meilleure lisibilité
    plt.xticks(rotation=15, ha='right')
    
    # Ajuster la mise en page
    plt.tight_layout()
    
    # Sauvegarder avec haute résolution
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Graphique sauvegardé: {output_path}")


def plot_scalability(results: Dict[str, BenchmarkResults], output_path: str = "results/scalability.png"):
    """
    Crée un graphique de scalabilité montrant le temps vs nombre de threads.
    
    Ce graphique montre comment le temps d'exécution diminue quand on augmente
    le nombre de threads. Idéalement, plus de threads = moins de temps.
    
    Args:
        results: Dictionnaire des résultats du benchmark
        output_path: Chemin où sauvegarder le graphique
    """
    ensure_output_directory()
    
    # Préparer les données
    thread_counts = [1, 2, 4, 8]  # 1 = mono-thread
    times = []
    errors = []
    
    key_map = {1: 'mono', 2: 'multi_2', 4: 'multi_4', 8: 'multi_8'}
    
    for threads in thread_counts:
        key = key_map[threads]
        if key in results:
            times.append(results[key].avg_time)
            errors.append(results[key].std_time)
        else:
            times.append(None)
            errors.append(None)
    
    # Créer le graphique
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Ligne avec marqueurs et barres d'erreur
    ax.errorbar(thread_counts, times, yerr=errors, 
                marker='o', markersize=10, linewidth=2.5, capsize=5,
                color='#3498db', markerfacecolor='#e74c3c', 
                markeredgewidth=2, markeredgecolor='#c0392b')
    
    # Ajouter les valeurs sur les points
    for x, y in zip(thread_counts, times):
        if y is not None:
            ax.text(x, y, f'{y:.3f}s', 
                   ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Configuration du graphique
    ax.set_xlabel('Nombre de Threads', fontsize=13, fontweight='bold')
    ax.set_ylabel('Temps d\'Exécution (secondes)', fontsize=13, fontweight='bold')
    ax.set_title('Scalabilité: Temps d\'Exécution vs Nombre de Threads', 
                 fontsize=15, fontweight='bold', pad=20)
    ax.set_xticks(thread_counts)
    ax.grid(True, alpha=0.3, linestyle='--')
    
    # Ajuster la mise en page
    plt.tight_layout()
    
    # Sauvegarder avec haute résolution
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Graphique sauvegardé: {output_path}")


def plot_speedup_chart(results: Dict[str, BenchmarkResults], output_path: str = "results/speedup.png"):
    """
    Crée un graphique du facteur d'accélération (speedup).
    
    Le speedup montre combien de fois le multi-thread est plus rapide que le mono-thread.
    Un speedup de 4x signifie que le multi-thread est 4 fois plus rapide.
    
    Args:
        results: Dictionnaire des résultats du benchmark
        output_path: Chemin où sauvegarder le graphique
    """
    ensure_output_directory()
    
    # Préparer les données
    thread_counts = [1, 2, 4, 8]
    speedups = []
    
    key_map = {1: 'mono', 2: 'multi_2', 4: 'multi_4', 8: 'multi_8'}
    
    for threads in thread_counts:
        key = key_map[threads]
        if key in results:
            speedups.append(results[key].speedup)
        else:
            speedups.append(1.0)
    
    # Créer le graphique
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Barres de speedup
    colors = ['#e74c3c', '#3498db', '#2ecc71', '#9b59b6']
    bars = ax.bar(thread_counts, speedups, color=colors, alpha=0.8, 
                   edgecolor='black', linewidth=1.5, width=0.6)
    
    # Ligne de référence (speedup idéal = linéaire)
    ideal_speedup = thread_counts
    ax.plot(thread_counts, ideal_speedup, 'r--', linewidth=2, 
            label='Speedup Idéal (linéaire)', alpha=0.7)
    
    # Ajouter les valeurs sur les barres
    for bar, speedup in zip(bars, speedups):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{speedup:.2f}x',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # Configuration du graphique
    ax.set_xlabel('Nombre de Threads', fontsize=13, fontweight='bold')
    ax.set_ylabel('Facteur d\'Accélération (Speedup)', fontsize=13, fontweight='bold')
    ax.set_title('Facteur d\'Accélération: Multi-thread vs Mono-thread', 
                 fontsize=15, fontweight='bold', pad=20)
    ax.set_xticks(thread_counts)
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Ajuster la mise en page
    plt.tight_layout()
    
    # Sauvegarder avec haute résolution
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Graphique sauvegardé: {output_path}")


def plot_monte_carlo_visualization(num_samples: int = 5000, output_path: str = "results/monte_carlo_method.png"):
    """
    Crée une visualisation de la méthode Monte Carlo.
    
    Ce graphique montre:
    - Le carré [-1, 1] × [-1, 1]
    - Le cercle unitaire inscrit
    - Les points aléatoires (rouge = dans le cercle, bleu = hors du cercle)
    
    C'est une illustration visuelle parfaite pour expliquer la méthode !
    
    Args:
        num_samples: Nombre de points à afficher (5000 recommandé pour la clarté)
        output_path: Chemin où sauvegarder le graphique
    """
    ensure_output_directory()
    
    # Générer les points aléatoires
    points_inside_x = []
    points_inside_y = []
    points_outside_x = []
    points_outside_y = []
    
    inside_count = 0
    
    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        if x*x + y*y <= 1:
            points_inside_x.append(x)
            points_inside_y.append(y)
            inside_count += 1
        else:
            points_outside_x.append(x)
            points_outside_y.append(y)
    
    # Calculer Pi avec ces points
    pi_estimate = 4.0 * inside_count / num_samples
    
    # Créer le graphique
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Dessiner le cercle unitaire
    circle = patches.Circle((0, 0), 1, fill=False, edgecolor='black', linewidth=2.5)
    ax.add_patch(circle)
    
    # Dessiner le carré
    square = patches.Rectangle((-1, -1), 2, 2, fill=False, edgecolor='black', linewidth=2.5)
    ax.add_patch(square)
    
    # Afficher les points
    ax.scatter(points_outside_x, points_outside_y, c='#3498db', s=1, alpha=0.5, label='Hors du cercle')
    ax.scatter(points_inside_x, points_inside_y, c='#e74c3c', s=1, alpha=0.5, label='Dans le cercle')
    
    # Configuration du graphique
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect('equal')
    ax.set_xlabel('X', fontsize=13, fontweight='bold')
    ax.set_ylabel('Y', fontsize=13, fontweight='bold')
    ax.set_title(f'Méthode Monte Carlo pour Calculer Pi\n{num_samples:,} points | Pi ≈ {pi_estimate:.6f}', 
                 fontsize=15, fontweight='bold', pad=20)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(True, alpha=0.3, linestyle='--')
    
    # Ajouter une annotation explicative
    textstr = f'Points dans cercle: {inside_count:,}\n'
    textstr += f'Points totaux: {num_samples:,}\n'
    textstr += f'Ratio: {inside_count/num_samples:.4f}\n'
    textstr += f'Pi ≈ 4 × {inside_count/num_samples:.4f} = {pi_estimate:.6f}'
    
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=props)
    
    # Ajuster la mise en page
    plt.tight_layout()
    
    # Sauvegarder avec haute résolution
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Graphique sauvegardé: {output_path}")


def generate_all_plots(results: Dict[str, BenchmarkResults]):
    """
    Génère tous les graphiques en une seule fois.
    
    Args:
        results: Dictionnaire des résultats du benchmark
    """
    print("\n📊 Génération des graphiques...")
    
    plot_execution_times(results)
    plot_scalability(results)
    plot_speedup_chart(results)
    plot_monte_carlo_visualization()
    
    print("✓ Tous les graphiques ont été générés avec succès!\n")


if __name__ == "__main__":
    # Test rapide du module
    print("=== Test du générateur de visualisations ===\n")
    
    # Créer des données de test
    from src.performance_analyzer import BenchmarkResults
    
    test_results = {
        'mono': BenchmarkResults('Mono-thread', [1.0, 1.1, 0.9], 1.0, 0.1, 0.9, 1.1, 3.14, 0.001, 1.0),
        'multi_2': BenchmarkResults('Multi-thread (2 threads)', [0.6, 0.65, 0.55], 0.6, 0.05, 0.55, 0.65, 3.14, 0.001, 1.67),
        'multi_4': BenchmarkResults('Multi-thread (4 threads)', [0.35, 0.4, 0.3], 0.35, 0.05, 0.3, 0.4, 3.14, 0.001, 2.86),
        'multi_8': BenchmarkResults('Multi-thread (8 threads)', [0.25, 0.3, 0.2], 0.25, 0.05, 0.2, 0.3, 3.14, 0.001, 4.0),
    }
    
    generate_all_plots(test_results)
