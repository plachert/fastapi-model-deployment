from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class InputData(BaseModel):
    text: str
    
class Prediction(BaseModel):
    text: str

