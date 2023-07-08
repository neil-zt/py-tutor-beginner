"""
This file includes helper methods that wrap the 
OpenAi client into a more user-friendly interface. 
"""

import os
import openai
from core.files import get_secret

# Get OpenAI API key and organization from environment variable
OPENAI_ORG = get_secret("OPENAI_ORG")
OPENAI_KEY = get_secret("OPENAI_KEY")

openai.organization = OPENAI_ORG
openai.api_key = OPENAI_KEY

BASE_MESSAGE = {"role": "system", "content": """回答請越短越好，盡可能在一句話裡完成所要說的內容。"""}
messages_cache = [BASE_MESSAGE]


def reset() -> None:
    """
    Resets the chat and append the base message
    """
    global messages_cache
    messages_cache = [BASE_MESSAGE]


def set_character(description: str) -> None:
    """
    Sets the character of the chat. 
    """
    global messages_cache
    messages_cache.append({"role": "system", "content": f"這是關於你的簡介：{description}"})


def ask(prompt: str) -> str:
    """
    Ask a question to the OpenAI API. 
    """
    global messages_cache
    print(messages_cache)
    messages_cache.append({"role": "user", "content": prompt})
    response = get_chat_response(messages_cache)
    messages_cache.append(response)
    return response["content"]


def get_chat_response(messages) -> dict[str, str]:
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """你叫阿丁"""},
        ] + messages
    )
    return dict(chat["choices"][0]["message"])
    