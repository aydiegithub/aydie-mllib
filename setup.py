from setuptools import setup, find_packages

setup(
    name="aydie_mllib",
    version="1.0.0",
    author="Aditya (Aydie) Dinesh K",
    author_email="business@aydie.in",
    description=(
        "This library helps machine learning engineers and developers "
        "automatically select the best model and its hyperparameters, "
        "eliminating the need to write algorithms from scratch."
    ),
    packages=find_packages(),
    install_requires=["PyYAML", "scikit-learn", "xgboost"],
    url="https://github.com/aydiegithub/aydie-mllib",
    project_urls={
        "Website": "https://aydie.in"
    }
)