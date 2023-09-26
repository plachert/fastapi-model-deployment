from fastapi import FastAPI
from pydantic import BaseModel
from model.model import __version__ as model_version
from model.model import dummy_predict

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:80"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    text: str
    
class Prediction(BaseModel):
    dummy_prediction: str
    
@app.get('/')
def read_root():
    return {f"Model version: {model_version}"}

@app.post('/predict', response_model=Prediction)
def predict(input_data: InputData):
    prediction = dummy_predict(input_data.text)
    return {"dummy_prediction": prediction}
    

