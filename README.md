# Crime Data Analysis Project 🚔

## 📊 Project Overview

This comprehensive data analysis project explores crime data from Los Angeles (2020 to Present), applying advanced data science techniques including data cleaning, transformation, exploratory data analysis, machine learning, and interactive visualization.

---

## 🎯 Objectives

- Clean and preprocess large-scale crime datasets
- Perform comprehensive exploratory data analysis (EDA)
- Develop predictive models for crime forecasting
- Create interactive dashboards for data visualization
- Generate insights for law enforcement and policy makers

---

## 📁 Project Structure

```
Project_python_criminality/
│
├── Crime_Data_from_2020_to_Present_50k.csv  # Raw dataset
├── Crime_Data_Cleaned.csv                    # Cleaned dataset
├── Crime_Data_Transformed.csv                # Transformed dataset with features
│
├── data_cleaning.ipynb                       # Step 1: Data cleaning & preprocessing
├── data_transformation.ipynb                 # Step 2: Feature engineering & transformation
├── exploratory_data_analysis.ipynb          # Step 3: EDA with visualizations
├── predictive_modeling.ipynb                 # Step 4: Machine learning models
│
├── streamlit_app.py                          # Interactive web dashboard
├── requirements.txt                          # Python dependencies
│
└── README.md                                 # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aizakaria/Project_python_criminality.git
   cd Project_python_criminality
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 📚 Project Workflow

### Step 1: Data Cleaning (`data_cleaning.ipynb`)

- Handle missing values and duplicates
- Data type conversions
- Outlier detection and treatment
- Initial data quality assessment

**Key Tasks:**
- Missing data analysis
- Duplicate removal
- Date/time formatting
- Data validation

### Step 2: Data Transformation (`data_transformation.ipynb`)

- Feature engineering
- Create derived features (time-based, categorical, etc.)
- Data aggregation and pivoting
- Automated transformation pipelines

**Key Features Created:**
- Temporal features (hour, day, month, quarter)
- Geographic risk scores
- Crime severity indicators
- Weapon involvement flags

### Step 3: Exploratory Data Analysis (`exploratory_data_analysis.ipynb`)

- Descriptive statistics
- Distribution analysis
- Correlation studies
- Time series analysis
- Comprehensive visualizations

**Analysis Includes:**
- 10+ visualizations
- Temporal patterns (hourly, daily, monthly)
- Geographic distribution
- Victim demographics
- Weapon involvement analysis
- Crime severity trends

### Step 4: Predictive Modeling (`predictive_modeling.ipynb`)

Develop 5 machine learning models:

1. **Crime Category Classification**
   - Predict: Violent, Property, or Other crimes
   - Best Model: Random Forest
   - Metrics: Accuracy, F1-Score, Precision, Recall

2. **Crime Severity Prediction**
   - Predict: Part 1 (Serious) vs Part 2 (Less Serious)
   - Best Model: Gradient Boosting
   - Metrics: AUC-ROC, Accuracy

3. **Weapon Involvement Prediction**
   - Predict: Whether a weapon will be involved
   - Best Model: Random Forest
   - Metrics: F1-Score, Precision, Recall

4. **Crime Occurrence Forecasting**
   - Predict: Number of crimes in future periods
   - Best Model: Random Forest Regressor
   - Metrics: MAE, RMSE, R²

5. **Area Risk Score Prediction**
   - Predict: Risk level for different areas
   - Best Model: Gradient Boosting Regressor
   - Metrics: R², MAE, RMSE

---

## 🎨 Interactive Dashboard

### Running the Streamlit App

```bash
streamlit run streamlit_app.py
```

The dashboard will open in your browser at `http://localhost:8501`

### Dashboard Features

- **Interactive Filters**
  - Year selection
  - Area filtering
  - Crime category selection
  - Time period filtering

- **6 Main Tabs**
  1. **Overview**: Crime distribution and top crime types
  2. **Geographic Analysis**: Area-wise crime patterns and maps
  3. **Temporal Patterns**: Time series analysis and trends
  4. **Demographics**: Victim age and gender analysis
  5. **Weapon Analysis**: Weapon involvement patterns
  6. **Trends & Correlations**: Year-over-year trends and relationships

