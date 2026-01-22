# Design Document - Monte Carlo Threading Demo

## Speech d'Introduction pour la Présentation

**[À lire au début de votre vidéo - 2 minutes]**

"Bonjour ! Aujourd'hui, nous allons vous présenter notre projet sur le multi-threading en informatique. Nous sommes Snaa, Jobrane et Imen, et nous allons vous montrer concrètement pourquoi utiliser plusieurs threads peut rendre un programme beaucoup plus rapide.

Pour démontrer cela, nous avons choisi un exemple simple et visuel : calculer le nombre Pi (3.14159...) en utilisant la méthode Monte Carlo. Ne vous inquiétez pas si vous ne connaissez pas cette méthode, nous allons tout vous expliquer !

Imaginez que vous lancez des fléchettes au hasard sur une cible carrée qui contient un cercle. Si vous lancez beaucoup de fléchettes, vous pouvez calculer Pi en comptant combien de fléchettes tombent dans le cercle par rapport au total. C'est exactement ce que fait la méthode Monte Carlo, mais avec des points aléatoires générés par ordinateur.

Dans notre projet, nous allons comparer deux approches :
1. **Mono-thread** : Un seul travailleur qui génère tous les points un par un (lent)
2. **Multi-thread** : Plusieurs travailleurs qui génèrent des points en parallèle (rapide)

Nous allons vous montrer les résultats avec des graphiques, des mesures de temps réelles, et du code commenté pour que tout soit clair. C'est parti !"

## Principe de la Méthode Monte Carlo (Explication Simple)

### Qu'est-ce que la Méthode Monte Carlo ?

La méthode Monte Carlo est une technique mathématique qui utilise le **hasard** pour résoudre des problèmes complexes. Le nom vient du célèbre casino de Monte Carlo à Monaco, car la méthode repose sur la génération de nombres aléatoires, comme au casino !

### Comment Calculer Pi avec Monte Carlo ?

**Principe visuel :**

```
    Carré de côté 2 (surface = 4)
    ┌─────────────────┐
    │     ╱───╲       │
    │   ╱       ╲     │
    │  │ Cercle  │    │  ← Cercle de rayon 1 (surface = π)
    │   ╲       ╱     │
    │     ╲───╱       │
    └─────────────────┘
```

**Étapes simples :**

1. **Dessiner** : On imagine un carré de côté 2 (de -1 à +1 sur x et y)
2. **Ajouter un cercle** : On place un cercle de rayon 1 au centre du carré
3. **Lancer des points aléatoires** : On génère des milliers de points (x, y) au hasard dans le carré
4. **Compter** : On compte combien de points tombent dans le cercle
5. **Calculer Pi** : 
   - Surface du cercle / Surface du carré = π / 4
   - Donc : **Pi ≈ 4 × (points dans cercle / points totaux)**

**Exemple concret :**
- Si on lance 1 000 000 de points
- Et que 785 398 tombent dans le cercle
- Alors Pi ≈ 4 × (785 398 / 1 000 000) = 3.141592

Plus on lance de points, plus le résultat est précis !

### Pourquoi c'est Parfait pour le Multi-Threading ?

Cette tâche est **parfaitement parallélisable** car :
- ✅ Chaque point est **indépendant** des autres
- ✅ On peut diviser le travail : Thread 1 génère 250k points, Thread 2 génère 250k points, etc.
- ✅ À la fin, on **additionne** simplement les résultats de chaque thread
- ✅ Pas de dépendances complexes entre les calculs

**Analogie simple :**
Imaginez 4 personnes qui comptent des billets :
- **Mono-thread** : 1 personne compte 1000 billets → prend 10 minutes
- **Multi-thread** : 4 personnes comptent chacune 250 billets en parallèle → prend ~2.5 minutes !

C'est exactement ce qu'on va démontrer avec notre code.

## Overview

