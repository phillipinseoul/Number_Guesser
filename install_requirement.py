import subprocess
import sys
import get_pip
import os
import importlib
import contextlib

def install(package):
    '''
    installs a package using pip

    :param package: string
    '''
    subprocess.call([sys.executable, "-m", "pip", "install", package])

required = []
failed = []

# Try to open requirements.txt file & Read all required packages
try:
    file = open("requirements.txt", "r")
    file_lines = file.readlines()
    required = [line.strip().lower() for line in file_lines]
    file.close()
except FileNotFoundError:
    print("[ERROR] No requirements.txt file found");


