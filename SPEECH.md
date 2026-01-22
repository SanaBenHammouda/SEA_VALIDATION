# 🎤 Speech de Présentation Complet

**Monte Carlo Threading Demo - Script Détaillé (5-10 minutes)**

> Ce document contient le script complet à lire pendant votre présentation vidéo.  
> Timing total : 10 minutes  
> Divisé en 7 sections avec timing précis

---

## 📌 Instructions d'Utilisation

- **Lisez naturellement** : Ne récitez pas comme un robot
- **Faites des pauses** : Respirez entre les phrases
- **Montrez de l'enthousiasme** : Souriez et variez le ton
- **Synchronisez avec l'écran** : Montrez ce dont vous parlez
- **Pratiquez** : Répétez plusieurs fois avant d'enregistrer

---

## 🎬 Section 1 : Introduction (0:00 - 1:00)

### À Montrer à l'Écran
- Vous-même (caméra) ou slide de titre
- Titre du projet : "Monte Carlo Threading Demo"

### Script

"Bonjour à tous !

Nous sommes Snaa, Jobrane et Imen, et aujourd'hui nous sommes ravis de vous présenter notre projet sur le multi-threading en informatique.

Notre objectif est simple mais important : vous montrer **concrètement** pourquoi utiliser plusieurs threads peut rendre un programme beaucoup plus rapide.

Pour démontrer cela, nous avons choisi un exemple à la fois visuel et facile à comprendre : calculer le nombre Pi - vous savez, 3.14159... - en utilisant une méthode appelée Monte Carlo.

Ne vous inquiétez pas si vous ne connaissez pas cette méthode, nous allons tout vous expliquer de manière simple et claire.

Alors, c'est parti !"

---

## 🎲 Section 2 : Explication de Monte Carlo (1:00 - 3:00)

### À Montrer à l'Écran
- Graphique `results/monte_carlo_method.png` (TRÈS IMPORTANT)
- Schéma du carré et du cercle

### Script

"Commençons par expliquer ce qu'est la méthode Monte Carlo.

La méthode Monte Carlo est une technique mathématique qui utilise le **hasard** pour résoudre des problèmes complexes. Le nom vient du célèbre casino de Monte Carlo à Monaco, parce que la méthode repose sur la génération de nombres aléatoires, un peu comme au casino !

Mais comment peut-on calculer Pi avec du hasard ? C'est en fait assez ingénieux.

Imaginez que vous avez une cible carrée, et qu'à l'intérieur de ce carré, il y a un cercle parfait. Maintenant, imaginez que vous lancez des fléchettes au hasard sur cette cible. Certaines fléchettes vont tomber dans le cercle, d'autres en dehors.

Si vous lancez beaucoup, beaucoup de fléchettes, le ratio entre le nombre de fléchettes dans le cercle et le nombre total de fléchettes va vous donner une approximation de Pi divisé par 4.

Pourquoi ? Parce que mathématiquement, le ratio entre l'aire du cercle et l'aire du carré est égal à Pi sur 4.

Donc, si on multiplie ce ratio par 4, on obtient Pi !

[MONTRER LE GRAPHIQUE monte_carlo_method.png]

Voici exactement ce que fait notre programme. Vous voyez tous ces points ? Les points rouges sont ceux qui sont tombés dans le cercle, et les points bleus sont ceux qui sont en dehors.

Notre programme génère des millions de ces points aléatoires, compte combien sont dans le cercle, et calcule Pi avec la formule :

Pi ≈ 4 × (points dans cercle / points totaux)

Plus on génère de points, plus le résultat est précis ! Avec 1 million de points, on obtient Pi avec 4 à 6 décimales correctes. C'est impressionnant, non ?

Et le meilleur dans tout ça ? Chaque point est complètement **indépendant** des autres. Ça veut dire qu'on peut facilement diviser le travail entre plusieurs threads. C'est là que le multi-threading entre en jeu !"

---

## ⚡ Section 3 : Explication du Multi-Threading (3:00 - 4:00)

### À Montrer à l'Écran
- Schéma ou animation : 1 personne vs 4 personnes
- Slide avec l'analogie des billets

### Script

"Maintenant, parlons du multi-threading. Pourquoi est-ce si important ?

Laissez-moi vous donner une analogie très simple.