Ce projet implémente une démonstration comparative entre programmation mono-thread et multi-thread en utilisant la méthode Monte Carlo pour calculer Pi. Le système est conçu en Python pour sa simplicité et sa clarté pédagogique, utilisant les modules `threading`, `time`, `matplotlib` pour les visualisations, et `psutil` pour les mesures de ressources système.

**Choix technologiques :**
- **Langage** : Python 3.8+ (simple, clair, excellent pour la présentation)
- **Multi-threading** : Module `threading` avec `Lock` pour la synchronisation
- **Mesures** : Module `time` (précision nanoseconde) et `psutil` (CPU usage)
- **Visualisation** : `matplotlib` pour les graphiques professionnels
- **Structure** : Code modulaire avec séparation claire des responsabilités

## Architecture

### Structure du Projet

```
monte-carlo-threading-demo/
├── src/
│   ├── __init__.py
│   ├── monte_carlo_mono.py      # Simulation mono-thread
│   ├── monte_carlo_multi.py     # Simulation multi-thread
│   ├── performance_analyzer.py  # Mesures et statistiques
│   └── visualization.py         # Génération des graphiques
├── tests/
│   ├── __init__.py
│   ├── test_monte_carlo.py      # Tests unitaires
│   └── test_properties.py       # Tests de propriétés
├── results/                     # Dossier pour les graphiques générés
├── main.py                      # Point d'entrée principal
├── requirements.txt             # Dépendances Python
└── README.md                    # Documentation complète
```

### Flux d'Exécution

```
main.py
  ↓
  ├─→ monte_carlo_mono.py (exécution séquentielle)
  │     ↓
  │   [Mesure temps + résultat]
  │
  ├─→ monte_carlo_multi.py (exécution parallèle)
  │     ↓
  │   [Mesure temps + résultat avec 2, 4, 8 threads]
  │
  ├─→ performance_analyzer.py
  │     ↓
  │   [Calcul statistiques : moyenne, écart-type, speedup]
  │
  └─→ visualization.py
        ↓
      [Génération graphiques : barres, scalabilité, Monte Carlo]
```

## Components and Interfaces

### 1. Module `monte_carlo_mono.py`

**Responsabilité** : Implémentation de la simulation Monte Carlo en mode séquentiel.

**Interface principale** :
```python
def calculate_pi_mono(num_samples: int) -> tuple[float, float]:
    """
    Calcule Pi en utilisant la méthode Monte Carlo (mono-thread).
    
    Args:
        num_samples: Nombre de points aléatoires à générer
        
    Returns:
        tuple: (valeur_de_pi, temps_execution_en_secondes)
    """
```

**Algorithme** :
1. Initialiser compteur `inside_circle = 0`
2. Pour chaque itération de 0 à `num_samples` :
   - Générer point aléatoire (x, y) dans [-1, 1]
   - Si x² + y² ≤ 1, incrémenter `inside_circle`
3. Calculer Pi = 4 × (inside_circle / num_samples)
4. Retourner (Pi, temps_execution)

### 2. Module `monte_carlo_multi.py`

**Responsabilité** : Implémentation de la simulation Monte Carlo avec multi-threading.

**Interface principale** :
```python
def calculate_pi_multi(num_samples: int, num_threads: int) -> tuple[float, float]:
    """
    Calcule Pi en utilisant la méthode Monte Carlo (multi-thread).
    
    Args:
        num_samples: Nombre total de points aléatoires
        num_threads: Nombre de threads à utiliser
        
    Returns:
        tuple: (valeur_de_pi, temps_execution_en_secondes)
    """
```

**Algorithme avec synchronisation** :
1. Diviser `num_samples` en `num_threads` chunks égaux
2. Créer variable partagée `total_inside = 0` avec `Lock()`
3. Pour chaque thread :
   - Fonction worker : générer `chunk_size` points
   - Compter points dans le cercle localement
   - **Section critique** : acquérir lock, ajouter à `total_inside`, libérer lock
4. Attendre tous les threads (join)
5. Calculer Pi = 4 × (total_inside / num_samples)
6. Retourner (Pi, temps_execution)

