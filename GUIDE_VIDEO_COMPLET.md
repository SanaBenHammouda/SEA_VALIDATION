# 🎬 GUIDE VIDÉO COMPLET - ÉTAPE PAR ÉTAPE

**Monte Carlo Threading Demo - Script + Commandes + Écran**

> Ce guide vous dit EXACTEMENT quoi dire, quoi taper, et quoi montrer à chaque moment de la vidéo.

---

## 📌 AVANT DE COMMENCER

### Préparation de l'Écran

1. **Ouvrir ces fenêtres :**
   - Terminal (plein écran)
   - Dossier `results/` (pour les graphiques)
   - Éditeur de code avec `src/monte_carlo_mono.py` et `src/monte_carlo_multi.py`
   - Ce fichier (GUIDE_VIDEO_COMPLET.md) pour suivre

2. **Naviguer vers le projet :**
   ```bash
   cd monte-carlo-threading-demo
   ```

3. **Tester que tout fonctionne :**
   ```bash
   python demo_quick.py
   ```

---

## 🎥 MINUTE 0:00 - 1:00 : INTRODUCTION

### 🎬 À MONTRER
- Vous-même (caméra) OU slide avec titre du projet

### 🎤 À DIRE

```
"Bonjour à tous !

Nous sommes Snaa, Jobrane et Imen, et aujourd'hui nous allons vous 
présenter notre projet sur le multi-threading en informatique.

Notre objectif est simple : vous montrer CONCRÈTEMENT pourquoi utiliser 
plusieurs threads peut rendre un programme beaucoup plus rapide.

Pour cela, nous avons choisi un exemple visuel et facile à comprendre : 
calculer le nombre Pi en utilisant la méthode Monte Carlo.

Ne vous inquiétez pas si vous ne connaissez pas cette méthode, nous 
allons tout vous expliquer !

Alors, c'est parti !"
```

### 💻 COMMANDE
Aucune commande pour cette section.

---

## 🎥 MINUTE 1:00 - 3:00 : EXPLICATION MONTE CARLO

### 🎬 À MONTRER
1. **D'abord** : Ouvrir le dossier `results/`
2. **Ensuite** : Afficher le graphique `monte_carlo_method.png` en GRAND

### 🎤 À DIRE

```
"Qu'est-ce que la méthode Monte Carlo ?

C'est une technique mathématique qui utilise le HASARD pour résoudre 
des problèmes complexes. Le nom vient du casino de Monte Carlo !

Imaginez que vous lancez des fléchettes au hasard sur une cible carrée 
qui contient un cercle.

[MONTRER LE GRAPHIQUE monte_carlo_method.png]

Voici exactement ce que fait notre programme !

Vous voyez tous ces points ?
- Les points ROUGES sont dans le cercle
- Les points BLEUS sont en dehors

Notre programme génère des millions de points aléatoires, compte combien 
sont dans le cercle, et calcule Pi avec cette formule :

Pi ≈ 4 × (points dans cercle / points totaux)

Avec 1 million de points, on obtient Pi avec 4 à 6 décimales correctes !

Et le meilleur ? Chaque point est INDÉPENDANT des autres. On peut 
facilement diviser le travail entre plusieurs threads !"
```

### 💻 COMMANDE
```bash
# Ouvrir le dossier results/ dans l'explorateur de fichiers
# Puis double-cliquer sur monte_carlo_method.png
```

### 📸 CAPTURE D'ÉCRAN
Montrer le graphique en plein écran pendant 10-15 secondes.

---

## 🎥 MINUTE 3:00 - 4:00 : EXPLICATION MULTI-THREADING

### 🎬 À MONTRER
- Slide ou dessin simple : 1 personne vs 4 personnes
- OU simplement vous-même qui expliquez avec les mains

### 🎤 À DIRE

```
"Maintenant, pourquoi le multi-threading ?

Imaginez que vous devez compter 1 million de billets.

Si vous êtes SEUL : ça prend 10 minutes.

Si vous êtes 4 PERSONNES qui comptent chacune 250 000 billets en 
parallèle : ça prend 2 minutes et demie !

Vous venez de gagner 4 fois en vitesse !

C'est EXACTEMENT le principe du multi-threading :

- MONO-THREAD = 1 personne qui fait tout, un par un
- MULTI-THREAD = 4 personnes qui travaillent en parallèle

Dans notre cas :
- Mono-thread : génère tous les points un par un (lent)
- Multi-thread : plusieurs threads génèrent des points en parallèle (rapide)

Et comme chaque point est indépendant, c'est le cas IDÉAL pour le 
multi-threading !"
```

