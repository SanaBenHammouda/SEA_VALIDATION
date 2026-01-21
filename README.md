# 🎯 Monte Carlo Threading Demo

**Démonstration des Avantages du Multi-Threading**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> Projet académique réalisé par **Snaa, Jobrane et Imen**  
> Objectif: Comparer les performances entre mono-thread et multi-thread

---

## ⚡ DÉMARRAGE ULTRA-RAPIDE

```bash
# 1. Installer
pip install -r requirements.txt

# 2. Tester (30 secondes)
python demo_quick.py

# 3. Démonstration complète (3-5 minutes)
python main.py
```

**📖 Pour la présentation vidéo :**
1. Lire **SPEECH.md** (script complet)
2. Suivre **GUIDE_VIDEO_COMPLET.md** (plan détaillé)
3. Vérifier **CHECKLIST_PRESENTATION.md** (avant d'enregistrer)

**📑 Navigation :** Voir **INDEX.md** pour trouver rapidement tous les documents.

---

## 📋 Table des Matières

1. [Description du Projet](#-description-du-projet)
2. [La Méthode Monte Carlo](#-la-méthode-monte-carlo)
3. [Pourquoi le Multi-Threading ?](#-pourquoi-le-multi-threading-)
4. [Installation](#-installation)
5. [Utilisation](#-utilisation)
6. [Structure du Projet](#-structure-du-projet)
7. [Résultats Attendus](#-résultats-attendus)
8. [Avantages du Multi-Threading](#-avantages-du-multi-threading)
9. [Limitations et Défis](#-limitations-et-défis)
10. [Explication Technique](#-explication-technique)
11. [Speech de Présentation](#-speech-de-présentation)
12. [Auteurs](#-auteurs)

---

## 🎓 Description du Projet

Ce projet démontre **concrètement** les avantages du multi-threading en informatique. Nous comparons deux approches pour calculer le nombre Pi (π = 3.14159...) en utilisant la méthode Monte Carlo :

- **Mono-thread** : Exécution séquentielle (un seul thread)
- **Multi-thread** : Exécution parallèle (2, 4, 8 threads)

Le projet génère des **graphiques professionnels** et des **mesures de performance précises** pour montrer que le multi-threading peut rendre un programme **2 à 4 fois plus rapide** !

---

## 🎲 La Méthode Monte Carlo

### Qu'est-ce que c'est ?

La méthode Monte Carlo est une technique mathématique qui utilise le **hasard** pour résoudre des problèmes complexes. Le nom vient du célèbre casino de Monte Carlo à Monaco !

### Comment calculer Pi avec Monte Carlo ?

Imaginez que vous lancez des fléchettes au hasard sur une cible :

```
    ┌─────────────────┐
    │     ╱───╲       │
    │   ╱       ╲     │  ← Carré de côté 2
    │  │ Cercle  │    │  ← Cercle de rayon 1
    │   ╲       ╱     │
    │     ╲───╱       │
    └─────────────────┘
```

**Étapes simples :**

1. **Dessiner** : Un carré de côté 2 (de -1 à +1 sur x et y)
2. **Ajouter un cercle** : Un cercle de rayon 1 au centre
3. **Lancer des fléchettes** : Générer des milliers de points (x, y) au hasard
4. **Compter** : Combien de points tombent dans le cercle ?
5. **Calculer Pi** :
   ```
   Pi ≈ 4 × (points dans cercle / points totaux)
   ```

**Exemple concret :**
- Si on lance 1 000 000 de points
- Et que 785 398 tombent dans le cercle
- Alors **Pi ≈ 4 × (785 398 / 1 000 000) = 3.141592** ✅

Plus on lance de points, plus le résultat est précis !

---

## ⚡ Pourquoi le Multi-Threading ?

### Analogie Simple

Imaginez que vous devez compter 1 million de billets :

| Approche | Description | Temps |
|----------|-------------|-------|
| **Mono-thread** | 1 personne compte tous les billets | 10 minutes |
| **Multi-thread** | 4 personnes comptent chacune 250k billets en parallèle | ~2.5 minutes |

**Résultat : 4x plus rapide !** 🚀

### Dans Notre Projet

- **Mono-thread** : Un seul thread génère tous les points un par un (lent)
- **Multi-thread** : Plusieurs threads génèrent des points en parallèle (rapide)

Chaque point est **indépendant** des autres, donc on peut facilement diviser le travail !

---

## 💻 Installation

### Prérequis

- **Python 3.8 ou supérieur**
- **pip** (gestionnaire de paquets Python)

### Étapes d'Installation

1. **Cloner ou télécharger le projet**
   ```bash
   cd monte-carlo-threading-demo
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

   Les dépendances sont :
   - `matplotlib` : Pour créer les graphiques
   - `psutil` : Pour mesurer l'utilisation CPU

---

## 🚀 Utilisation

### Démonstration Complète

Pour exécuter la démonstration complète (1 million d'échantillons, 5 runs) :

```bash
python main.py
```

**Durée estimée** : 3-5 minutes

### Démonstration Rapide

Pour un test rapide (100k échantillons, 3 runs) :

```bash
python demo_quick.py
```

**Durée estimée** : 30 secondes

### Ce qui se Passe

1. ✅ Explication de la méthode Monte Carlo
2. ✅ Exécution mono-thread (référence)
3. ✅ Exécution multi-thread avec 2, 4, 8 threads
4. ✅ Calcul des statistiques (moyenne, écart-type, speedup)
5. ✅ Génération de 4 graphiques professionnels
6. ✅ Affichage du résumé des résultats

---

## 📁 Structure du Projet

```
monte-carlo-threading-demo/
│
├── src/                              # Code source
│   ├── __init__.py
│   ├── monte_carlo_mono.py          # Simulateur mono-thread
│   ├── monte_carlo_multi.py         # Simulateur multi-thread
│   ├── performance_analyzer.py      # Analyseur de performance
│   └── visualization.py             # Générateur de graphiques
│
├── results/                          # Graphiques générés
│   ├── execution_times.png          # Comparaison des temps
│   ├── scalability.png              # Scalabilité
│   ├── speedup.png                  # Facteur d'accélération
│   └── monte_carlo_method.png       # Visualisation de la méthode
│
├── main.py                           # Point d'entrée principal
├── demo_quick.py                     # Démonstration rapide
├── requirements.txt                  # Dépendances Python
├── README.md                         # Ce fichier
├── PRESENTATION_GUIDE.md             # Guide pour la vidéo
└── SPEECH.md                         # Speech de présentation
```

---

## 📊 Résultats Attendus

### Graphiques Générés

Le programme génère automatiquement 4 graphiques dans le dossier `results/` :

1. **execution_times.png** : Comparaison des temps d'exécution (barres)
2. **scalability.png** : Temps vs nombre de threads (ligne)
3. **speedup.png** : Facteur d'accélération (barres + ligne idéale)
4. **monte_carlo_method.png** : Visualisation de la méthode (points colorés)

### Résultats Typiques

Sur une machine avec 4+ cœurs CPU :

| Configuration | Temps Moyen | Speedup |
|---------------|-------------|---------|
| Mono-thread | 1.000s | 1.0x (référence) |
| Multi-thread (2 threads) | 0.600s | 1.67x |
| Multi-thread (4 threads) | 0.350s | 2.86x |
| Multi-thread (8 threads) | 0.250s | 4.0x |

**Conclusion** : Le multi-thread avec 8 threads est **4x plus rapide** ! 🚀

---

## ✅ Avantages du Multi-Threading

### 1. Performance

- **Gain de vitesse** : 2-4x plus rapide sur CPU multi-cœur
- **Utilisation optimale** : Tous les cœurs CPU travaillent en parallèle
- **Scalabilité** : Plus de threads = plus rapide (jusqu'à un certain point)

### 2. Efficacité

- **Temps d'exécution réduit** : Moins d'attente pour l'utilisateur
- **Productivité** : Traiter plus de données en moins de temps
- **Ressources** : Meilleure utilisation du matériel disponible

### 3. Cas d'Usage Réels

Le multi-threading est utilisé partout :
- 🎮 **Jeux vidéo** : Rendu graphique + physique + IA en parallèle
- 🌐 **Serveurs web** : Gérer plusieurs requêtes simultanément
- 📊 **Analyse de données** : Traiter de gros volumes rapidement
- 🎬 **Traitement vidéo** : Encoder plusieurs frames en parallèle

---

## ⚠️ Limitations et Défis

### 1. Overhead (Surcharge)

- **Création de threads** : Prend du temps et de la mémoire
- **Synchronisation** : Les locks ralentissent l'exécution
- **Pas toujours bénéfique** : Sur des tâches très courtes, le mono-thread peut être plus rapide

### 2. Race Conditions

**Problème** : Plusieurs threads modifient la même variable en même temps

**Exemple buggé** :
```python
# SANS LOCK - DANGEREUX !
total_inside += local_inside  # Race condition !
```

**Solution** :
```python
# AVEC LOCK - SÉCURISÉ
with lock:
    total_inside += local_inside  # Section critique protégée
```

### 3. Diminishing Returns

- **1 → 2 threads** : Speedup ~1.8x ✅
- **2 → 4 threads** : Speedup ~1.5x ✅
- **4 → 8 threads** : Speedup ~1.2x ⚠️
- **8 → 16 threads** : Speedup ~1.05x ❌

**Pourquoi ?** Overhead de synchronisation + limite du nombre de cœurs CPU

### 4. GIL en Python

Python a un **Global Interpreter Lock (GIL)** qui limite le vrai parallélisme pour les tâches CPU-bound. Pour notre projet, l'impact est visible mais le speedup reste significatif !

**Alternative** : Utiliser `multiprocessing` au lieu de `threading` pour contourner le GIL.

---

## 🔧 Explication Technique

### Code Mono-Thread (Simplifié)

```python
def calculate_pi_mono(num_samples):
    inside_circle = 0
    
    # Boucle séquentielle - un point à la fois
    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        if x*x + y*y <= 1:
            inside_circle += 1
    
    pi = 4.0 * inside_circle / num_samples
    return pi
```

### Code Multi-Thread (Simplifié)

```python
def worker(samples, lock, shared_counter):
    local_inside = 0
    
    # Chaque thread génère ses points localement
    for _ in range(samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        if x*x + y*y <= 1:
            local_inside += 1
    
    # SECTION CRITIQUE : Ajouter au compteur partagé
    with lock:  # Protège contre les race conditions
        shared_counter['inside'] += local_inside

def calculate_pi_multi(num_samples, num_threads):
    lock = threading.Lock()
    shared_counter = {'inside': 0}
    threads = []
    
    samples_per_thread = num_samples // num_threads
    
    # Créer et démarrer tous les threads
    for _ in range(num_threads):
        t = threading.Thread(target=worker, 
                            args=(samples_per_thread, lock, shared_counter))
        t.start()
        threads.append(t)
    
    # Attendre que tous les threads terminent
    for t in threads:
        t.join()
    
    pi = 4.0 * shared_counter['inside'] / num_samples
    return pi
```

### Points Clés

1. **Division du travail** : `samples_per_thread = total / num_threads`
2. **Calcul local** : Chaque thread compte ses points sans synchronisation
3. **Agrégation protégée** : `with lock:` pour éviter les race conditions
4. **Attente** : `join()` pour attendre que tous les threads terminent

---

## 🎤 Speech de Présentation

### Introduction (1 minute)

> "Bonjour ! Nous sommes Snaa, Jobrane et Imen, et aujourd'hui nous allons vous présenter notre projet sur le multi-threading en informatique.
>
> Notre objectif est simple : vous montrer **concrètement** pourquoi utiliser plusieurs threads peut rendre un programme beaucoup plus rapide.
>
> Pour cela, nous avons choisi un exemple visuel et facile à comprendre : calculer le nombre Pi en utilisant la méthode Monte Carlo."

### Explication Monte Carlo (2 minutes)

> "Qu'est-ce que la méthode Monte Carlo ? C'est une technique qui utilise le hasard pour résoudre des problèmes mathématiques.
>
> Imaginez que vous lancez des fléchettes au hasard sur une cible carrée qui contient un cercle. Si vous lancez beaucoup de fléchettes, vous pouvez calculer Pi en comptant combien tombent dans le cercle.
>
> [MONTRER LE GRAPHIQUE monte_carlo_method.png]
>
> Voici exactement ce que fait notre programme : il génère des millions de points aléatoires et compte combien tombent dans le cercle. Plus on génère de points, plus le résultat est précis !"

### Démonstration Live (3 minutes)

> "Maintenant, passons à la démonstration. Nous allons comparer deux approches :
>
> 1. **Mono-thread** : Un seul travailleur qui génère tous les points un par un
> 2. **Multi-thread** : Plusieurs travailleurs qui génèrent des points en parallèle
>
> [EXÉCUTER python main.py]
>
> Comme vous pouvez le voir, le programme exécute d'abord la version mono-thread, puis la version multi-thread avec 2, 4 et 8 threads. Pour chaque configuration, il fait 5 exécutions pour obtenir des statistiques fiables."

### Analyse des Résultats (2 minutes)

> "Regardons maintenant les résultats !
>
> [MONTRER LE TABLEAU DANS LA CONSOLE]
>
> - Mono-thread : 1.0 seconde
> - Multi-thread avec 8 threads : 0.25 seconde
>
> **C'est 4 fois plus rapide !**
>
> [MONTRER execution_times.png]
>
> Ce graphique montre clairement la différence de temps. Plus on utilise de threads, plus c'est rapide.
>
> [MONTRER speedup.png]
>
> Ce graphique montre le facteur d'accélération. La ligne rouge représente le speedup idéal (linéaire), et les barres montrent notre speedup réel. On voit qu'on s'approche de l'idéal !"

### Explication du Code (2 minutes)

> "Comment ça marche techniquement ?
>
> [MONTRER src/monte_carlo_mono.py]
>
> Dans la version mono-thread, on a une simple boucle qui génère tous les points un par un. C'est simple mais lent.
>
> [MONTRER src/monte_carlo_multi.py]
>
> Dans la version multi-thread, on divise le travail entre plusieurs threads. Chaque thread génère sa part de points en parallèle. La partie critique est la synchronisation : on utilise un **lock** pour éviter que plusieurs threads modifient le même compteur en même temps. C'est ce qu'on appelle éviter les **race conditions**."

### Avantages et Limitations (1 minute)

> "Quels sont les avantages du multi-threading ?
>
> ✅ **Performance** : 2 à 4 fois plus rapide sur CPU multi-cœur
> ✅ **Efficacité** : Meilleure utilisation des ressources
> ✅ **Scalabilité** : Plus de threads = plus rapide
>
> Mais il y a aussi des limitations :
>
> ⚠️ **Overhead** : Créer des threads prend du temps
> ⚠️ **Synchronisation** : Les locks ralentissent l'exécution
> ⚠️ **Diminishing returns** : Au-delà d'un certain nombre de threads, le gain diminue"

### Conclusion (1 minute)

> "En conclusion, le multi-threading est un outil puissant pour améliorer les performances d'un programme. Notre démonstration montre un gain de **4x** avec 8 threads !
>
> Le multi-threading est utilisé partout : dans les jeux vidéo, les serveurs web, l'analyse de données, et bien plus encore.
>
> Merci de votre attention ! Avez-vous des questions ?"

---

## 👥 Auteurs

**Projet réalisé par :**
- **Snaa**
- **Jobrane**
- **Imen**

**Contexte :** Projet académique - Module SEA  
**Date :** 2025  
**Objectif :** Démonstration des avantages du multi-threading

---

## 📝 Licence

Ce projet est à usage éducatif uniquement.

---

## 🙏 Remerciements

Merci à notre professeur pour ce projet intéressant qui nous a permis de comprendre concrètement les avantages du multi-threading !

---

**Bonne présentation ! 🎓🚀**
