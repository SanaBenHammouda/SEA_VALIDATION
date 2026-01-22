# Implementation Plan: Monte Carlo Threading Demo

## Overview

Ce plan d'implémentation guide la création complète du projet de démonstration Monte Carlo comparant mono-thread et multi-thread. Le projet sera développé en Python avec une structure simple et directe, sans tests unitaires, pour se concentrer sur la démonstration fonctionnelle et la présentation.

**Configuration simplifiée** : 1 million d'itérations, 5 runs pour les statistiques.

## Tasks

- [x] 1. Configuration initiale du projet
  - Créer la structure de dossiers (src/, results/)
  - Créer le fichier requirements.txt avec les dépendances (matplotlib, psutil)
  - Créer les fichiers __init__.py pour le package Python
  - _Requirements: 8.1_

- [x] 2. Implémenter le simulateur Monte Carlo mono-thread
  - Créer le module src/monte_carlo_mono.py avec la fonction calculate_pi_mono()
  - Implémenter la génération de points aléatoires dans [-1, 1]
  - Implémenter le comptage des points dans le cercle unitaire (x² + y² ≤ 1)
  - Implémenter le calcul de Pi avec la formule: Pi ≈ 4 × (inside / total)
  - Mesurer le temps d'exécution avec time.perf_counter()
  - Ajouter des commentaires détaillés en français expliquant chaque étape
  - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5_

- [x] 3. Implémenter le simulateur Monte Carlo multi-thread
  - Créer le module src/monte_carlo_multi.py avec la fonction calculate_pi_multi()
  - Implémenter la division du travail entre threads (samples_per_thread = total / num_threads)
  - Créer la fonction worker(samples, lock, shared_counter) pour chaque thread
  - Implémenter la synchronisation avec threading.Lock() pour protéger le compteur partagé
  - Implémenter l'accumulation thread-safe des résultats (with lock:)
  - Mesurer le temps d'exécution total
  - Ajouter des commentaires en français expliquant la synchronisation et les sections critiques
  - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 5.1, 5.2, 5.4, 5.5_

- [x] 4. Checkpoint - Tester manuellement les simulateurs
  - Exécuter monte_carlo_mono.py avec 100k échantillons et vérifier le résultat (~3.14)
  - Exécuter monte_carlo_multi.py avec 100k échantillons et 4 threads
  - Vérifier que les deux donnent des résultats cohérents
  - Demander à l'utilisateur si des questions se posent

- [x] 5. Implémenter l'analyseur de performance
  - Créer le module src/performance_analyzer.py
  - Créer les dataclasses SimulationResult et BenchmarkResults
  - Implémenter run_benchmark(num_samples, num_runs) qui exécute plusieurs runs
  - Implémenter le calcul des statistiques : moyenne, min, max, écart-type (statistics.stdev)
  - Implémenter calculate_speedup(mono_time, multi_time) = mono_time / multi_time
  - Implémenter measure_cpu_usage() avec psutil.cpu_percent()
  - Ajouter la validation des entrées avec messages d'erreur clairs en français
  - Ajouter des commentaires expliquant les calculs statistiques
  - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5_

- [x] 6. Implémenter le générateur de visualisations
  - Créer le module src/visualization.py
  - Implémenter ensure_output_directory() pour créer le dossier results/
  - Implémenter plot_execution_times(results) : graphique en barres comparant mono vs multi (2, 4, 8 threads)
  - Implémenter plot_scalability(results) : graphique ligne montrant temps vs nombre de threads
  - Implémenter plot_monte_carlo_visualization(num_samples) : visualisation des points dans/hors cercle
  - Implémenter plot_speedup_chart(results) : graphique du facteur d'accélération
  - Configurer matplotlib : 300 DPI, style professionnel, labels en français
  - Ajouter des barres d'erreur (écart-type) sur tous les graphiques
  - Ajouter des commentaires expliquant chaque graphique
  - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5_

- [x] 7. Créer le point d'entrée principal
  - Créer main.py avec la fonction main()
  - Configurer les paramètres : NUM_SAMPLES = 1_000_000, NUM_RUNS = 5
  - Implémenter le flux : afficher titre → mono-thread → multi-thread (2,4,8) → analyse → visualisation
  - Ajouter des messages de progression clairs et colorés dans la console (avec emojis)
  - Afficher les résultats formatés : temps, Pi calculé, speedup, utilisation CPU
  - Créer un tableau récapitulatif des résultats dans la console
  - Gérer les erreurs avec try/except et messages clairs en français
  - Ajouter des commentaires expliquant le flux d'exécution
  - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5_