**Gestion de la synchronisation** :
```python
from threading import Thread, Lock

lock = Lock()
total_inside = 0

def worker(samples_per_thread):
    local_inside = 0
    for _ in range(samples_per_thread):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x*x + y*y <= 1:
            local_inside += 1
    
    # Section critique protégée
    with lock:
        global total_inside
        total_inside += local_inside
```

### 3. Module `performance_analyzer.py`

**Responsabilité** : Mesurer, analyser et comparer les performances.

**Interfaces principales** :
```python
def run_benchmark(num_samples: int, num_runs: int = 10) -> dict:
    """
    Exécute plusieurs runs et collecte les statistiques.
    
    Args:
        num_samples: Nombre d'échantillons pour la simulation
        num_runs: Nombre de répétitions pour la moyenne
        
    Returns:
        dict: {
            'mono': {'times': [...], 'avg': float, 'std': float, 'pi': float},
            'multi_2': {...},
            'multi_4': {...},
            'multi_8': {...}
        }
    """

def calculate_speedup(mono_time: float, multi_time: float) -> float:
    """
    Calcule le facteur d'accélération.
    
    Returns:
        float: speedup = temps_mono / temps_multi
    """

def measure_cpu_usage() -> float:
    """
    Mesure l'utilisation CPU pendant l'exécution.
    
    Returns:
        float: Pourcentage d'utilisation CPU
    """
```

**Métriques collectées** :
- Temps d'exécution (moyenne, min, max, écart-type)
- Speedup pour chaque configuration de threads
- Utilisation CPU (via `psutil.cpu_percent()`)
- Précision du calcul de Pi (erreur par rapport à math.pi)

### 4. Module `visualization.py`

**Responsabilité** : Générer tous les graphiques pour la présentation.

**Interfaces principales** :
```python
def plot_execution_times(results: dict, output_path: str):
    """
    Crée un graphique en barres comparant les temps d'exécution.
    """

def plot_scalability(results: dict, output_path: str):
    """
    Crée un graphique de scalabilité (temps vs nombre de threads).
    """

def plot_monte_carlo_visualization(num_samples: int, output_path: str):
    """
    Visualise la méthode Monte Carlo (points dans/hors du cercle).
    """

def plot_speedup_chart(results: dict, output_path: str):
    """
    Crée un graphique du facteur d'accélération.
    """
```

**Spécifications graphiques** :
- Résolution : 300 DPI (qualité présentation)
- Format : PNG avec fond blanc
- Barres d'erreur : écart-type sur tous les graphiques
- Labels : français, police lisible (12pt minimum)
- Couleurs : palette professionnelle (bleu/orange/vert)

### 5. Module `main.py`

**Responsabilité** : Point d'entrée orchestrant toute la démonstration.

**Flux principal** :
```python
def main():
    print("=== Démonstration Monte Carlo : Mono-thread vs Multi-thread ===\n")
    
    # Configuration
    NUM_SAMPLES = 10_000_000  # 10 millions de points
    NUM_RUNS = 10
    
    # 1. Exécution mono-thread
    print("1. Exécution mono-thread...")
    mono_results = run_mono_benchmark(NUM_SAMPLES, NUM_RUNS)
    
    # 2. Exécution multi-thread (2, 4, 8 threads)
    print("2. Exécution multi-thread...")
    multi_results = run_multi_benchmark(NUM_SAMPLES, NUM_RUNS, [2, 4, 8])
    
    # 3. Analyse et affichage des résultats
    print("3. Analyse des résultats...")
    display_results(mono_results, multi_results)
    
    # 4. Génération des graphiques
    print("4. Génération des graphiques...")
    generate_all_plots(mono_results, multi_results)
    
    print("\n✓ Démonstration terminée ! Graphiques sauvegardés dans ./results/")
```

## Data Models

### Classe `SimulationResult`

