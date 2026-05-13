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
story = 'Once upon a time, there was a small robot named Beep who lived in a busy toy shop. Every night, when the shop closed, Beep would walk around and make sure all the toys were happy.'
# Create a prompt that completes the story
prompt = f"""Complete the story delimited by triple backticks. 
 ```{story}```"""

# Get the generated response 
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)