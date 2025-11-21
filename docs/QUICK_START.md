# Quick Start Guide - Crime Data Analysis Project

## 🚀 Quick Start (3 Steps)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Interactive Dashboard
```bash
streamlit run streamlit_app.py
```

### 3. Open in Browser
Navigate to: `http://localhost:8501`

---

## 📓 Working with Notebooks

### Option 1: Jupyter Notebook
```bash
jupyter notebook
```

### Option 2: Jupyter Lab
```bash
jupyter lab
```

### Option 3: VS Code
Open `.ipynb` files directly in VS Code

---

## 🎯 Project Execution Order

1. **Data Cleaning** (`data_cleaning.ipynb`)
   - Load raw data
   - Handle missing values
   - Remove duplicates
   - Output: `Crime_Data_Cleaned.csv`

2. **Data Transformation** (`data_transformation.ipynb`)
   - Feature engineering
   - Create derived features
   - Output: `Crime_Data_Transformed.csv`

3. **Exploratory Data Analysis** (`exploratory_data_analysis.ipynb`)
   - Statistical analysis
   - Generate visualizations
   - Output: Multiple PNG files

4. **Predictive Modeling** (`predictive_modeling.ipynb`)
   - Train ML models
   - Evaluate performance
   - Output: Model `.pkl` files

5. **Interactive Dashboard** (`streamlit_app.py`)
   - Visualize insights
   - Interactive filtering
   - Real-time exploration

---

## 🐍 Using the Quick Start Script

```bash
python run_project.py
```

This interactive menu provides:
- Run Streamlit Dashboard
- Open Jupyter Notebooks
- Check Project Status
- Install Dependencies
- View Model Summary

---

## 📊 Dashboard Features

### Filters Available:
- **Years**: 2020-2023
- **Areas**: All LA areas
- **Crime Categories**: Violent, Property, Other
- **Time Periods**: Night, Morning, Afternoon, Evening

### Tabs:
1. **Overview**: General crime statistics
2. **Geographic**: Area-wise analysis
3. **Temporal**: Time patterns
4. **Demographics**: Victim analysis
5. **Weapon**: Weapon involvement
6. **Trends**: Correlations and trends

---

## 🤖 Using Trained Models

### Load a Model
```python
import joblib
import pandas as pd

# Load model
model_info = joblib.load('crime_category_classifier_model.pkl')
model = model_info['model']
scaler = model_info['scaler']
features = model_info['features']

# Prepare your data
X_new = df[features].fillna(0)
X_scaled = scaler.transform(X_new)

# Make predictions
predictions = model.predict(X_scaled)
```

---

## 🔧 Troubleshooting

### Issue: Module not found
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: Data file not found
**Solution:**
- Ensure you have run the notebooks in order
- Check if CSV files are in the project root

### Issue: Port already in use (Streamlit)
**Solution:**
```bash
streamlit run streamlit_app.py --server.port 8502
```

### Issue: Kernel dies in Jupyter
**Solution:**
- Reduce data sample size
- Increase system memory
- Close other applications

---

## 📈 Expected Outputs

### Data Files:
- `Crime_Data_Cleaned.csv` (after Step 1)
- `Crime_Data_Transformed.csv` (after Step 2)
- `Crime_Pivot_*.csv` (after Step 2)

### Visualizations:
- `eda_*.png` (10 files after Step 3)
- `model*.png` (5 files after Step 4)
- `feature_importance.png` (after Step 4)

### Models:
- `crime_category_classifier_model.pkl`
- `crime_severity_classifier_model.pkl`
- `weapon_involvement_classifier_model.pkl`
- `crime_occurrence_regressor_model.pkl`
- `area_risk_regressor_model.pkl`
- `label_encoders.pkl`

---

## 💡 Tips for Success

1. **Run notebooks sequentially** - Each step depends on the previous
2. **Check data files** - Ensure CSV files exist before proceeding
3. **Monitor memory usage** - Large datasets may require optimization
4. **Save frequently** - Save notebooks after significant changes
5. **Document findings** - Add markdown cells with insights

---

## 🎨 Customization

### Modify Dashboard Colors
Edit `streamlit_app.py`:
```python
# Line ~20
st.markdown("""
    <style>
    h1 {
        color: #YOUR_COLOR;
    }
    </style>
""", unsafe_allow_html=True)
```

### Add New Features
In `data_transformation.ipynb`:
```python
# Create custom feature
df['new_feature'] = your_transformation
```

### Adjust Model Parameters
In `predictive_modeling.ipynb`:
```python
# Example: Random Forest
RandomForestClassifier(
    n_estimators=200,  # Increase trees
    max_depth=15,      # Control depth
    random_state=42
)
```

---

## 📚 Additional Resources

- **Streamlit Docs**: https://docs.streamlit.io
- **Pandas Docs**: https://pandas.pydata.org/docs
- **Scikit-learn Docs**: https://scikit-learn.org/stable

---

## 🆘 Getting Help

1. Check the README.md
2. Review notebook markdown cells
3. Check error messages carefully
4. Verify all dependencies are installed
5. Ensure data files are present

---

## ✅ Project Checklist

- [ ] Dependencies installed
- [ ] Raw data file present
- [ ] Data cleaning completed
- [ ] Data transformation completed
- [ ] EDA completed with visualizations
- [ ] Models trained and saved
- [ ] Dashboard running successfully
- [ ] README reviewed
- [ ] Results documented

---

**Happy Analyzing! 🚔📊**