- [x] 8. Checkpoint - Exécuter et vérifier le projet complet
  - Exécuter python main.py et vérifier tous les résultats
  - Vérifier que tous les graphiques sont générés dans results/
  - Vérifier les temps d'exécution et le speedup (doit être > 1.5x avec 4 threads)
  - Vérifier que les graphiques sont clairs et professionnels
  - Demander à l'utilisateur si des ajustements sont nécessaires

- [x] 9. Créer la documentation complète (README.md)
  - **Section 1** : Titre et badges du projet
  - **Section 2** : Description du projet (objectif, contexte académique)
  - **Section 3** : Explication de la méthode Monte Carlo avec schéma ASCII
  - **Section 4** : Principe du multi-threading avec analogie simple (4 personnes comptant des billets)
  - **Section 5** : Prérequis (Python 3.8+, pip)
  - **Section 6** : Installation (commandes pip install)
  - **Section 7** : Utilisation (une seule commande : python main.py)
  - **Section 8** : Structure du projet (arborescence des fichiers avec explications)
  - **Section 9** : Résultats attendus (temps, speedup, description des graphiques)
  - **Section 10** : Avantages du multi-threading (performance, scalabilité, utilisation CPU)
  - **Section 11** : Limitations et défis (overhead, GIL Python, diminishing returns)
  - **Section 12** : Explication technique du code (extraits commentés)
  - **Section 13** : Auteurs (Snaa, Jobrane, Imen) et contexte (projet académique)
  - Utiliser un langage simple, clair, accessible aux débutants
  - Ajouter des emojis pour rendre le README plus engageant
  - _Requirements: 6.1, 6.2, 6.4, 6.5, 7.2, 7.3, 7.4_

- [x] 10. Créer le guide de présentation vidéo (PRESENTATION_GUIDE.md)
  - **Introduction (1 min)** : Speech d'ouverture, présentation de l'équipe
  - **Explication Monte Carlo (2 min)** : Principe simple avec analogie des fléchettes
  - **Démonstration live (3 min)** : Exécuter main.py, montrer les résultats en temps réel
  - **Analyse des graphiques (2 min)** : Expliquer chaque graphique généré
  - **Explication du code (2 min)** : Montrer les parties clés (mono vs multi, synchronisation)
  - **Avantages et limitations (1 min)** : Résumer les gains et les défis
  - **Conclusion (1 min)** : Récapitulatif, questions anticipées
  - Inclure le script complet à lire mot pour mot
  - Inclure les transitions entre sections
  - Inclure les points clés à emphasiser
  - Inclure des conseils pour une présentation convaincante
  - _Requirements: 6.3_

- [x] 11. Créer un script de démonstration rapide (demo_quick.py)
  - Version allégée avec 100k échantillons (30 secondes d'exécution)
  - 3 runs au lieu de 5
  - Affichage simplifié des résultats
  - Utile pour tester rapidement pendant la présentation
  - Ajouter des commentaires expliquant les différences avec main.py
  - _Requirements: 8.1, 8.2_

- [x] 12. Exécuter et capturer les résultats finaux
  - Exécuter python main.py sur une machine multi-cœur
  - Capturer la sortie console complète (copier-coller dans un fichier)
  - Vérifier que tous les graphiques dans results/ sont de haute qualité
  - Créer un fichier RESULTS.md avec les résultats réels et captures d'écran
  - Inclure les timings exacts, le speedup mesuré, et les graphiques
  - _Requirements: 7.5_

- [x] 13. Créer le speech de présentation complet (SPEECH.md)
  - Écrire le script complet de 5-10 minutes
  - Diviser en sections avec timing (Introduction 1min, Monte Carlo 2min, etc.)
  - Inclure les phrases exactes à dire pour chaque partie
  - Inclure les moments où montrer l'écran / le code / les graphiques
  - Inclure les transitions fluides entre sections
  - Inclure les réponses aux questions fréquentes
  - Écrire dans un style naturel et conversationnel
  - _Requirements: 6.3_

- [x] 14. Validation finale et préparation présentation
  - Relire tout le README et vérifier qu'il est complet
  - Pratiquer le speech de présentation (chronométrer)
  - Vérifier que tous les fichiers sont présents et bien organisés
  - Tester l'exécution sur une machine propre si possible
  - Créer une checklist pour la vidéo (quoi filmer, dans quel ordre)
  - Vérifier que les graphiques sont imprimables (haute résolution)
  - S'assurer que tout est prêt pour enregistrer la vidéo
  - _Requirements: All_

## Notes

- Pas de tests unitaires - focus sur la démonstration fonctionnelle
- Configuration simplifiée : 1 million d'itérations, 5 runs
- Tous les commentaires et messages en français
- Code simple et clair pour faciliter l'explication
- Documentation complète pour une présentation convaincante
- Graphiques professionnels haute résolution (300 DPI)
- Speech de présentation détaillé pour la vidéo
