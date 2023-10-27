import wikipedia
from fastapi import FastAPI
import pyjokes
from pydantic import BaseModel

app = FastAPI()


class Joke(BaseModel):
    friend: str
    joke: str


class JokeInput(BaseModel):
    friend: str


@app.post("/", response_model=Joke)
def create_joke(joke_input: JokeInput):
    """Создание шутки"""
    return Joke(friend=joke_input.friend, joke=pyjokes.get_joke())