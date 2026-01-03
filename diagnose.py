#!/usr/bin/env python3
"""
Diagnostic script to check if the backend is properly configured
"""

import os
import sys

def check_google_api_key():
    """Check if GOOGLE_API_KEY is set"""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if api_key:
        print("✓ GOOGLE_API_KEY is set")
        print(f"  Key starts with: {api_key[:10]}...")
        return True
    else:
        print("✗ GOOGLE_API_KEY is NOT set")
        print("  Run: set GOOGLE_API_KEY=your_key_here (Windows)")
        print("  Or:  export GOOGLE_API_KEY=your_key_here (Linux/Mac)")
        return False

def check_python_packages():
    """Check if required packages are installed"""
    packages = {
        'fastapi': 'FastAPI',
        'uvicorn': 'Uvicorn',
        'google.generativeai': 'Google Generative AI',
        'pydantic': 'Pydantic'
    }
    
    missing = []
    for module, name in packages.items():
        try:
            __import__(module)
            print(f"✓ {name} is installed")
        except ImportError:
            print(f"✗ {name} is NOT installed")
            missing.append(module)
    
    return len(missing) == 0, missing

def check_backend_running():
    """Check if backend is accessible"""
    try:
        import requests
        response = requests.get('http://localhost:8000/')
        if response.status_code == 200:
            print("✓ Backend is running and responding")
            return True
    except requests.exceptions.ConnectionError:
        print("✗ Backend is NOT running")
        print("  Run: uvicorn main:app --reload --port 8000")
        return False
    except Exception as e:
        print(f"✗ Error checking backend: {e}")
        return False

def main():
    print("\n" + "="*50)
    print("Insta Notes - Backend Diagnostic Check")
    print("="*50 + "\n")
    
    checks = {
        "Google API Key": check_google_api_key(),
        "Python Packages": check_python_packages()[0],
        "Backend Server": check_backend_running(),
    }
    
    print("\n" + "="*50)
    print("Summary:")
    print("="*50)
    
    all_passed = True
    for check_name, passed in checks.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}: {check_name}")
        if not passed:
            all_passed = False
    
    print("="*50 + "\n")
    
    if all_passed:
        print("All checks passed! Try generating notes now.")
    else:
        print("Please fix the issues above and try again.")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