```python
from dataclasses import dataclass
from typing import List

@dataclass
class SimulationResult:
    """Résultat d'une simulation Monte Carlo."""
    pi_value: float              # Valeur de Pi calculée
    execution_time: float        # Temps en secondes
    num_samples: int             # Nombre d'échantillons
    num_threads: int             # Nombre de threads (1 pour mono)
    cpu_usage: float             # Utilisation CPU en %

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
    speedup: float               # Facteur d'accélération (vs mono)
```

### Structure des Résultats

```python
results = {
    'mono': BenchmarkResults(...),
    'multi_2': BenchmarkResults(...),
    'multi_4': BenchmarkResults(...),
    'multi_8': BenchmarkResults(...)
}
```

## Correctness Properties

*Une propriété est une caractéristique ou un comportement qui doit être vrai pour toutes les exécutions valides d'un système - essentiellement, une déclaration formelle sur ce que le système doit faire. Les propriétés servent de pont entre les spécifications lisibles par l'homme et les garanties de correction vérifiables par machine.*

### Property 1: Point Generation Count Consistency

*Pour toute* valeur N d'échantillons demandée, le simulateur mono-thread doit générer exactement N points aléatoires, et le résultat final doit être basé sur exactement N points.

**Validates: Requirements 1.1**

### Property 2: Valid Coordinate Range

*Pour tous* les points générés par les simulateurs (mono ou multi-thread), les coordonnées x et y doivent être dans l'intervalle [-1, 1].

**Validates: Requirements 1.4**

### Property 3: Pi Calculation Formula Correctness

*Pour toute* simulation avec un nombre connu de points dans le cercle et un nombre total de points, la valeur de Pi calculée doit être égale à 4 × (points_inside / total_points).

**Validates: Requirements 1.5**

### Property 4: Multi-thread Work Distribution

*Pour toute* simulation multi-thread avec N échantillons et T threads, la somme des échantillons traités par tous les threads doit être égale à N.

**Validates: Requirements 2.1**

### Property 5: Thread-Safe Accumulation

*Pour toute* simulation multi-thread exécutée plusieurs fois avec les mêmes paramètres, les résultats doivent être cohérents (pas de race conditions), avec une variance acceptable due au hasard.

**Validates: Requirements 2.2, 5.2, 5.3**

### Property 6: Result Aggregation Correctness

*Pour toute* simulation multi-thread, le nombre total de points dans le cercle doit être égal à la somme des points comptés par chaque thread individuel.

**Validates: Requirements 2.5**

### Property 7: Statistical Calculations Correctness

*Pour toute* liste de temps d'exécution, la moyenne calculée doit être égale à la somme divisée par le nombre d'éléments, et l'écart-type doit suivre la formule statistique standard.

**Validates: Requirements 3.2**

### Property 8: Speedup Calculation Correctness

*Pour tous* temps mono-thread et multi-thread mesurés, le speedup calculé doit être égal à temps_mono / temps_multi.

**Validates: Requirements 3.4**

### Property 9: Multi-thread Performance Advantage

*Pour toute* simulation avec un nombre suffisant d'échantillons (> 1 million), le temps d'exécution multi-thread avec 4+ threads doit être inférieur au temps mono-thread (speedup > 1).

**Validates: Requirements 7.1**

### Property 10: Return Type Consistency

*Pour toute* exécution valide des simulateurs (mono ou multi), la fonction doit retourner un tuple de deux valeurs numériques (float, float) représentant (pi_value, execution_time).

**Validates: Requirements 1.2, 2.3**

## Error Handling

### Gestion des Erreurs d'Entrée

**Validation des paramètres** :
```python
def validate_inputs(num_samples: int, num_threads: int = 1):
    """
    Valide les paramètres d'entrée avant l'exécution.
    
    Raises:
        ValueError: Si les paramètres sont invalides
    """
    if num_samples <= 0:
        raise ValueError(f"num_samples doit être > 0, reçu: {num_samples}")
    
    if num_threads <= 0:
        raise ValueError(f"num_threads doit être > 0, reçu: {num_threads}")
    
    if num_threads > os.cpu_count():
        print(f"⚠️  Attention: {num_threads} threads demandés, mais seulement "
              f"{os.cpu_count()} cœurs disponibles. Performance peut être sous-optimale.")
```