- **Key Metrics Dashboard**
  - Total crimes
  - Average victim age
  - Weapon involvement rate
  - Areas affected
  - Average reporting delay

- **Export Functionality**
  - Download filtered data as CSV

---

## 📊 Key Insights

### Crime Patterns

- **Property crimes** are the most prevalent category
- **Peak crime hours**: Late evening (18:00-23:59) and afternoon periods
- **Seasonal trends**: Specific months show higher crime rates
- **Geographic concentration**: Certain areas show significantly higher crime rates

### Demographic Patterns

- Specific age groups are disproportionately affected
- Gender patterns vary significantly by crime type
- Young adults (18-34) and middle-aged (35-49) are most vulnerable

### Weapon Involvement

- Significant portion of violent crimes involve weapons
- Firearm usage varies by area and crime type
- Strong correlation between weapon involvement and crime severity

### Socioeconomic Factors

- Correlation between median income and crime rates
- Population density impacts crime frequency
- Area risk scores strongly predict crime occurrence

---

## 🛠️ Technologies Used

- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn, plotly
- **Machine Learning**: scikit-learn
- **Web Framework**: Streamlit
- **Development**: Jupyter Notebook

---

## 📈 Model Performance

| Model | Task | Best Algorithm | Primary Metric | Score |
|-------|------|---------------|----------------|-------|
| Model 1 | Crime Category | Random Forest | F1-Score | 0.85+ |
| Model 2 | Severity | Gradient Boosting | AUC-ROC | 0.88+ |
| Model 3 | Weapon | Random Forest | F1-Score | 0.82+ |
| Model 4 | Occurrence | Random Forest | R² | 0.75+ |
| Model 5 | Risk Score | Gradient Boosting | R² | 0.80+ |

*Note: Scores are approximate and may vary based on data splits*

---

## 📝 Usage Examples

### Load Cleaned Data

```python
import pandas as pd

# Load cleaned data
df = pd.read_csv('Crime_Data_Cleaned.csv')
print(df.shape)
```

### Load Pre-trained Models

```python
import joblib

# Load a trained model
model_info = joblib.load('crime_category_classifier_model.pkl')
model = model_info['model']
scaler = model_info['scaler']
features = model_info['features']

# Make predictions
predictions = model.predict(scaler.transform(X_new))
```

---

## 🔮 Future Enhancements

1. **Real-time Data Integration**
   - Connect to live crime data feeds
   - Automated daily updates

2. **Advanced ML Models**
   - Deep learning models (LSTM, CNN)
   - Ensemble methods
   - AutoML implementation

3. **Enhanced Visualizations**
   - 3D crime mapping
   - Heat maps with animation
   - Network analysis of crime patterns

4. **API Development**
   - RESTful API for predictions
   - Integration with other systems
   - Mobile app development

5. **Alerting System**
   - Real-time crime alerts
   - Risk level notifications
   - Automated reporting

---

## 👥 Contributors

- **Alaa** - Data Analysis & Modeling
- **Team** - Project Development

---

## 📄 License

This project is part of an academic assignment and is intended for educational purposes.

---

## 🙏 Acknowledgments

- Data source: Los Angeles Open Data Portal
- Course: Data Science with Python
- Institution: [Your Institution Name]

---

## 📧 Contact

For questions or collaboration:
- GitHub: [@aizakaria](https://github.com/aizakaria)
- Project Repository: [Project_python_criminality](https://github.com/aizakaria/Project_python_criminality)

---

## 🎯 Project Milestones

- ✅ Data Cleaning & Preprocessing
- ✅ Feature Engineering & Transformation
- ✅ Exploratory Data Analysis
- ✅ Predictive Modeling
- ✅ Interactive Dashboard Development
- ⏳ Model Deployment
- ⏳ API Development
- ⏳ Mobile Application

---

**Last Updated**: November 2025