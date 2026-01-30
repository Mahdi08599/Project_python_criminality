"""
Tableau de Bord d'Analyse de la Criminalité à Los Angeles
=========================================================
Application web interactive pour explorer et visualiser les données de criminalité
de Los Angeles de 2020 à aujourd'hui.

 Ce projet analyse plus de 50 000 incidents criminels pour identifier les tendances,
   les zones à risque et les patterns temporels.

Auteur: Équipe d'Analyse de Données Criminelles
Date: Novembre 2025
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(
    page_title="Analyse Criminalité LA | Dashboard",
    page_icon="🚔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé pour un meilleur style
st.markdown("""
    <style>
    /* Style principal */
    .main {
        padding: 0rem 1rem;
    }
    
    /* Cartes métriques */
    .stMetric {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Titres */
    h1 {
        color: #1e3a8a;
        font-weight: 800;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    h2 {
        color: #dc2626;
        font-weight: 700;
    }
    
    h3 {
        color: #059669;
    }
    
    /* Boîtes d'info */
    .info-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    /* Boutons */
    .stButton>button {
        border-radius: 20px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        font-weight: 600;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 30px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        margin-top: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# Chargement des données avec mise en cache
@st.cache_data
def load_data():
    """Charge et prétraite les données de criminalité"""
    df = pd.read_csv('data/Crime_Data_Transformed.csv')
    df['Date Rptd'] = pd.to_datetime(df['Date Rptd'])
    df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])
    return df

# En-tête principal avec présentation du projet
st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 40px; border-radius: 20px; margin-bottom: 30px; 
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);'>
        <h1 style='color: white; text-align: center; margin: 0; font-size: 48px;'>
             Tableau de Bord de la Criminalité à Los Angeles
        </h1>
        <p style='color: white; text-align: center; font-size: 20px; margin: 15px 0 0 0;'>
            Analyse Interactive des Données Criminelles (2020 - Aujourd'hui)
        </p>
    </div>
    """, unsafe_allow_html=True)

# Présentation du projet
with st.expander("📖 À propos de ce projet - Cliquez pour en savoir plus", expanded=False):
    st.markdown("""
    ###  Objectif du Projet
    
    Ce dashboard interactif permet d'explorer et d'analyser **plus de 50 000 incidents criminels** 
    survenus à Los Angeles depuis 2020. Notre objectif est de fournir des insights clairs et 
    actionnables sur la criminalité urbaine.
    
    ###  Ce que vous découvrirez :
    
    - **Vue d'ensemble** : Distribution des types de crimes et leur gravité
    - **Analyse Géographique** : Zones les plus touchées et cartographie des incidents
    - **Tendances Temporelles** : Patterns par jour, mois, année et heure de la journée
    - **Profil des Victimes** : Analyse démographique (âge, genre)
    - **Analyse des Armes** : Implication d'armes dans les crimes
    - **Corrélations** : Relations entre population, revenus et criminalité
    
    ###  Fonctionnalités :
    
     **Filtres interactifs** pour personnaliser votre analyse  
     **Visualisations dynamiques** avec graphiques interactifs  
     **Statistiques en temps réel** basées sur vos sélections  
     **Export des données** filtrées au format CSV
    
    ###  Comment utiliser ce dashboard :
    
    1. **Utilisez les filtres** dans la barre latérale gauche pour sélectionner vos critères
    2. **Explorez les onglets** pour découvrir différentes analyses
    3. **Survolez les graphiques** pour obtenir des détails supplémentaires
    4. **Téléchargez les données** filtrées si besoin
    
    ---
    **Astuce** : Commencez avec tous les filtres actifs, puis affinez progressivement votre recherche !
    """)

st.markdown("<br>", unsafe_allow_html=True)

# Chargement des données avec animation
with st.spinner(' Chargement des données criminelles en cours...'):
    df = load_data()

st.success(f" **{len(df):,} incidents** chargés avec succès !")

# =====================================
# PANNEAU DE FILTRES (SIDEBAR)
# =====================================
st.sidebar.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 20px; border-radius: 15px; margin-bottom: 20px;'>
        <h2 style='color: white; text-align: center; margin: 0;'>🔍 FILTRES</h2>
        <p style='color: white; text-align: center; margin: 5px 0 0 0; font-size: 14px;'>
            Personnalisez votre analyse
        </p>
    </div>
    """, unsafe_allow_html=True)

# Filtre par Année
st.sidebar.markdown("### Période d'Analyse")
years = sorted(df['year'].unique())
selected_years = st.sidebar.multiselect(
    "Sélectionnez la/les année(s) :",
    options=years,
    default=years,
    help="Choisissez une ou plusieurs années pour filtrer les données"
)

st.sidebar.markdown("---")

# Filtre par Zone géographique
st.sidebar.markdown("###  Zones Géographiques")
areas = sorted(df['AREA NAME'].unique())
area_selection_mode = st.sidebar.radio(
    "Mode de sélection des zones :",
    options=["Toutes les zones", "Sélection personnalisée", "Top zones"],
    help="Choisissez comment filtrer les zones"
)

if area_selection_mode == "Toutes les zones":
    selected_areas = areas
elif area_selection_mode == "Top zones":
    top_n = st.sidebar.slider("Nombre de zones à afficher :", 5, 20, 10)
    top_areas = df['AREA NAME'].value_counts().head(top_n).index.tolist()
    selected_areas = top_areas
else:
    selected_areas = st.sidebar.multiselect(
        "Sélectionnez les zones :",
        options=areas,
        default=areas[:5] if len(areas) > 5 else areas,
        help="Zones de Los Angeles à analyser"
    )

st.sidebar.markdown("---")

# Filtre par Catégorie de Crime
st.sidebar.markdown("###  Types de Crimes")
crime_categories = sorted(df['crime_category'].unique())
selected_categories = st.sidebar.multiselect(
    "Sélectionnez les catégories :",
    options=crime_categories,
    default=crime_categories,
    help="Catégories de crimes à inclure dans l'analyse"
)

st.sidebar.markdown("---")