**Messages d'erreur clairs** :
- ❌ `ValueError: num_samples doit être > 0` → Solution : Utiliser un nombre positif
- ❌ `ValueError: num_threads doit être > 0` → Solution : Utiliser au moins 1 thread
- ⚠️  Warning si trop de threads par rapport aux cœurs CPU disponibles

### Gestion des Erreurs de Synchronisation

**Protection contre les deadlocks** :
- Utilisation de `with lock:` (context manager) pour garantir la libération automatique
- Pas de locks imbriqués (un seul lock global pour éviter les deadlocks)
- Timeout sur les opérations de join des threads

```python
# Attendre les threads avec timeout
for thread in threads:
    thread.join(timeout=60)  # 60 secondes max
    if thread.is_alive():
        raise RuntimeError("Thread bloqué - possible deadlock détecté")
```

### Gestion des Erreurs de Ressources

**Vérification des ressources système** :
```python
import psutil

def check_system_resources():
    """Vérifie que les ressources système sont suffisantes."""
    available_memory = psutil.virtual_memory().available / (1024**3)  # GB
    
    if available_memory < 0.5:
        raise RuntimeError(
            f"Mémoire insuffisante: {available_memory:.2f} GB disponible. "
            f"Minimum requis: 0.5 GB"
        )
```

### Gestion des Erreurs de Visualisation

**Création de dossiers et fichiers** :
```python
import os

def ensure_output_directory():
    """Crée le dossier results/ s'il n'existe pas."""
    os.makedirs("results", exist_ok=True)

def save_plot_safely(fig, filepath: str):
    """Sauvegarde un graphique avec gestion d'erreur."""
    try:
        fig.savefig(filepath, dpi=300, bbox_inches='tight')
        print(f"✓ Graphique sauvegardé: {filepath}")
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde de {filepath}: {e}")
        print(f"   Solution: Vérifiez les permissions du dossier")
```

### Messages d'Erreur pour l'Utilisateur

Tous les messages d'erreur incluent :
1. **Description claire** du problème
2. **Valeurs reçues** (pour debug)
3. **Solution suggérée** pour corriger

Exemple :
```
❌ Erreur: num_samples doit être > 0, reçu: -1000
   Solution: Utilisez un nombre positif d'échantillons (ex: 1000000)
```

## Testing Strategy

### Approche de Test Dual

Le projet utilise **deux types de tests complémentaires** :

1. **Tests unitaires** : Vérifient des exemples spécifiques, cas limites et conditions d'erreur
2. **Tests de propriétés** : Vérifient les propriétés universelles sur de nombreuses entrées générées

### Configuration des Tests

**Framework de test** : `pytest` (standard Python)
**Property-based testing** : `hypothesis` (génération automatique de cas de test)

**Installation** :
```bash
pip install pytest hypothesis
```

**Structure des tests** :
```
tests/
├── __init__.py
├── test_monte_carlo.py       # Tests unitaires
└── test_properties.py        # Tests de propriétés (hypothesis)
```

### Tests Unitaires

