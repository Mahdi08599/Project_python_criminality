#  PROJECT ARCHITECTURE

## Crime Data Analysis - Los Angeles

Cette documentation décrit l'organisation complète du projet d'analyse des données criminelles de Los Angeles.

---

##  Structure du Projet

```
Project_python_criminality/
│
├── 📊 data/                          # Fichiers de données
│   ├── Crime_Data_from_2020_to_Present_50k.csv (RAW - 50,000 records)
│   ├── Crime_Data_Cleaned.csv        # Données nettoyées
│   ├── Crime_Data_Transformed.csv    # Données transformées (48 features)
│   ├── Crime_Pivot_Area_Time.csv     # Tableau croisé Zone/Temps
│   └── Crime_Pivot_Category_Year.csv # Tableau croisé Catégorie/Année
│
├── 📓 notebooks/                     # Jupyter Notebooks
│   ├── data_cleaning.ipynb           # Phase 1: Nettoyage des données
│   ├── data_transformation.ipynb     # Phase 2: Transformation & Feature Engineering
│   ├── exploratory_data_analysis.ipynb # Phase 3: Analyse exploratoire (EDA)
│   └── predictive_modeling.ipynb     # Phase 4: Modèles prédictifs ML
│
├── 📈 visualizations/                # Graphiques et visualisations (PNG)
│   ├── eda_crime_category_distribution.png
│   ├── eda_top10_crime_types.png
│   ├── eda_time_series_trends.png
│   ├── eda_geographic_distribution.png
│   ├── eda_temporal_patterns.png
│   ├── eda_victim_demographics.png
│   ├── eda_correlation_heatmap.png
│   ├── eda_weapon_analysis.png
│   ├── eda_severity_by_area.png
│   ├── eda_year_over_year_trends.png
│   ├── feature_importance.png
│   ├── model1_crime_category_classification.png
│   ├── model2_crime_severity_prediction.png
│   └── model4_crime_occurrence_prediction.png
│
├── 🤖 models/                        # Modèles ML entraînés (.pkl)
│   ├── crime_category_classifier_model.pkl      # Classification catégories
│   ├── crime_severity_classifier_model.pkl      # Prédiction sévérité
│   ├── weapon_involvement_classifier_model.pkl  # Prédiction armes
│   ├── crime_occurrence_regressor_model.pkl     # Prévision occurrences
│   ├── area_risk_regressor_model.pkl            # Score de risque par zone
│   └── label_encoders.pkl                       # Encodeurs pour déploiement
│
├── 🐍 scripts/                       # Scripts Python utilitaires
│   ├── run_project.py                # Menu interactif principal
│   ├── test_environment.py           # Test d'environnement
│   └── demo_predictions.py           # Démonstration des modèles
│
├── 📚 docs/                          # Documentation complète
│   ├── QUICK_START.md                # Guide de démarrage rapide
│   ├── KEY_INSIGHTS_REPORT.md        # Rapport détaillé des insights
│   ├── PRESENTATION_GUIDE.md         # Guide de présentation
│   └── PROJECT_SUMMARY.md            # Résumé complet du projet
│
├── 🌐 Web Application
│   └── streamlit_app.py              # Dashboard interactif Streamlit
│
├── 📄 Configuration Files
│   ├── README.md                     # Documentation principale
│   ├── requirements.txt              # Dépendances Python
│   ├── ARCHITECTURE.md               # Architecture du projet (ce fichier)
│   └── .gitignore                    # Fichiers ignorés par Git
│
└── 🗂️ Version Control
    └── .git/                         # Dépôt Git
```

---

##  Workflow du Projet

### 1️⃣ Phase de Préparation des Données
```
Crime_Data_from_2020_to_Present_50k.csv (RAW)
            ↓
    [data_cleaning.ipynb]
            ↓
    Crime_Data_Cleaned.csv
            ↓
    [data_transformation.ipynb]
            ↓
    Crime_Data_Transformed.csv + Pivot Tables
```

### 2️⃣ Phase d'Analyse Exploratoire
```
Crime_Data_Transformed.csv
            ↓
    [exploratory_data_analysis.ipynb]
            ↓
    10+ Visualizations PNG
    + Statistical Insights
```

