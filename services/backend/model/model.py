from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline


__version__ = "dslim/bert-base-NER"


tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

ner = pipeline("ner", model=model, tokenizer=tokenizer)


def recognize_entities(text: str):
    return ner(text)
