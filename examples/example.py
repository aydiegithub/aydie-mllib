import pandas as pd
from sklearn.datasets import make_regression
from aydie_mllib import ModelBuilder
from aydie_mllib.config import generate_sample_model_config
import os

# --- Step 1: Generate and Customize the Configuration ---
# For a real-world example, we'll first generate the config, then
# we would manually edit it. For this script, we'll just use the generated one
# and assume it has been customized as per the README.


# Create a 'config' directory for our example
CONFIG_DIR = "config_for_example" # or you can use your own config path

if not os.path.exists(CONFIG_DIR):
    print(f"Generating sample config in '{CONFIG_DIR}/' directory...")
    generate_sample_model_config(export_dir=CONFIG_DIR)


"""
# NOTE: For this script to work as intended, you should open
# `config_for_example/model_config.yaml` and update it with RandomForest and XGBoost
# details as shown in the README.md file.
"""

# --- Step 2: Load or Create Data ---
print("\nCreating dummy regression data...")
X, y = make_regression(n_samples=1000, n_features=20, noise=0.1, random_state=42)

# Convert to pandas DataFrame, as is common in ML projects
X = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])
print("Data created successfully.")


# --- Step 3: Initialize the ModelFactory ---
# Point the factory to the configuration file we want to use.
MODEL_CONFIG_PATH = os.path.join(CONFIG_DIR, "model_config.yaml")
print(f"\nInitializing ModelFactory with config: {MODEL_CONFIG_PATH}")
model_factory = ModelFactory(model_config_path=MODEL_CONFIG_PATH)


# --- Step 4: Run the training pipeline to find the best model ---
# The get_best_model() method handles everything: initializing models,
# running grid search, and comparing the results.
print("\nStarting model training and hyperparameter search...")
try:
    best_model_detail = model_factory.get_best_model(X=X, y=y, base_accuracy=0.6)

    # --- Step 5: Display the results ---
    print("\n--- Best Model Found ---")
    print(f"Model Class:       {best_model_detail.best_model.__class__.__name__}")
    print(f"Best Score (R^2):  {best_model_detail.best_score:.4f}")
    print(f"Best Parameters:   {best_model_detail.best_parameters}")

    # You can now use this best model for making predictions on new data
    # best_model = best_model_detail.best_model
    # predictions = best_model.predict(X)
    # print("\nPrediction on first 5 samples:", predictions[:5])

except Exception as e:
    print(f"\nAn error occurred: {e}")
    print("Please ensure 'config_for_example/model_config.yaml' is correctly configured with valid models from sklearn and xgboost.")

