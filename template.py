"""
# Author: Aditya Dinesh K (Aydie)
# GitHub: https://github.com/aydiegithub
# GitLab: https://gitlab.com/aydie
# Website: https://aydie.in
# Description: This script sets up the project directory structure for the US Visa Approval Status ML pipeline.
"""

import os
from pathlib import Path

""" 
your_project_name/
├── your_library_name/
│   ├── __init__.py
│   ├── constant.py
│   └── config/
│       └── __init__.py
├── examples/
│   └── example.py
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py
"""

project_name = "aydie_mllib"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/constants.py",
    f"{project_name}/config/__init__.py",
    
    f"examples/example.py",
    f".gitignore",
    f"requirements.txt",
    f"setup.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"{filename} already exists")
        
print("\n✅ Files Created.....\nExited....\n")
        