# Filtre par Période de la Journée
st.sidebar.markdown("###  Moment de la Journée")
time_periods = sorted(df['time_period'].unique())
selected_time_periods = st.sidebar.multiselect(
    "Sélectionnez les plages horaires :",
    options=time_periods,
    default=time_periods,
    help="Périodes de la journée : Matin, Après-midi, Soirée, Nuit"
)

st.sidebar.markdown("---")

# Filtre supplémentaire : Implication d'armes
st.sidebar.markdown("###  Armes")
weapon_filter = st.sidebar.selectbox(
    "Filtrer par armes :",
    options=["Tous", "Avec armes uniquement", "Sans armes uniquement"],
    help="Filtrer selon l'implication d'armes dans les crimes"
)

# Application des filtres
filtered_df = df[
    (df['year'].isin(selected_years)) &
    (df['AREA NAME'].isin(selected_areas)) &
    (df['crime_category'].isin(selected_categories)) &
    (df['time_period'].isin(selected_time_periods))
]

# Filtre armes
if weapon_filter == "Avec armes uniquement":
    filtered_df = filtered_df[filtered_df['weapon_involved'] == 1]
elif weapon_filter == "Sans armes uniquement":
    filtered_df = filtered_df[filtered_df['weapon_involved'] == 0]

st.sidebar.markdown("---")

# Résumé des filtres appliqués
st.sidebar.markdown("###  Résultat du Filtrage")
st.sidebar.markdown(f"""
    <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                padding: 15px; border-radius: 10px; color: white;'>
        <p style='margin: 0; font-size: 16px; font-weight: bold;'>
             {len(filtered_df):,} incidents
        </p>
        <p style='margin: 5px 0 0 0; font-size: 14px;'>
            sur {len(df):,} au total
        </p>
        <p style='margin: 5px 0 0 0; font-size: 14px;'>
            ({len(filtered_df)/len(df)*100:.1f}% des données)
        </p>
    </div>
    """, unsafe_allow_html=True)

# Bouton de réinitialisation
st.sidebar.markdown("<br>", unsafe_allow_html=True)
if st.sidebar.button(" Réinitialiser tous les filtres", use_container_width=True):
    st.rerun()

# =====================================
# INDICATEURS CLÉS (KPIs)
# =====================================
st.markdown("##  Indicateurs Clés en un Coup d'Œil")
st.markdown("<br>", unsafe_allow_html=True)

# Calcul des métriques
total_crimes = len(filtered_df)
total_percentage = (len(filtered_df)/len(df)*100)
avg_victim_age = filtered_df['Vict Age'].mean()
weapon_rate = (filtered_df['weapon_involved'].sum() / len(filtered_df) * 100) if len(filtered_df) > 0 else 0
unique_areas = filtered_df['AREA NAME'].nunique()
avg_delay = filtered_df['reporting_delay_days'].mean() if 'reporting_delay_days' in filtered_df.columns else 0

# Création des cartes KPI
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 25px; border-radius: 15px; text-align: center; color: white; box-shadow: 0 8px 16px rgba(0,0,0,0.2);
                transition: transform 0.3s ease;'>
        <h3 style='margin: 0; font-size: 15px; font-weight: 500; opacity: 0.9;'> Total des Crimes</h3>
        <h1 style='margin: 10px 0; font-size: 38px; font-weight: bold;'>{total_crimes:,}</h1>
        <p style='margin: 0; font-size: 13px; opacity: 0.85;'> {total_percentage:.1f}% du total</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                padding: 25px; border-radius: 15px; text-align: center; color: white; box-shadow: 0 8px 16px rgba(0,0,0,0.2);'>
        <h3 style='margin: 0; font-size: 15px; font-weight: 500; opacity: 0.9;'>👤 Âge Moyen Victime</h3>
        <h1 style='margin: 10px 0; font-size: 38px; font-weight: bold;'>{avg_victim_age:.1f}</h1>
        <p style='margin: 0; font-size: 13px; opacity: 0.85;'>ans</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); 
                padding: 25px; border-radius: 15px; text-align: center; color: white; box-shadow: 0 8px 16px rgba(0,0,0,0.2);'>
        <h3 style='margin: 0; font-size: 15px; font-weight: 500; opacity: 0.9;'>🔫 Taux d'Armes</h3>
        <h1 style='margin: 10px 0; font-size: 38px; font-weight: bold;'>{weapon_rate:.1f}%</h1>
        <p style='margin: 0; font-size: 13px; opacity: 0.85;'>crimes avec armes</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #30cfd0 0%, #330867 100%); 
                padding: 25px; border-radius: 15px; text-align: center; color: white; box-shadow: 0 8px 16px rgba(0,0,0,0.2);'>
        <h3 style='margin: 0; font-size: 15px; font-weight: 500; opacity: 0.9;'> Zones Touchées</h3>
        <h1 style='margin: 10px 0; font-size: 38px; font-weight: bold;'>{unique_areas}</h1>
        <p style='margin: 0; font-size: 13px; opacity: 0.85;'>quartiers concernés</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                padding: 25px; border-radius: 15px; text-align: center; color: white; box-shadow: 0 8px 16px rgba(0,0,0,0.2);'>
        <h3 style='margin: 0; font-size: 15px; font-weight: 500; opacity: 0.9;'> Délai Moyen</h3>
        <h1 style='margin: 10px 0; font-size: 38px; font-weight: bold;'>{avg_delay:.1f}</h1>
        <p style='margin: 0; font-size: 13px; opacity: 0.85;'>jours pour signaler</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Message d'alerte si pas de données
if len(filtered_df) == 0:
    st.error(" Aucune donnée ne correspond aux filtres sélectionnés. Veuillez ajuster vos critères.")
    st.stop()

st.markdown("---")

# =====================================
# ONGLETS D'ANALYSE
# =====================================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Vue d'Ensemble", 
    "🗺️ Analyse Géographique", 
    "⏰ Tendances Temporelles", 
    "👥 Profil des Victimes", 
    "🔫 Analyse des Armes",
    "📈 Corrélations & Tendances"
])