Imaginez que vous devez compter 1 million de billets de banque. Si vous êtes tout seul, ça va vous prendre... disons 10 minutes. C'est long, c'est ennuyeux, et vous allez probablement perdre le compte à un moment donné !

Mais maintenant, imaginez que vous êtes 4 personnes. Vous divisez les billets en 4 piles de 250 000 billets chacune. Chaque personne compte sa pile en parallèle. À la fin, vous additionnez les résultats.

Combien de temps ça va prendre ? Environ 2 minutes et demie ! Vous venez de gagner 7 minutes et demie, soit un gain de 4 fois !

C'est **exactement** le principe du multi-threading en informatique :

- **Mono-thread**, c'est comme avoir une seule personne qui fait tout le travail, un par un, séquentiellement.

- **Multi-thread**, c'est comme avoir plusieurs personnes qui travaillent en parallèle sur des parties différentes du problème.

Dans notre cas avec Monte Carlo :
- Le mono-thread génère tous les points aléatoires un par un
- Le multi-thread divise le travail : un thread génère 250 000 points, un autre 250 000 points, et ainsi de suite, tous en même temps !

Et comme chaque point est indépendant, il n'y a pas de problème de coordination complexe. C'est le cas idéal pour le multi-threading !"

---

## 🚀 Section 4 : Démonstration Live (4:00 - 6:00)

### À Montrer à l'Écran
- Terminal en plein écran
- Exécution de `python main.py`
- Résultats en temps réel

### Script

"Bon, assez de théorie ! Passons à la pratique avec une démonstration en direct.

[OUVRIR LE TERMINAL]

Je vais maintenant exécuter notre programme principal. Il va comparer les performances entre mono-thread et multi-thread.

[TAPER : python main.py]

Comme vous pouvez le voir, le programme commence par nous expliquer brièvement la méthode Monte Carlo et le principe du multi-threading.

[APPUYER SUR ENTRÉE]

Et maintenant, le benchmark commence !

Le programme va d'abord exécuter la version mono-thread. Il va générer 1 million de points aléatoires, un par un, et calculer Pi. Pour avoir des statistiques fiables, il va faire ça 5 fois.

[ATTENDRE LES RÉSULTATS MONO-THREAD]

Voilà ! La version mono-thread a terminé. Vous voyez les 5 runs avec leurs temps respectifs. En moyenne, ça a pris environ 1 seconde.

Maintenant, le programme passe à la version multi-thread. Il va tester avec 2 threads, puis 4 threads, puis 8 threads.

[ATTENDRE LES RÉSULTATS MULTI-THREAD 2]

Avec 2 threads, on voit déjà une amélioration ! Le temps moyen est d'environ 0.6 seconde. Le programme calcule automatiquement le 'speedup', c'est-à-dire le facteur d'accélération. Ici, on a un speedup de 1.67x. Pas mal !

[ATTENDRE LES RÉSULTATS MULTI-THREAD 4]

Avec 4 threads, c'est encore mieux ! On est passé à environ 0.35 seconde. Le speedup est maintenant de 2.86x. On commence à voir les vrais bénéfices du multi-threading !

[ATTENDRE LES RÉSULTATS MULTI-THREAD 8]

Et enfin, avec 8 threads... Wow ! On est descendu à 0.25 seconde ! Le speedup est de 4x. Ça veut dire qu'on est **4 fois plus rapide** qu'avec le mono-thread !

[MONTRER LE TABLEAU RÉCAPITULATIF]

Voici le tableau récapitulatif. On voit clairement la progression : plus on utilise de threads, plus c'est rapide. Et regardez la précision de Pi : dans tous les cas, on obtient 3.14159... avec plusieurs décimales correctes.

Le programme a également généré automatiquement des graphiques professionnels. Allons les voir !"

---

## 📊 Section 5 : Analyse des Graphiques (6:00 - 8:00)

### À Montrer à l'Écran
- Dossier `results/`
- Chaque graphique un par un

### Script

"Le programme a créé 4 graphiques dans le dossier 'results'. Regardons-les ensemble.

[OUVRIR results/execution_times.png]

Premier graphique : la comparaison des temps d'exécution.

C'est un graphique en barres qui montre très clairement la différence entre les configurations. La barre rouge, c'est le mono-thread. Les barres bleues, vertes et violettes, ce sont les versions multi-thread avec 2, 4 et 8 threads.