### 💻 COMMANDE
Aucune commande pour cette section.

---

## 🎥 MINUTE 4:00 - 6:00 : DÉMONSTRATION LIVE

### 🎬 À MONTRER
- Terminal en PLEIN ÉCRAN
- Résultats qui s'affichent en temps réel

### 🎤 À DIRE

```
"Passons à la démonstration en direct !

[MONTRER LE TERMINAL]

Je vais exécuter notre programme principal qui va comparer les 
performances entre mono-thread et multi-thread.
```

### 💻 COMMANDE 1
```bash
python main.py
```

### 🎤 CONTINUER À DIRE

```
Le programme nous explique d'abord la méthode Monte Carlo et le 
multi-threading.

[ATTENDRE L'AFFICHAGE]

Maintenant, il nous demande d'appuyer sur Entrée pour commencer.
```

### 💻 COMMANDE 2
```bash
# Appuyer sur ENTRÉE
```

### 🎤 CONTINUER À DIRE

```
Le benchmark commence !

D'abord, la version MONO-THREAD. Il va générer 1 million de points, 
5 fois, pour avoir des statistiques fiables.

[ATTENDRE LES 5 RUNS MONO-THREAD]

Voilà ! Mono-thread terminé. En moyenne : environ 1 seconde.

Maintenant, MULTI-THREAD avec 2 threads...

[ATTENDRE LES RÉSULTATS]

Avec 2 threads : 0.6 seconde. Speedup de 1.67x !

Maintenant avec 4 threads...

[ATTENDRE LES RÉSULTATS]

Avec 4 threads : 0.35 seconde. Speedup de 2.86x !

Et enfin avec 8 threads...

[ATTENDRE LES RÉSULTATS]

Avec 8 threads : 0.25 seconde. Speedup de 4x !

C'est 4 FOIS PLUS RAPIDE qu'avec le mono-thread !

[MONTRER LE TABLEAU RÉCAPITULATIF]

Voici le tableau qui résume tout. On voit clairement : plus de threads 
= plus rapide !

Le programme génère maintenant les graphiques...

[ATTENDRE LA FIN]

Parfait ! Tous les graphiques sont générés. Allons les voir !
```

### 📸 CAPTURE D'ÉCRAN
- Capturer le tableau récapitulatif final
- Laisser visible 5-10 secondes

---

## 🎥 MINUTE 6:00 - 8:00 : ANALYSE DES GRAPHIQUES

### 🎬 À MONTRER
Ouvrir le dossier `results/` et montrer chaque graphique UN PAR UN.

### 💻 COMMANDE
```bash
# Ouvrir l'explorateur de fichiers
# Naviguer vers results/
```

---

### 📊 GRAPHIQUE 1 : execution_times.png

### 🎤 À DIRE

```
"Premier graphique : comparaison des temps d'exécution.

[OUVRIR execution_times.png]

C'est un graphique en barres. Vous voyez comme les barres diminuent ?

- Barre ROUGE : mono-thread (le plus lent)
- Barres BLEUES/VERTES/VIOLETTES : multi-thread (de plus en plus rapide)

Les petites barres noires au-dessus sont les barres d'erreur. Elles 
montrent la variabilité entre les exécutions.

Plus c'est bas, plus c'est rapide !"
```

### 📸 CAPTURE D'ÉCRAN
Montrer le graphique en plein écran pendant 10 secondes.

---

### 📊 GRAPHIQUE 2 : scalability.png

### 🎤 À DIRE

```
"Deuxième graphique : la scalabilité.

[OUVRIR scalability.png]

Cette courbe montre comment le temps évolue quand on augmente le nombre 
de threads.

Idéalement, on voudrait une ligne qui descend rapidement. Et c'est 
presque ce qu'on obtient !

De 1 à 4 threads : descente rapide.
De 4 à 8 threads : ça continue mais moins vite.

C'est normal, c'est ce qu'on appelle les 'diminishing returns'."
```

