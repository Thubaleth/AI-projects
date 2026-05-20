import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
Api_Key = os.getenv("OpenAi_API_key")

def get_response(system_prompt,prompt):
    client = OpenAI(api_key=Api_Key)
    response = client.chat.completions.create(
         model="gpt-4o-mini",
         messages = [ 
                      {"role":"system","content":system_prompt},
                      {"role":"user","content":prompt}
                    ]
    )  

    return response.choices[0].message.content

response = get_response("You are an expert data scientist that explains complex concepts in understandable terms", "Define AI")
print(response)