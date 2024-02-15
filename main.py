from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from preprocessing import encode_cols, load_preprocessor
from models import get_model
from sklearn.feature_extraction import DictVectorizer
from typing import List
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator
from config import PATH_TO_PREPROCESSOR, PATH_TO_MODEL, CATEGORICAL_COLS
 
 
app = FastAPI()
class InputData(BaseModel):
    cut: object
    color: object
    clarity: object
 
config = {}
# Load configuration from config.json
with open("config.py", "r") as config_file:
    exec(config_file.read(), config)
 
def run_inference(user_input: List[InputData], dv: DictVectorizer, model: BaseEstimator) -> np.ndarray:
    df = pd.DataFrame([x.dict() for x in user_input])
    df = encode_cols(df)
    dicts = df[CATEGORICAL_COLS].to_dict(orient="records")
    X = dv.transform(dicts)
    print(X.shape)
    y = model.predict(X)
    # logger.info(f"Predicted trip duration: {y}")
    return y
 
@app.get("/")
def read_root():
    return {"message": "Welcome to the Diamond Price Predictor!"}
 
@app.post("/predict_diamond_price")
def predict_duration_route(payload: InputData):
    dv = load_preprocessor(PATH_TO_PREPROCESSOR)
    model = get_model(PATH_TO_MODEL)
    y = run_inference([payload], dv, model)
    return {"diamond_price_prediction: ": y[0]}