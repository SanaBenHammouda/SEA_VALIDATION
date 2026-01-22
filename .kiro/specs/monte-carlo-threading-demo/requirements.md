# Requirements Document

## Introduction

Ce projet démontre les avantages du multi-threading en comparant deux implémentations d'une simulation Monte Carlo pour calculer Pi : une version mono-thread (séquentielle) et une version multi-thread (parallèle). Le projet inclut des mesures de performance, des visualisations graphiques, et une documentation complète pour une présentation académique.

## Glossary

- **System**: L'application de démonstration Monte Carlo
- **Mono_Thread_Simulator**: Le module qui exécute la simulation de manière séquentielle
- **Multi_Thread_Simulator**: Le module qui exécute la simulation avec plusieurs threads parallèles
- **Performance_Analyzer**: Le composant qui mesure et compare les temps d'exécution
- **Visualization_Generator**: Le composant qui crée les graphiques de résultats
- **User**: L'utilisateur qui exécute la démonstration (étudiant, professeur)

## Requirements

### Requirement 1: Simulation Monte Carlo Mono-Thread

**User Story:** En tant qu'utilisateur, je veux exécuter une simulation Monte Carlo séquentielle pour calculer Pi, afin d'avoir une référence de performance de base.

#### Acceptance Criteria

1. WHEN a user launches the mono-thread simulation with N iterations, THE Mono_Thread_Simulator SHALL generate N random points and calculate Pi sequentially
2. WHEN the simulation completes, THE Mono_Thread_Simulator SHALL return the calculated Pi value and execution time
3. THE Mono_Thread_Simulator SHALL use a single thread for all computations
4. WHEN generating random points, THE Mono_Thread_Simulator SHALL use coordinates between -1 and 1
5. THE Mono_Thread_Simulator SHALL count points inside the unit circle and calculate Pi using the formula: Pi ≈ 4 × (points_inside / total_points)

### Requirement 2: Simulation Monte Carlo Multi-Thread

**User Story:** En tant qu'utilisateur, je veux exécuter une simulation Monte Carlo parallèle pour calculer Pi, afin de démontrer les gains de performance du multi-threading.

#### Acceptance Criteria

1. WHEN a user launches the multi-thread simulation with N iterations and T threads, THE Multi_Thread_Simulator SHALL distribute N iterations across T threads
2. WHEN threads execute in parallel, THE Multi_Thread_Simulator SHALL ensure thread-safe accumulation of results
3. WHEN the simulation completes, THE Multi_Thread_Simulator SHALL return the calculated Pi value and execution time
4. THE Multi_Thread_Simulator SHALL use mutex/locks to prevent race conditions on shared variables
5. WHEN all threads complete, THE Multi_Thread_Simulator SHALL aggregate results from all threads correctly

### Requirement 3: Mesure et Analyse de Performance

**User Story:** En tant qu'utilisateur, je veux mesurer précisément les temps d'exécution des deux versions, afin de quantifier les gains de performance du multi-threading.

#### Acceptance Criteria

1. WHEN a simulation runs, THE Performance_Analyzer SHALL measure execution time with millisecond precision
2. WHEN multiple runs are executed, THE Performance_Analyzer SHALL calculate average time, minimum time, maximum time, and standard deviation
3. THE Performance_Analyzer SHALL execute at least 10 runs for each configuration to ensure statistical validity
4. WHEN comparing versions, THE Performance_Analyzer SHALL calculate the speedup ratio (mono_time / multi_time)
5. THE Performance_Analyzer SHALL measure CPU usage during execution

### Requirement 4: Visualisation des Résultats

**User Story:** En tant qu'utilisateur, je veux voir des graphiques clairs des résultats, afin de comprendre visuellement les différences de performance.

#### Acceptance Criteria

1. WHEN results are available, THE Visualization_Generator SHALL create a bar chart comparing execution times (mono vs multi)
2. WHEN testing with different thread counts, THE Visualization_Generator SHALL create a line graph showing scalability
3. WHEN displaying results, THE Visualization_Generator SHALL include error bars showing standard deviation
4. THE Visualization_Generator SHALL create a visualization of the Monte Carlo simulation (points inside/outside circle)
5. THE Visualization_Generator SHALL save all graphs as PNG files with high resolution (300 DPI minimum)

### Requirement 5: Gestion de la Synchronisation

**User Story:** En tant que développeur, je veux gérer correctement la synchronisation entre threads, afin d'éviter les race conditions et garantir des résultats corrects.

#### Acceptance Criteria

1. WHEN multiple threads access shared variables, THE Multi_Thread_Simulator SHALL use locks/mutex to protect critical sections
2. WHEN threads write to shared counters, THE Multi_Thread_Simulator SHALL ensure atomic operations or proper locking
3. IF a race condition is detected, THEN THE System SHALL prevent incorrect results
4. THE Multi_Thread_Simulator SHALL avoid deadlocks by using proper lock ordering
5. WHEN threads complete, THE Multi_Thread_Simulator SHALL properly release all locks and resources

### Requirement 6: Documentation et Présentation

**User Story:** En tant qu'utilisateur, je veux une documentation complète et claire, afin de comprendre le projet et pouvoir le présenter facilement.

#### Acceptance Criteria

1. THE System SHALL provide a README.md file with complete installation instructions
2. THE README SHALL include clear commands to run all demonstrations
3. THE README SHALL include a presentation speech explaining the project step-by-step
4. WHEN code is written, THE System SHALL include comments explaining each important section
5. THE README SHALL explain the Monte Carlo method in simple terms for non-technical audiences

### Requirement 7: Comparaison des Avantages

**User Story:** En tant qu'utilisateur, je veux voir clairement les avantages du multi-threading, afin de comprendre quand et pourquoi l'utiliser.

#### Acceptance Criteria

1. THE System SHALL demonstrate performance advantages (speedup with multiple threads)
2. THE System SHALL show resource usage differences (CPU cores utilization)
3. THE System SHALL explain scalability (performance vs number of threads)
4. THE System SHALL document limitations (overhead, diminishing returns with too many threads)
5. THE System SHALL provide concrete timing measurements proving the gains

### Requirement 8: Exécution et Tests

**User Story:** En tant qu'utilisateur, je veux exécuter facilement toutes les démonstrations, afin de voir les résultats sans complications techniques.

#### Acceptance Criteria

1. THE System SHALL provide a single command to run the complete demonstration
2. WHEN executed, THE System SHALL run both mono-thread and multi-thread versions automatically
3. WHEN tests complete, THE System SHALL display results in the console with clear formatting
4. THE System SHALL generate all graphs automatically without user intervention
5. WHEN errors occur, THE System SHALL display clear error messages with solutions
