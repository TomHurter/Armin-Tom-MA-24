import sys

def verify_python_version():
    print("1. Vérification de Python")
    if sys.version_info.major!=3:
        print("Error, u need at least python 3 to run this script")
        sys.exit(1)
    else:
        print(f"Python version is {sys.version_info.major}.{sys.version_info.minor} ok")



def show_interpreter_info():
    print("2. Info sur l'interpréteur")
    print(f"Path: {sys.executable}")

verify_python_version()
show_interpreter_info()
