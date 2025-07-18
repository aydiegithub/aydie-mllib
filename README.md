# aydie-mllib

**aydie-mllib** is a Python library designed to automate and simplify the process of training and tuning machine learning models. By leveraging a simple YAML configuration file, you can easily test multiple algorithms, perform hyperparameter tuning with `GridSearchCV`, and find the best model for your data without writing repetitive boilerplate code.

This library is built to be extensible and supports any model that follows the scikit-learn API, including popular libraries like XGBoost.

---

## Features

-   **Configuration-Driven:** Define your entire model training pipeline in a single YAML file.
-   **Automated Grid Search:** Automatically performs hyperparameter tuning for multiple models.
-   **Model Agnostic:** Works with any scikit-learn compatible model (e.g., `RandomForestRegressor`, `SVR`, `XGBClassifier`).
-   **Find the Best:** Compares the tuned models and returns the one with the highest score.
-   **Easy to Use:** Includes a helper function to generate a sample configuration file to get you started instantly.

---

## Installation

You can install `aydie-mllib` directly from PyPI (once you publish it):

```bash
pip install aydie-mllib
```

Or, install it directly from the source for the latest version:

```bash
git clone [https://github.com/aydiegithub/aydie-mllib.git](https://github.com/aydiegithub/aydie-mllib.git)
cd aydie-mllib
pip install .
```

---

## Quickstart Guide

Here's how to get up and running with `aydie-mllib` in just a few steps.

### 1. Generate the Configuration File

First, create a Python script to generate or create a sample `model_config.yaml` file. This will be the blueprint for your training pipeline.

**`generate_config.py`**

```python
from aydie_mllib.config import generate_sample_model_config

# This will create a 'config' directory and place 'model_config.yaml' inside it.
file_path = generate_sample_model_config(export_dir="config")

print(f"Sample config file has been generated at: {file_path}")
```

### 2. Customize `model_config.yaml`

Now, open the newly created `config/model_config.yaml` and customize it for the models you want to test. Let's set it up to compare a `RandomForestRegressor` and an `XGBRegressor`.

```yaml
grid_search:
  class: GridSearchCV
  module: sklearn.model_selection
  params:
    cv: 5
    verbose: 1
model_selection:
  module_0:
    class: RandomForestRegressor
    module: sklearn.ensemble
    params:
      n_estimators: 100
      random_state: 42
    search_param_grid:
      n_estimators:
        - 100
        - 200
      max_depth:
        - 5
        - 10
        - null
  module_1:
    class: XGBRegressor
    module: xgboost
    params:
      objective: reg:squarederror
    search_param_grid:
      n_estimators:
        - 50
        - 100
      learning_rate:
        - 0.05
        - 0.1
```

### 3. Find the Best Model

Finally, use the `ModelBuilder` to load your configuration, train the models, and find the best one.

**`run_training.py`**

```python
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
```

---

## How it Works

The library is centered around the `ModelBuilder` class, which orchestrates the entire process based on your `model_config.yaml` file.

-   **`grid_search` section**: Defines the hyperparameter search strategy. By default, it uses `sklearn.model_selection.GridSearchCV`. You can customize its parameters like `cv` (cross-validation folds).
-   **`model_selection` section**: This is a dictionary where each key (e.g., `module_0`) represents a model to be evaluated.
    -   `module`: The Python module where the model class is located (e.g., `sklearn.ensemble` or `xgboost`).
    -   `class`: The name of the model class (e.g., `RandomForestRegressor`).
    -   `params`: A dictionary of fixed parameters that will be passed to the model's constructor.
    -   `search_param_grid`: The dictionary of hyperparameters to be tuned by the grid search.

---

## Connect with Me

-   🌐 **Website:** [aydie.in](https://aydie.in)
-   💼 **LinkedIn:** [@aydiemusic](https://www.linkedin.com/in/aydiemusic)
-   🐦 **X (Twitter):** [@aydiemusic](https://x.com/aydiemusic)
-   📸 **Instagram:** [@aydiemusic](https://www.instagram.com/aydiemusic)
-   📺 **YouTube:** [@aydiemusic](https://www.youtube.com/@aydiemusic)
-   📧 **Contact:** [business@aydie.in](mailto:business@aydie.in)

---

## Contributing

Contributions are welcome! If you have ideas for improvements or find a bug, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
