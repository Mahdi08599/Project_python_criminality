#  Guide de Démarrage Rapide - Dashboard Criminalité LA

##  Accès Rapide

### Lancer l'application
```bash
streamlit run streamlit_app.py
```

### Ouvrir dans le navigateur
```
http://localhost:8501
```

---

##  Les 5 Choses à Savoir

### 1.  Commencez par Lire "À propos du projet"
Cliquez sur la section extensible en haut de la page pour comprendre :
- L'objectif du dashboard
- Les données analysées
- Comment l'utiliser

### 2.  Utilisez les Filtres (Barre Latérale Gauche)
- **Années** : Sélectionnez la période d'analyse
- **Zones** : Choisissez les quartiers de Los Angeles
- **Crimes** : Filtrez par type de criminalité
- **Horaires** : Analysez par moment de la journée
- **Armes** : Isolez les crimes avec ou sans armes

💡 **Astuce** : Le compteur en bas des filtres montre combien d'incidents correspondent à vos critères

### 3.  Explorez les 6 Onglets
Chaque onglet offre une perspective différente :

| Onglet | Contenu |
|--------|---------|
| 📊 Vue d'Ensemble | Distribution générale des crimes |
| 🗺️ Analyse Géographique | Où se passent les crimes ? |
| ⏰ Tendances Temporelles | Quand se passent les crimes ? |
| 👥 Profil des Victimes | Qui sont les victimes ? |
| 🔫 Analyse des Armes | Quelles armes sont utilisées ? |
| 📈 Corrélations | Relations entre variables |

### 4.  Interagissez avec les Graphiques
- **Survolez** les éléments pour voir les détails
- **Cliquez** sur les légendes pour filtrer
- **Zoomez** sur les cartes et graphiques
- **Lisez** les messages colorés (insights automatiques)

### 5.  Exportez Vos Données
En bas de la barre latérale :
- Cliquez sur "📥 Télécharger en CSV"
- Le fichier contient toutes les données filtrées
- Format compatible Excel, Python, R, etc.

---

## Comprendre les Couleurs

### Cartes KPIs (en haut)
- **Violet** 🟣 : Total des crimes
- **Rose** 🩷 : Âge moyen des victimes
- **Orange** 🟠 : Taux d'armes
- **Bleu foncé** 🔵 : Zones touchées
- **Cyan** 🔷 : Délai de signalement

### Messages
- **🟢 Vert** : Information positive
- **🟡 Jaune** : Attention, point important
- **🔴 Rouge** : Alerte, situation critique
- **🔵 Bleu** : Information neutre

---

##  Exemples d'Analyses Possibles

### Analyse 1 : "Quels sont les quartiers les plus dangereux en 2023 ?"
1. Filtre **Année** : Sélectionner uniquement 2023
2. Onglet **🗺️ Analyse Géographique**
3. Regarder le graphique "Top 15 des Zones"
4. Résultat affiché immédiatement

### Analyse 2 : "À quelle heure les vols sont-ils les plus fréquents ?"
1. Filtre **Type de crime** : Sélectionner "Property Crimes" ou "Theft"
2. Onglet **⏰ Tendances Temporelles**
3. Regarder le graphique "Par Heure"
4. Consulter la carte de chaleur Jour × Heure

### Analyse 3 : "Les crimes avec armes touchent-ils plus les jeunes ?"
1. Filtre **Armes** : "Avec armes uniquement"
2. Onglet **👥 Profil des Victimes**
3. Regarder "Distribution par Tranche d'Âge"
4. Comparer avec tous les crimes (réinitialiser les filtres)

### Analyse 4 : "Y a-t-il une corrélation entre revenu et criminalité ?"
1. Onglet **📈 Corrélations & Tendances**
2. Regarder le scatter plot "Revenu Médian vs Nombre de Crimes"
3. Observer la ligne de tendance
4. Consulter la matrice de corrélation

---

##  Raccourcis Clavier

- **R** : Recharger l'application (après modification des filtres)
- **Ctrl/Cmd + clic** : Ouvrir un lien dans un nouvel onglet
- **Échap** : Fermer les popups/dialogs

---

