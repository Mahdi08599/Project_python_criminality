"""
Model Prediction Demo
=====================
Demonstration script showing how to use the trained models for predictions.
"""

import pandas as pd
import numpy as np
import joblib
from datetime import datetime

def print_header(text):
    """Print formatted header"""
    print("\n" + "=" * 80)
    print(text)
    print("=" * 80 + "\n")

def load_models():
    """Load all trained models"""
    print("📦 Loading trained models...")
    
    models = {}
    model_files = [
        'crime_category_classifier_model.pkl',
        'crime_severity_classifier_model.pkl',
        'weapon_involvement_classifier_model.pkl',
        'crime_occurrence_regressor_model.pkl',
        'area_risk_regressor_model.pkl'
    ]
    
    for model_file in model_files:
        try:
            models[model_file] = joblib.load(model_file)
            print(f"  ✅ Loaded: {model_file}")
        except FileNotFoundError:
            print(f"  ❌ Not found: {model_file}")
    
    return models

def predict_crime_category(model_info, features_dict):
    """
    Predict the category of a crime
    
    Parameters:
    -----------
    model_info : dict
        Dictionary containing model, scaler, and feature names
    features_dict : dict
        Dictionary of feature values
    
    Returns:
    --------
    prediction : str
        Predicted crime category
    """
    model = model_info['model']
    scaler = model_info['scaler']
    features = model_info['features']
    
    # Create feature array
    X = np.array([[features_dict.get(f, 0) for f in features]])
    
    # Scale features
    X_scaled = scaler.transform(X)
    
    # Predict
    prediction = model.predict(X_scaled)[0]
    probabilities = model.predict_proba(X_scaled)[0]
    
    return prediction, probabilities, model.classes_

def predict_weapon_involvement(model_info, features_dict):
    """Predict whether a weapon will be involved"""
    model = model_info['model']
    scaler = model_info['scaler']
    features = model_info['features']
    
    X = np.array([[features_dict.get(f, 0) for f in features]])
    X_scaled = scaler.transform(X)
    
    prediction = model.predict(X_scaled)[0]
    probability = model.predict_proba(X_scaled)[0][1]
    
    return prediction, probability

def demo_scenario_1():
    """Demo: Predict crime for a specific scenario"""
    print_header("DEMO SCENARIO 1: Late Night Theft in Central LA")
    
    # Example features
    features = {
        'Vict Age': 35,
        'AREA': 1,  # Central
        'hour': 23,  # 11 PM
        'month': 7,  # July
        'quarter': 3,
        'year': 2023,
        'is_weekend': 1,
        'reporting_delay_days': 1,
        'area_risk_score': 75.5,
        'population': 50000,
        'median_income': 45000,
        'area_size_sq_miles': 8.5,
        'crimes_per_1000': 35.2,
        'is_night': 1,
        'is_rush_hour': 0,
        # Add encoded features (simplified)
        'AREA NAME_encoded': 0,
        'day_name_encoded': 5,
        'month_name_encoded': 6,
        'time_period_encoded': 3,
        'victim_age_group_encoded': 2,
        'location_type_encoded': 1,
        'weapon_category_encoded': 0
    }
    
    print("📋 Scenario Details:")
    print(f"  Location: Central LA (Area {features['AREA']})")
    print(f"  Time: {features['hour']}:00 (Late Evening)")
    print(f"  Date: July 2023, Weekend")
    print(f"  Victim Age: {features['Vict Age']}")
    print(f"  Area Risk Score: {features['area_risk_score']}")
    
    return features

def demo_scenario_2():
    """Demo: Morning crime in affluent area"""
    print_header("DEMO SCENARIO 2: Morning Incident in West LA")
    
    features = {
        'Vict Age': 42,
        'AREA': 8,  # West LA
        'hour': 9,  # 9 AM
        'month': 3,  # March
        'quarter': 1,
        'year': 2023,
        'is_weekend': 0,
        'reporting_delay_days': 0,
        'area_risk_score': 45.2,
        'population': 65000,
        'median_income': 75000,
        'area_size_sq_miles': 10.2,
        'crimes_per_1000': 25.8,
        'is_night': 0,
        'is_rush_hour': 1,
        'AREA NAME_encoded': 7,
        'day_name_encoded': 2,
        'month_name_encoded': 2,
        'time_period_encoded': 1,
        'victim_age_group_encoded': 2,
        'location_type_encoded': 0,
        'weapon_category_encoded': 0
    }
    
    print("📋 Scenario Details:")
    print(f"  Location: West LA (Area {features['AREA']})")
    print(f"  Time: {features['hour']}:00 (Morning Rush Hour)")
    print(f"  Date: March 2023, Weekday")
    print(f"  Victim Age: {features['Vict Age']}")
    print(f"  Area Risk Score: {features['area_risk_score']}")
    print(f"  Median Income: ${features['median_income']:,}")
    
    return features

