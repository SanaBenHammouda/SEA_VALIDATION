"""
Analyseur de Performance pour Monte Carlo Threading Demo

Ce module mesure et analyse les performances des simulateurs mono-thread et multi-thread.
Il calcule des statistiques (moyenne, écart-type, min, max) et le facteur d'accélération (speedup).
"""

import statistics
from dataclasses import dataclass
from typing import List, Dict
import psutil
import os

from src.monte_carlo_mono import calculate_pi_mono
from src.monte_carlo_multi import calculate_pi_multi


@dataclass
class SimulationResult:
    """Résultat d'une simulation Monte Carlo."""
    pi_value: float              # Valeur de Pi calculée
    execution_time: float        # Temps en secondes
    num_samples: int             # Nombre d'échantillons
    num_threads: int             # Nombre de threads (1 pour mono)
    cpu_usage: float = 0.0       # Utilisation CPU en %


@dataclass
class BenchmarkResults:
    """Résultats agrégés de plusieurs runs."""
    configuration: str           # "mono" ou "multi_N"
    times: List[float]           # Liste des temps de tous les runs
    avg_time: float              # Temps moyen
    std_time: float              # Écart-type
    min_time: float              # Temps minimum
    max_time: float              # Temps maximum
    avg_pi: float                # Valeur moyenne de Pi
    pi_error: float              # Erreur par rapport à math.pi
    speedup: float = 1.0         # Facteur d'accélération (vs mono)


def calculate_speedup(mono_time: float, multi_time: float) -> float:
    """
    Calcule le facteur d'accélération (speedup).
    
    Le speedup mesure combien de fois le multi-thread est plus rapide que le mono-thread.
    Speedup = temps_mono / temps_multi
    
    Exemples:
    - Speedup = 2.0 → multi-thread est 2x plus rapide
    - Speedup = 4.0 → multi-thread est 4x plus rapide
    - Speedup = 1.0 → même vitesse (pas d'amélioration)
    
    Args:
        mono_time: Temps d'exécution mono-thread en secondes
        multi_time: Temps d'exécution multi-thread en secondes
        
    Returns:
        float: Facteur d'accélération
    """
    if multi_time == 0:
        return 0.0
    return mono_time / multi_time


def measure_cpu_usage() -> float:
    """
    Mesure l'utilisation CPU actuelle du système.
    
    Returns:
        float: Pourcentage d'utilisation CPU (0-100)
    """
    return psutil.cpu_percent(interval=0.1)


