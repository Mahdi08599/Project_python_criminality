#!/usr/bin/env python3
"""
Environment Test Script
=======================
Tests if all required packages and data files are present and working correctly.
"""

import sys
import os

def print_section(title):
    """Print a formatted section title"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def test_python_version():
    """Check Python version"""
    print_section("PYTHON VERSION")
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✅ Python version is compatible (3.8+)")
        return True
    else:
        print("❌ Python 3.8 or higher is required")
        return False

def test_core_packages():
    """Test core data science packages"""
    print_section("CORE PACKAGES")
    
    packages = {
        'pandas': 'Data manipulation',
        'numpy': 'Numerical computing',
        'matplotlib': 'Basic plotting',
        'seaborn': 'Statistical visualization',
        'sklearn': 'Machine learning'
    }
    
    all_ok = True
    for package, description in packages.items():
        try:
            if package == 'sklearn':
                import sklearn
                version = sklearn.__version__
            else:
                mod = __import__(package)
                version = mod.__version__
            
            print(f"✅ {package:12s} {version:10s} - {description}")
        except ImportError:
            print(f"❌ {package:12s} {'NOT FOUND':10s} - {description}")
            all_ok = False
    
    return all_ok

def test_optional_packages():
    """Test optional packages for advanced features"""
    print_section("OPTIONAL PACKAGES")
    
    packages = {
        'streamlit': 'Interactive dashboard',
        'plotly': 'Interactive visualizations',
        'joblib': 'Model serialization'
    }
    
    for package, description in packages.items():
        try:
            mod = __import__(package)
            version = getattr(mod, '__version__', 'unknown')
            print(f"✅ {package:12s} {version:10s} - {description}")
        except ImportError:
            print(f"⚠️  {package:12s} {'NOT FOUND':10s} - {description}")

def test_data_files():
    """Check if data files exist"""
    print_section("DATA FILES")
    
    files = {
        'Crime_Data_from_2020_to_Present_50k.csv': 'Raw data (required)',
        'Crime_Data_Cleaned.csv': 'Cleaned data',
        'Crime_Data_Transformed.csv': 'Transformed data'
    }
    
    all_ok = True
    for filename, description in files.items():
        if os.path.exists(filename):
            size_mb = os.path.getsize(filename) / (1024 * 1024)
            print(f"✅ {filename:40s} ({size_mb:.1f} MB) - {description}")
        else:
            print(f"❌ {filename:40s} (NOT FOUND) - {description}")
            if 'required' in description.lower():
                all_ok = False
    
    return all_ok

def test_notebooks():
    """Check if notebooks exist"""
    print_section("JUPYTER NOTEBOOKS")
    
    notebooks = [
        'data_cleaning.ipynb',
        'data_transformation.ipynb',
        'exploratory_data_analysis.ipynb',
        'predictive_modeling.ipynb'
    ]
    
    for notebook in notebooks:
        if os.path.exists(notebook):
            print(f"✅ {notebook}")
        else:
            print(f"❌ {notebook}")

def test_project_files():
    """Check if project files exist"""
    print_section("PROJECT FILES")
    
    files = {
        'streamlit_app.py': 'Dashboard application',
        'requirements.txt': 'Dependencies list',
        'README.md': 'Documentation',
        'run_project.py': 'Quick start script'
    }
    
    for filename, description in files.items():
        if os.path.exists(filename):
            print(f"✅ {filename:20s} - {description}")
        else:
            print(f"❌ {filename:20s} - {description}")

def test_basic_functionality():
    """Test basic data operations"""
    print_section("FUNCTIONALITY TEST")
    
    try:
        import pandas as pd
        import numpy as np
        
        # Test pandas
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['a', 'b', 'c']
        })
        print("✅ Pandas DataFrame creation works")
        
        # Test numpy
        arr = np.array([1, 2, 3])
        mean = np.mean(arr)
        print(f"✅ NumPy operations work (mean: {mean})")
        
        # Test matplotlib
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        plt.close(fig)
        print("✅ Matplotlib plotting works")
        
        # Test sklearn
        from sklearn.ensemble import RandomForestClassifier
        clf = RandomForestClassifier(n_estimators=10)
        print("✅ Scikit-learn model creation works")
        
        return True
        
    except Exception as e:
        print(f"❌ Functionality test failed: {e}")
        return False

def test_data_loading():
    """Test if data can be loaded"""
    print_section("DATA LOADING TEST")
    
    try:
        import pandas as pd
        
        # Try to load raw data
        if os.path.exists('Crime_Data_from_2020_to_Present_50k.csv'):
            df = pd.read_csv('Crime_Data_from_2020_to_Present_50k.csv', nrows=10)
            print(f"✅ Successfully loaded raw data")
            print(f"   Shape: {df.shape}")
            print(f"   Columns: {len(df.columns)}")
            return True
        else:
            print("⚠️  Raw data file not found - skipping test")
            return None
            
    except Exception as e:
        print(f"❌ Data loading failed: {e}")
        return False

def generate_report(results):
    """Generate summary report"""
    print_section("SUMMARY REPORT")
    
    total_tests = len(results)
    passed = sum(1 for r in results.values() if r is True)
    failed = sum(1 for r in results.values() if r is False)
    skipped = sum(1 for r in results.values() if r is None)
    
    print(f"\nTotal Tests: {total_tests}")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"⚠️  Skipped: {skipped}")
    
    success_rate = (passed / (total_tests - skipped) * 100) if (total_tests - skipped) > 0 else 0
    print(f"\nSuccess Rate: {success_rate:.1f}%")
    
    if failed == 0:
        print("\n🎉 All tests passed! Your environment is ready.")
        print("\n📚 Next steps:")
        print("   1. Run: streamlit run streamlit_app.py")
        print("   2. Or: jupyter notebook")
        print("   3. Or: python run_project.py")
    else:
        print("\n⚠️  Some tests failed. Please:")
        print("   1. Run: pip install -r requirements.txt")
        print("   2. Ensure all data files are present")
        print("   3. Run this test again")

def main():
    """Main test function"""
    print("\n" + "🔬" * 35)
    print("\n  CRIME DATA ANALYSIS PROJECT - ENVIRONMENT TEST")
    print("\n" + "🔬" * 35)
    
    # Run all tests
    results = {
        'Python Version': test_python_version(),
        'Core Packages': test_core_packages(),
        'Data Files': test_data_files(),
        'Basic Functionality': test_basic_functionality(),
        'Data Loading': test_data_loading()
    }
    
    # Optional tests (don't affect overall status)
    test_optional_packages()
    test_notebooks()
    test_project_files()
    
    # Generate report
    generate_report(results)
    
    print("\n" + "=" * 70)
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user.")
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
