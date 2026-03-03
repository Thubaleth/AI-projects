import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
Api_key = os.getenv("openAI_Api_key")

if not Api_key:
    raise ValueError("Open AI key not been found from env file")

def get_response(prompt):
    client = OpenAI(api_key=Api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_completion_tokens=100,
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content

#find and replace text
prompt="""Replace car with plane and adjust phrase:
A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Cars are often associated with freedom, independence, and mobility."""

print(get_response(prompt))