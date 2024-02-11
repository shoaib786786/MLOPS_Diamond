import pickle
 
def get_model(model_path: str):
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        raise FileNotFoundError(f"Model not found at path: {model_path}")
    except Exception as e:
        print(f"Error loading model: {e}")
        return None  # Return None to handle the error gracefully