### 📸 CAPTURE D'ÉCRAN
Montrer le graphique en plein écran pendant 10 secondes.

---

### 📊 GRAPHIQUE 3 : speedup.png

### 🎤 À DIRE

```
"Troisième graphique : le facteur d'accélération.

[OUVRIR speedup.png]

Les barres colorées montrent notre speedup RÉEL.
La ligne rouge pointillée montre le speedup IDÉAL (linéaire).

Avec 2 threads : 1.67x
Avec 4 threads : 2.86x
Avec 8 threads : 4x !

On s'approche de la ligne idéale. C'est excellent !"
```

### 📸 CAPTURE D'ÉCRAN
Montrer le graphique en plein écran pendant 10 secondes.

---

### 📊 GRAPHIQUE 4 : monte_carlo_method.png

### 🎤 À DIRE

```
"Et le dernier graphique : visualisation de la méthode Monte Carlo.

[OUVRIR monte_carlo_method.png]

C'est mon préféré ! Très visuel.

Le carré noir : notre zone de lancement.
Le cercle noir : notre cible.
Points rouges : dans le cercle.
Points bleus : en dehors.

En bas à gauche, les statistiques : nombre de points, ratio, et Pi calculé.

Parfait pour expliquer visuellement la méthode !"
```

### 📸 CAPTURE D'ÉCRAN
Montrer le graphique en plein écran pendant 10 secondes.

---

## 🎥 MINUTE 8:00 - 9:00 : EXPLICATION DU CODE

### 🎬 À MONTRER
Ouvrir l'éditeur de code avec les fichiers sources.

### 💻 COMMANDE
```bash
# Ouvrir VS Code ou votre éditeur
code .
# OU simplement ouvrir les fichiers dans un éditeur
```

---

### 📄 FICHIER 1 : monte_carlo_mono.py

### 🎤 À DIRE

```
"Regardons le code pour comprendre comment ça marche.

[OUVRIR src/monte_carlo_mono.py]

Voici la version MONO-THREAD. C'est simple.

Une boucle 'for' qui génère tous les points un par un.

Pour chaque point :
- On génère x et y aléatoires entre -1 et 1
- On vérifie si x² + y² ≤ 1
- Si oui, on incrémente le compteur

À la fin, on calcule Pi = 4 × (inside / total).

Simple, clair, mais LENT."
```

### 📸 CAPTURE D'ÉCRAN
Montrer le code, zoomer sur la boucle principale.

---

### 📄 FICHIER 2 : monte_carlo_multi.py

### 🎤 À DIRE

```
"Maintenant, la version MULTI-THREAD.

[OUVRIR src/monte_carlo_multi.py]

C'est plus complexe.

On divise le travail : 1 million de points ÷ 4 threads = 250 000 par thread.

Chaque thread a sa fonction 'worker' qui génère ses points LOCALEMENT.

[MONTRER LA FONCTION WORKER]

Pas de synchronisation ici, c'est rapide !

Mais à la fin, il faut additionner les résultats.

[MONTRER LA SECTION CRITIQUE]

Vous voyez ce 'with lock:' ?

C'est une SECTION CRITIQUE. Le lock garantit qu'un seul thread à la 
fois peut modifier le compteur partagé.

Pourquoi ? Pour éviter les RACE CONDITIONS.

Si deux threads modifient en même temps, le résultat serait incorrect.

Avec le lock, on évite ce problème. C'est comme un feu rouge : un seul 
thread passe à la fois."
```

### 📸 CAPTURE D'ÉCRAN
Montrer le code, zoomer sur la section critique avec le lock.

---

## 🎥 MINUTE 9:00 - 10:00 : CONCLUSION

### 🎬 À MONTRER
- Retour sur vous-même (caméra)
- OU slide de conclusion

### 🎤 À DIRE

