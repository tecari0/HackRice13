import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")

def chatgpt_response(prompt):
    response = openai.Completion.create(
        model = "text-davinci-002",
        prompt = prompt,
        temperature = 1,
        max_tokens = 100
    )
    prompt_response = ""
    response_dict = response.get("choice") # type: ignore
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]["text"]
    return prompt_response