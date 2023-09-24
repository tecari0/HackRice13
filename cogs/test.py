import os
import openai
openai.api_key= os.getenv("OPENAI_API_KEY")
#openai.api_key = "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"

def get_completion(prompt, model="gpt-3.5-turbo"):
# def get_completion(prompt, model="gpt-4"):
    messages = [{"role": "user", "content": prompt}]
    print(messages)
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    print(response.choices[0].message["content"])
    return response.choices[0].message["content"]

response = get_completion("Hello, I am a bot. How are you?")
print(response)