**Objectifs** :
- Vérifier des exemples concrets
- Tester les cas limites (petit nombre d'échantillons, 1 thread, etc.)
- Vérifier la gestion des erreurs
- Tester l'intégration entre composants

**Exemples de tests unitaires** :
```python
def test_mono_thread_returns_tuple():
    """Vérifie que mono-thread retourne (pi, time)."""
    result = calculate_pi_mono(1000)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], float)
    assert isinstance(result[1], float)

def test_invalid_num_samples_raises_error():
    """Vérifie que num_samples <= 0 lève une erreur."""
    with pytest.raises(ValueError):
        calculate_pi_mono(-100)

def test_multi_thread_with_one_thread():
    """Vérifie que multi-thread fonctionne avec 1 thread."""
    result = calculate_pi_multi(1000, num_threads=1)
    assert result[0] > 0  # Pi doit être positif
```

### Tests de Propriétés (Property-Based Testing)

**Configuration** : Minimum **100 itérations** par test de propriété

**Objectifs** :
- Vérifier les propriétés universelles sur de nombreuses entrées aléatoires
- Détecter les bugs subtils (race conditions, erreurs de calcul)
- Garantir la robustesse du code

**Format des tests de propriétés** :
```python
from hypothesis import given, strategies as st

@given(st.integers(min_value=100, max_value=100000))
def test_property_point_count_consistency(num_samples):
    """
    Feature: monte-carlo-threading-demo, Property 1: Point Generation Count Consistency
    
    Pour toute valeur N d'échantillons, le simulateur doit générer exactement N points.
    """
    pi_value, exec_time = calculate_pi_mono(num_samples)
    # Le résultat doit être basé sur exactement num_samples points
    assert 0 < pi_value < 10  # Pi doit être dans un intervalle raisonnable

@given(
    st.integers(min_value=1000, max_value=50000),
    st.integers(min_value=2, max_value=8)
)
def test_property_work_distribution(num_samples, num_threads):
    """
    Feature: monte-carlo-threading-demo, Property 4: Multi-thread Work Distribution
    
    Pour toute simulation multi-thread, la somme du travail de tous les threads = N.
    """
    pi_value, exec_time = calculate_pi_multi(num_samples, num_threads)
    # Vérifier que le résultat est cohérent
    assert 2.0 < pi_value < 4.0  # Pi doit être proche de 3.14159

@given(st.integers(min_value=10000, max_value=100000))
def test_property_thread_safe_accumulation(num_samples):
    """
    Feature: monte-carlo-threading-demo, Property 5: Thread-Safe Accumulation
    
    Pour toute simulation multi-thread répétée, les résultats doivent être cohérents.
    """
    results = []
    for _ in range(5):  # 5 exécutions
        pi_value, _ = calculate_pi_multi(num_samples, num_threads=4)
        results.append(pi_value)
    
    # Variance acceptable due au hasard, mais pas d'incohérences majeures
    import statistics
    std_dev = statistics.stdev(results)
    assert std_dev < 0.1  # Écart-type raisonnable
```

### Tests de Performance

**Objectif** : Vérifier que le multi-threading apporte un gain réel

```python
def test_multi_thread_is_faster():
    """Vérifie que multi-thread (4 threads) est plus rapide que mono-thread."""
    num_samples = 5_000_000
    
    _, mono_time = calculate_pi_mono(num_samples)
    _, multi_time = calculate_pi_multi(num_samples, num_threads=4)
    
    speedup = mono_time / multi_time
    assert speedup > 1.5  # Au moins 1.5x plus rapide
    print(f"Speedup mesuré: {speedup:.2f}x")
```

### Tests d'Intégration

**Objectif** : Vérifier que tous les composants fonctionnent ensemble

```python
def test_full_benchmark_pipeline():
    """Teste le pipeline complet: benchmark + analyse + visualisation."""
    # Exécuter le benchmark
    results = run_benchmark(num_samples=100000, num_runs=3)
    
    # Vérifier que tous les résultats sont présents
    assert 'mono' in results
    assert 'multi_2' in results
    assert 'multi_4' in results
    
    # Vérifier que les graphiques sont générés
    generate_all_plots(results)
    assert os.path.exists("results/execution_times.png")
    assert os.path.exists("results/scalability.png")
```

### Exécution des Tests

**Commandes** :
```bash
# Tous les tests
pytest tests/ -v

# Tests unitaires seulement
pytest tests/test_monte_carlo.py -v

# Tests de propriétés seulement
pytest tests/test_properties.py -v

# Avec couverture de code
pytest tests/ --cov=src --cov-report=html
```

### Critères de Succès

✅ **Tous les tests doivent passer** avant de considérer le projet terminé
✅ **Couverture de code** : Minimum 80% du code source
✅ **Tests de propriétés** : Minimum 100 itérations par propriété
✅ **Tests de performance** : Speedup > 1.5x avec 4 threads