##  FAQ - Questions Fréquentes

### Q : Pourquoi certains graphiques mettent du temps à charger ?
**R** : Le dashboard analyse plus de 50 000 incidents. Les calculs peuvent prendre quelques secondes selon vos filtres.

### Q : Puis-je voir tous les crimes sur la carte ?
**R** : Pour des raisons de performance, la carte affiche un échantillon de 5 000 points maximum. Tous les autres graphiques utilisent l'ensemble des données.

### Q : Comment revenir à la vue initiale ?
**R** : Cliquez sur "🔄 Réinitialiser tous les filtres" en bas de la barre latérale.

### Q : Les données sont-elles mises à jour automatiquement ?
**R** : Non, les données datent du dernier chargement du fichier CSV. Pour mettre à jour, remplacez le fichier source et relancez l'application.

### Q : Puis-je partager mes filtres avec quelqu'un ?
**R** : Actuellement non, mais vous pouvez noter vos critères et les partager textuellement, ou prendre des captures d'écran.

### Q : Le dashboard fonctionne-t-il hors ligne ?
**R** : Oui, une fois lancé localement, il fonctionne sans connexion internet.

---

##  Résolution de Problèmes

### Problème : L'application ne se lance pas
```bash
# Vérifier que Streamlit est installé
pip install streamlit

# Vérifier que vous êtes dans le bon dossier
cd /Users/salam/Documents/GitHub/Project_python_criminality

# Relancer
streamlit run streamlit_app.py
```

### Problème : "ModuleNotFoundError"
```bash
# Installer toutes les dépendances
pip install -r requirements.txt
```

### Problème : Les graphiques ne s'affichent pas
- Rafraîchir la page (F5)
- Vider le cache du navigateur
- Essayer un autre navigateur (Chrome, Firefox, Safari)

### Problème : Message "Aucune donnée ne correspond aux filtres"
- Vos filtres sont trop restrictifs
- Cliquez sur "🔄 Réinitialiser tous les filtres"
- Élargissez progressivement vos critères

---

##  Pour Aller Plus Loin

### Personnalisation
Le fichier `streamlit_app.py` est entièrement modifiable :
- Changez les couleurs dans la section CSS
- Ajoutez de nouveaux graphiques
- Modifiez les textes et descriptions
- Créez de nouveaux filtres

### Documentation Streamlit
- [Guide officiel Streamlit](https://docs.streamlit.io)
- [Plotly Documentation](https://plotly.com/python/)
- [Pandas Tutorial](https://pandas.pydata.org/docs/)

---

## 🎓 Tutoriel Vidéo (Simulé)

### Partie 1 : Découverte (0-5 min)
1. Lancement et première impression
2. Lecture de "À propos du projet"
3. Tour des 6 onglets

### Partie 2 : Filtres (5-10 min)
1. Utilisation des filtres de base
2. Modes de sélection avancés
3. Observation du compteur en temps réel

### Partie 3 : Analyse Pratique (10-20 min)
1. Analyse d'un quartier spécifique
2. Identification des heures dangereuses
3. Étude des victimes
4. Export des résultats

---

##  Checklist de Maîtrise

- [ ] J'ai lu la section "À propos du projet"
- [ ] J'ai exploré les 6 onglets
- [ ] J'ai utilisé au moins 3 filtres différents
- [ ] J'ai survolé les graphiques pour voir les détails
- [ ] J'ai exporté des données en CSV
- [ ] J'ai réinitialisé les filtres
- [ ] Je comprends les messages colorés
- [ ] J'ai identifié un insight intéressant

---

##  Défis d'Analyse

Testez vos compétences avec ces défis :

###  Défi Bronze
Trouvez le quartier avec le plus de crimes en 2023

###  Défi Argent
Identifiez quelle tranche d'âge est la plus touchée par les crimes avec armes

###  Défi Or
Découvrez s'il existe une corrélation entre le revenu médian d'un quartier et son taux de criminalité

###  Défi Diamant
Créez un profil complet du crime le plus fréquent : type, zone, moment, victime type

---

**Bon courage dans votre exploration ! 🚀**

*Version 2.0 - Mise à jour : 19 novembre 2025*