### 3️⃣ Phase de Modélisation Prédictive
```
Crime_Data_Transformed.csv
            ↓
    [predictive_modeling.ipynb]
            ↓
    5 ML Models (.pkl files)
    + Performance Metrics
    + Feature Importance
```

### 4️⃣ Phase de Déploiement
```
Models + Data
      ↓
[streamlit_app.py]
      ↓
Interactive Dashboard
(localhost:8501)
```

---

##  Détails des Composants

### 📁 Data (data/)
| Fichier | Taille | Description | Usage |
|---------|--------|-------------|-------|
| `Crime_Data_from_2020_to_Present_50k.csv` | ~15MB | Données brutes | Source initiale |
| `Crime_Data_Cleaned.csv` | ~12MB | Données nettoyées | Post-cleaning |
| `Crime_Data_Transformed.csv` | ~18MB | 48 features | ML & Dashboard |
| `Crime_Pivot_Area_Time.csv` | ~500KB | Agrégation zone/temps | Analyse rapide |
| `Crime_Pivot_Category_Year.csv` | ~300KB | Agrégation catégorie/année | Tendances |

### 📓 Notebooks (notebooks/)
| Notebook | Cellules | Durée d'exécution | Output |
|----------|----------|-------------------|--------|
| `data_cleaning.ipynb` | ~15 | 2-3 min | Cleaned CSV |
| `data_transformation.ipynb` | ~20 | 3-5 min | Transformed CSV + Pivots |
| `exploratory_data_analysis.ipynb` | ~25 | 5-7 min | 10 PNG + Stats |
| `predictive_modeling.ipynb` | ~30 | 10-15 min | 5 Models + Metrics |

### 🤖 Models (models/)
| Model | Type | Accuracy/Score | Size | Input Features |
|-------|------|----------------|------|----------------|
| Crime Category Classifier | Random Forest | 85%+ F1 | ~5MB | 45 features |
| Crime Severity Classifier | Gradient Boosting | 88%+ AUC-ROC | ~3MB | 42 features |
| Weapon Involvement | Random Forest | 82%+ F1 | ~4MB | 40 features |
| Crime Occurrence | RF Regressor | 75%+ R² | ~6MB | 48 features |
| Area Risk Score | GB Regressor | 80%+ R² | ~4MB | 35 features |

### 🐍 Scripts (scripts/)
| Script | Lignes | Fonction | Usage |
|--------|--------|----------|-------|
| `run_project.py` | 200+ | Menu interactif | `python scripts/run_project.py` |
| `test_environment.py` | 150+ | Validation setup | `python scripts/test_environment.py` |
| `demo_predictions.py` | 300+ | Démo modèles | `python scripts/demo_predictions.py` |

### 📚 Documentation (docs/)
| Document | Pages | Contenu |
|----------|-------|---------|
| `QUICK_START.md` | 3 | Installation & Démarrage rapide |
| `KEY_INSIGHTS_REPORT.md` | 15+ | Analyses détaillées & Recommandations |
| `PRESENTATION_GUIDE.md` | 10+ | Structure présentation 20 slides |
| `PROJECT_SUMMARY.md` | 12+ | Résumé complet du projet |

---

##  Guide d'Utilisation

### Installation Initiale
```bash
# 1. Cloner le repository
git clone https://github.com/aizakaria/Project_python_criminality.git
cd Project_python_criminality

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Tester l'environnement
python scripts/test_environment.py
```

### Exécution des Notebooks (Ordre recommandé)
```bash
# Lancer Jupyter
jupyter notebook

# Exécuter dans l'ordre:
# 1. notebooks/data_cleaning.ipynb
# 2. notebooks/data_transformation.ipynb
# 3. notebooks/exploratory_data_analysis.ipynb
# 4. notebooks/predictive_modeling.ipynb
```

### Lancer le Dashboard
```bash
# Option 1: Directement
streamlit run streamlit_app.py

# Option 2: Via le menu interactif
python scripts/run_project.py
# Puis sélectionner option 1
```

### Tester les Modèles
```bash
# Démonstration avec exemples pré-définis
python scripts/demo_predictions.py
```

---

##  Configuration Requise

### Environnement Python
- **Python**: 3.8 ou supérieur
- **RAM**: Minimum 4GB, recommandé 8GB
- **Espace disque**: ~500MB pour données + modèles
- **OS**: Windows, macOS, Linux

