import joblib

def save_model(model, filepath: str):
    """
    Save the fitted model to filepath using joblib.
    """
    joblib.dump(model, filepath)

def load_model(filepath: str):
    """
    Load and return the model from filepath.
    """
    return joblib.load(filepath)