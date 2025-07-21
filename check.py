'''from aydie_mllib.config import generate_sample_model_config

# This will create a 'config' directory and place 'model_config.yaml' inside it.
file_path = generate_sample_model_config(export_dir="config")

print(f"Sample config file has been generated at: {file_path}")'''

import pandas as pd
from sklearn.model_selection import train_test_split
from aydie_mllib import ModelBuilder

# --- 1. Load your data ---
# As an example, let's create some dummy data
from sklearn.datasets import make_regression
X, y = make_regression(n_samples=1000, n_features=20, noise=0.1, random_state=42)
X = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])


# --- 2. Initialize the ModelBuilder ---
# Point it to your configuration file
model_builder = ModelBuilder(model_config_path="config/model_config.yaml")


# --- 3. Get the best model ---
# The get_best_model method runs the entire pipeline
best_model_detail = model_builder.get_best_model(X=X, y=y, base_accuracy=0.6)


# --- 4. Print the results ---
print("\n--- Best Model Found ---")
print(f"Model Class: {best_model_detail.best_model.__class__.__name__}")
print(f"Best Score (R^2): {best_model_detail.best_score:.4f}")
print(f"Best Parameters: {best_model_detail.best_parameters}")

# You can now use this best model for predictions
# best_model = best_model_detail.best_model
# predictions = best_model.predict(X)