### Dépendances Principales
```
streamlit >= 1.28.0      # Dashboard interactif
pandas >= 2.0.0          # Manipulation de données
numpy >= 1.24.0          # Calculs numériques
scikit-learn >= 1.3.0    # Machine Learning
plotly >= 5.17.0         # Visualisations interactives
matplotlib >= 3.7.0      # Graphiques statiques
seaborn >= 0.12.0        # Visualisations statistiques
statsmodels >= 0.14.0    # Modèles statistiques
```

---

##  Métriques du Projet

### Statistiques des Données
- **Total des enregistrements**: 50,000+
- **Période couverte**: 2020-2023
- **Zones géographiques**: 21 areas
- **Types de crimes**: 140+
- **Features créées**: 48

### Performance des Modèles
- **Modèles développés**: 5
- **Précision moyenne**: 82%+
- **Meilleur modèle**: Crime Severity (88% AUC-ROC)
- **Temps d'entraînement total**: ~15 minutes

### Code & Documentation
- **Lignes de code Python**: ~2,500+
- **Cellules de notebooks**: ~90+
- **Visualisations générées**: 13+
- **Pages de documentation**: 40+

---

##  Points d'Entrée du Projet

### Pour l'Analyse
1. **Notebooks** → `notebooks/exploratory_data_analysis.ipynb`
2. **Insights** → `docs/KEY_INSIGHTS_REPORT.md`

### Pour le ML
1. **Entraînement** → `notebooks/predictive_modeling.ipynb`
2. **Démo** → `scripts/demo_predictions.py`

### Pour la Visualisation
1. **Dashboard** → `streamlit_app.py`
2. **Images** → `visualizations/`

### Pour la Documentation
1. **Démarrage** → `docs/QUICK_START.md`
2. **Vue d'ensemble** → `README.md`
3. **Présentation** → `docs/PRESENTATION_GUIDE.md`

---

##  Sécurité & Bonnes Pratiques

### Fichiers Ignorés (.gitignore)
```
# Environnements virtuels
venv/
env/
.venv/

# Cache Python
__pycache__/
*.pyc
*.pyo

# Jupyter
.ipynb_checkpoints/

# IDE
.vscode/
.idea/

# Données sensibles (si applicable)
*.secret
.env
```

### Gestion des Modèles
- Modèles sauvegardés avec `joblib` (pickle sécurisé)
- Versioning des modèles recommandé
- Checkpoints réguliers pendant l'entraînement

---

##  Support & Contact

### Structure de l'Équipe
- **Data Cleaning**: notebooks/data_cleaning.ipynb
- **Feature Engineering**: notebooks/data_transformation.ipynb
- **EDA & Visualizations**: notebooks/exploratory_data_analysis.ipynb
- **ML Modeling**: notebooks/predictive_modeling.ipynb
- **Dashboard Development**: streamlit_app.py
- **Documentation**: docs/

### Ressources
- **GitHub**: https://github.com/aizakaria/Project_python_criminality
- **Branch**: alaa
- **Documentation**: docs/
- **Issue Tracker**: GitHub Issues

---

##  Mise à Jour de l'Architecture

**Dernière mise à jour**: 18 Novembre 2025  
**Version du projet**: 1.0  
**Status**: Production Ready ✅

---

##  Notes d'Architecture

### Design Patterns Utilisés
1. **Separation of Concerns**: Données, notebooks, scripts, docs séparés
2. **DRY (Don't Repeat Yourself)**: Fonctions réutilisables dans scripts
3. **Modularity**: Chaque notebook = phase distincte
4. **Documentation First**: Docs complètes avant déploiement

### Scalabilité
- ✅ Supporte des datasets plus larges (ajuster chunksize)
- ✅ Modèles peuvent être réentraînés facilement
- ✅ Dashboard peut gérer filtres dynamiques
- ✅ Architecture extensible pour nouveaux modèles

### Maintenance
- 📅 Réentraînement modèles: Mensuel recommandé
- 🔄 Mise à jour données: Selon disponibilité source
- 🐛 Bug fixes: Via GitHub Issues
- 📊 Monitoring: Logs Streamlit pour usage dashboard

---

** Architecture Complète et Organisée !**

Tous les composants sont clairement organisés et documentés pour une utilisation optimale.
