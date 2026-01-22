# ⚡ COMMANDES RAPIDES

**Les commandes essentielles pour votre présentation**

---

## 🚀 INSTALLATION (À faire AVANT la vidéo)

```bash
# 1. Installer les dépendances
pip install -r requirements.txt

# 2. Tester que tout fonctionne
python demo_quick.py
```

---

## 🎬 PENDANT LA VIDÉO

### Commande 1 : Lancer la Démonstration (Minute 4:00)

```bash
python main.py
```

**Puis appuyer sur ENTRÉE quand demandé**

---

### Commande 2 : Ouvrir les Graphiques (Minute 6:00)

**Windows :**
```bash
explorer results
```

**Mac :**
```bash
open results
```

**Linux :**
```bash
xdg-open results
```

---

### Commande 3 : Ouvrir le Code (Minute 8:00)

**Avec VS Code :**
```bash
code .
```

**OU ouvrir manuellement :**
- `src/monte_carlo_mono.py`
- `src/monte_carlo_multi.py`

---

## 📊 GRAPHIQUES À MONTRER (Dans cet ordre)

1. **Minute 1:00** → `results/monte_carlo_method.png`
2. **Minute 6:00** → `results/execution_times.png`
3. **Minute 6:30** → `results/scalability.png`
4. **Minute 7:00** → `results/speedup.png`

---

## 🎤 PHRASES CLÉS À DIRE

- "4 fois plus rapide !"
- "Chaque point est indépendant"
- "C'est comme avoir plusieurs travailleurs"
- "Speedup de 4x"

---

## ⏱️ TIMING

| Minute | Action |
|--------|--------|
| 0-1 | Introduction |
| 1-3 | Expliquer Monte Carlo + montrer graphique |
| 3-4 | Expliquer multi-threading |
| 4-6 | **COMMANDE : python main.py** |
| 6-8 | Montrer les 4 graphiques |
| 8-9 | Montrer le code |
| 9-10 | Conclusion |

---

## 🆘 EN CAS DE PROBLÈME

### Le programme ne démarre pas
```bash
pip install -r requirements.txt
python --version  # Vérifier Python 3.8+
```

### Les graphiques ne s'affichent pas
```bash
# Vérifier qu'ils existent
dir results  # Windows
ls results   # Mac/Linux
```

### Erreur d'import
```bash
# Réinstaller les dépendances
pip install --upgrade matplotlib psutil
```

---

## ✅ CHECKLIST RAPIDE

- [ ] `pip install -r requirements.txt` ✅
- [ ] `python demo_quick.py` fonctionne ✅
- [ ] Dossier `results/` contient 4 graphiques ✅
- [ ] Vous avez répété le speech ✅
- [ ] Micro et caméra testés ✅

---

**C'EST TOUT ! Vous êtes prêt ! 🚀**
