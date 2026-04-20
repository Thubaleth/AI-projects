import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() #this will load the enviroment variable
Api_key = os.getenv("OpenAi_API_key")

if not Api_key:
    raise ValueError("Open AI key not found from env file")

def get_response(prompt):
    client = OpenAI(api_key=Api_key)
    response = client.chat.completions.create(
       model="gpt-4o-mini",
       max_completion_tokens=100, #dont want long response
       messages=[{"role":"user","content":prompt}]
    )
    

    return response.choices[0].message.content

response = get_response("I want to learn to speak Dutch.")

print(response)