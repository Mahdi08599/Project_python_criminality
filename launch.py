#!/usr/bin/env python3
"""
Quick Launcher for Crime Data Analysis Project
==============================================
Usage: python launch.py [option]

Options:
  dashboard   - Launch Streamlit dashboard
  menu        - Interactive menu
  test        - Test environment
  jupyter     - Open Jupyter notebooks
"""

import sys
import subprocess
import os

# Change to project root directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def launch_dashboard():
    """Launch Streamlit dashboard"""
    print("🚀 Launching Streamlit Dashboard...")
    subprocess.run(["streamlit", "run", "streamlit_app.py"])

def launch_menu():
    """Launch interactive menu"""
    print("📋 Launching Interactive Menu...")
    subprocess.run(["python", "scripts/run_project.py"])

def test_environment():
    """Test environment"""
    print("🧪 Testing Environment...")
    subprocess.run(["python", "scripts/test_environment.py"])

def open_jupyter():
    """Open Jupyter notebooks"""
    print("📓 Opening Jupyter Notebooks...")
    subprocess.run(["jupyter", "notebook", "notebooks/"])

def show_help():
    """Show help message"""
    print(__doc__)

def main():
    """Main launcher"""
    if len(sys.argv) < 2:
        # Default: show menu
        launch_menu()
    else:
        option = sys.argv[1].lower()
        
        if option in ['dashboard', 'dash', 'd']:
            launch_dashboard()
        elif option in ['menu', 'm']:
            launch_menu()
        elif option in ['test', 't']:
            test_environment()
        elif option in ['jupyter', 'notebook', 'j', 'n']:
            open_jupyter()
        elif option in ['help', 'h', '-h', '--help']:
            show_help()
        else:
            print(f"❌ Unknown option: {option}")
            show_help()

if __name__ == "__main__":
    main()
