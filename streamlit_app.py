"""
Crime Data Analysis - Interactive Dashboard
============================================
A Streamlit web application for exploring and visualizing crime data from 2020 to present.

Author: Crime Data Analysis Team
Date: November 2025
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

# Page configuration
st.set_page_config(
    page_title="Crime Data Analysis Dashboard",
    page_icon="🚔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
    }
    h1 {
        color: #1f77b4;
    }
    h2 {
        color: #ff7f0e;
    }
    </style>
    """, unsafe_allow_html=True)

# Cache data loading
@st.cache_data
def load_data():
    """Load and preprocess the crime data"""
    df = pd.read_csv('Crime_Data_Transformed.csv')
    df['Date Rptd'] = pd.to_datetime(df['Date Rptd'])
    df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])
    return df

# Main title
st.title("🚔 Crime Data Analysis Dashboard")
st.markdown("### Interactive Exploratory Data Analysis - Los Angeles Crime Data (2020-Present)")
st.markdown("---")

# Load data with spinner
with st.spinner('Loading crime data...'):
    df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")
st.sidebar.markdown("---")

# Year filter
years = sorted(df['year'].unique())
selected_years = st.sidebar.multiselect(
    "Select Year(s)",
    options=years,
    default=years
)

# Area filter
areas = sorted(df['AREA NAME'].unique())
selected_areas = st.sidebar.multiselect(
    "Select Area(s)",
    options=areas,
    default=areas[:5] if len(areas) > 5 else areas
)

# Crime category filter
crime_categories = sorted(df['crime_category'].unique())
selected_categories = st.sidebar.multiselect(
    "Select Crime Category",
    options=crime_categories,
    default=crime_categories
)

# Time period filter
time_periods = sorted(df['time_period'].unique())
selected_time_periods = st.sidebar.multiselect(
    "Select Time Period",
    options=time_periods,
    default=time_periods
)

# Apply filters
filtered_df = df[
    (df['year'].isin(selected_years)) &
    (df['AREA NAME'].isin(selected_areas)) &
    (df['crime_category'].isin(selected_categories)) &
    (df['time_period'].isin(selected_time_periods))
]

st.sidebar.markdown("---")
st.sidebar.info(f"**Filtered Records:** {len(filtered_df):,} / {len(df):,}")

# Key Metrics with better styling
st.markdown("## 📊 Key Metrics")
st.markdown("<br>", unsafe_allow_html=True)

# Create metrics with custom styling
col1, col2, col3, col4, col5 = st.columns(5)

total_crimes = len(filtered_df)
total_percentage = (len(filtered_df)/len(df)*100)
avg_victim_age = filtered_df['Vict Age'].mean()
weapon_rate = (filtered_df['weapon_involved'].sum() / len(filtered_df) * 100) if len(filtered_df) > 0 else 0
unique_areas = filtered_df['AREA NAME'].nunique()
avg_delay = filtered_df['reporting_delay_days'].mean() if 'reporting_delay_days' in filtered_df.columns else 0

with col1:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 25px; border-radius: 15px; text-align: center; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h3 style='margin: 0; font-size: 16px; font-weight: 500;'>🔢 Total Crimes</h3>
        <h1 style='margin: 10px 0; font-size: 36px; font-weight: bold;'>{total_crimes:,}</h1>
        <p style='margin: 0; font-size: 14px; opacity: 0.9;'>↑ {total_percentage:.1f}% of total</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                padding: 25px; border-radius: 15px; text-align: center; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h3 style='margin: 0; font-size: 16px; font-weight: 500;'>👤 Avg Victim Age</h3>
        <h1 style='margin: 10px 0; font-size: 36px; font-weight: bold;'>{avg_victim_age:.1f}</h1>
        <p style='margin: 0; font-size: 14px; opacity: 0.9;'>years old</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); 
                padding: 25px; border-radius: 15px; text-align: center; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h3 style='margin: 0; font-size: 16px; font-weight: 500;'>🔫 Weapon Rate</h3>
        <h1 style='margin: 10px 0; font-size: 36px; font-weight: bold;'>{weapon_rate:.1f}%</h1>
        <p style='margin: 0; font-size: 14px; opacity: 0.9;'>involved weapons</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #30cfd0 0%, #330867 100%); 
                padding: 25px; border-radius: 15px; text-align: center; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h3 style='margin: 0; font-size: 16px; font-weight: 500;'>📍 Areas</h3>
        <h1 style='margin: 10px 0; font-size: 36px; font-weight: bold;'>{unique_areas}</h1>
        <p style='margin: 0; font-size: 14px; opacity: 0.9;'>affected zones</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); 
                padding: 25px; border-radius: 15px; text-align: center; color: #333; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h3 style='margin: 0; font-size: 16px; font-weight: 500;'>⏱️ Avg Delay</h3>
        <h1 style='margin: 10px 0; font-size: 36px; font-weight: bold;'>{avg_delay:.1f}</h1>
        <p style='margin: 0; font-size: 14px; opacity: 0.8;'>days to report</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("---")