# =====================================
# ONGLET 1 : VUE D'ENSEMBLE
# =====================================
with tab1:
    st.markdown("##  Distribution Générale des Crimes")
    st.markdown("*Aperçu complet de la répartition des crimes par catégorie et type*")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("###  Répartition par Catégorie")
        category_counts = filtered_df['crime_category'].value_counts()
        
        fig = px.pie(
            values=category_counts.values,
            names=category_counts.index,
            title="<b>Distribution des Catégories de Crimes</b>",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig.update_traces(
            textposition='inside', 
            textinfo='percent+label',
            textfont_size=12,
            marker=dict(line=dict(color='white', width=2))
        )
        fig.update_layout(
            font=dict(size=12),
            title_font_size=16,
            showlegend=True,
            legend=dict(orientation="v", yanchor="middle", y=0.5)
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.info(f"""
        **Insight :** La catégorie la plus fréquente est 
        **{category_counts.index[0]}** avec {category_counts.values[0]:,} cas 
        ({category_counts.values[0]/category_counts.sum()*100:.1f}% du total).
        """)
    
    with col2:
        st.markdown("###  Top 10 des Types de Crimes")
        top_crimes = filtered_df['Crm Cd Desc'].value_counts().head(10)
        
        fig = px.bar(
            x=top_crimes.values,
            y=top_crimes.index,
            orientation='h',
            title="<b>Les 10 Crimes les Plus Fréquents</b>",
            labels={'x': 'Nombre de Cas', 'y': 'Type de Crime'},
            color=top_crimes.values,
            color_continuous_scale='Reds'
        )
        fig.update_layout(
            showlegend=False, 
            yaxis={'categoryorder':'total ascending'},
            font=dict(size=11),
            title_font_size=16,
            xaxis_title="Nombre de cas",
            yaxis_title=""
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.info(f"""
        ** Insight :** Le crime le plus commun est 
        **{top_crimes.index[0]}** avec {top_crimes.values[0]:,} incidents.
        """)
    
    st.markdown("---")
    
    # Gravité des crimes
    st.markdown("###  Analyse de la Gravité des Crimes")
    st.markdown("*Classification des incidents selon leur niveau de sévérité*")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col3, col4 = st.columns([2, 1])
    
    with col3:
        severity_counts = filtered_df['crime_severity'].value_counts()
        
        fig = px.bar(
            x=severity_counts.index,
            y=severity_counts.values,
            title="<b>Distribution par Niveau de Gravité</b>",
            labels={'x': 'Niveau de Gravité', 'y': 'Nombre de Crimes'},
            color=severity_counts.values,
            color_continuous_scale='Viridis',
            text=severity_counts.values
        )
        fig.update_traces(texttemplate='%{text:,}', textposition='outside')
        fig.update_layout(
            font=dict(size=12),
            title_font_size=16,
            xaxis_title="Gravité",
            yaxis_title="Nombre de crimes"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col4:
        st.markdown("####  Tableau Récapitulatif")
        stats_df = filtered_df[['crime_category', 'crime_severity']].value_counts().head(10).reset_index()
        stats_df.columns = ['Catégorie', 'Gravité', 'Nombre']
        st.dataframe(
            stats_df,
            use_container_width=True,
            hide_index=True
        )
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 15px; border-radius: 10px; color: white; margin-top: 20px;'>
            <p style='margin: 0; font-size: 14px; font-weight: bold;'>
                 Total Catégories : {filtered_df['crime_category'].nunique()}
            </p>
            <p style='margin: 5px 0 0 0; font-size: 14px;'>
                 Types Uniques : {filtered_df['Crm Cd Desc'].nunique()}
            </p>
        </div>
        """, unsafe_allow_html=True)

# =====================================
# ONGLET 2 : ANALYSE GÉOGRAPHIQUE
# =====================================
with tab2:
    st.markdown("##  Distribution Géographique des Crimes")
    st.markdown("*Analyse spatiale pour identifier les zones à risque*")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("###  Top 15 des Zones les Plus Touchées")
        top_areas = filtered_df['AREA NAME'].value_counts().head(15)
        
        fig = px.bar(
            x=top_areas.values,
            y=top_areas.index,
            orientation='h',
            title="<b>Classement des Quartiers par Nombre de Crimes</b>",
            labels={'x': 'Nombre de Crimes', 'y': 'Nom du Quartier'},
            color=top_areas.values,
            color_continuous_scale='Reds',
            text=top_areas.values
        )
        fig.update_traces(texttemplate='%{text:,}', textposition='outside')
        fig.update_layout(
            yaxis={'categoryorder':'total ascending'}, 
            height=500,
            font=dict(size=11),
            title_font_size=16,
            xaxis_title="Nombre de crimes",
            yaxis_title=""
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.warning(f"""
        ⚠️ **Zone la plus à risque :** {top_areas.index[0]} avec **{top_areas.values[0]:,} incidents** 
        ({top_areas.values[0]/len(filtered_df)*100:.1f}% du total des crimes)
        """)
    
    with col2:
        st.markdown("###  Statistiques par Zone")
        area_stats = filtered_df.groupby('AREA NAME').agg({
            'DR_NO': 'count',
            'area_risk_score': 'mean',
            'population': 'first',
            'median_income': 'first'
        }).round(2)
        area_stats.columns = ['Crimes', 'Score Risque', 'Population', 'Revenu']
        area_stats = area_stats.sort_values('Crimes', ascending=False).head(10)
        st.dataframe(area_stats, use_container_width=True, height=500)
        
        st.success(f"""
         **{unique_areas} zones différentes** sont représentées dans les données filtrées.
        """)
    
    st.markdown("---")
    
    # Carte de densité criminelle
    st.markdown("###  Carte Interactive des Incidents")
    st.markdown("*Visualisation géographique des emplacements de crimes*")
    
    # Échantillonnage pour performance
    map_data = filtered_df[['LAT', 'LON', 'crime_category']].dropna()
    if len(map_data) > 5000:
        map_data = map_data.sample(5000)
        st.info(f" Pour des performances optimales, affichage d'un échantillon de 5 000 incidents sur {len(filtered_df[['LAT', 'LON']].dropna()):,}")
    
    fig = px.scatter_mapbox(
        map_data,
        lat='LAT',
        lon='LON',
        color='crime_category',
        zoom=9,
        height=600,
        title="<b>Localisation des Crimes à Los Angeles</b>",
        mapbox_style="carto-positron",
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig.update_layout(
        font=dict(size=12),
        title_font_size=16,
        margin=dict(l=0, r=0, t=40, b=0)
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Comparaison des zones
    st.markdown("###  Comparaison des Catégories par Zone")
    st.markdown("*Top 5 des zones avec répartition détaillée par type de crime*")
    
    top_5_areas = filtered_df['AREA NAME'].value_counts().head(5).index
    area_category = pd.crosstab(
        filtered_df[filtered_df['AREA NAME'].isin(top_5_areas)]['AREA NAME'],
        filtered_df[filtered_df['AREA NAME'].isin(top_5_areas)]['crime_category']
    )
    
    fig = px.bar(
        area_category,
        barmode='group',
        title="<b>Catégories de Crimes dans les 5 Zones les Plus Touchées</b>",
        labels={'value': 'Nombre de Crimes', 'AREA NAME': 'Quartier'},
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig.update_layout(
        font=dict(size=12),
        title_font_size=16,
        xaxis_title="Quartier",
        yaxis_title="Nombre de crimes",
        legend_title="Catégorie",
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)

# =====================================
# ONGLET 3 : TENDANCES TEMPORELLES
# =====================================
with tab3:
    st.markdown("##  Analyse Temporelle des Crimes")
    st.markdown("*Découvrez les patterns et tendances dans le temps*")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Série temporelle
    st.markdown("###  Évolution des Crimes dans le Temps")
    
    col_agg1, col_agg2 = st.columns([3, 1])
    
    with col_agg1:
        time_agg = st.selectbox(
            "Sélectionnez la granularité temporelle :",
            options=["Quotidien", "Hebdomadaire", "Mensuel"],
            index=2,
            help="Choisissez comment agréger les données dans le temps"
        )
    
    with col_agg2:
        show_trend = st.checkbox("Afficher la tendance", value=True)
    
    df_ts = filtered_df.set_index('DATE OCC').sort_index()
    
    if time_agg == "Quotidien":
        time_series = df_ts.resample('D').size()
        window = 7
    elif time_agg == "Hebdomadaire":
        time_series = df_ts.resample('W').size()
        window = 4
    else:
        time_series = df_ts.resample('M').size()
        window = 3
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=time_series.index,
        y=time_series.values,
        mode='lines',
        name='Nombre de Crimes',
        line=dict(color='#667eea', width=2.5),
        fill='tozeroy',
        fillcolor='rgba(102, 126, 234, 0.1)'
    ))
    
    if show_trend and time_agg == "Quotidien":
        rolling_avg = time_series.rolling(window=window).mean()
        fig.add_trace(go.Scatter(
            x=rolling_avg.index,
            y=rolling_avg.values,
            mode='lines',
            name=f'Moyenne Mobile ({window} jours)',
            line=dict(color='#ff7f0e', width=3, dash='dash')
        ))
    
    fig.update_layout(
        title=f"<b>Tendance {time_agg}e des Crimes</b>",
        xaxis_title="Date",
        yaxis_title="Nombre de Crimes",
        hovermode='x unified',
        height=450,
        font=dict(size=12),
        title_font_size=16,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Stats de la série temporelle
    col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
    with col_stat1:
        st.metric(" Moyenne", f"{time_series.mean():.0f}", help="Nombre moyen de crimes par période")
    with col_stat2:
        st.metric(" Maximum", f"{time_series.max():.0f}", help="Pic maximum de crimes")
    with col_stat3:
        st.metric(" Minimum", f"{time_series.min():.0f}", help="Minimum de crimes")
    with col_stat4:
        st.metric(" Écart-type", f"{time_series.std():.0f}", help="Variabilité des données")
    
    st.markdown("---")
    
    # Patterns temporels
    st.markdown("###  Patterns Cycliques")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("####  Par Jour de la Semaine")
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_names_fr = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        day_counts = filtered_df['day_name'].value_counts().reindex(day_order)
        
        fig = px.bar(
            x=day_names_fr,
            y=day_counts.values,
            title="<b>Crimes par Jour</b>",
            labels={'x': 'Jour', 'y': 'Nombre'},
            color=day_counts.values,
            color_continuous_scale='Blues',
            text=day_counts.values
        )
        fig.update_traces(texttemplate='%{text:,}', textposition='outside')
        fig.update_layout(font=dict(size=10), title_font_size=14, xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
        
        max_day_idx = day_counts.values.argmax()
        st.caption(f" Jour le plus criminel : **{day_names_fr[max_day_idx]}**")
    
    with col2:
        st.markdown("####  Par Mois")
        month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December']
        month_names_fr = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun',
                         'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']
        month_counts = filtered_df['month_name'].value_counts().reindex(month_order)
        
        fig = px.line(
            x=month_names_fr,
            y=month_counts.values,
            title="<b>Crimes par Mois</b>",
            labels={'x': 'Mois', 'y': 'Nombre'},
            markers=True
        )
        fig.update_traces(line_color='#f5576c', line_width=3, marker=dict(size=10))
        fig.update_layout(font=dict(size=10), title_font_size=14)
        st.plotly_chart(fig, use_container_width=True)
        
        max_month_idx = month_counts.values.argmax()
        st.caption(f" Mois le plus criminel : **{month_names_fr[max_month_idx]}**")
    
    with col3:
        st.markdown("####  Par Heure")
        hour_counts = filtered_df['hour'].value_counts().sort_index()
        
        fig = px.line(
            x=hour_counts.index,
            y=hour_counts.values,
            title="<b>Crimes par Heure</b>",
            labels={'x': 'Heure', 'y': 'Nombre'},
            markers=True
        )
        fig.update_traces(line_color='#764ba2', line_width=3, marker=dict(size=8))
        fig.update_layout(font=dict(size=10), title_font_size=14)
        st.plotly_chart(fig, use_container_width=True)
        
        max_hour = hour_counts.idxmax()
        st.caption(f" Heure la plus criminelle : **{max_hour}h**")
    
    st.markdown("---")
    
    # Analyse par période de la journée
    st.markdown("###  Distribution par Moment de la Journée")
    
    col_period1, col_period2 = st.columns([2, 1])
    
    with col_period1:
        time_period_order = ['Night (00:00-05:59)', 'Morning (06:00-11:59)',
                             'Afternoon (12:00-17:59)', 'Evening (18:00-23:59)']
        time_names_fr = [' Nuit\n(00h-06h)', 'Matin\n(06h-12h)', 
                        ' Après-midi\n(12h-18h)', ' Soirée\n(18h-00h)']
        time_counts = filtered_df['time_period'].value_counts().reindex(time_period_order)
        
        fig = px.bar(
            x=time_names_fr,
            y=time_counts.values,
            title="<b>Répartition des Crimes selon le Moment de la Journée</b>",
            labels={'x': 'Période', 'y': 'Nombre de Crimes'},
            color=time_counts.values,
            color_continuous_scale='Sunset',
            text=time_counts.values
        )
        fig.update_traces(texttemplate='%{text:,}', textposition='outside')
        fig.update_layout(font=dict(size=12), title_font_size=16, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col_period2:
        st.markdown("####  Insights Clés")
        max_period_idx = time_counts.values.argmax()
        min_period_idx = time_counts.values.argmin()
        
        max_period_name = time_names_fr[max_period_idx].split('\n')[0]
        min_period_name = time_names_fr[min_period_idx].split('\n')[0]
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); 
                    padding: 15px; border-radius: 10px; color: white; margin-bottom: 10px;'>
            <p style='margin: 0; font-size: 14px;'><b> Période la plus risquée :</b></p>
            <p style='margin: 5px 0 0 0; font-size: 16px; font-weight: bold;'>
                {max_period_name}
            </p>
            <p style='margin: 5px 0 0 0; font-size: 13px;'>
                {time_counts.values[max_period_idx]:,} incidents
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #30cfd0 0%, #330867 100%); 
                    padding: 15px; border-radius: 10px; color: white;'>
            <p style='margin: 0; font-size: 14px;'><b> Période la plus sûre :</b></p>
            <p style='margin: 5px 0 0 0; font-size: 16px; font-weight: bold;'>
                {min_period_name}
            </p>
            <p style='margin: 5px 0 0 0; font-size: 13px;'>
                {time_counts.values[min_period_idx]:,} incidents
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Heatmap jour vs heure
    st.markdown("###  Carte de Chaleur : Jour × Heure")
    st.markdown("*Visualisation des périodes les plus criminelles*")
    
    heatmap_data = pd.crosstab(filtered_df['day_name'], filtered_df['hour'])
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_names_fr_full = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    heatmap_data = heatmap_data.reindex(day_order)
    heatmap_data.index = day_names_fr_full
    
    fig = px.imshow(
        heatmap_data,
        labels=dict(x="Heure de la Journée", y="Jour de la Semaine", color="Nombre de Crimes"),
        x=heatmap_data.columns,
        y=heatmap_data.index,
        color_continuous_scale='YlOrRd',
        aspect="auto",
        title="<b>Intensité Criminelle par Jour et Heure</b>"
    )
    fig.update_layout(
        height=450,
        font=dict(size=12),
        title_font_size=16
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("""
     **Comment lire cette carte :** Les zones plus foncées (rouge) indiquent des périodes 
    avec plus de crimes, tandis que les zones claires (jaune) représentent des périodes plus calmes.
    """)

# =====================================
# ONGLET 4 : PROFIL DES VICTIMES
# =====================================
with tab4:
    st.markdown("##  Analyse Démographique des Victimes")
    st.markdown("*Qui sont les victimes de crimes à Los Angeles ?*")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("###  Distribution par Tranche d'Âge")
        age_order = ['Child (0-17)', 'Young Adult (18-34)', 'Middle Age (35-49)', 
                     'Senior (50-64)', 'Elderly (65+)']
        age_names_fr = [' Enfants\n(0-17 ans)', ' Jeunes Adultes\n(18-34 ans)', 
                       ' Adultes\n(35-49 ans)', ' Seniors\n(50-64 ans)', ' Âgés\n(65+ ans)']
        age_counts = filtered_df['victim_age_group'].value_counts()
        age_counts = age_counts.reindex([a for a in age_order if a in age_counts.index])
        
        # Mapping pour les labels français
        age_mapping = dict(zip(age_order, age_names_fr))
        age_labels_fr = [age_mapping.get(age, age) for age in age_counts.index]
        
        fig = px.bar(
            x=age_labels_fr,
            y=age_counts.values,
            title="<b>Victimes par Tranche d'Âge</b>",
            labels={'x': 'Tranche d\'Âge', 'y': 'Nombre de Victimes'},
            color=age_counts.values,
            color_continuous_scale='Teal',
            text=age_counts.values
        )
        fig.update_traces(texttemplate='%{text:,}', textposition='outside')
        fig.update_layout(
            font=dict(size=11), 
            title_font_size=16,
            showlegend=False,
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig, use_container_width=True)
        
        most_affected_age = age_labels_fr[0] if len(age_labels_fr) > 0 else "N/A"
        st.info(f" **Groupe le plus touché :** {most_affected_age} avec {age_counts.values[0]:,} victimes")
    
    with col2:
        st.markdown("###  Répartition par Genre")
        sex_counts = filtered_df['Vict Sex'].value_counts().head(5)
        
        # Mapping genre en français
        gender_mapping = {
            'M': 'Hommes',
            'F': 'Femmes',
            'X': 'Non spécifié',
            'Unknown': 'Inconnu',
            'H': 'Hommes'
        }
        sex_labels_fr = [gender_mapping.get(sex, sex) for sex in sex_counts.index]
        
        fig = px.pie(
            values=sex_counts.values,
            names=sex_labels_fr,
            title="<b>Victimes par Genre</b>",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig.update_traces(
            textposition='inside', 
            textinfo='percent+label',
            textfont_size=13,
            marker=dict(line=dict(color='white', width=2))
        )
        fig.update_layout(font=dict(size=12), title_font_size=16)
        st.plotly_chart(fig, use_container_width=True)
        
        if len(sex_counts) > 0:
            top_gender = sex_labels_fr[0]
            top_pct = (sex_counts.values[0] / sex_counts.sum() * 100)
            st.info(f" **Genre majoritaire :** {top_gender} ({top_pct:.1f}%)")
    
    st.markdown("---")
    
    # Distribution détaillée des âges
    st.markdown("###  Distribution Détaillée des Âges")
    
    col_hist1, col_hist2 = st.columns([3, 1])
    
    with col_hist1:
        fig = px.histogram(
            filtered_df,
            x='Vict Age',
            nbins=50,
            title="<b>Histogramme de l'Âge des Victimes</b>",
            labels={'Vict Age': 'Âge', 'count': 'Fréquence'},
            color_discrete_sequence=['#667eea']
        )
        fig.update_layout(
            showlegend=False,
            font=dict(size=12),
            title_font_size=16
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col_hist2:
        st.markdown("####  Statistiques")
        st.metric("Âge Moyen", f"{filtered_df['Vict Age'].mean():.1f} ans")
        st.metric("Âge Médian", f"{filtered_df['Vict Age'].median():.0f} ans")
        st.metric("Écart-type", f"{filtered_df['Vict Age'].std():.1f}")
    
    st.markdown("---")
    
    # Démographie par catégorie de crime
    st.markdown("###  Profil des Victimes par Type de Crime")
    st.markdown("*Analyse croisée : catégories de crimes × tranches d'âge*")
    
    demo_category = pd.crosstab(
        filtered_df['crime_category'],
        filtered_df['victim_age_group']
    )
    
    # Réordonner les colonnes
    age_order_demo = ['Child (0-17)', 'Young Adult (18-34)', 'Middle Age (35-49)', 
                      'Senior (50-64)', 'Elderly (65+)']
    demo_category = demo_category[[col for col in age_order_demo if col in demo_category.columns]]
    
    fig = px.bar(
        demo_category,
        barmode='stack',
        title="<b>Répartition des Tranches d'Âge selon les Catégories de Crimes</b>",
        labels={'value': 'Nombre de Cas', 'crime_category': 'Catégorie de Crime'},
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig.update_layout(
        font=dict(size=12),
        title_font_size=16,
        xaxis_title="Catégorie de Crime",
        yaxis_title="Nombre de victimes",
        legend_title="Tranche d'Âge",
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.success("""
     **Analyse :** Ce graphique montre comment les différentes tranches d'âge sont affectées 
    par chaque catégorie de crime. Les couleurs empilées permettent de voir la composition 
    démographique pour chaque type de criminalité.
    """)

# =====================================
# ONGLET 5 : ANALYSE DES ARMES
# =====================================
with tab5:
    st.markdown("##  Analyse de l'Implication des Armes")
    st.markdown("*Étude de l'utilisation d'armes dans les crimes*")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("###  Présence d'Armes")
        weapon_counts = filtered_df['weapon_involved'].value_counts()
        
        # Créer les labels et valeurs en fonction des données disponibles
        weapon_data = []
        weapon_labels_display = []
        weapon_colors = []
        
        if 0 in weapon_counts.index:
            weapon_data.append(weapon_counts[0])
            weapon_labels_display.append(' Sans Arme')
            weapon_colors.append('#90EE90')
        
        if 1 in weapon_counts.index:
            weapon_data.append(weapon_counts[1])
            weapon_labels_display.append(' Avec Arme')
            weapon_colors.append('#FF6B6B')
        
        fig = px.pie(
            values=weapon_data,
            names=weapon_labels_display,
            title="<b>Proportion Globale d'Utilisation d'Armes</b>",
            color_discrete_sequence=weapon_colors,
            hole=0.5
        )
        fig.update_traces(
            textposition='inside', 
            textinfo='percent+label',
            textfont_size=14,
            marker=dict(line=dict(color='white', width=3))
        )
        fig.update_layout(font=dict(size=12), title_font_size=16)
        st.plotly_chart(fig, use_container_width=True)
        
        #Calcul du pourcentage d'incidents avec armes
        if 1 in weapon_counts.index:
            weapon_pct = (weapon_counts[1] / weapon_counts.sum() * 100)
        else:
            weapon_pct = 0
        
        if weapon_pct > 50:
            st.error(f" **{weapon_pct:.1f}%** des crimes impliquent des armes")
        elif weapon_pct > 30:
            st.warning(f" **{weapon_pct:.1f}%** des crimes impliquent des armes")
        else:
            st.success(f" Seulement **{weapon_pct:.1f}%** des crimes impliquent des armes")
    
    with col2:
        st.markdown("###  Catégories d'Armes")
        weapon_cat = filtered_df[filtered_df['weapon_involved'] == 1]['weapon_category'].value_counts()
        
        fig = px.bar(
            x=weapon_cat.index,
            y=weapon_cat.values,
            title="<b>Types d'Armes Utilisées</b>",
            labels={'x': 'Catégorie d\'Arme', 'y': 'Nombre de Cas'},
            color=weapon_cat.values,
            color_continuous_scale='Reds',
            text=weapon_cat.values
        )
        fig.update_traces(texttemplate='%{text:,}', textposition='outside')
        fig.update_layout(
            font=dict(size=11), 
            title_font_size=16,
            showlegend=False,
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig, use_container_width=True)
        
        if len(weapon_cat) > 0:
            st.info(f" **Arme la plus utilisée :** {weapon_cat.index[0]} ({weapon_cat.values[0]:,} cas)")
    
    st.markdown("---")
    
    # Armes par catégorie de crime
    st.markdown("###  Utilisation d'Armes par Catégorie de Crime")
    st.markdown("*Pourcentage de crimes avec armes pour chaque catégorie*")
    
    weapon_crime = pd.crosstab(
        filtered_df['crime_category'],
        filtered_df['weapon_involved'],
        normalize='index'
    ) * 100
    weapon_crime.columns = ['Sans Arme', 'Avec Arme']
    
    fig = px.bar(
        weapon_crime,
        barmode='group',
        title="<b>Taux d'Implication d'Armes par Catégorie</b>",
        labels={'value': 'Pourcentage (%)', 'crime_category': 'Catégorie de Crime'},
        color_discrete_map={'Sans Arme': '#90EE90', 'Avec Arme': '#FF6B6B'}
    )
    fig.update_layout(
        font=dict(size=12),
        title_font_size=16,
        xaxis_title="Catégorie de Crime",
        yaxis_title="Pourcentage (%)",
        legend_title="Type",
        height=450
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Armes par zone
    st.markdown("###  Taux d'Armes par Zone (Top 10)")
    st.markdown("*Zones avec le plus fort taux d'utilisation d'armes*")
    
    col_weapon1, col_weapon2 = st.columns([2, 1])
    
    with col_weapon1:
        top_10_areas = filtered_df['AREA NAME'].value_counts().head(10).index
        area_weapon = filtered_df[filtered_df['AREA NAME'].isin(top_10_areas)].groupby('AREA NAME')['weapon_involved'].apply(
            lambda x: (x == 1).sum() / len(x) * 100
        ).sort_values(ascending=False)
        
        fig = px.bar(
            x=area_weapon.values,
            y=area_weapon.index,
            orientation='h',
            title="<b>Taux d'Implication d'Armes par Zone</b>",
            labels={'x': 'Taux d\'Armes (%)', 'y': 'Zone'},
            color=area_weapon.values,
            color_continuous_scale='Oranges',
            text=area_weapon.values
        )
        fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        fig.update_layout(
            yaxis={'categoryorder':'total ascending'},
            font=dict(size=11),
            title_font_size=16
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col_weapon2:
        st.markdown("####  Zones à Risque")
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #FF6B6B 0%, #C92A2A 100%); 
                    padding: 15px; border-radius: 10px; color: white; margin-bottom: 10px;'>
            <p style='margin: 0; font-size: 13px;'><b> Zone #1 :</b></p>
            <p style='margin: 5px 0 0 0; font-size: 15px; font-weight: bold;'>
                {area_weapon.index[0]}
            </p>
            <p style='margin: 5px 0 0 0; font-size: 14px;'>
                {area_weapon.values[0]:.1f}% avec armes
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #FFA94D 0%, #FF6B35 100%); 
                    padding: 15px; border-radius: 10px; color: white; margin-bottom: 10px;'>
            <p style='margin: 0; font-size: 13px;'><b>🥈 Zone #2 :</b></p>
            <p style='margin: 5px 0 0 0; font-size: 15px; font-weight: bold;'>
                {area_weapon.index[1]}
            </p>
            <p style='margin: 5px 0 0 0; font-size: 14px;'>
                {area_weapon.values[1]:.1f}% avec armes
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #FFD93D 0%, #F28C28 100%); 
                    padding: 15px; border-radius: 10px; color: white;'>
            <p style='margin: 0; font-size: 13px;'><b> Zone #3 :</b></p>
            <p style='margin: 5px 0 0 0; font-size: 15px; font-weight: bold;'>
                {area_weapon.index[2]}
            </p>
            <p style='margin: 5px 0 0 0; font-size: 14px;'>
                {area_weapon.values[2]:.1f}% avec armes
            </p>
        </div>
        """, unsafe_allow_html=True)

# =====================================
# ONGLET 6 : CORRÉLATIONS & TENDANCES
# =====================================
with tab6:
    st.markdown("##  Tendances et Corrélations")
    st.markdown("*Analyse approfondie des relations entre variables*")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tendances annuelles
    st.markdown("###  Évolution Annuelle par Catégorie")
    st.markdown("*Tendances des crimes au fil des années*")
    
    year_category = pd.crosstab(filtered_df['year'], filtered_df['crime_category'])
    
    fig = px.line(
        year_category,
        title="<b>Tendances Annuelles des Crimes par Catégorie</b>",
        labels={'value': 'Nombre de Crimes', 'year': 'Année'},
        markers=True
    )
    fig.update_layout(
        font=dict(size=12),
        title_font_size=16,
        xaxis_title="Année",
        yaxis_title="Nombre de crimes",
        legend_title="Catégorie",
        height=450,
        hovermode='x unified'
    )
    fig.update_traces(line=dict(width=3), marker=dict(size=8))
    st.plotly_chart(fig, use_container_width=True)
    
    # Calcul des variations
    year_totals = filtered_df['year'].value_counts().sort_index()
    if len(year_totals) > 1:
        first_year = year_totals.index[0]
        last_year = year_totals.index[-1]
        variation = ((year_totals.iloc[-1] - year_totals.iloc[0]) / year_totals.iloc[0] * 100)
        
        if variation > 0:
            st.warning(f"**Augmentation de {variation:.1f}%** entre {first_year} et {last_year}")
        else:
            st.success(f" **Diminution de {abs(variation):.1f}%** entre {first_year} et {last_year}")
    
    st.markdown("---")
    
    # Matrice de corrélation
    st.markdown("### 🔗 Matrice de Corrélation")
    st.markdown("*Relations entre les différentes variables*")
    
    corr_vars = ['Vict Age', 'weapon_involved', 'is_weekend', 'reporting_delay_days',
                 'area_risk_score', 'population', 'median_income', 'crimes_per_1000', 'hour']
    corr_vars = [var for var in corr_vars if var in filtered_df.columns]
    
    # Mapping des noms en français
    var_names_fr = {
        'Vict Age': 'Âge Victime',
        'weapon_involved': 'Arme Impliquée',
        'is_weekend': 'Week-end',
        'reporting_delay_days': 'Délai Déclaration',
        'area_risk_score': 'Score Risque Zone',
        'population': 'Population',
        'median_income': 'Revenu Médian',
        'crimes_per_1000': 'Crimes/1000 hab',
        'hour': 'Heure'
    }
    
    correlation = filtered_df[corr_vars].corr()
    
    # Renommer les axes
    correlation_renamed = correlation.rename(columns=var_names_fr, index=var_names_fr)
    
    fig = px.imshow(
        correlation_renamed,
        labels=dict(color="Corrélation"),
        x=correlation_renamed.columns,
        y=correlation_renamed.columns,
        color_continuous_scale='RdBu_r',
        aspect="auto",
        zmin=-1,
        zmax=1,
        title="<b>Matrice de Corrélation entre Variables</b>"
    )
    fig.update_layout(
        height=650,
        font=dict(size=11),
        title_font_size=16
    )
    fig.update_xaxes(tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("""
     **Comment lire cette matrice :**
    - **Rouge** : Corrélation positive forte (quand l'un augmente, l'autre augmente)
    - **Bleu** : Corrélation négative forte (quand l'un augmente, l'autre diminue)
    - **Blanc** : Pas de corrélation significative
    - Les valeurs vont de **-1** (corrélation négative parfaite) à **+1** (corrélation positive parfaite)
    """)
    
    st.markdown("---")
    
    # Analyse de relations
    st.markdown("### 🔬 Analyse des Relations")
    st.markdown("*Exploration des liens entre facteurs socio-économiques et criminalité*")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("####  Population vs Taux de Criminalité")
        area_data = filtered_df.groupby('AREA NAME').agg({
            'DR_NO': 'count',
            'population': 'first',
            'median_income': 'first'
        }).reset_index()
        area_data['crime_rate'] = area_data['DR_NO'] / area_data['population'] * 1000
        
        fig = px.scatter(
            area_data,
            x='population',
            y='crime_rate',
            hover_data=['AREA NAME'],
            title="<b>Population vs Taux de Criminalité (pour 1000 hab.)</b>",
            labels={'population': 'Population', 'crime_rate': 'Taux de Criminalité'},
            trendline="ols",
            color='crime_rate',
            color_continuous_scale='Reds',
            size='DR_NO'
        )
        fig.update_layout(
            font=dict(size=11),
            title_font_size=14,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.caption(" La taille des points représente le nombre total de crimes")
    
    with col2:
        st.markdown("####  Revenu Médian vs Nombre de Crimes")
        fig = px.scatter(
            area_data,
            x='median_income',
            y='DR_NO',
            hover_data=['AREA NAME'],
            title="<b>Revenu vs Total des Crimes</b>",
            labels={'median_income': 'Revenu Médian', 'DR_NO': 'Total des Crimes'},
            trendline="ols",
            color='DR_NO',
            color_continuous_scale='Viridis',
            size='population'
        )
        fig.update_layout(
            font=dict(size=11),
            title_font_size=14,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.caption(" La taille des points représente la population de la zone")
    
    st.markdown("---")
    
    # Patterns mensuels annuels
    st.markdown("###  Patterns Mensuels Multi-Années")
    st.markdown("*Comparaison des cycles mensuels entre différentes années*")
    
    monthly_year = filtered_df.groupby(['year', 'month']).size().reset_index(name='count')
    
    fig = px.line(
        monthly_year,
        x='month',
        y='count',
        color='year',
        title="<b>Cycles Mensuels de Criminalité par Année</b>",
        labels={'month': 'Mois', 'count': 'Nombre de Crimes', 'year': 'Année'},
        markers=True
    )
    fig.update_layout(
        font=dict(size=12),
        title_font_size=16,
        xaxis_title="Mois",
        yaxis_title="Nombre de crimes",
        legend_title="Année",
        height=450,
        hovermode='x unified'
    )
    fig.update_traces(line=dict(width=3), marker=dict(size=8))
    st.plotly_chart(fig, use_container_width=True)
    
    st.success("""
    **Insights :** Ce graphique permet d'identifier si certains mois sont systématiquement 
    plus criminels d'une année à l'autre, révélant des patterns saisonniers récurrents.
    """)

# =====================================
# FOOTER
# =====================================
st.markdown("---")
st.markdown("""
    <div class='footer'>
        <h3 style='margin: 0 0 15px 0; font-size: 24px;'>
            🚔 Tableau de Bord d'Analyse de la Criminalité
        </h3>
        <p style='margin: 5px 0; font-size: 16px;'>
            📊 Période des données : 2020 - Aujourd'hui
        </p>
        <p style='margin: 5px 0; font-size: 16px;'>
            📍 Zone : Los Angeles, Californie
        </p>
        <p style='margin: 15px 0 5px 0; font-size: 14px;'>
            Développé avec Streamlit 🎈 | © 2025 Équipe d'Analyse Criminelle
        </p>
        <p style='margin: 5px 0 0 0; font-size: 12px; opacity: 0.8;'>
            💡 Données issues des archives publiques de la police de Los Angeles
        </p>
    </div>
    """, unsafe_allow_html=True)

# =====================================
# TÉLÉCHARGEMENT DES DONNÉES (SIDEBAR)
# =====================================
st.sidebar.markdown("---")
st.sidebar.markdown("""
    <div style='background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                padding: 15px; border-radius: 10px; text-align: center;'>
        <h3 style='color: white; margin: 0; font-size: 18px;'> EXPORT</h3>
        <p style='color: white; margin: 5px 0 0 0; font-size: 13px;'>
            Téléchargez les données filtrées
        </p>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.markdown("<br>", unsafe_allow_html=True)

# Bouton de téléchargement
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.sidebar.download_button(
    label=" Télécharger en CSV",
    data=csv,
    file_name=f"crimes_LA_filtres_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
    mime="text/csv",
    use_container_width=True,
    help="Télécharge les données actuellement filtrées au format CSV"
)

# Statistiques du téléchargement
st.sidebar.markdown(f"""
<div style='background: #f0f2f6; padding: 10px; border-radius: 8px; margin-top: 10px;'>
    <p style='margin: 0; font-size: 12px; color: #666;'>
         Fichier contiendra : <b>{len(filtered_df):,} lignes</b>
    </p>
    <p style='margin: 5px 0 0 0; font-size: 12px; color: #666;'>
         Colonnes : <b>{len(filtered_df.columns)}</b>
    </p>
</div>
""", unsafe_allow_html=True)

# Informations supplémentaires
st.sidebar.markdown("---")
st.sidebar.markdown("### Aide")
st.sidebar.info("""
**Besoin d'aide ?**

- Utilisez les **filtres** en haut pour personnaliser votre analyse
- **Survolez** les graphiques pour plus de détails
- **Cliquez** sur les légendes pour filtrer les catégories
- Les onglets offrent différentes perspectives d'analyse
)
