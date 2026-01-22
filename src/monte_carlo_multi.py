"""
Simulateur Monte Carlo Multi-Thread pour le calcul de Pi

Ce module implémente la méthode Monte Carlo en mode parallèle (plusieurs threads).
Le travail est divisé entre plusieurs threads qui s'exécutent en parallèle,
avec synchronisation pour éviter les race conditions.
"""

import random
import time
import threading
from typing import List


def worker(samples_per_thread: int, lock: threading.Lock, shared_counter: dict):
    """
    Fonction exécutée par chaque thread pour calculer sa part du travail.
    
    Chaque thread:
    1. Génère ses propres points aléatoires (localement, sans synchronisation)
    2. Compte combien tombent dans le cercle (localement)
    3. Ajoute son résultat au compteur partagé (avec synchronisation)
    
    Args:
        samples_per_thread: Nombre de points à générer par ce thread
        lock: Verrou pour protéger l'accès au compteur partagé
        shared_counter: Dictionnaire partagé contenant le compteur total
    """
    # Compteur local (pas besoin de synchronisation ici)
    local_inside = 0
    
    # Générer les points aléatoires pour ce thread
    for _ in range(samples_per_thread):
        # Générer un point aléatoire (x, y) dans [-1, 1] × [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        # Vérifier si le point est dans le cercle unitaire
        distance_squared = x * x + y * y
        
        if distance_squared <= 1:
            local_inside += 1
    
    # SECTION CRITIQUE: Ajouter le résultat local au compteur partagé
    # On utilise un lock pour éviter les race conditions
    # (plusieurs threads qui modifient la même variable en même temps)
    with lock:
        shared_counter['inside_circle'] += local_inside


def calculate_pi_multi(num_samples: int, num_threads: int) -> tuple[float, float]:
    """
    Calcule Pi en utilisant la méthode Monte Carlo (multi-thread).
    
    Principe:
    - Diviser le travail total en chunks égaux pour chaque thread
    - Chaque thread génère ses points et compte localement
    - Les résultats sont agrégés de manière thread-safe avec un lock
    - Le calcul final de Pi utilise le total agrégé
    
    Args:
        num_samples: Nombre total de points aléatoires à générer
        num_threads: Nombre de threads à utiliser pour le calcul parallèle
        
    Returns:
        tuple: (valeur_de_pi, temps_execution_en_secondes)
        
    Raises:
        ValueError: Si num_samples <= 0 ou num_threads <= 0
    """
    # Validation des entrées
    if num_samples <= 0:
        raise ValueError(f"num_samples doit être > 0, reçu: {num_samples}")
    
    if num_threads <= 0:
        raise ValueError(f"num_threads doit être > 0, reçu: {num_threads}")
    
    # Avertissement si trop de threads
    import os
    cpu_count = os.cpu_count() or 1
    if num_threads > cpu_count:
        print(f"⚠️  Attention: {num_threads} threads demandés, mais seulement "
              f"{cpu_count} cœurs disponibles.")
    
    # Démarrer le chronomètre
    start_time = time.perf_counter()
    
    # Diviser le travail entre les threads
    samples_per_thread = num_samples // num_threads
    remaining_samples = num_samples % num_threads
    
    # Créer le lock pour protéger le compteur partagé
    lock = threading.Lock()
    
    # Créer le compteur partagé (dictionnaire pour pouvoir le modifier dans les threads)
    shared_counter = {'inside_circle': 0}
    
    # Créer et démarrer tous les threads
    threads: List[threading.Thread] = []
    
    for i in range(num_threads):
        # Le dernier thread prend les échantillons restants
        samples_for_this_thread = samples_per_thread
        if i == num_threads - 1:
            samples_for_this_thread += remaining_samples
        
        # Créer le thread avec la fonction worker
        thread = threading.Thread(
            target=worker,
            args=(samples_for_this_thread, lock, shared_counter)
        )
        
        # Démarrer le thread (il commence à s'exécuter en parallèle)
        thread.start()
        
        # Ajouter à la liste pour pouvoir attendre sa fin plus tard
        threads.append(thread)
    
    # Attendre que tous les threads aient terminé leur travail
    # (join = attendre la fin du thread)
    for thread in threads:
        thread.join(timeout=60)  # Timeout de 60 secondes pour éviter les blocages
        
        if thread.is_alive():
            raise RuntimeError("Thread bloqué - possible deadlock détecté")
    
    # Tous les threads ont terminé, on peut maintenant calculer Pi
    total_inside = shared_counter['inside_circle']
    pi_estimate = 4.0 * total_inside / num_samples
    
    # Arrêter le chronomètre
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    
    return pi_estimate, execution_time


if __name__ == "__main__":
    # Test rapide du module
    print("=== Test du simulateur Monte Carlo Multi-Thread ===\n")
    
    # Test avec différentes configurations
    test_configs = [
       (50000000, 4),
        (50000000, 8)
      

    ]
    
    for samples, threads in test_configs:
        pi_value, exec_time = calculate_pi_multi(samples, threads)
        error = abs(pi_value - 3.14159265359)
        
        print(f"Échantillons: {samples:>10,} | Threads: {threads}")
        print(f"  Pi calculé: {pi_value:.8f}")
        print(f"  Erreur:     {error:.8f}")
        print(f"  Temps:      {exec_time:.4f} secondes")
        print()
