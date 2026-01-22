import sys
import os

# Ajouter le dossier src au path pour les imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.performance_analyzer import run_benchmark, display_results_table
from src.visualization import generate_all_plots


def print_header():
    print("\n" + "=" * 80)
    print("🎯 DÉMONSTRATION MONTE CARLO: MONO-THREAD VS MULTI-THREAD")
    print("=" * 80)
    print("📌 Objectif: Comparer les performances entre exécution séquentielle")
    print("            et exécution parallèle pour le calcul de Pi")
    print("=" * 80 + "\n")


def print_monte_carlo_explanation():
    print("📚 QU'EST-CE QUE LA MÉTHODE MONTE CARLO ?")
    print("-" * 80)
    print("""
La méthode Monte Carlo utilise le HASARD pour résoudre des problèmes mathématiques.

Pour calculer Pi:
1. On imagine un carré de côté 2 avec un cercle de rayon 1 à l'intérieur
2. On lance des "fléchettes" aléatoires dans le carré
3. On compte combien tombent dans le cercle
4. Le ratio (points dans cercle / points totaux) ≈ π/4
5. Donc: Pi ≈ 4 × (points_dans_cercle / points_totaux)

Plus on lance de fléchettes, plus le résultat est précis !
""")
    print("-" * 80 + "\n")


def print_threading_explanation():
    print("⚡ POURQUOI LE MULTI-THREADING ?")
    print("-" * 80)
    print("""
Analogie simple:
- MONO-THREAD = 1 personne qui compte 1 million de billets
- MULTI-THREAD = 4 personnes qui comptent chacune 250k billets en parallèle

Résultat: Le multi-thread est BEAUCOUP plus rapide !

Dans notre cas:
- Mono-thread: Génère tous les points un par un (lent)
- Multi-thread: Plusieurs threads génèrent des points en parallèle (rapide)
""")
    print("-" * 80 + "\n")


def main():
    try:
        print_header()
        print_monte_carlo_explanation()
        print_threading_explanation()

        NUM_SAMPLES = 50_000_000
        NUM_RUNS = 5

        print("⚙️  CONFIGURATION")
        print(f"   • Échantillons par simulation: {NUM_SAMPLES:,}")
        print(f"   • Nombre de runs par configuration: {NUM_RUNS}")
        print("   • Configurations testées: Mono-thread, Multi-thread (2, 4, 8 threads)\n")

        input("Appuyez sur Entrée pour commencer le benchmark...\n")

        print("🚀 DÉMARRAGE DU BENCHMARK")
        print("   Cela peut prendre quelques minutes...\n")

        results = run_benchmark(num_samples=NUM_SAMPLES, num_runs=NUM_RUNS)

        display_results_table(results)

        print("📊 GÉNÉRATION DES GRAPHIQUES")
        print("   Création des visualisations pour la présentation...\n")

        generate_all_plots(results)

        print("\n" + "=" * 80)
        print("✅ DÉMONSTRATION TERMINÉE AVEC SUCCÈS !")
        print("=" * 80)

        best_speedup = max(
            results["multi_2"].speedup,
            results["multi_4"].speedup,
            results["multi_8"].speedup
        )

        print(f"""
📈 RÉSULTATS CLÉS:
   • Meilleur speedup: {best_speedup:.2f}x plus rapide avec le multi-threading
   • Temps mono-thread: {results['mono'].avg_time:.3f}s
   • Temps multi-thread (8 threads): {results['multi_8'].avg_time:.3f}s
   • Gain de temps: {(results['mono'].avg_time - results['multi_8'].avg_time):.3f}s

📁 FICHIERS GÉNÉRÉS:
   • results/execution_times.png - Comparaison des temps
   • results/scalability.png - Graphique de scalabilité
   • results/speedup.png - Facteur d'accélération
   • results/monte_carlo_method.png - Visualisation de la méthode
""")

    except KeyboardInterrupt:
        print("\n\n⚠️  Benchmark interrompu par l'utilisateur.")
        sys.exit(1)

    except Exception as e:
        print(f"\n\n❌ ERREUR: {e}")
        print(f"   Type: {type(e).__name__}")
        print("\n💡 Solution: Vérifiez que toutes les dépendances sont installées:")
        print("   pip install -r requirements.txt")
        sys.exit(1)


if __name__ == "__main__":
    main()
