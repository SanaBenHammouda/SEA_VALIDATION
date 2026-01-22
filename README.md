# 🎯 Monte Carlo Threading  🎯

**Démonstration des Avantages du Multi-Threading**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> Projet académique réalisé par **Sana , Jobrane et Imen**  
> Objectif: Comparer les performances entre mono-thread et multi-thread

---

## ⚡ DÉMARRAGE 

```bash
# 1. Installer
pip install -r requirements.txt

# 2. Tester (30 secondes)
python demo_quick.py

# 3. Démonstration complète (3-5 minutes)
python main.py
```
 

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

---<img width="2848" height="2965" alt="monte_carlo_method" src="https://github.com/user-attachments/assets/6e273cdc-829f-4601-9c64-d3b1b4836270" />


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
 <img width="2967" height="1765" alt="execution_times" src="https://github.com/user-attachments/assets/8a341b9a-8663-44c8-abc0-8d71a733ac3f" />

3. **scalability.png** : Temps vs nombre de threads (ligne)
 <img width="2967" height="1765" alt="scalability" src="https://github.com/user-attachments/assets/3feadb67-5ee2-48d4-a7b6-6c6c65f42705" />

5. **speedup.png** : Facteur d'accélération (barres + ligne idéale)
   <img width="2967" height="1766" alt="speedup" src="https://github.com/user-attachments/assets/ebf72b8e-c5fe-4923-9b1a-5d6de42bcbde" />

7. **monte_carlo_method.png** : Visualisation de la méthode (points colorés)


## ✅ Avantages du Multi-Threading

### 1. Performance

- **Gain de vitesse** : 2-4x plus rapide sur CPU multi-cœur
- **Utilisation optimale** : Tous les cœurs CPU travaillent en parallèle
- **Scalabilité** : Plus de threads = plus rapide (jusqu'à un certain point)

### 2. Efficacité

- **Temps d'exécution réduit** : Moins d'attente pour l'utilisateur
- **Productivité** : Traiter plus de données en moins de temps
- **Ressources** : Meilleure utilisation du matériel disponible

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


## 👥 Auteurs

**Projet réalisé par :**
- **Sana Ben Hammouda**
- **Mohamed Jobrane Ben Salah **
- **Imen Sebteoui **

**Contexte :** Projet académique - Module SEA  
**Date :** 2025  
**Objectif :** Démonstration des avantages du multi-threading

---

## 🙏 Remerciements

Merci à notre professeur pour ce projet intéressant qui nous a permis de comprendre concrètement les avantages du multi-threading !

---