Vous voyez comme la hauteur des barres diminue ? Ça montre visuellement que le temps d'exécution diminue avec plus de threads.

Les petites barres noires au-dessus, ce sont les barres d'erreur. Elles montrent l'écart-type, c'est-à-dire la variabilité entre les différentes exécutions. Plus elles sont petites, plus les résultats sont stables.

[OUVRIR results/scalability.png]

Deuxième graphique : la scalabilité.

C'est une courbe qui montre comment le temps d'exécution évolue quand on augmente le nombre de threads. Idéalement, on voudrait une ligne droite qui descend rapidement. Et c'est presque ce qu'on obtient !

On voit que de 1 à 4 threads, la descente est assez linéaire. De 4 à 8 threads, ça continue de descendre mais un peu moins vite. C'est normal, c'est ce qu'on appelle les 'diminishing returns' - les rendements décroissants.

[OUVRIR results/speedup.png]

Troisième graphique : le facteur d'accélération, ou 'speedup'.

Les barres colorées montrent notre speedup réel pour chaque configuration. La ligne rouge pointillée, c'est le speedup idéal, parfaitement linéaire.

Avec 2 threads, on a un speedup de 1.67x. Avec 4 threads, 2.86x. Et avec 8 threads, 4x !

On voit qu'on s'approche de la ligne idéale, surtout avec 4 et 8 threads. C'est excellent ! Ça montre que notre implémentation du multi-threading est efficace.

[OUVRIR results/monte_carlo_method.png]

Et enfin, le quatrième graphique : la visualisation de la méthode Monte Carlo.

C'est mon graphique préféré parce qu'il est très visuel et facile à comprendre. Vous voyez le carré noir ? C'est notre zone de lancement de fléchettes. Le cercle noir au milieu, c'est notre cible.

Les points rouges sont ceux qui sont tombés dans le cercle. Les points bleus sont ceux qui sont en dehors.

En bas à gauche, il y a un petit encadré qui donne les statistiques : combien de points dans le cercle, combien au total, le ratio, et la valeur de Pi calculée.

C'est parfait pour expliquer visuellement comment fonctionne la méthode Monte Carlo !"

---

## 💻 Section 6 : Explication du Code (8:00 - 9:00)

### À Montrer à l'Écran
- Fichier `src/monte_carlo_mono.py`
- Fichier `src/monte_carlo_multi.py`
- Sections clés du code

### Script

"Maintenant, regardons rapidement le code pour comprendre comment tout ça fonctionne techniquement.

[OUVRIR src/monte_carlo_mono.py]

Voici le code de la version mono-thread. C'est assez simple.

On a une boucle 'for' qui va de 0 à num_samples. Pour chaque itération, on génère un point aléatoire avec des coordonnées x et y entre -1 et 1.

Ensuite, on vérifie si le point est dans le cercle avec la formule x² + y² ≤ 1. Si c'est le cas, on incrémente notre compteur.

À la fin, on calcule Pi avec la formule 4 × (inside_circle / num_samples).

C'est simple, c'est clair, mais c'est lent parce que tout est fait séquentiellement.

[OUVRIR src/monte_carlo_multi.py]

Maintenant, la version multi-thread. C'est un peu plus complexe.

On commence par diviser le travail. Si on a 1 million de points et 4 threads, chaque thread va générer 250 000 points.

Ensuite, on crée une fonction 'worker' qui va être exécutée par chaque thread. Cette fonction génère ses points localement, sans synchronisation. C'est important pour la performance !

[MONTRER LA FONCTION WORKER]

Chaque thread compte ses points dans une variable locale. Pas de problème de synchronisation ici.

Mais à la fin, il faut bien additionner les résultats de tous les threads. Et c'est là qu'on a besoin de synchronisation.

[MONTRER LA SECTION CRITIQUE]

Vous voyez ce 'with lock:' ? C'est ce qu'on appelle une section critique. Le 'lock' garantit qu'un seul thread à la fois peut exécuter ce code.

Pourquoi c'est important ? Parce que si deux threads essaient de modifier 'shared_counter' en même temps, on peut avoir ce qu'on appelle une 'race condition' - une condition de course. Le résultat serait incorrect.

