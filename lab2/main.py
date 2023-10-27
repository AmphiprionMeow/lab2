import wikipedia
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

"""Path запрос"""


@app.get("/")
def Names():
    return wikipedia.search("Bill")


"""Query запрос"""


@app.get("/sentence/{about}")
def About_Something(about: str, sentence: int):
    result = wikipedia.summary(about, sentences=sentence)
    return result


"""Роут с передачей параметров в теле запроса"""


class TextInput(BaseModel):
    about: str
    sentence: int


@app.post("/")
def create_joke(text_input: TextInput):
    """Создание текста"""
    return wikipedia.summary(text_input.about, sentences=text_input.sentence)
