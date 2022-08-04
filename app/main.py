from typing import Union,List

from fastapi import FastAPI
from app.models.weather import Weather
from app.pred_models.reglog import get_reglog_prediction
import pandas as pd

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict_weather")
def predict_weather(weather:Weather):
    weather_dict = weather.dict()
    df = pd.DataFrame([weather_dict])
    x = get_reglog_prediction(df)
    return int(x[0])


@app.post("/predict_weather_batch")
def predict_weather_batch(weather_batch:List[Weather]):
    weather_batch_dict = map(lambda x: x.dict(),weather_batch)
    df = pd.DataFrame(weather_batch_dict)
    x = get_reglog_prediction(df)
    return x.tolist()
