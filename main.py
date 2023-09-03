from typing import Union
from fastapi import FastAPI

from models.kogpt2 import KoGPTChatbot
from models.kobart import SpeachStyleConverter
from models.openai_api import OpenAIChat


app = FastAPI()
kogpt_chatbot = KoGPTChatbot()
speach_style_converter = SpeachStyleConverter()
openai_chatbot = OpenAIChat()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/nlp/get_answer")
def read_item(text: Union[str, None] = None, target_style_name: Union[str, None] = None):
    answer = kogpt_chatbot.get_answer(text)
    result = speach_style_converter.convert(answer, target_style_name)
    return {"answer": result}

@app.get("/nlp/get_answer_from_gpt_api")
def read_item(text: Union[str, None] = None):
    result = openai_chatbot.get_answer(text)
    return {"answer": result}