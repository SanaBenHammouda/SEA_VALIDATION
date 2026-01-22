"""
Démonstration Rapide - Monte Carlo Threading Demo

Version allégée pour test rapide (30 secondes environ).
Utilise moins d'échantillons et moins de runs.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.performance_analyzer import run_benchmark, display_results_table
from src.visualization import generate_all_plots


def main():
    print("\n" + "="*80)
    print("🎯 DÉMONSTRATION RAPIDE - MONTE CARLO THREADING")
    print("="*80 + "\n")
    
    # Configuration allégée pour test rapide
    NUM_SAMPLES = 100_000  # 100k au lieu de 1M
    NUM_RUNS = 3           # 3 runs au lieu de 5
    
    print(f"⚙️  Configuration rapide:")
    print(f"   • Échantillons: {NUM_SAMPLES:,}")
    print(f"   • Runs: {NUM_RUNS}\n")
    
    # Exécuter le benchmark
    results = run_benchmark(num_samples=NUM_SAMPLES, num_runs=NUM_RUNS)
    
    # Afficher les résultats
    display_results_table(results)
    
    # Générer les graphiques
    generate_all_plots(results)
    
    print("\n✅ Démonstration rapide terminée !\n")


if __name__ == "__main__":
    main()