Avec le lock, on évite ce problème. C'est un peu comme un feu rouge : un seul thread peut passer à la fois.

[MONTRER LA CRÉATION DES THREADS]

Ensuite, on crée tous les threads avec 'threading.Thread', on les démarre avec 'start()', et on attend qu'ils terminent avec 'join()'.

Une fois que tous les threads ont terminé, on peut calculer Pi avec le total agrégé.

Et voilà ! C'est comme ça qu'on implémente le multi-threading en Python."

---

## 🎯 Section 7 : Conclusion (9:00 - 10:00)

### À Montrer à l'Écran
- Retour sur vous-même (caméra)
- Slide de conclusion avec les points clés

### Script

"Alors, qu'est-ce qu'on retient de tout ça ?

Notre projet démontre clairement les avantages du multi-threading :

**Premièrement, la performance.** On a obtenu un speedup de 4x avec 8 threads. Ça veut dire qu'on a divisé le temps d'exécution par 4 ! C'est énorme quand on travaille avec de gros volumes de données.

**Deuxièmement, l'efficacité.** On utilise mieux les ressources de notre ordinateur. Au lieu d'avoir 7 cœurs CPU qui ne font rien pendant que 1 seul travaille, on les fait tous travailler en parallèle.

**Troisièmement, la scalabilité.** Plus on a de cœurs CPU, plus on peut aller vite. C'est parfait pour les serveurs modernes qui ont 16, 32, ou même 64 cœurs !

Mais il faut aussi être honnête sur les limitations :

**L'overhead.** Créer des threads prend du temps et de la mémoire. Sur des tâches très courtes, le mono-thread peut être plus rapide.

**La synchronisation.** Les locks ralentissent l'exécution. Il faut trouver le bon équilibre entre parallélisme et synchronisation.

**Les diminishing returns.** Au-delà d'un certain nombre de threads, le gain diminue. On ne peut pas juste ajouter des threads à l'infini.

Mais malgré ces limitations, le multi-threading reste un outil extrêmement puissant et largement utilisé dans l'informatique moderne.

Vous le retrouvez partout :
- Dans les **jeux vidéo**, pour gérer le rendu graphique, la physique et l'intelligence artificielle en parallèle
- Dans les **serveurs web**, pour traiter plusieurs requêtes simultanément
- Dans l'**analyse de données**, pour traiter de gros volumes rapidement
- Dans le **traitement d'images et de vidéos**, pour encoder plusieurs frames en parallèle

Notre démonstration avec la méthode Monte Carlo est un exemple parfait de tâche parallélisable : chaque point est indépendant, donc on peut facilement diviser le travail.

En conclusion, le multi-threading, c'est comme avoir plusieurs travailleurs au lieu d'un seul. Quand c'est bien fait, ça peut rendre votre programme 2, 3, 4 fois plus rapide, voire plus !

Nous espérons que cette démonstration vous a aidé à comprendre concrètement les avantages du multi-threading.

Merci beaucoup de votre attention ! Nous sommes maintenant prêts à répondre à vos questions."

---

## 📝 Notes Finales

### Timing Récapitulatif

- **0:00 - 1:00** : Introduction (1 min)
- **1:00 - 3:00** : Explication Monte Carlo (2 min)
- **3:00 - 4:00** : Explication Multi-Threading (1 min)
- **4:00 - 6:00** : Démonstration Live (2 min)
- **6:00 - 8:00** : Analyse des Graphiques (2 min)
- **8:00 - 9:00** : Explication du Code (1 min)
- **9:00 - 10:00** : Conclusion (1 min)

**Total : 10 minutes**

### Conseils de Présentation

✅ **Respirez** : Prenez des pauses naturelles  
✅ **Souriez** : Montrez votre enthousiasme  
✅ **Regardez la caméra** : Créez une connexion avec l'audience  
✅ **Variez le ton** : Ne soyez pas monotone  
✅ **Montrez ce dont vous parlez** : Synchronisez avec l'écran  

### Phrases Clés à Emphasizer

- "4 fois plus rapide !"
- "Chaque point est indépendant"
- "C'est comme avoir plusieurs travailleurs"
- "Le multi-threading est utilisé partout"
- "Speedup de 4x"

---

**Bonne chance pour votre présentation ! Vous allez assurer ! 🚀**
