"""
Simulateur Monte Carlo Mono-Thread pour le calcul de Pi

Ce module implémente la méthode Monte Carlo en mode séquentiel (un seul thread).
La méthode consiste à générer des points aléatoires dans un carré et compter
combien tombent dans un cercle inscrit pour estimer la valeur de Pi.
"""

import random
import time


def calculate_pi_mono(num_samples: int) -> tuple[float, float]:
    """
    Calcule Pi en utilisant la méthode Monte Carlo (mono-thread).
    
    Principe:
    - On génère des points aléatoires (x, y) dans un carré [-1, 1] × [-1, 1]
    - On compte combien de points tombent dans le cercle unitaire (x² + y² ≤ 1)
    - Le ratio (points dans cercle / points totaux) ≈ (aire cercle / aire carré) = π/4
    - Donc: Pi ≈ 4 × (points_dans_cercle / points_totaux)
    
    Args:
        num_samples: Nombre de points aléatoires à générer
        
    Returns:
        tuple: (valeur_de_pi, temps_execution_en_secondes)
        
    Raises:
        ValueError: Si num_samples <= 0
    """
    # Validation de l'entrée
    if num_samples <= 0:
        raise ValueError(f"num_samples doit être > 0, reçu: {num_samples}")
    
    # Démarrer le chronomètre
    start_time = time.perf_counter()
    
    # Compteur pour les points qui tombent dans le cercle
    inside_circle = 0
    
    # Générer les points aléatoires un par un (séquentiel)
    for _ in range(num_samples):
        # Générer un point aléatoire (x, y) dans le carré [-1, 1] × [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        # Vérifier si le point est dans le cercle unitaire
        # Un point est dans le cercle si: x² + y² ≤ 1
        distance_squared = x * x + y * y
        
        if distance_squared <= 1:
            inside_circle += 1
    
    # Calculer Pi en utilisant la formule: Pi ≈ 4 × (inside / total)
    # Explication: aire_cercle/aire_carré = πr²/(2r)² = π/4
    pi_estimate = 4.0 * inside_circle / num_samples
    
    # Arrêter le chronomètre
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    
    return pi_estimate, execution_time


if __name__ == "__main__":
    # Test rapide du module
    print("=== Test du simulateur Monte Carlo Mono-Thread ===\n")
    
    # Test avec différentes tailles d'échantillons
    test_samples = [50000000]
    
    for samples in test_samples:
        pi_value, exec_time = calculate_pi_mono(samples)
        error = abs(pi_value - 3.14159265359)
        
        print(f"Échantillons: {samples:>10,}")
        print(f"  Pi calculé: {pi_value:.8f}")
        print(f"  Erreur:     {error:.8f}")
        print(f"  Temps:      {exec_time:.4f} secondes")
        print()
