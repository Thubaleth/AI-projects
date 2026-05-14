import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
Api_key = os.getenv("OpenAi_API_key")

def get_response(prompt):
    client = OpenAI(api_key=Api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":"You are a helpful assistance"},
            {"role":"user","content":prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content

# Dummy text to analyze
text = """
Artificial Intelligence is transforming the way people work and communicate. 
From healthcare to education, AI-powered tools are helping solve complex problems 
faster and more efficiently. Many companies are now investing heavily in AI research 
to build smarter applications for the future.
"""

# Create the instructions
instructions = instructions = (
    "Determine the language of the following text and generate a suitable title for it. "
    "Use the provided output format. The text will be delimited using triple backticks."
)

# Create the output format
output_format = (
    "Text:\n"
    "Language:\n"
    "Title:"
)



# Create the final prompt
prompt =f"""
{instructions}

Output format:
{output_format}

Text to analyze:
{text}
"""
response = get_response(prompt)
print(response)