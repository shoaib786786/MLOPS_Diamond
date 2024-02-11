from sklearn.feature_extraction import DictVectorizer
import pickle
from web_service.config import PATH_TO_PREPROCESSOR
 
# preprocess_path = "C:/Git/Stephanie/stephina/lessons/02-model-deployment/web_service/local_models/preprocessing.pkl"
 
def save_picked(path: str, dv: DictVectorizer):
    with open(path, "wb") as f:
        pickle.dump(dv, f)
 
dv = DictVectorizer()
save_picked(PATH_TO_PREPROCESSOR, dv)