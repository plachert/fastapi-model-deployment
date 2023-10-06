from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from model.model import __version__ as model_version
from model.model import recognize_entities


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class InputData(BaseModel):
    text: str
    
class NamedEntity(BaseModel):
    entity: str
    score: float
    index: int
    word: str
    start: int
    end: int
    
class NamedEntities(BaseModel):
    named_entities: List[NamedEntity]

    
@app.get('/')
def read_root():
    return {f"Model version: {model_version}"}

@app.post('/predict', response_model=NamedEntities)
def predict(input_data: InputData):
    named_entities = recognize_entities(input_data.text)
    return {"named_entities": named_entities}
