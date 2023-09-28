import streamlit as st
from annotated_text import annotated_text
import requests
from text_utils import annotate_text
import json


def call_api(text):
    input_data = {"text": text}
    response = requests.post(url="http://127.0.0.1:8000/predict", data=json.dumps(input_data))
    annotated_text = annotate_text(text, response.json()["named_entities"])
    return annotated_text


text = "Warsaw is the capitol of Poland."

annotated_text(call_api(text))