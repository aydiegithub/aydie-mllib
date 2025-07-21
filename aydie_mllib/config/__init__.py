import os
import sys
import yaml
import logging

from aydie_mllib.constants import *
from aydie_mllib.exception import AydieException

logger = logging.getLogger(__name__)


def generate_sample_model_config(export_dir: str) -> str:
    """
    Generates a sample model.yaml file in the specified directory. This helps
    users get started with the required configuration format.

    Args:
        export_dir (str): The directory where the 'model.yaml' file will be saved.

    Returns:
        str: The full file path of the generated 'model.yaml' file.

    Example:
        from aydie_mllib.config import generate_sample_model_config
        
        # This will create a 'config' directory (if it doesn't exist)
        # and save 'model.yaml' inside it.
        file_path = generate_sample_model_config(export_dir="config")
        print(f"Sample config file generated at: {file_path}")
    """
    try:
        # Define the default structure of the model configuration
        model_config = {
            GRID_SEARCH_KEY: {
                MODULE_KEY: "sklearn.model_selection",
                CLASS_KEY: "GridSearchCV",
                PARAM_KEY: {
                    "cv": 5,
                    "verbose": 1
                }
            },
            MODEL_SELECTION_KEY: {
                "module_0": {
                    MODULE_KEY: "sklearn.ensemble",
                    CLASS_KEY: "RandomForestRegressor",
                    PARAM_KEY: {
                        "random_state": 42
                    },
                    SEARCH_PARAM_GRID_KEY: {
                        "n_estimators": [100, 200],
                        "max_depth": [5, 10]
                    }
                },
                "module_1": {
                    MODULE_KEY: "xgboost",
                    CLASS_KEY: "XGBRegressor",
                    PARAM_KEY: {
                        "objective": "reg:squarederror"
                    },
                    SEARCH_PARAM_GRID_KEY: {
                        "n_estimators": [50, 100],
                        "learning_rate": [0.05, 0.1]
                    }
                }
            }
        }
        
        os.makedirs(export_dir, exist_ok=True)
        
        # Define the full path for the output file
        export_file_path = os.path.join(export_dir, MODEL_CONFIG_FILE_NAME)
        
        # Write the dictionary to the YAML file
        with open(export_file_path, 'w') as file:
            yaml.dump(model_config, file, sort_keys=False) # sort_keys=False keeps the order
            
        logger.info(f"Sample model configuration file created at: {export_file_path}")
        return export_file_path
    
    except Exception as e:
        logger.error(f"Failed to generate sample model config: {e}")
        raise AydieException(e, sys) from e