```
"En conclusion, qu'est-ce qu'on retient ?

Notre projet démontre clairement les AVANTAGES du multi-threading :

✅ PERFORMANCE : Speedup de 4x avec 8 threads
✅ EFFICACITÉ : Meilleure utilisation des ressources CPU
✅ SCALABILITÉ : Plus de threads = plus rapide

Mais aussi les LIMITATIONS :

⚠️ OVERHEAD : Créer des threads prend du temps
⚠️ SYNCHRONISATION : Les locks ralentissent
⚠️ DIMINISHING RETURNS : Au-delà d'un certain nombre, le gain diminue

Le multi-threading est utilisé PARTOUT :
- Jeux vidéo
- Serveurs web
- Analyse de données
- Traitement d'images

Notre démonstration avec Monte Carlo montre parfaitement comment diviser 
une tâche en sous-tâches indépendantes pour gagner en performance.

Merci de votre attention ! Nous sommes prêts à répondre à vos questions."
```

### 💻 COMMANDE
Aucune commande pour cette section.

---

## 📝 RÉSUMÉ DES COMMANDES

### Commandes à Exécuter Pendant la Vidéo

```bash
# 1. Naviguer vers le projet
cd monte-carlo-threading-demo

# 2. Exécuter le programme principal (Minute 4:00)
python main.py

# 3. Appuyer sur ENTRÉE quand demandé

# 4. Ouvrir le dossier results/ (Minute 6:00)
# (Utiliser l'explorateur de fichiers)

# 5. Ouvrir l'éditeur de code (Minute 8:00)
code .
# OU ouvrir manuellement les fichiers
```

---

## 📊 ORDRE D'AFFICHAGE DES GRAPHIQUES

1. **monte_carlo_method.png** (Minute 1:00) - Pour expliquer la méthode
2. **execution_times.png** (Minute 6:00) - Comparaison des temps
3. **scalability.png** (Minute 6:30) - Scalabilité
4. **speedup.png** (Minute 7:00) - Facteur d'accélération
5. **monte_carlo_method.png** (Minute 7:30) - Rappel de la méthode

---

## 🎯 POINTS CLÉS À EMPHASIZER

### Phrases à Dire avec ÉNERGIE

- "4 FOIS PLUS RAPIDE !" 🚀
- "Chaque point est INDÉPENDANT" ✅
- "C'est comme avoir plusieurs travailleurs" 👥
- "Le multi-threading est utilisé PARTOUT" 🌍
- "Speedup de 4x" 📈

---

## ⏱️ TIMING RÉCAPITULATIF

| Minute | Section | Commande | Écran |
|--------|---------|----------|-------|
| 0:00-1:00 | Introduction | Aucune | Vous / Titre |
| 1:00-3:00 | Monte Carlo | Ouvrir results/ | monte_carlo_method.png |
| 3:00-4:00 | Multi-Threading | Aucune | Vous / Slide |
| 4:00-6:00 | Démo Live | `python main.py` | Terminal |
| 6:00-8:00 | Graphiques | Ouvrir images | 4 graphiques |
| 8:00-9:00 | Code | `code .` | Fichiers .py |
| 9:00-10:00 | Conclusion | Aucune | Vous / Slide |

---

## ✅ CHECKLIST AVANT D'ENREGISTRER

- [ ] Terminal ouvert et dans le bon dossier
- [ ] Dossier results/ accessible
- [ ] Éditeur de code prêt
- [ ] Ce guide ouvert pour suivre
- [ ] Micro et caméra testés
- [ ] Notifications désactivées
- [ ] Vous avez répété au moins 1 fois

---

## 🎬 CONSEILS FINAUX

### Pendant l'Enregistrement

✅ **Respirez** : Prenez des pauses naturelles  
✅ **Souriez** : Montrez votre enthousiasme  
✅ **Parlez lentement** : Articulez bien  
✅ **Montrez ce dont vous parlez** : Synchronisez avec l'écran  
✅ **Variez le ton** : Ne soyez pas monotone  

### Si Vous Faites une Erreur

- **Ne paniquez pas** : C'est normal !
- **Faites une pause** : Respirez
- **Reprenez** : Recommencez la phrase
- **Montage** : Vous pourrez couper au montage

---

## 🚀 VOUS ÊTES PRÊT !

Suivez ce guide étape par étape et vous allez faire une présentation PARFAITE !

**Bonne chance Snaa, Jobrane et Imen ! 🎓✨**

---

**Projet** : Monte Carlo Threading Demo  
**Auteurs** : Snaa, Jobrane, Imen  
**Date** : 2025