def main():
    """Main demonstration function"""
    print("\n" + "🚔" * 40)
    print_header("CRIME PREDICTION MODEL DEMONSTRATION")
    print("This script demonstrates how to use the trained models for predictions")
    
    # Check if data file exists
    try:
        df = pd.read_csv('Crime_Data_Transformed.csv', nrows=5)
        print("✅ Data file found!")
    except FileNotFoundError:
        print("⚠️  Crime_Data_Transformed.csv not found. Some demos may not work.")
        print("    Please run data_transformation.ipynb first.")
    
    # Load models
    models = load_models()
    
    if not models:
        print("\n❌ No models found! Please train models first by running:")
        print("   jupyter notebook predictive_modeling.ipynb")
        return
    
    # Demo Scenario 1
    features_1 = demo_scenario_1()
    
    if 'crime_category_classifier_model.pkl' in models:
        prediction, probs, classes = predict_crime_category(
            models['crime_category_classifier_model.pkl'], 
            features_1
        )
        
        print("\n🎯 PREDICTIONS:")
        print(f"\n  Crime Category: {prediction}")
        print(f"\n  Probabilities:")
        for cls, prob in zip(classes, probs):
            print(f"    - {cls}: {prob*100:.2f}%")
    
    if 'weapon_involvement_classifier_model.pkl' in models:
        weapon_pred, weapon_prob = predict_weapon_involvement(
            models['weapon_involvement_classifier_model.pkl'],
            features_1
        )
        
        print(f"\n  Weapon Involvement: {'YES' if weapon_pred == 1 else 'NO'}")
        print(f"  Probability: {weapon_prob*100:.2f}%")
    
    # Demo Scenario 2
    features_2 = demo_scenario_2()
    
    if 'crime_category_classifier_model.pkl' in models:
        prediction, probs, classes = predict_crime_category(
            models['crime_category_classifier_model.pkl'], 
            features_2
        )
        
        print("\n🎯 PREDICTIONS:")
        print(f"\n  Crime Category: {prediction}")
        print(f"\n  Probabilities:")
        for cls, prob in zip(classes, probs):
            print(f"    - {cls}: {prob*100:.2f}%")
    
    # Batch prediction example
    print_header("DEMO: BATCH PREDICTIONS")
    print("Processing multiple records from dataset...\n")
    
    try:
        df_sample = pd.read_csv('Crime_Data_Transformed.csv', nrows=10)
        print(f"✅ Loaded {len(df_sample)} records for batch prediction")
        
        if 'crime_category_classifier_model.pkl' in models:
            model_info = models['crime_category_classifier_model.pkl']
            features = model_info['features']
            
            # Prepare features
            X = df_sample[features].fillna(0)
            X_scaled = model_info['scaler'].transform(X)
            
            # Predict
            predictions = model_info['model'].predict(X_scaled)
            
            print("\n📊 Batch Prediction Results:")
            print(f"\nPredicted Categories:")
            print(pd.Series(predictions).value_counts())
            
    except Exception as e:
        print(f"⚠️  Could not perform batch predictions: {e}")
    
    # Summary
    print_header("SUMMARY & NEXT STEPS")
    print("✅ Successfully demonstrated model predictions")
    print("\n📚 To use these models in your application:")
    print("   1. Load the model using joblib.load()")
    print("   2. Prepare your features dictionary")
    print("   3. Scale features using the model's scaler")
    print("   4. Call model.predict() or model.predict_proba()")
    print("\n💡 For production deployment:")
    print("   - Create a REST API using Flask/FastAPI")
    print("   - Add input validation")
    print("   - Implement error handling")
    print("   - Add logging and monitoring")
    print("\n🔗 Check streamlit_app.py for interactive predictions!")
    
    print("\n" + "🚔" * 40 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