def run_benchmark(num_samples: int, num_runs: int = 5) -> Dict[str, BenchmarkResults]:
    """
    Exécute un benchmark complet avec plusieurs runs pour obtenir des statistiques fiables.
    
    Le benchmark exécute:
    1. Mono-thread (num_runs fois)
    2. Multi-thread avec 2 threads (num_runs fois)
    3. Multi-thread avec 4 threads (num_runs fois)
    4. Multi-thread avec 8 threads (num_runs fois)
    
    Pour chaque configuration, on calcule:
    - Temps moyen, min, max, écart-type
    - Valeur moyenne de Pi et erreur
    - Speedup par rapport au mono-thread
    
    Args:
        num_samples: Nombre d'échantillons pour chaque simulation
        num_runs: Nombre de répétitions pour calculer les statistiques
        
    Returns:
        dict: Dictionnaire avec les résultats pour chaque configuration
              Clés: 'mono', 'multi_2', 'multi_4', 'multi_8'
    """
    import math
    
    # Validation des entrées
    if num_samples <= 0:
        raise ValueError(f"num_samples doit être > 0, reçu: {num_samples}")
    
    if num_runs <= 0:
        raise ValueError(f"num_runs doit être > 0, reçu: {num_runs}")
    
    print(f"📊 Benchmark avec {num_samples:,} échantillons, {num_runs} runs par configuration\n")
    
    results = {}
    
    # ========== MONO-THREAD ==========
    print("🔄 Exécution mono-thread...")
    mono_times = []
    mono_pi_values = []
    
    for run in range(num_runs):
        pi_value, exec_time = calculate_pi_mono(num_samples)
        mono_times.append(exec_time)
        mono_pi_values.append(pi_value)
        print(f"  Run {run + 1}/{num_runs}: {exec_time:.4f}s, Pi = {pi_value:.6f}")
    
    # Calculer les statistiques pour mono-thread
    mono_avg = statistics.mean(mono_times)
    mono_std = statistics.stdev(mono_times) if len(mono_times) > 1 else 0.0
    mono_pi_avg = statistics.mean(mono_pi_values)
    
    results['mono'] = BenchmarkResults(
        configuration='Mono-thread',
        times=mono_times,
        avg_time=mono_avg,
        std_time=mono_std,
        min_time=min(mono_times),
        max_time=max(mono_times),
        avg_pi=mono_pi_avg,
        pi_error=abs(mono_pi_avg - math.pi),
        speedup=1.0  # Référence
    )
    
    print(f"  ✓ Moyenne: {mono_avg:.4f}s ± {mono_std:.4f}s\n")
    
    # ========== MULTI-THREAD avec différentes configurations ==========
    thread_configs = [2, 4, 8]
    
    for num_threads in thread_configs:
        print(f"🔄 Exécution multi-thread ({num_threads} threads)...")
        multi_times = []
        multi_pi_values = []
        
        for run in range(num_runs):
            pi_value, exec_time = calculate_pi_multi(num_samples, num_threads)
            multi_times.append(exec_time)
            multi_pi_values.append(pi_value)
            print(f"  Run {run + 1}/{num_runs}: {exec_time:.4f}s, Pi = {pi_value:.6f}")
        
        # Calculer les statistiques pour cette configuration multi-thread
        multi_avg = statistics.mean(multi_times)
        multi_std = statistics.stdev(multi_times) if len(multi_times) > 1 else 0.0
        multi_pi_avg = statistics.mean(multi_pi_values)
        speedup = calculate_speedup(mono_avg, multi_avg)
        
        results[f'multi_{num_threads}'] = BenchmarkResults(
            configuration=f'Multi-thread ({num_threads} threads)',
            times=multi_times,
            avg_time=multi_avg,
            std_time=multi_std,
            min_time=min(multi_times),
            max_time=max(multi_times),
            avg_pi=multi_pi_avg,
            pi_error=abs(multi_pi_avg - math.pi),
            speedup=speedup
        )
        
        print(f"  ✓ Moyenne: {multi_avg:.4f}s ± {multi_std:.4f}s")
        print(f"  ✓ Speedup: {speedup:.2f}x\n")
    
    return results


def display_results_table(results: Dict[str, BenchmarkResults]):
    """
    Affiche un tableau récapitulatif des résultats dans la console.
    
    Args:
        results: Dictionnaire des résultats du benchmark
    """
    print("\n" + "="*80)
    print("📊 RÉSULTATS DU BENCHMARK")
    print("="*80)
    
    # En-tête du tableau
    print(f"{'Configuration':<25} {'Temps (s)':<15} {'Speedup':<12} {'Pi calculé':<15}")
    print("-"*80)
    
    # Lignes du tableau
    for key in ['mono', 'multi_2', 'multi_4', 'multi_8']:
        if key in results:
            r = results[key]
            time_str = f"{r.avg_time:.4f} ± {r.std_time:.4f}"
            speedup_str = f"{r.speedup:.2f}x" if r.speedup > 1 else "-"
            pi_str = f"{r.avg_pi:.8f}"
            
            print(f"{r.configuration:<25} {time_str:<15} {speedup_str:<12} {pi_str:<15}")
    
    print("="*80)
    
    # Informations système
    cpu_count = os.cpu_count() or 1
    cpu_usage = measure_cpu_usage()
    print(f"\n💻 Système: {cpu_count} cœurs CPU, utilisation actuelle: {cpu_usage:.1f}%")
    print()


if __name__ == "__main__":
    # Test rapide du module
    print("=== Test de l'analyseur de performance ===\n")
    
    # Benchmark avec un petit nombre d'échantillons pour le test
    results = run_benchmark(num_samples=100000, num_runs=3)
    
    # Afficher les résultats
    display_results_table(results)
