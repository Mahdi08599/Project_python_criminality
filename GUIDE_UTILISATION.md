#  GUIDE D'UTILISATION RAPIDE

## Crime Data Analysis Project - Los Angeles

---

##  Démarrage Ultra-Rapide

### Option 1 : Lanceur Automatique (Recommandé)
```bash
# Dashboard interactif
python launch.py dashboard

# Menu interactif
python launch.py menu

# Test environnement
python launch.py test

# Notebooks Jupyter
python launch.py jupyter
```

### Option 2 : Commandes Directes
```bash
# Dashboard Streamlit
streamlit run streamlit_app.py

# Menu interactif
python scripts/run_project.py

# Test environnement
python scripts/test_environment.py

# Jupyter
jupyter notebook notebooks/
```

---

##  Organisation des Fichiers

```
🏠 Racine du projet
│
├── 📊 data/                  → Toutes les données CSV
├── 📓 notebooks/             → 3 notebooks Jupyter
├── 📈 visualizations/        → Graphiques PNG générés
├── 🐍 scripts/               → Scripts Python utilitaires
├── 📚 docs/                  → Documentation complète
│
├── 🚀 launch.py              → Lanceur rapide
├── 🌐 streamlit_app.py       → Dashboard web
├── 📖 README.md              → Documentation principale
├── 🏗️ ARCHITECTURE.md        → Architecture détaillée
└── 📦 requirements.txt       → Dépendances Python
```

---

##  Accès Rapide aux Composants

###  Dashboard Web
**URL après lancement** : http://localhost:8501

**Fonctionnalités** :
- ✅ Filtres interactifs (année, zone, catégorie)
- ✅ 6 onglets d'analyse
- ✅ Métriques clés colorées
- ✅ Graphiques Plotly interactifs
- ✅ Export CSV

**Lancer** :
```bash
python launch.py dashboard
# ou
streamlit run streamlit_app.py
```

###  Notebooks Jupyter
**Ordre d'exécution** :
1. `notebooks/data_cleaning.ipynb` (2-3 min)
2. `notebooks/data_transformation.ipynb` (3-5 min)
3. `notebooks/exploratory_data_analysis.ipynb` (5-7 min)

**Lancer** :
```bash
python launch.py jupyter
# ou
jupyter notebook notebooks/
```

###  Données
**Fichiers disponibles** :
- `data/Crime_Data_from_2020_to_Present_50k.csv` (Brut - 50k records)
- `data/Crime_Data_Cleaned.csv` (Nettoyé)
- `data/Crime_Data_Transformed.csv` (Transformé - 48 features)
- `data/Crime_Pivot_*.csv` (Tableaux croisés)

---

##  Installation & Configuration

### Prérequis
```bash
Python 3.8+
pip
4GB RAM minimum
500MB espace disque
```

### Installation Complète
```bash
# 1. Cloner le repository
git clone https://github.com/aizakaria/Project_python_criminality.git
cd Project_python_criminality

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Tester l'installation
python launch.py test
# ou
python scripts/test_environment.py

# 4. Lancer le dashboard
python launch.py dashboard
```

---

##  Documentation Complète

### Guides Disponibles
| Document | Description | Chemin |
|----------|-------------|--------|
| **README.md** | Vue d'ensemble | `README.md` |
| **ARCHITECTURE.md** | Architecture détaillée | `ARCHITECTURE.md` |
| **QUICK_START.md** | Démarrage rapide | `docs/QUICK_START.md` |
| **KEY_INSIGHTS_REPORT.md** | Résultats d'analyse | `docs/KEY_INSIGHTS_REPORT.md` |
| **PRESENTATION_GUIDE.md** | Guide présentation | `docs/PRESENTATION_GUIDE.md` |
| **PROJECT_SUMMARY.md** | Résumé complet | `docs/PROJECT_SUMMARY.md` |

### Accès Documentation
```bash
# Ouvrir dans l'éditeur
code docs/

# Lire dans le terminal
cat docs/QUICK_START.md
```

---

##  Commandes Essentielles

### Développement
```bash
# Installer une nouvelle dépendance
pip install package_name
pip freeze > requirements.txt

# Mettre à jour les dépendances
pip install -r requirements.txt --upgrade

# Lancer Jupyter avec un port spécifique
jupyter notebook --port=8888 notebooks/
```