# Create tabs for different visualizations
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📈 Overview", 
    "🗺️ Geographic Analysis", 
    "⏰ Temporal Patterns", 
    "👥 Demographics", 
    "🔫 Weapon Analysis",
    "📉 Trends & Correlations"
])

# TAB 1: Overview
with tab1:
    st.header("Crime Distribution Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Crime Category Distribution")
        category_counts = filtered_df['crime_category'].value_counts()
        
        fig = px.pie(
            values=category_counts.values,
            names=category_counts.index,
            title="Crime Categories",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Top 10 Crime Types")
        top_crimes = filtered_df['Crm Cd Desc'].value_counts().head(10)
        
        fig = px.bar(
            x=top_crimes.values,
            y=top_crimes.index,
            orientation='h',
            title="Most Common Crime Types",
            labels={'x': 'Number of Cases', 'y': 'Crime Type'},
            color=top_crimes.values,
            color_continuous_scale='Reds'
        )
        fig.update_layout(showlegend=False, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
    
    # Crime Severity
    st.subheader("Crime Severity Distribution")
    col3, col4 = st.columns([2, 1])
    
    with col3:
        severity_counts = filtered_df['crime_severity'].value_counts()
        fig = px.bar(
            x=severity_counts.index,
            y=severity_counts.values,
            title="Distribution by Severity Level",
            labels={'x': 'Severity', 'y': 'Number of Crimes'},
            color=severity_counts.values,
            color_continuous_scale='Viridis'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col4:
        st.markdown("#### Statistics")
        st.dataframe(
            filtered_df[['crime_category', 'crime_severity']].value_counts().head(10),
            use_container_width=True
        )

# TAB 2: Geographic Analysis
with tab2:
    st.header("Geographic Distribution")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Top 15 Areas by Crime Count")
        top_areas = filtered_df['AREA NAME'].value_counts().head(15)
        
        fig = px.bar(
            x=top_areas.values,
            y=top_areas.index,
            orientation='h',
            title="Crime Distribution Across Areas",
            labels={'x': 'Number of Crimes', 'y': 'Area Name'},
            color=top_areas.values,
            color_continuous_scale='Blues'
        )
        fig.update_layout(yaxis={'categoryorder':'total ascending'}, height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Area Statistics")
        area_stats = filtered_df.groupby('AREA NAME').agg({
            'DR_NO': 'count',
            'area_risk_score': 'mean',
            'population': 'first',
            'median_income': 'first'
        }).round(2)
        area_stats.columns = ['Crimes', 'Risk Score', 'Population', 'Income']
        area_stats = area_stats.sort_values('Crimes', ascending=False).head(10)
        st.dataframe(area_stats, use_container_width=True)
    
    # Crime density map
    st.subheader("Crime Density Map")
    
    # Sample data for performance (if dataset is large)
    map_data = filtered_df[['LAT', 'LON', 'crime_category']].dropna()
    if len(map_data) > 5000:
        map_data = map_data.sample(5000)
    
    fig = px.scatter_mapbox(
        map_data,
        lat='LAT',
        lon='LON',
        color='crime_category',
        zoom=9,
        height=500,
        title="Crime Locations",
        mapbox_style="carto-positron"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Area comparison
    st.subheader("Area Comparison: Crime Categories")
    top_5_areas = filtered_df['AREA NAME'].value_counts().head(5).index
    area_category = pd.crosstab(
        filtered_df[filtered_df['AREA NAME'].isin(top_5_areas)]['AREA NAME'],
        filtered_df[filtered_df['AREA NAME'].isin(top_5_areas)]['crime_category']
    )
    
    fig = px.bar(
        area_category,
        barmode='group',
        title="Crime Categories by Top 5 Areas",
        labels={'value': 'Number of Crimes', 'AREA NAME': 'Area'}
    )
    st.plotly_chart(fig, use_container_width=True)

# TAB 3: Temporal Patterns
with tab3:
    st.header("Temporal Analysis")
    
    # Time series
    st.subheader("Crime Trends Over Time")
    
    time_agg = st.selectbox(
        "Select Time Aggregation",
        options=["Daily", "Weekly", "Monthly"],
        index=2
    )
    
    df_ts = filtered_df.set_index('DATE OCC').sort_index()
    
    if time_agg == "Daily":
        time_series = df_ts.resample('D').size()
    elif time_agg == "Weekly":
        time_series = df_ts.resample('W').size()
    else:
        time_series = df_ts.resample('M').size()
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=time_series.index,
        y=time_series.values,
        mode='lines',
        name='Crime Count',
        line=dict(color='#1f77b4', width=2)
    ))
    
    if time_agg == "Daily":
        rolling_avg = time_series.rolling(window=7).mean()
        fig.add_trace(go.Scatter(
            x=rolling_avg.index,
            y=rolling_avg.values,
            mode='lines',
            name='7-Day Moving Average',
            line=dict(color='#ff7f0e', width=2, dash='dash')
        ))
    
    fig.update_layout(
        title=f"{time_agg} Crime Trends",
        xaxis_title="Date",
        yaxis_title="Number of Crimes",
        hovermode='x unified',
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Temporal patterns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("By Day of Week")
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_counts = filtered_df['day_name'].value_counts().reindex(day_order)
        
        fig = px.bar(
            x=day_order,
            y=day_counts.values,
            title="Crimes by Day",
            labels={'x': 'Day', 'y': 'Count'},
            color=day_counts.values,
            color_continuous_scale='Blues'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("By Month")
        month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December']
        month_counts = filtered_df['month_name'].value_counts().reindex(month_order)
        
        fig = px.line(
            x=month_order,
            y=month_counts.values,
            title="Crimes by Month",
            labels={'x': 'Month', 'y': 'Count'},
            markers=True
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        st.subheader("By Hour")
        hour_counts = filtered_df['hour'].value_counts().sort_index()
        
        fig = px.line(
            x=hour_counts.index,
            y=hour_counts.values,
            title="Crimes by Hour",
            labels={'x': 'Hour', 'y': 'Count'},
            markers=True
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Time period analysis
    st.subheader("Crime Distribution by Time Period")
    time_period_order = ['Night (00:00-05:59)', 'Morning (06:00-11:59)',
                         'Afternoon (12:00-17:59)', 'Evening (18:00-23:59)']
    time_counts = filtered_df['time_period'].value_counts().reindex(time_period_order)
    
    fig = px.bar(
        x=['Night', 'Morning', 'Afternoon', 'Evening'],
        y=time_counts.values,
        title="Crimes by Time of Day",
        labels={'x': 'Time Period', 'y': 'Number of Crimes'},
        color=time_counts.values,
        color_continuous_scale='Sunset'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Heatmap: Day vs Hour
    st.subheader("Crime Heatmap: Day of Week vs Hour")
    heatmap_data = pd.crosstab(filtered_df['day_name'], filtered_df['hour'])
    heatmap_data = heatmap_data.reindex(day_order)
    
    fig = px.imshow(
        heatmap_data,
        labels=dict(x="Hour", y="Day of Week", color="Crime Count"),
        x=heatmap_data.columns,
        y=heatmap_data.index,
        color_continuous_scale='YlOrRd',
        aspect="auto"
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

# TAB 4: Demographics
with tab4:
    st.header("Victim Demographics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Age Group Distribution")
        age_order = ['Child (0-17)', 'Young Adult (18-34)', 'Middle Age (35-49)', 
                     'Senior (50-64)', 'Elderly (65+)']
        age_counts = filtered_df['victim_age_group'].value_counts()
        age_counts = age_counts.reindex([a for a in age_order if a in age_counts.index])
        
        fig = px.bar(
            x=age_counts.index,
            y=age_counts.values,
            title="Victims by Age Group",
            labels={'x': 'Age Group', 'y': 'Number of Victims'},
            color=age_counts.values,
            color_continuous_scale='Teal'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Gender Distribution")
        sex_counts = filtered_df['Vict Sex'].value_counts().head(5)
        
        fig = px.pie(
            values=sex_counts.values,
            names=sex_counts.index,
            title="Victims by Gender",
            hole=0.3,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Age distribution histogram
    st.subheader("Detailed Age Distribution")
    fig = px.histogram(
        filtered_df,
        x='Vict Age',
        nbins=50,
        title="Victim Age Distribution (Histogram)",
        labels={'Vict Age': 'Age', 'count': 'Frequency'},
        color_discrete_sequence=['#636EFA']
    )
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # Demographics by crime category
    st.subheader("Demographics by Crime Category")
    demo_category = pd.crosstab(
        filtered_df['crime_category'],
        filtered_df['victim_age_group']
    )
    
    fig = px.bar(
        demo_category,
        barmode='stack',
        title="Age Groups Across Crime Categories",
        labels={'value': 'Number of Cases', 'crime_category': 'Crime Category'}
    )
    st.plotly_chart(fig, use_container_width=True)

# TAB 5: Weapon Analysis
with tab5:
    st.header("Weapon Involvement Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Weapon Involvement")
        weapon_counts = filtered_df['weapon_involved'].value_counts()
        weapon_labels = ['No Weapon', 'Weapon Involved']
        
        fig = px.pie(
            values=weapon_counts.values,
            names=weapon_labels,
            title="Overall Weapon Involvement",
            color_discrete_sequence=['#90EE90', '#FF6B6B'],
            hole=0.4
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Weapon Categories")
        weapon_cat = filtered_df[filtered_df['weapon_involved'] == 1]['weapon_category'].value_counts()
        
        fig = px.bar(
            x=weapon_cat.index,
            y=weapon_cat.values,
            title="Types of Weapons Used",
            labels={'x': 'Weapon Category', 'y': 'Number of Cases'},
            color=weapon_cat.values,
            color_continuous_scale='Reds'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Weapon by crime category
    st.subheader("Weapon Usage by Crime Category")
    weapon_crime = pd.crosstab(
        filtered_df['crime_category'],
        filtered_df['weapon_involved'],
        normalize='index'
    ) * 100
    weapon_crime.columns = ['No Weapon', 'Weapon']
    
    fig = px.bar(
        weapon_crime,
        barmode='group',
        title="Weapon Involvement Percentage by Crime Category",
        labels={'value': 'Percentage (%)', 'crime_category': 'Crime Category'}
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Top weapons by area
    st.subheader("Weapon Usage by Area (Top 10)")
    top_10_areas = filtered_df['AREA NAME'].value_counts().head(10).index
    area_weapon = filtered_df[filtered_df['AREA NAME'].isin(top_10_areas)].groupby('AREA NAME')['weapon_involved'].apply(
        lambda x: (x == 1).sum() / len(x) * 100
    ).sort_values(ascending=False)
    
    fig = px.bar(
        x=area_weapon.values,
        y=area_weapon.index,
        orientation='h',
        title="Weapon Involvement Rate by Area",
        labels={'x': 'Weapon Involvement (%)', 'y': 'Area'},
        color=area_weapon.values,
        color_continuous_scale='Oranges'
    )
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)

# TAB 6: Trends & Correlations
with tab6:
    st.header("Trends and Correlations")
    
    # Year-over-year trends
    st.subheader("Year-over-Year Crime Trends")
    year_category = pd.crosstab(filtered_df['year'], filtered_df['crime_category'])
    
    fig = px.line(
        year_category,
        title="Crime Trends by Category (Yearly)",
        labels={'value': 'Number of Crimes', 'year': 'Year'},
        markers=True
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Correlation analysis
    st.subheader("Correlation Matrix")
    
    corr_vars = ['Vict Age', 'weapon_involved', 'is_weekend', 'reporting_delay_days',
                 'area_risk_score', 'population', 'median_income', 'crimes_per_1000', 'hour']
    corr_vars = [var for var in corr_vars if var in filtered_df.columns]
    
    correlation = filtered_df[corr_vars].corr()
    
    fig = px.imshow(
        correlation,
        labels=dict(color="Correlation"),
        x=correlation.columns,
        y=correlation.columns,
        color_continuous_scale='RdBu_r',
        aspect="auto",
        zmin=-1,
        zmax=1
    )
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)
    
    # Scatter plots
    st.subheader("Relationship Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Population vs Crime Rate**")
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
            title="Population vs Crime Rate (per 1000)",
            labels={'population': 'Population', 'crime_rate': 'Crime Rate'},
            trendline="ols"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.write("**Median Income vs Crime Count**")
        fig = px.scatter(
            area_data,
            x='median_income',
            y='DR_NO',
            hover_data=['AREA NAME'],
            title="Income vs Total Crimes",
            labels={'median_income': 'Median Income', 'DR_NO': 'Total Crimes'},
            trendline="ols"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Monthly patterns across years
    st.subheader("Monthly Patterns Across Years")
    monthly_year = filtered_df.groupby(['year', 'month']).size().reset_index(name='count')
    
    fig = px.line(
        monthly_year,
        x='month',
        y='count',
        color='year',
        title="Monthly Crime Patterns by Year",
        labels={'month': 'Month', 'count': 'Number of Crimes', 'year': 'Year'},
        markers=True
    )
    st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: gray; padding: 20px;'>
        <p>Crime Data Analysis Dashboard | Data Period: 2020 - Present</p>
        <p>Built with Streamlit 🎈 | © 2025 Crime Analysis Team</p>
    </div>
    """, unsafe_allow_html=True)

# Download filtered data
st.sidebar.markdown("---")
st.sidebar.header("📥 Download Data")
if st.sidebar.button("Download Filtered Data"):
    csv = filtered_df.to_csv(index=False)
    st.sidebar.download_button(
        label="Download CSV",
        data=csv,
        file_name=f"filtered_crime_data_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )
