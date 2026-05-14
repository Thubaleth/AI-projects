import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
Api_key = os.getenv("OpenAi_API_key")


def get_response(prompt):
    client = OpenAI(api_key=Api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"system","content":"you are a helpful assistant"},
                  {"role":"user","content":prompt}
                  ]

    )
    
    return response.choices[0].message.content

# Create a prompt that generates the table
prompt = "Generate a table containing 10 books I should read if I am a science fiction lover, with columns for Title, Author, and Year."

# Get the response
response = get_response(prompt)
print(response)