### Git & Version Control
```bash
# Statut
git status

# Ajouter modifications
git add .

# Commit
git commit -m "Description des changements"

# Push vers GitHub
git push origin alaa

# Voir l'historique
git log --oneline
```

### Tests & Validation
```bash
# Test environnement complet
python scripts/test_environment.py

# Vérifier les données
ls -lh data/

# Vérifier les visualisations
ls -lh visualizations/

# Tester un notebook
jupyter nbconvert --execute --to notebook notebooks/data_cleaning.ipynb
```

---

## 🐛 Résolution de Problèmes

### Problème : Module non trouvé
```bash
# Solution
pip install -r requirements.txt
```

### Problème : Fichier de données introuvable
```bash
# Vérifier la structure
ls data/

# Si vide, les fichiers sont peut-être à la racine
# Déplacer vers data/
mv *.csv data/
```

### Problème : Port Streamlit déjà utilisé
```bash
# Utiliser un autre port
streamlit run streamlit_app.py --server.port 8502
```

### Problème : Jupyter kernel mort
```bash
# Redémarrer le kernel
# Dans Jupyter : Kernel > Restart & Clear Output
# Ou
jupyter notebook --debug
```

### Problème : Mémoire insuffisante
```bash
# Réduire la taille des données
head -n 10000 data/Crime_Data_Transformed.csv > data/Crime_Data_Sample.csv

# Modifier le notebook pour utiliser le sample
```

---

## 📊 Visualisations Disponibles

### Dans visualizations/
- `eda_crime_category_distribution.png` - Distribution des catégories
- `eda_top10_crime_types.png` - Top 10 types de crimes
- `eda_time_series_trends.png` - Tendances temporelles
- `eda_geographic_distribution.png` - Distribution géographique
- `eda_temporal_patterns.png` - Patterns temporels
- `eda_victim_demographics.png` - Démographie victimes
- `eda_correlation_heatmap.png` - Corrélations
- `eda_weapon_analysis.png` - Analyse armes
- `eda_severity_by_area.png` - Sévérité par zone
- `eda_year_over_year_trends.png` - Tendances annuelles

---

## 🎓 Cas d'Usage

### Pour une Présentation
```bash
# 1. Lancer le dashboard
python launch.py dashboard

# 2. Ouvrir la documentation
code docs/PRESENTATION_GUIDE.md

# 3. Ouvrir les visualizations
open visualizations/
```

### Pour une Analyse
```bash
# 1. Ouvrir les notebooks
python launch.py jupyter

# 2. Exécuter dans l'ordre
# data_cleaning → data_transformation → EDA

# 3. Consulter les insights
cat docs/KEY_INSIGHTS_REPORT.md
```

### Pour un Développement
```bash
# 1. Tester l'environnement
python launch.py test

# 2. Créer une nouvelle feature
code notebooks/

# 3. Tester localement
streamlit run streamlit_app.py
```

---

## 🌐 URLs Importantes

### Local
- **Dashboard** : http://localhost:8501
- **Jupyter** : http://localhost:8888

### GitHub
- **Repository** : https://github.com/aizakaria/Project_python_criminality
- **Branch** : alaa

### Documentation
- **Streamlit Docs** : https://docs.streamlit.io
- **Pandas Docs** : https://pandas.pydata.org/docs/
- **Scikit-learn** : https://scikit-learn.org/

---

## 📞 Support

### Fichiers d'Aide
- `README.md` - Documentation principale
- `docs/QUICK_START.md` - Démarrage rapide
- `ARCHITECTURE.md` - Architecture détaillée

### Commandes d'Aide
```bash
# Aide launcher
python launch.py help

# Aide Streamlit
streamlit run --help

# Aide Python
python --help
```

---

## ✅ Checklist Démarrage

- [ ] Python 3.8+ installé
- [ ] Dépendances installées (`pip install -r requirements.txt`)
- [ ] Tests passés (`python launch.py test`)
- [ ] Dashboard lancé (`python launch.py dashboard`)
- [ ] Documentation lue (`README.md`, `ARCHITECTURE.md`)
- [ ] Notebooks explorés (`jupyter notebook notebooks/`)

---

**🎉 Projet prêt à l'emploi !**

Pour toute question, consultez la documentation dans `docs/` ou `ARCHITECTURE.md`.
